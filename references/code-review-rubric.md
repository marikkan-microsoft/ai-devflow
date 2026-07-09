# Code Review Rubric

Pulled in by `review-code`. Devflow reviews on **two independent axes** run in
parallel so they don't contaminate each other, then synthesized into one verdict.

## The two axes

| Axis | Persona | The question | Ignores |
| --- | --- | --- | --- |
| **Spec** | `spec-auditor` | Does it do what was asked — completely, exactly, nothing extra? | Style/quality |
| **Standards** | `code-reviewer` | Is the code good — correct, readable, sound, secure, fast? | "Is it what was asked" |

Run both against a **fixed baseline** (the diff since branch base or last reviewed
commit). Add `security-auditor` / `performance-auditor` to the fan-out when the
change warrants.

## Severity labels

| Label | Meaning | Effect on verdict |
| --- | --- | --- |
| **Critical** | Security hole, data loss, broken functionality, missing requirement | Blocks — REQUEST CHANGES |
| **Important** | Missing test, wrong abstraction, poor error handling | Should fix before merge |
| **Suggestion** | Naming, style, optional optimization | Optional |

Every Critical/Important finding carries a specific fix and a `file:line`.

## Change sizing

- Prefer diffs under ~a few hundred lines; small changes get better reviews.
- Flag oversized diffs and suggest a split (by layer, by slice, or prep-then-change).
- A large mechanical change (rename, format) is fine if isolated in its own commit.

## Synthesis

1. Merge both axis reports.
2. Any Critical → **REQUEST CHANGES**; otherwise weigh Important findings.
3. State one **verdict**: APPROVE | REQUEST CHANGES.
4. Always name at least one thing done well — specific praise reinforces patterns.
5. Route blockers back through the build loop, or to `resolve-pr-feedback` for PRs.

## Reviewer norms

- Review the **tests first** — they reveal intent and coverage.
- Read the **spec/task** before the code.
- Be timely: a fast, focused review beats a perfect late one.
- Critique the code, not the author; give reasons, not just verdicts.
- When unsure, ask or suggest investigation — don't guess in a comment.
