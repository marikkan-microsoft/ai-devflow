---
name: api-and-interface-design
description: Designs APIs and module boundaries contract-first, with explicit error semantics and boundary validation. Use when designing a public interface, module boundary, API endpoint, or any contract other code will depend on.
---

# API and Interface Design

## Overview

Interfaces are the most expensive thing to change because others depend on them.
This skill designs them **contract-first** — the shape and semantics before the
implementation — accounting for how they'll be misused (Hyrum's Law: every
observable behavior becomes something a consumer relies on). A small, well-chosen
interface hiding a deep implementation is the goal.

## When to Use

- Designing a public API, endpoint, or protocol.
- Defining a module boundary or a package's public surface.
- Any contract other code (or teams, or external users) will depend on.

**When NOT to use:** Purely internal helpers with a single call site and no
stability expectation.

**Related:** Pairs with `domain-modeling` (vocabulary + ADRs) and
`test-driven-development` (contract tests). Record boundary decisions as ADRs.

## Process

### 1. Define the contract first

Specify inputs, outputs, types, and the operations — the **small surface** — before
writing the implementation. Design the interface you wish you had to call.

### 2. Nail the error semantics

Define what happens on every failure: error types, status codes, partial failure,
idempotency, retries, and timeouts. Errors are part of the contract, not an
afterthought.

### 3. Validate at the boundary

Untrusted input is validated and normalized **at the interface**, once, so the
core can trust its inputs. Never let unvalidated data past the boundary.

### 4. Design against Hyrum's Law

Assume every observable behavior — ordering, timing, error text — will be depended
on. Hide what you don't want to guarantee. Keep the surface minimal so there's
less to accidentally promise.

### 5. Version deliberately (One-Version rule)

Prefer one supported version of a contract over parallel forks. Plan evolution:
additive changes, deprecation paths, and compatibility guarantees up front.

### 6. Write contract tests

Pin the contract with tests (via `test-driven-development`) so changes that break
consumers fail loudly. Record the shape and its rationale in an ADR.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll design the API as I implement." | Implementation leaks into the contract and locks in accidents. Contract first. |
| "Errors are edge cases, later." | Consumers integrate against errors first. Define them now. |
| "Validate deeper, not at the edge." | Unvalidated input corrupts the core. Validate at the boundary. |
| "Expose it all for flexibility." | Every exposed detail becomes a promise (Hyrum). Keep it small. |

## Red Flags

- The interface mirrors the implementation's internal structure.
- Error behavior is undefined or inconsistent across operations.
- Validation is scattered through the core instead of at the boundary.
- The public surface is large "just in case".

## Verification

- The contract (inputs, outputs, errors) is specified before implementation.
- Boundary validation exists and is tested.
- Contract tests pin the intended behavior.
- The interface is minimal; evolution/versioning is documented in an ADR.
