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

## Related

Links to `adr/*.md`, other `solutions/*.md`, docs, or upstream issues.
