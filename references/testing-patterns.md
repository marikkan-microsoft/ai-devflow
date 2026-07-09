# Testing Patterns

Reference pulled in by `test-driven-development` and `test-engineer`. Language-
agnostic; translate the examples to your stack.

## What a good test is

- Verifies **behavior through a public interface**, not implementation details —
  so it survives refactors. If a pure refactor breaks the test, the test was
  coupled to internals.
- Reads like a **specification**: the name states the capability
  ("user can check out with a valid cart").
- Is **deterministic**: no reliance on time, ordering, network, or randomness
  unless controlled.

## The test pyramid

```
        ╱╲        E2E (~5%)      — few, slow, full-stack; critical journeys only
       ╱──╲       Integration    — some; modules + real boundaries (db, http)
      ╱────╲      (~15%)
     ╱──────╲     Unit (~80%)    — many, fast, isolated; logic and edge cases
    ╱────────╲
```

Invert this at your peril: an E2E-heavy suite is slow, flaky, and expensive to
maintain.

## Structure: Arrange–Act–Assert

```
// Arrange — set up the world
// Act     — perform the one behavior under test
// Assert  — verify the observable outcome
```

One behavior per test. Multiple unrelated assertions hide which contract broke.

## DAMP over DRY (in tests)

Descriptive And Meaningful Phrases beat Don't-Repeat-Yourself. A little
duplication that keeps each test readable in isolation is better than a clever
shared abstraction that makes failures hard to diagnose. Extract *setup* helpers;
don't hide the *intent*.

## The Prove-It pattern (bug fixes)

1. Write a test that reproduces the bug — it must **fail**.
2. Fix the code — the test **passes**.
3. Run the full suite — no regressions.
   The reproduction test stays forever as the guardrail.

## Edge cases to reach for

- Empty / null / missing inputs.
- Boundaries: 0, 1, max, off-by-one.
- Error and failure paths (not just the happy path).
- Concurrency / ordering where relevant.
- Unicode, timezones, and locale for text and dates.

## Anti-patterns

- **Testing the mock** — over-mocking until the test only proves the mock was
  called. Assert real outcomes.
- **Assertion-free tests** — code runs, nothing is verified. Green but worthless.
- **Brittle snapshot everything** — huge snapshots that get blindly re-approved.
- **Implementation-coupled tests** — assert private state; break on refactor.
- **Slow unit tests** — hidden I/O; keep units in-memory and fast.
- **Shared mutable fixtures** — tests that pass alone but fail together.
