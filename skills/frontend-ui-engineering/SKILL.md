---
name: frontend-ui-engineering
description: Builds user-facing interfaces with sound component architecture, state management, and accessibility. Use when creating or modifying UI — components, design-system usage, responsive layout, or accessible interactions.
---

# Frontend UI Engineering

## Overview

UI is where correctness meets humans. This skill builds interfaces that are
well-architected (composable components, clear state ownership), consistent (design
system, not one-off styles), responsive, and **accessible by default** (WCAG 2.1
AA). Accessibility and state discipline are designed in, not bolted on.

## When to Use

- Building or modifying components and views.
- Implementing responsive layouts or design-system usage.
- Any user-facing interaction, form, or navigation.

**When NOT to use:** Backend-only or non-visual changes.

**Related:** Pairs with `browser-verification` for runtime checks, `test-driven-development`
for component logic, and `accessibility` items in
[references/definition-of-done.md](../../references/definition-of-done.md).

## Process

### 1. Model components and state

Decompose into components with a single responsibility and a clear prop contract.
Decide **where state lives** — local, lifted, or shared — and keep a single source
of truth. Derive, don't duplicate, state.

### 2. Use the design system

Reach for existing tokens, primitives, and patterns before inventing styles.
One-off styling is drift; consistency is a feature.

### 3. Build accessible by default

Semantic HTML first; ARIA only to fill gaps. Ensure keyboard operability, visible
focus, labels for every control, sufficient color contrast, and correct roles.
Accessibility is a requirement, not a nice-to-have.

### 4. Make it responsive and resilient

Design for the range of viewports and for loading, empty, and error states — not
just the happy path with ideal data.

### 5. Verify at runtime

Confirm behavior in a real browser with `browser-verification`: interaction,
console cleanliness, and an accessibility pass (keyboard + a checker).

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll add accessibility later." | Later means never and a rebuild. Semantic + keyboard from the start. |
| "One-off styles are quicker." | They fragment the system and compound. Use the design system. |
| "State can live wherever." | Duplicated state desyncs. One source of truth. |
| "It looks right in my viewport." | Users aren't all on your screen. Handle the range + edge states. |

## Red Flags

- `div`/`span` used where semantic elements belong; controls with no labels.
- Interactions that can't be driven by keyboard; focus is invisible or trapped.
- The same state stored in two places.
- No loading/empty/error states.

## Verification

- Components have single responsibilities and a clear state owner.
- Keyboard-operable, labeled, sufficient contrast; passes an a11y checker.
- Responsive across target viewports; loading/empty/error states handled.
- Runtime-verified in a browser with a clean console.
