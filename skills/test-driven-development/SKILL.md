---
name: test-driven-development
description: Drives development with tests using a red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior — write a failing test before the code that makes it pass.
---

# Test-Driven Development

## Overview

Write a failing test before the code that makes it pass. Tests are **proof** —
"seems right" is not done. For bugs, reproduce with a failing test before fixing.
A codebase with good tests is an agent's superpower; one without is a liability.
This skill is the loop that produces tests worth keeping.

## When to Use

- Implementing any new logic or behavior.
- Fixing any bug (the Prove-It pattern).
- Modifying or refactoring existing functionality.
- Adding edge-case handling.

**When NOT to use:** Pure config, docs, or static-content changes with no
behavioral impact.

**Related:** Invoked per slice by `incremental-implementation` and
`subagent-driven-implementation`. Runtime/UI checks pair with
`browser-verification`. Details in
[references/testing-patterns.md](../../references/testing-patterns.md).

## Process

### The loop

```
   RED                 GREEN                REFACTOR
Write a failing   Write the minimum    Clean up with the
test that pins ─▶ code to pass it   ─▶ tests still green ─▶ (repeat)
the behavior       (no more)            (no behavior change)
```

### Step 1 — RED

Write the test first; run it; watch it **fail** for the right reason. A test that
passes immediately, or fails on a typo, proves nothing. The test should read like
a specification of the behavior ("user can checkout with a valid cart").

### Step 2 — GREEN

Write the **minimum** code to make it pass. Resist building beyond the test
(YAGNI). Run the test; watch it pass.

### Step 3 — REFACTOR

With the test green, improve names, remove duplication, and clarify structure —
**without changing behavior**. Re-run tests after each refactor.

### The Prove-It pattern (bugs)

Do **not** start by fixing. Start by writing a test that reproduces the bug and
**fails** (confirming the bug). Then fix until it passes. Then run the full suite
to prove no regression. The reproduction test becomes the permanent guardrail.

### Test quality rules

- **Test behavior through public interfaces**, not implementation details — so
  tests survive refactors.
- **Follow the pyramid:** mostly small/fast unit tests, fewer integration, very
  few E2E.
- **DAMP over DRY** in tests: a readable test that repeats itself beats a clever
  abstract one.
- Name tests as capabilities, and use `CONTEXT.md` vocabulary.
- For a prohibition or validation gate, use a deliberately invalid fixture
  **and a valid control**. Prove rejection is caused by the intended violation,
  not broken setup; then prove allowed behavior still passes. Do not copy an
  executor's "failed first" claim as evidence of a run.

### Discipline

Any code written **before** its test is suspect — delete it and re-derive it from
a failing test, or at minimum retrofit a failing test that would have caught its
absence.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll add tests after it works." | After never comes, and the test just mirrors the code. Test first. |
| "This is too simple to test." | Simple code breaks too, and the test is cheap. Write it. |
| "The test passed first try — good." | Then it wasn't RED first; it may prove nothing. Make it fail first. |
| "I'll fix the bug, then maybe a test." | Without a failing repro you can't prove the fix. Prove-It first. |
| "Tests should be DRY like prod code." | Over-abstracted tests hide intent and break together. DAMP. |

## Red Flags

- Code exists with no test, or a test that never failed.
- Tests assert on private internals and break on every refactor.
- A bug was "fixed" with no reproducing test.
- The suite is red and you're moving on anyway.

## Verification

- Every behavior change has a test that was seen to fail, then pass.
- Bug fixes include a reproduction test that failed before the fix.
- The full suite is green and the build compiles.
- Tests verify behavior via public interfaces, not implementation.
