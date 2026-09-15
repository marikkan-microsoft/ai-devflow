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

## Boundary map

For cross-boundary work; omit when the existing path is already clear.

| Producer / consumer | Current contract (file:line) | Unproven assumption | Read-only prerequisite / proof needed |
| --- | --- | --- | --- |
| <components> | <interface, data, error semantics> | <unknown integration behavior> | <safe check or bounded spike> |

## Planning inputs

Classify findings as **constraint**, **assumption**, **option**, or **deferred**.
Link locked decisions/ADRs and name which unknown could invalidate the approach.
An option is not an approved requirement; mark any scope decision for its owner.
If singular/plural, required/optional, or derived/chosen assumptions changed,
identify the affected domain invariant rather than guessing at a new model.

## Constraints, risks & unknowns

- Constraint: …
- Risk: …
- Unknown (needs a spike): …

## Prior art

Related `solutions/*.md`, ADRs, and past changes in this area worth reusing.
