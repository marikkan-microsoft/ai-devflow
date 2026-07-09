---
name: browser-verification
description: Verifies web behavior against live runtime data using a browser / DevTools MCP — DOM, console, network, and performance. Use when building or debugging anything that runs in a browser, instead of assuming it works from the code.
---

# Browser Verification

## Overview

For anything that runs in a browser, the source code is a hypothesis and the
running page is the truth. This skill checks behavior against **live runtime
data** — the rendered DOM, console output, network traffic, and performance —
using a browser or a DevTools MCP integration, so "it should work" becomes "I saw
it work".

## When to Use

- Building or changing UI, client-side logic, or anything user-facing on the web.
- Debugging a browser issue (rendering, console errors, failed requests).
- Confirming an accessibility or performance concern with real data.

**When NOT to use:** Non-browser code. Use the test suite and `verify-before-done`
instead.

**Related:** Completes `frontend-ui-engineering`; supplies runtime evidence to
`verify-before-done`; supports `debug-root-cause` and `performance-optimization`
for browser issues.

## Process

### 1. Connect to the running app

Open the page (or connect the DevTools MCP) against a real running build. Verify
against the actual environment, not a mental model of it.

### 2. Exercise the behavior

Drive the real interaction — click, type, navigate, submit. Reproduce the exact
user path in question, including edge and error paths.

### 3. Read the runtime signals

Inspect the evidence:

- **DOM:** the rendered structure and state match expectations.
- **Console:** no unexpected errors or warnings.
- **Network:** requests fire with correct params; responses and status codes are
  as expected; no failed or duplicated calls.
- **Performance:** capture metrics when speed is in question (see
  `performance-optimization`).

### 4. Check accessibility live

Tab through with the keyboard, confirm visible focus and labels, and run an a11y
checker on the rendered page.

### 5. Capture the evidence

Record what you observed (values, screenshots, console/network excerpts) so
`verify-before-done` has concrete runtime proof, not an assertion.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The code looks right, it'll render fine." | Rendering surprises live in runtime. Open the page. |
| "Console warnings don't matter." | They're the app telling you what's wrong. Read them. |
| "I'll assume the request works." | Wrong params/duplicate calls hide there. Watch the network. |
| "Keyboard a11y is fine, probably." | Verify it — tab through and run a checker. |

## Red Flags

- You claimed UI works without opening it.
- Console errors/warnings are present and ignored.
- Network calls were never inspected.
- No runtime evidence was captured for the verification step.

## Verification

- The behavior was exercised in a real browser and observed to work.
- Console is clean (or remaining messages are understood and acceptable).
- Network requests/responses match expectations.
- Keyboard/a11y checked; runtime evidence captured for `verify-before-done`.
