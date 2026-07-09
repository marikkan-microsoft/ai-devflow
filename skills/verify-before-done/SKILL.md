---
name: verify-before-done
description: Gates any claim of completion behind concrete evidence. Use before saying a task is done, before review, or before shipping — to prove the work with tests, build output, and runtime data rather than assertion.
---

# Verify Before Done

## Overview

"Done" is a claim that requires proof. This skill is the gate every task passes
before it can be called complete: it demands **evidence** — a green test run, a
clean build, runtime data, the artifact at its path — not the agent's confidence.
It exists specifically to defeat the "seems right, moving on" failure mode.

## When to Use

- Before declaring any task or change complete.
- Before handing off to `review-code` or `ship-it`.
- After a fix, to confirm it actually fixed the thing (and broke nothing).

**When NOT to use:** Never skip it. If a check is genuinely impossible, that
absence is itself a finding to report, not a reason to bypass the gate.

**Related:** The exit gate after the build skills; precedes `review-code` and
`ship-it`. Standing bar in
[references/definition-of-done.md](../../references/definition-of-done.md).

## Process

### 1. Restate what "done" means here

Pull the acceptance criteria from `plan.md`/`spec.md` (or the bug's reproduction).
Done is *those* criteria met — not "it runs".

### 2. Gather evidence, don't assert

For the change, collect and actually look at:

- **Tests:** run the full suite. Paste/note the summary. New behavior has a test
  that was red then green.
- **Build:** compile/typecheck clean.
- **Runtime:** where behavior is observable, exercise it and capture the result
  (output, `browser-verification` data, logs).
- **Artifacts:** the expected file exists at its path (spec/research/plan/solution).

### 3. Check the criteria off explicitly

Walk each acceptance criterion / success criterion and mark it met or not, with
the evidence beside it. An unmet criterion means **not done**.

### 4. Look for collateral damage

Confirm no regressions (full suite, not just the new test), no new warnings/lint
errors, and nothing left half-done or commented out.

### 5. Report honestly

State what was verified, how, and anything you could **not** verify. Unverifiable
gaps are surfaced, never hidden.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "It looks correct." | Looking ≠ proving. Run it. |
| "I ran the new test, that's enough." | Regressions hide in the rest. Run the full suite. |
| "The build probably passes." | "Probably" isn't evidence. Build it. |
| "I'll note it's untested but done." | Untested behavior isn't done. Test or flag as incomplete. |

## Red Flags

- "Done" with no test/build output cited.
- Only the new test was run, not the full suite.
- Acceptance criteria weren't checked one by one.
- Known gaps are omitted from the report.

## Verification

- Full test suite run and green; build clean.
- Every acceptance/success criterion checked off with evidence.
- Observable behavior exercised and captured.
- Any unverifiable items explicitly reported.
