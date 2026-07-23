# Constitution: &lt;project&gt;

> The project's **binding principles** — the standing, project-specific rules
> every change must respect. Distinct from `CONTEXT.md` (shared *vocabulary*),
> ADRs (individual *decisions*), and `/references/` (devflow's *generic*
> standards): this file is where **your** non-negotiables live. Authored and
> maintained by `domain-modeling`; enforced by `analyze-artifacts` (pre-build)
> and `review-code` (post-build).

## Core principles

Number them. Each principle is **declarative and testable** — state it as a rule
that can be checked, not an aspiration. Mark the ones that are **NON-NEGOTIABLE**;
those are hard gates. Prefer MUST / MUST NOT over "should". For each, one line of
rationale so a future reader knows *why* before proposing an amendment.

- **P1 — &lt;name&gt; (NON-NEGOTIABLE)** — &lt;the rule, as a MUST&gt;.
  _Why:_ &lt;one line&gt;.
  <!-- e.g. "P1 — Test-Backed Change (NON-NEGOTIABLE) — Every behavioral change
       MUST land with a test seen red then green. Why: prevents silent regressions." -->
- **P2 — &lt;name&gt;** — &lt;the rule&gt;. _Why:_ &lt;one line&gt;.
- **P3 — &lt;name&gt;** — &lt;the rule&gt;. _Why:_ &lt;one line&gt;.

## Additional constraints

Project-wide standards that aren't a single principle but still bind every change
— e.g. security requirements, performance budgets (P95 latency, bundle size),
data-handling rules ("money as integer cents"), dependency policy ("no new
runtime dependency without an ADR").

## Governance

- This constitution **supersedes** ad-hoc preference. A change that conflicts with
  a NON-NEGOTIABLE principle is a **Critical** finding — resolve it by changing the
  spec/plan/code, not by diluting the principle.
- **Amendments** require an ADR (context, the change, consequences) and a version
  bump below. Supersede a principle rather than silently rewriting it.

---

**Version:** 1.0.0 · **Ratified:** &lt;yyyy-mm-dd&gt; · **Last amended:** &lt;yyyy-mm-dd&gt;
