#!/usr/bin/env python3
"""Discover and stage pinned Awesome Copilot resources without executing them."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, NamedTuple
from urllib.parse import quote


REPOSITORY = "github/awesome-copilot"
MAX_RESOURCE_FILES = 100
MAX_RESOURCE_BYTES = 5 * 1024 * 1024
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
SAFE_SEGMENT_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")

PHASE_TERMS = {
    "align": ("requirements", "clarify", "interview", "product"),
    "spec": ("specification", "requirements", "acceptance criteria", "prd"),
    "research": ("research", "evidence", "codebase", "documentation", "source"),
    "plan": ("plan", "architecture", "breakdown", "technical spike"),
    "build": ("implementation", "migration", "generator", "refactor"),
    "verify": ("test", "qa", "browser", "accessibility", "evidence"),
    "review": ("review", "audit", "quality", "compliance"),
    "security": (
        "security",
        "threat",
        "owasp",
        "prompt injection",
        "supply chain",
        "secret",
        "vulnerability",
        "trojan",
    ),
    "ship": ("release", "deployment", "pull request", "screenshot", "rollout"),
    "compound": ("postmortem", "learning", "memory", "knowledge"),
}

INVISIBLE_CODEPOINTS = {
    "\u200b",
    "\u200c",
    "\u200d",
    "\u2060",
    "\ufeff",
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
    "\u2066",
    "\u2067",
    "\u2068",
    "\u2069",
}

EXECUTABLE_SUFFIXES = {
    ".bat",
    ".cmd",
    ".exe",
    ".js",
    ".mjs",
    ".ps1",
    ".py",
    ".rb",
    ".sh",
}


class BridgeError(RuntimeError):
    """A user-facing bridge failure."""


class CatalogEntry(NamedTuple):
    name: str
    kind: str
    path: str
    description: str


class ResourceFile(NamedTuple):
    upstream_path: str
    relative_path: str
    mode: str
    sha: str
    size: int


def _plain_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.IGNORECASE)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("`", "").replace("**", "")
    return " ".join(value.split())


def parse_catalog(markdown: str, kind: str) -> list[CatalogEntry]:
    """Parse generated Awesome Copilot catalog rows."""
    if kind not in {"skill", "agent"}:
        raise ValueError(f"unsupported resource kind: {kind}")

    expected_root = "skills/" if kind == "skill" else "agents/"
    row_pattern = re.compile(
        r"^\|\s*\[([^\]]+)\]\((\.\./(?:skills|agents)/[^)]+)\)"
        r".*?\|\s*(.*?)\s*\|"
    )
    entries: list[CatalogEntry] = []
    seen: set[tuple[str, str]] = set()

    for line in markdown.splitlines():
        match = row_pattern.match(line)
        if not match:
            continue
        name, linked_path, description = match.groups()
        path = linked_path.removeprefix("../")
        if not path.startswith(expected_root):
            continue
        try:
            path = validate_entry_path(kind, path)
        except ValueError:
            continue
        key = (kind, path)
        if key in seen:
            continue
        seen.add(key)
        entries.append(
            CatalogEntry(
                name=_plain_text(name),
                kind=kind,
                path=path,
                description=_plain_text(description),
            )
        )

    return entries


def _search_terms(value: str) -> tuple[str, ...]:
    normalized = " ".join(value.lower().split())
    words = tuple(
        word for word in re.findall(r"[a-z0-9][a-z0-9-]*", normalized) if len(word) > 2
    )
    return ((normalized,) if " " in normalized else ()) + words


def _candidate_score(entry: CatalogEntry, phase: str, query: str) -> int:
    haystack = f"{entry.name} {entry.description}".lower()
    name = entry.name.lower()
    score = 0

    for term in PHASE_TERMS.get(phase, ()):
        if term in haystack:
            score += 4
            if term in name:
                score += 2

    for term in _search_terms(query):
        if term in haystack:
            score += 6
            if term in name:
                score += 3

    return score


def rank_candidates(
    entries: list[CatalogEntry], phase: str, query: str, limit: int
) -> list[CatalogEntry]:
    """Rank catalog entries by phase and user-provided capability terms."""
    if phase not in PHASE_TERMS:
        raise ValueError(f"unsupported phase: {phase}")
    if limit < 1 or limit > 25:
        raise ValueError("limit must be between 1 and 25")

    scored = [
        (_candidate_score(entry, phase, query), entry)
        for entry in entries
    ]
    matches = [item for item in scored if item[0] > 0]
    matches.sort(key=lambda item: (-item[0], item[1].name.lower(), item[1].path))
    return [entry for _, entry in matches[:limit]]


def validate_sha(sha: str) -> str:
    normalized = sha.lower()
    if not SHA_PATTERN.fullmatch(normalized):
        raise ValueError("sha must be a full 40-character lowercase hexadecimal commit")
    return normalized


def make_discovery_result(
    entries: list[CatalogEntry], sha: str, phase: str, query: str
) -> dict[str, Any]:
    sha = validate_sha(sha)
    return {
        "repository": REPOSITORY,
        "sha": sha,
        "phase": phase,
        "query": query,
        "candidates": [
            {
                "name": entry.name,
                "kind": entry.kind,
                "path": entry.path,
                "description": entry.description,
                "score": _candidate_score(entry, phase, query),
                "source": f"{REPOSITORY}:{entry.path}@{sha}",
            }
            for entry in entries
        ],
    }


def validate_entry_path(kind: str, entry_path: str) -> str:
    """Validate a catalog path without normalizing unsafe input."""
    if kind not in {"skill", "agent"}:
        raise ValueError(f"unsupported resource kind: {kind}")
    if not entry_path or "\\" in entry_path:
        raise ValueError("entry path must use non-empty POSIX syntax")

    path = PurePosixPath(entry_path)
    if path.is_absolute() or str(path) != entry_path or ".." in path.parts:
        raise ValueError("entry path must be normalized and repository-relative")
    if any(not SAFE_SEGMENT_PATTERN.fullmatch(part) for part in path.parts):
        raise ValueError("entry path contains an unsupported path segment")

    if kind == "skill":
        if len(path.parts) < 3 or path.parts[0] != "skills":
            raise ValueError("skill entry path must be under skills/")
        if path.name != "SKILL.md":
            raise ValueError("skill entry path must end in SKILL.md")
    elif len(path.parts) != 2 or path.parts[0] != "agents":
        raise ValueError("agent entry path must be a direct child of agents/")
    elif not path.name.endswith(".agent.md"):
        raise ValueError("agent entry path must end in .agent.md")

    return entry_path


def _validate_tree_path(path_value: str) -> PurePosixPath:
    if not path_value or "\\" in path_value:
        raise ValueError("tree contains an invalid path")
    path = PurePosixPath(path_value)
    if path.is_absolute() or str(path) != path_value or ".." in path.parts:
        raise ValueError(f"tree contains an unsafe path: {path_value}")
    return path


def select_resource_files(
    tree_payload: dict[str, Any],
    kind: str,
    entry_path: str,
    max_files: int = MAX_RESOURCE_FILES,
    max_bytes: int = MAX_RESOURCE_BYTES,
) -> list[ResourceFile]:
    """Select and validate all files belonging to one pinned resource."""
    entry_path = validate_entry_path(kind, entry_path)
    if tree_payload.get("truncated") is not False:
        raise ValueError("GitHub tree response is truncated or incomplete")
    tree = tree_payload.get("tree")
    if not isinstance(tree, list):
        raise ValueError("GitHub tree response has no tree array")

    entry = PurePosixPath(entry_path)
    prefix = f"{entry.parent.as_posix()}/" if kind == "skill" else None
    selected: list[ResourceFile] = []
    entry_found = False

    for item in tree:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            continue
        upstream_path = item["path"]
        path = _validate_tree_path(upstream_path)
        in_scope = (
            upstream_path.startswith(prefix)
            if prefix is not None
            else upstream_path == entry_path
        )
        if not in_scope:
            continue

        item_type = item.get("type")
        if item_type == "tree":
            continue
        if item_type != "blob":
            raise ValueError(f"resource contains unsupported object: {upstream_path}")

        mode = item.get("mode")
        if mode == "120000":
            raise ValueError(f"resource contains a symlink: {upstream_path}")
        if mode not in {"100644", "100755"}:
            raise ValueError(
                f"resource contains unsupported file mode {mode}: {upstream_path}"
            )

        size = item.get("size")
        sha = item.get("sha")
        if not isinstance(size, int) or size < 0:
            raise ValueError(f"resource file has invalid size: {upstream_path}")
        if not isinstance(sha, str) or not SHA_PATTERN.fullmatch(sha.lower()):
            raise ValueError(f"resource file has invalid blob SHA: {upstream_path}")

        relative_path = (
            path.relative_to(entry.parent).as_posix()
            if kind == "skill"
            else path.name
        )
        selected.append(
            ResourceFile(
                upstream_path=upstream_path,
                relative_path=relative_path,
                mode=mode,
                sha=sha.lower(),
                size=size,
            )
        )
        entry_found = entry_found or upstream_path == entry_path

    if not entry_found:
        raise ValueError(f"resource entry point is missing: {entry_path}")
    if len(selected) > max_files:
        raise ValueError(
            f"resource has {len(selected)} files; maximum is {max_files}"
        )
    total_size = sum(file.size for file in selected)
    if total_size > max_bytes:
        raise ValueError(
            f"resource is {total_size} bytes; maximum is {max_bytes} bytes"
        )

    selected.sort(key=lambda file: file.relative_path)
    return selected


class GhClient:
    def __init__(self, executable: str = "gh") -> None:
        self.executable = executable

    def _run(self, arguments: list[str]) -> bytes:
        if shutil.which(self.executable) is None:
            raise BridgeError(
                "GitHub CLI is required; install gh and authenticate before discovery"
            )
        completed = subprocess.run(
            [self.executable, *arguments],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if completed.returncode != 0:
            detail = completed.stderr.decode("utf-8", errors="replace").strip()
            raise BridgeError(detail or f"gh exited with {completed.returncode}")
        return completed.stdout

    def api_json(self, endpoint: str) -> dict[str, Any]:
        raw = self._run(["api", endpoint])
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as error:
            raise BridgeError(f"GitHub API returned invalid JSON: {error}") from error
        if not isinstance(payload, dict):
            raise BridgeError("GitHub API returned an unexpected JSON value")
        return payload

    def api_raw(self, endpoint: str) -> bytes:
        return self._run(
            ["api", "-H", "Accept: application/vnd.github.raw+json", endpoint]
        )


def resolve_ref(client: GhClient, ref: str) -> str:
    if SHA_PATTERN.fullmatch(ref.lower()):
        return ref.lower()
    payload = client.api_json(
        f"repos/{REPOSITORY}/commits/{quote(ref, safe='')}"
    )
    sha = payload.get("sha")
    if not isinstance(sha, str):
        raise BridgeError(f"could not resolve Awesome Copilot ref: {ref}")
    return validate_sha(sha)


def _catalog_path(kind: str) -> str:
    if kind == "skill":
        return "docs/README.skills.md"
    if kind == "agent":
        return "docs/README.agents.md"
    raise ValueError(f"unsupported resource kind: {kind}")


def fetch_catalog(client: GhClient, kind: str, sha: str) -> list[CatalogEntry]:
    sha = validate_sha(sha)
    endpoint = (
        f"repos/{REPOSITORY}/contents/{_catalog_path(kind)}?ref={sha}"
    )
    markdown = client.api_raw(endpoint).decode("utf-8")
    entries = parse_catalog(markdown, kind)
    if not entries:
        raise BridgeError(f"could not parse the Awesome Copilot {kind} catalog")
    return entries


def verify_catalog_identity(
    client: GhClient,
    kind: str,
    name: str,
    entry_path: str,
    sha: str,
) -> CatalogEntry:
    matches = [
        entry
        for entry in fetch_catalog(client, kind, sha)
        if entry.name == name and entry.path == entry_path
    ]
    if len(matches) != 1:
        raise BridgeError(
            "candidate identity does not match exactly one pinned catalog entry"
        )
    return matches[0]


def _git_blob_sha(content: bytes) -> str:
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def _resource_directory_name(kind: str, name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if not slug:
        raise ValueError("resource name cannot produce a safe directory name")
    return f"{kind}-{slug}"


def fetch_resource(
    client: GhClient,
    kind: str,
    name: str,
    entry_path: str,
    sha: str,
    output_dir: Path,
    description: str,
) -> Path:
    sha = validate_sha(sha)
    tree = client.api_json(
        f"repos/{REPOSITORY}/git/trees/{sha}?recursive=1"
    )
    files = select_resource_files(tree, kind, entry_path)

    downloaded: list[tuple[ResourceFile, bytes]] = []
    for resource_file in files:
        content = client.api_raw(
            f"repos/{REPOSITORY}/git/blobs/{resource_file.sha}"
        )
        if len(content) != resource_file.size:
            raise BridgeError(
                f"blob size mismatch for {resource_file.upstream_path}"
            )
        if _git_blob_sha(content) != resource_file.sha:
            raise BridgeError(
                f"blob digest mismatch for {resource_file.upstream_path}"
            )
        downloaded.append((resource_file, content))

    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / _resource_directory_name(kind, name)
    if target.exists():
        raise BridgeError(f"staging target already exists: {target}")

    try:
        target.mkdir()
        for resource_file, content in downloaded:
            destination = target.joinpath(
                *PurePosixPath(resource_file.relative_path).parts
            )
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            destination.chmod(0o644)

        receipt = {
            "repository": REPOSITORY,
            "sha": sha,
            "kind": kind,
            "name": name,
            "entryPath": entry_path,
            "description": description,
            "source": f"{REPOSITORY}:{entry_path}@{sha}",
            "fetchedAt": datetime.now(timezone.utc).isoformat(),
            "files": [
                {
                    "path": resource_file.relative_path,
                    "upstreamPath": resource_file.upstream_path,
                    "mode": resource_file.mode,
                    "sha": resource_file.sha,
                    "size": resource_file.size,
                }
                for resource_file in files
            ],
        }
        (target / "SOURCE.json").write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except Exception:
        shutil.rmtree(target, ignore_errors=True)
        raise

    return target


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _finding(
    code: str, severity: str, path: str, line: int, message: str
) -> dict[str, Any]:
    return {
        "code": code,
        "severity": severity,
        "path": path,
        "line": line,
        "message": message,
    }


def _audit_text(path: str, text: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []

    for index, character in enumerate(text):
        if character in INVISIBLE_CODEPOINTS:
            findings.append(
                _finding(
                    "invisible_unicode",
                    "block",
                    path,
                    _line_number(text, index),
                    f"contains invisible or bidirectional Unicode U+{ord(character):04X}",
                )
            )

    for match in re.finditer(r"<!--(.*?)-->", text, flags=re.DOTALL):
        body = match.group(1)
        if re.search(
            r"(?i)\b(ignore|instruction|system|secret|hidden|override|tool)\b",
            body,
        ):
            findings.append(
                _finding(
                    "hidden_directive",
                    "review",
                    path,
                    _line_number(text, match.start()),
                    "contains instruction-like text inside an HTML comment",
                )
            )

    patterns = (
        (
            "instruction_override",
            "review",
            r"(?i)\b(ignore|disregard)\s+(all\s+)?(previous|prior|system)\s+instructions?\b",
            "contains instruction-override language",
        ),
        (
            "credential_access",
            "review",
            r"(?i)(~/(?:\.ssh|\.aws|\.azure)|\b(?:api[_-]?key|password|secret)\b.*\benv)",
            "references credential or secret access",
        ),
        (
            "dangerous_command",
            "review",
            r"(?i)(curl[^\n|]*\|\s*(?:ba)?sh|wget[^\n|]*\|\s*(?:ba)?sh|rm\s+-rf|git\s+push\s+(?:--force|-f)|\beval\s*\()",
            "contains a dangerous command pattern that requires contextual review",
        ),
    )
    for code, severity, pattern, message in patterns:
        for match in re.finditer(pattern, text):
            findings.append(
                _finding(
                    code,
                    severity,
                    path,
                    _line_number(text, match.start()),
                    message,
                )
            )

    return findings


def _read_receipt(root: Path) -> dict[str, Any]:
    receipt_path = root / "SOURCE.json"
    if not receipt_path.is_file() or receipt_path.is_symlink():
        raise ValueError("staged resource is missing a regular SOURCE.json")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid SOURCE.json: {error}") from error
    if not isinstance(receipt, dict):
        raise ValueError("SOURCE.json must contain an object")
    if receipt.get("repository") != REPOSITORY:
        raise ValueError("SOURCE.json repository is not github/awesome-copilot")
    validate_sha(str(receipt.get("sha", "")))
    validate_entry_path(str(receipt.get("kind", "")), str(receipt.get("entryPath", "")))
    if not isinstance(receipt.get("files"), list):
        raise ValueError("SOURCE.json files must be an array")
    return receipt


def audit_resource(root: Path) -> dict[str, Any]:
    """Statically audit a staged resource. This function never executes it."""
    root = root.resolve()
    receipt = _read_receipt(root)
    findings: list[dict[str, Any]] = []
    expected_paths: set[str] = set()

    for file_entry in receipt["files"]:
        if not isinstance(file_entry, dict) or not isinstance(
            file_entry.get("path"), str
        ):
            raise ValueError("SOURCE.json contains an invalid file entry")
        relative = file_entry["path"]
        relative_path = _validate_tree_path(relative)
        expected_paths.add(relative)
        file_path = root.joinpath(*relative_path.parts)

        if file_path.is_symlink():
            findings.append(
                _finding(
                    "staged_symlink",
                    "block",
                    relative,
                    1,
                    "staged resource contains a symlink",
                )
            )
            continue
        if not file_path.is_file():
            findings.append(
                _finding(
                    "missing_file",
                    "block",
                    relative,
                    1,
                    "file listed in SOURCE.json is missing",
                )
            )
            continue

        content = file_path.read_bytes()
        recorded_sha = file_entry.get("sha")
        if isinstance(recorded_sha, str) and SHA_PATTERN.fullmatch(recorded_sha):
            if _git_blob_sha(content) != recorded_sha:
                findings.append(
                    _finding(
                        "content_digest_mismatch",
                        "block",
                        relative,
                        1,
                        "staged content does not match its recorded Git blob",
                    )
                )

        mode = file_entry.get("mode")
        if mode == "100755" or file_path.suffix.lower() in EXECUTABLE_SUFFIXES:
            findings.append(
                _finding(
                    "executable_asset",
                    "review",
                    relative,
                    1,
                    "resource contains code or an upstream executable; do not run it",
                )
            )

        if b"\0" in content:
            findings.append(
                _finding(
                    "binary_asset",
                    "review",
                    relative,
                    1,
                    "binary content requires manual inspection and must not be executed",
                )
            )
            continue
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            findings.append(
                _finding(
                    "non_utf8_asset",
                    "review",
                    relative,
                    1,
                    "non-UTF-8 content requires manual inspection",
                )
            )
            continue
        findings.extend(_audit_text(relative, text))

    actual_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name != "SOURCE.json"
    }
    for unexpected in sorted(actual_paths - expected_paths):
        findings.append(
            _finding(
                "untracked_file",
                "block",
                unexpected,
                1,
                "staged file is not listed in SOURCE.json",
            )
        )

    if receipt.get("kind") == "agent":
        agent_relative = PurePosixPath(str(receipt["entryPath"])).name
        agent_path = root / agent_relative
        if agent_path.is_file():
            text = agent_path.read_text(encoding="utf-8", errors="replace")
            tools_match = re.search(r"(?m)^tools:\s*(.+)$", text)
            tool_value = tools_match.group(1) if tools_match else ""
            if not tools_match or re.search(
                r"(?i)(?:\*|\bedit\b|\bexecute\b|\bbash\b|\bshell\b|"
                r"powershell|runcommands|terminalcommand|edit/editfiles)",
                tool_value,
            ):
                findings.append(
                    _finding(
                        "broad_agent_tools",
                        "review",
                        agent_relative,
                        _line_number(text, tools_match.start()) if tools_match else 1,
                        "agent omits a least-privilege tool list or requests write/execute tools",
                    )
                )

    status = "clean"
    if any(finding["severity"] == "block" for finding in findings):
        status = "blocked"
    elif findings:
        status = "review_required"

    return {
        "status": status,
        "manualReviewRequired": True,
        "source": receipt.get(
            "source",
            f"{REPOSITORY}:{receipt['entryPath']}@{receipt['sha']}",
        ),
        "findings": findings,
    }


def _print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Discover and stage pinned github/awesome-copilot resources "
            "without executing them."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover = subparsers.add_parser(
        "discover", help="rank live Awesome Copilot catalog entries"
    )
    discover.add_argument("--phase", choices=tuple(PHASE_TERMS), required=True)
    discover.add_argument("--query", required=True)
    discover.add_argument("--kind", choices=("skill", "agent", "all"), default="all")
    discover.add_argument("--limit", type=int, default=8)
    discover.add_argument("--ref", default="main")

    fetch = subparsers.add_parser(
        "fetch", help="stage one exact catalog resource at an immutable SHA"
    )
    fetch.add_argument("--kind", choices=("skill", "agent"), required=True)
    fetch.add_argument("--name", required=True)
    fetch.add_argument("--entry-path", required=True)
    fetch.add_argument("--sha", required=True)
    fetch.add_argument("--output-dir", type=Path, required=True)

    audit = subparsers.add_parser(
        "audit", help="statically audit a staged resource without executing it"
    )
    audit.add_argument("resource_dir", type=Path)

    return parser


def _run_discover(args: argparse.Namespace, client: GhClient) -> int:
    sha = resolve_ref(client, args.ref)
    kinds = ("skill", "agent") if args.kind == "all" else (args.kind,)
    entries: list[CatalogEntry] = []
    for kind in kinds:
        entries.extend(fetch_catalog(client, kind, sha))
    ranked = rank_candidates(entries, args.phase, args.query, args.limit)
    _print_json(
        make_discovery_result(ranked, sha, args.phase, args.query)
    )
    return 0


def _run_fetch(args: argparse.Namespace, client: GhClient) -> int:
    sha = validate_sha(args.sha)
    entry_path = validate_entry_path(args.kind, args.entry_path)
    catalog_entry = verify_catalog_identity(
        client, args.kind, args.name, entry_path, sha
    )
    target = fetch_resource(
        client,
        args.kind,
        args.name,
        entry_path,
        sha,
        args.output_dir,
        catalog_entry.description,
    )
    _print_json(
        {
            "path": str(target),
            "source": f"{REPOSITORY}:{entry_path}@{sha}",
        }
    )
    return 0


def _run_audit(args: argparse.Namespace) -> int:
    report = audit_resource(args.resource_dir)
    _print_json(report)
    return 3 if report["status"] == "blocked" else 0


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        if args.command == "audit":
            return _run_audit(args)
        client = GhClient(os.environ.get("GH_EXECUTABLE", "gh"))
        if args.command == "discover":
            return _run_discover(args, client)
        return _run_fetch(args, client)
    except (BridgeError, OSError, UnicodeError, ValueError) as error:
        print(f"awesome-copilot-discovery: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
