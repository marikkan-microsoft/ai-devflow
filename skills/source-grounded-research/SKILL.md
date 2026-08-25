---
name: source-grounded-research
description: Grounds framework and library decisions in official documentation and primary sources, with citations. Use when working with an unfamiliar framework/API, verifying how something actually behaves, or when correctness depends on authoritative sources.
---

# Source-Grounded Research

## Overview

Agents confidently invent API signatures, config options, and behaviors that
don't exist. This skill forces framework/library decisions to be grounded in
**official documentation and primary sources**, cited, with anything unverified
explicitly flagged. It's how you get authoritative, source-cited code instead of
plausible-looking fiction.

## When to Use

- Using an unfamiliar framework, library, or external API.
- A decision hinges on how something *actually* behaves (not how you recall it).
- Version-specific behavior matters.
- Answering a research question whose answer must be trustworthy.

**When NOT to use:** Well-trodden code in a stack you can verify locally by running
it, or logic with no external-dependency uncertainty.

**Related:** Complements `research-codebase` (internal facts) with external facts.
Findings worth keeping become `docs/devflow/solutions/*.md` or feed `write-spec`.
Uses `awesome-copilot-discovery` only when the research method itself needs
specialist guidance.

## Process

### 1. Frame the question

State precisely what you need to know and the version/context it applies to.

### 2. Go to primary sources

Prefer, in order: official docs → the library's source/types → maintainers'
release notes → reputable references. Treat blog posts and forum answers as leads
to verify, not authority.

### 3. Capability hook (conditional)

If the research needs a specialized method not present locally (for example,
formal threat modeling or a vendor-specific migration inventory), invoke
`awesome-copilot-discovery` with that exact gap. Use at most one accepted, pinned
resource. It may guide the method, but it is not a primary source: verify every
external claim it contributes against authoritative material.

### 4. Verify, then cite

For each claim you'll rely on, capture the source (URL/section, version). If you
can, confirm behavior with a tiny local check (a REPL snippet, a type probe).

### 5. Flag the unverified

Anything you could not confirm is labeled **UNVERIFIED** explicitly — never
smoothed over as fact. Distinguish "the docs say X" from "I assume X".

### 6. Record findings

Summarize the answer with citations. If it's a durable, reusable finding, write a
`solutions/` note so the next run doesn't re-research it.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'm pretty sure the API is like this." | "Pretty sure" ships bugs. Check the docs. |
| "The docs take too long." | Debugging invented APIs takes longer. |
| "This blog post confirms it." | Blogs go stale and are wrong. Verify against primary sources. |
| "I'll just try until it compiles." | Compiling ≠ correct. Ground it. |

## Red Flags

- You wrote an API call from memory without checking signatures.
- You treated an Awesome Copilot resource as evidence rather than methodology.
- Claims cite a forum answer as the sole authority.
- Version-specific behavior is assumed to match your training data.
- "UNVERIFIED" appears nowhere despite genuine uncertainty.

## Verification

- Every relied-upon external claim has a primary-source citation.
- Any discovered specialist resource has a pinned source and a recorded fit
  decision; its factual claims were independently verified.
- Version/context is recorded for version-sensitive facts.
- Unverified points are explicitly flagged.
- Reusable findings are captured in `solutions/` where warranted.
