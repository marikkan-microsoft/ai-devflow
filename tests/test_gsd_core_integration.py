"""Offline artifact contracts; these do not simulate an agent executing a skill."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/open-gsd/gsd-core"
REVISION = "9b750dc00aa385e0c2d5a47089cf3158da15e97f"
EXECUTION_SKILLS = (
    "plan-in-phases",
    "analyze-artifacts",
    "context-engineering",
    "using-devflow",
    "subagent-driven-implementation",
    "incremental-implementation",
    "autopilot",
    "verify-before-done",
)
COMMANDS = {
    "df",
    "df-align",
    "df-auto",
    "df-build",
    "df-compound",
    "df-debug",
    "df-domain",
    "df-feature",
    "df-fix",
    "df-idea",
    "df-plan",
    "df-pr",
    "df-research",
    "df-review",
    "df-ship",
    "df-simplify",
    "df-spec",
}
CONTRACT_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/gsd-core.md",
    "docs/comparison.md",
    "docs/architecture.md",
    "docs/artifacts.md",
    "docs/usage.md",
    "skills/README.md",
    "references/execution-checkpoints.md",
    "templates/plan.md",
    "templates/notes.md",
    "templates/spec.md",
    "templates/research.md",
    "agents/software-engineer.md",
    "references/definition-of-done.md",
    "skills/write-spec/SKILL.md",
    "skills/research-codebase/SKILL.md",
    "skills/domain-modeling/SKILL.md",
    "skills/test-driven-development/SKILL.md",
    "skills/ship-it/SKILL.md",
    "skills/compound-learnings/SKILL.md",
    *(f"skills/{name}/SKILL.md" for name in EXECUTION_SKILLS),
)


class GsdCoreIntegrationTests(unittest.TestCase):
    def read(self, relative_path):
        path = ROOT / relative_path
        self.assertTrue(path.is_file(), f"Missing artifact: {relative_path}")
        return path.read_text(encoding="utf-8")

    def test_gsd_is_the_seventh_foundation_not_the_optional_catalog(self):
        readme = self.read("README.md")
        comparison = self.read("docs/comparison.md")
        self.assertIn("synthesizes seven", readme)
        self.assertIn("## The seven systems", comparison)
        foundations = re.findall(r"^### \[([^]]+)\]", comparison, re.MULTILINE)
        self.assertEqual(len(foundations), 7)
        self.assertEqual(foundations[-1], "open-gsd/gsd-core")
        self.assertNotIn("github/awesome-copilot", foundations)
        self.assertIn(f"]({UPSTREAM})", readme)
        self.assertIn("on-demand, pinned specialist catalog", readme)

    def test_research_uses_one_immutable_upstream_revision(self):
        guide = self.read("docs/gsd-core.md")
        source_revisions = re.findall(
            re.escape(UPSTREAM) + r"/blob/([^/]+)/", guide
        )
        self.assertGreaterEqual(len(source_revisions), 5)
        self.assertEqual(set(source_revisions), {REVISION})
        self.assertIn(f"{UPSTREAM}/blob/{REVISION}/LICENSE", guide)
        self.assertIn("MIT", guide)
        self.assertIn("## What stays out", guide)

    def test_catalog_personas_and_native_commands_remain_unchanged(self):
        self.assertEqual(len(list(ROOT.glob("skills/*/SKILL.md"))), 32)
        self.assertEqual(len(list(ROOT.glob("agents/*.md"))), 6)
        for directory, suffix in (
            (".claude/commands", ".md"),
            (".github/prompts", ".prompt.md"),
            ("commands", ".toml"),
        ):
            with self.subTest(directory=directory):
                names = {
                    path.name[: -len(suffix)]
                    for path in (ROOT / directory).glob(f"*{suffix}")
                }
                self.assertEqual(names, COMMANDS)

    def test_extended_templates_keep_the_existing_artifact_contract(self):
        plan = self.read("templates/plan.md")
        for field in ("Files", "Satisfies", "Acceptance", "Depends on"):
            self.assertIn(f"**{field}:**", plan)
        for section in ("## Requirement coverage", "## Phase closure"):
            self.assertIn(section, plan)
        notes = self.read("templates/notes.md")
        for section in (
            "## Resume checkpoint",
            "## Evidence and open work",
            "## Next action",
        ):
            self.assertIn(section, notes)
        artifacts = self.read("docs/artifacts.md")
        self.assertIn("[notes.md](../templates/notes.md)", artifacts)

    def test_execution_producers_and_consumers_share_one_contract(self):
        for name in EXECUTION_SKILLS:
            with self.subTest(skill=name):
                text = self.read(f"skills/{name}/SKILL.md")
                self.assertIn("../../references/execution-checkpoints.md", text)
                sections = [
                    text.index(f"## {heading}")
                    for heading in (
                        "Overview",
                        "When to Use",
                        "Process",
                        "Common Rationalizations",
                        "Red Flags",
                        "Verification",
                    )
                ]
                self.assertEqual(sections, sorted(sections))
                self.assertIn(f"\nname: {name}\n", text)
                self.assertLessEqual(len(text.splitlines()), 200)

    def test_scope_and_research_templates_classify_planning_inputs(self):
        spec = self.read("templates/spec.md")
        self.assertIn("## Decision scope", spec)
        for field in ("Locked", "Discretion", "Deferred"):
            self.assertIn(f"**{field}:**", spec)
        research = self.read("templates/research.md")
        self.assertIn("## Boundary map", research)
        self.assertIn("## Planning inputs", research)

    def test_autopilot_audit_gate_preserves_the_small_fix_path(self):
        text = self.read("skills/autopilot/SKILL.md")
        checkpoint = text.split("### 2.", 1)[1].split("### 3.", 1)[0]
        feature_label = "- **Multi-task feature:**"
        small_label = "- **Confirmed bug or single-slice change:**"
        self.assertIn(feature_label, checkpoint)
        self.assertIn(small_label, checkpoint)
        self.assertIn("repro/task outline", checkpoint)
        feature, small = checkpoint.split(feature_label, 1)[1].split(
            small_label, 1
        )
        self.assertIn("run `analyze-artifacts`", feature)
        self.assertIn("Missing required artifacts block", feature)
        self.assertEqual(checkpoint.count("`analyze-artifacts`"), 1)
        self.assertRegex(small, r"(?s)skip.*TDD.*verification.*review")

    def test_local_links_and_section_targets_resolve(self):
        for relative_path in CONTRACT_FILES:
            text = self.read(relative_path)
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", text):
                url = urlsplit(target)
                if url.scheme or url.netloc or "<" in target:
                    continue
                with self.subTest(file=relative_path, target=target):
                    path = ROOT / relative_path
                    if url.path:
                        path = path.parent / unquote(url.path)
                    self.assertTrue(path.exists(), f"Broken link: {path}")
                    if url.fragment and path.is_file():
                        headings = re.findall(
                            r"^#{1,6}\s+(.+)$",
                            path.read_text(encoding="utf-8"),
                            re.MULTILINE,
                        )
                        anchors = {
                            re.sub(r"[^\w\- ]", "", heading.lower()).replace(
                                " ", "-"
                            )
                            for heading in headings
                        }
                        self.assertIn(unquote(url.fragment), anchors)


if __name__ == "__main__":
    unittest.main()
