---
title: <short problem statement>
slug: <kebab-slug>
date: <yyyy-mm-dd>
tags: [<area>, <symptom>, <tech>]
severity: low | medium | high
---

# <short problem statement>

> A compounding learning. The next time this class of problem appears, this note
> should turn hours of rediscovery into minutes. Keep it searchable and specific.

## Symptom

What was observed — the error, the failing behavior, the surprising result.
Include the exact message/stack if there was one.

## Root cause

The actual underlying cause (not the surface symptom). Reference `file:line`.

## Fix

What changed and why it works. Link the commit/PR. Include the minimal diff idea.

## How to recognize it next time

The tell-tale signs that point at this cause, so future-you (or another agent)
can jump straight here.

## Guardrail

The test, lint rule, type, assertion, or check added so this cannot silently
regress. If none, say why.

## Reuse & promotion (optional)

Omit when the sections above already make these boundaries clear. Existing notes
need no migration.

- **Applies / does not apply:** the contexts and counterexample that bound reuse.
- **Evidence:** current code/check receipt, checked revision or dirty state, and
  date. Separate observed results from unavailable or stale proof.
- **Promotion:** none by default. If a lesson recurs, name an existing
  skill/reference, supporting occurrences, and the scope/approval still needed.
  A proposal does not authorize shared or global instruction changes.

## Related

Links to `adr/*.md`, other `solutions/*.md`, docs, or upstream issues.
