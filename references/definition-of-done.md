# Definition of Done

The project-wide standing bar every change clears — distinct from a task's
per-change acceptance criteria. `verify-before-done` and `ship-it` enforce this;
`performance-optimization` and `frontend-ui-engineering` pull the relevant
sections. Adapt the specifics to your stack, keep the spirit.

## Every change

- [ ] The originating spec/task acceptance criteria are met and checked off.
- [ ] New/changed behavior has tests that were seen red, then green.
- [ ] The **full** test suite passes (not just the new tests).
- [ ] Build/typecheck/lint are clean — no new warnings.
- [ ] The diff is atomic and reviewed; no dead code, stray TODOs, or debug logs.
- [ ] Commit messages state what and why and reference the spec/issue.
- [ ] Docs/ADRs updated if behavior, APIs, or decisions changed.

## Correctness & safety

- [ ] Edge cases handled: null/empty, boundaries, error paths.
- [ ] No regressions (full suite + affected runtime paths exercised).
- [ ] Risky changes are behind a feature flag or have a stated, tested rollback.

## Security (see [security-checklist.md](security-checklist.md))

- [ ] Untrusted input validated at boundaries; queries parameterized; output encoded.
- [ ] Authorization enforced server-side; no secrets in code/logs/VCS.
- [ ] New dependencies checked for known vulnerabilities.

## Accessibility (user-facing changes)

- [ ] Keyboard operable; visible, non-trapped focus order.
- [ ] Semantic HTML; every control has an accessible name/label.
- [ ] Color contrast meets WCAG 2.1 AA; not reliant on color alone.
- [ ] Loading, empty, and error states handled.
- [ ] Passes an automated a11y checker on the rendered page.

## Performance (when a budget applies)

- [ ] An explicit target exists (e.g. LCP < 2.5s, p95 latency, memory, bundle size).
- [ ] Measured before/after under realistic conditions; the target metric improved
      or held.
- [ ] No N+1 queries, unbounded fetches, or needless re-renders introduced.
- [ ] A budget/benchmark guards the metric where feasible.

## Observability (production code)

- [ ] Meaningful structured logs at the right level; no secrets in logs.
- [ ] Key operations emit metrics; failures are alertable on symptoms.

## Shipping

- [ ] PR explains the change and links verification evidence.
- [ ] CI fully green; no gates bypassed.
- [ ] Rollout plan and rollback are clear for anything risky.
- [ ] Learnings captured via `compound-learnings`.
