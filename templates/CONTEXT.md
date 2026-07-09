# CONTEXT.md — <project> shared language

> The project's **domain model / ubiquitous language**. When agent and humans use
> the same words, code is named consistently, the codebase is easier to navigate,
> and the agent spends fewer tokens decoding jargon. Maintained by
> `domain-modeling`; read by every skill.

## Glossary

Define the domain terms precisely. Prefer the words the business/users actually
use. Each term: a one-line definition and, where useful, what it is **not**.

| Term | Definition | Not to be confused with |
| --- | --- | --- |
| <Term> | <precise one-line meaning> | <adjacent term> |

## Core concepts

Short prose on the central entities and how they relate. A small diagram helps.

## Boundaries & modules

The main modules/services, each described as a **deep module** — a lot of
capability behind a small, stable interface — and the seam it sits behind.

| Module | Interface (the small surface) | Hides (the depth) |
| --- | --- | --- |
| <name> | <public API> | <internal complexity> |

## Naming conventions

Project-specific naming rules so generated code matches existing code (casing,
file layout, test naming, event/DTO conventions).

## Decisions

Link the ADRs that shaped this vocabulary (they live alongside this file under
`adr/`).
