# Research: <title>

- **Slug:** <kebab-slug>
- **For spec:** [spec.md](spec.md)
- **Date:** <yyyy-mm-dd>

> Goal: document how the system works **today** in the area this change touches,
> with exact file:line references, so planning and implementation don't have to
> rediscover it. Facts, not plans.

## Summary

Three to five sentences: the current behavior, the key components involved, and
the main constraint or risk the change must respect.

## Relevant components

| Component | Path | Responsibility |
| --- | --- | --- |
| <name> | `src/...:L10-L80` | <what it does> |

## Current behavior / control flow

Walk the path the code takes today. Reference exact `file:line`. Include a small
diagram if it clarifies.

## Data & contracts

Schemas, types, API shapes, events, invariants that must be preserved.

## Integration points & dependencies

What calls this, what this calls, external services, feature flags.

## Constraints, risks & unknowns

- Constraint: …
- Risk: …
- Unknown (needs a spike): …

## Prior art

Related `solutions/*.md`, ADRs, and past changes in this area worth reusing.
