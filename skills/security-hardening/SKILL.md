---
name: security-hardening
description: Prevents the OWASP Top 10 and hardens auth, secrets, and dependencies. Use when handling user input, authentication/authorization, data storage, external integrations, or any security-sensitive change.
---

# Security Hardening

## Overview

Security is designed in at the boundaries, not patched on after a breach. This
skill applies a consistent defense against the **OWASP Top 10** — validating
untrusted input, parameterizing queries, encoding output, enforcing
auth/authorization, keeping secrets out of code, and auditing dependencies — for
any change that touches a trust boundary.

## When to Use

- Handling user input, file uploads, or deserialization.
- Authentication, authorization, sessions, or access control.
- Data storage, queries, or external/third-party integrations.
- Adding dependencies or handling secrets/tokens.

**When NOT to use:** Changes with no trust boundary or sensitive data at all — but
be honest about whether that's really true.

**Related:** Feeds the `security-auditor` persona and `review-code`. Checklist in
[references/security-checklist.md](../../references/security-checklist.md).

## Process

### 1. Map the trust boundaries

Identify where untrusted data enters (requests, params, headers, files, external
responses) and what sensitive assets are in reach (PII, credentials, money).

### 2. Validate and encode

Validate/normalize input **at the boundary** (allow-lists over deny-lists).
**Parameterize** every query — never build SQL/commands by string concatenation.
**Encode output** for its sink (HTML, URL, shell) to stop injection/XSS.

### 3. Enforce authn/authz correctly

Check authorization on **every** protected operation, server-side, per object
(guard against IDOR). Fail closed. Don't trust client-side checks or hidden
fields.

### 4. Protect secrets and data

Keep secrets out of code, logs, and version control — use env/secret managers.
Use vetted crypto libraries, not hand-rolled. Enforce transport security and least
privilege on data access.

### 5. Audit dependencies

Check new/updated dependencies for known vulnerabilities; pin and update
deliberately. Minimize the dependency surface.

### 6. Verify the hardening

Add tests for the abuse cases (rejected input, denied access, no secret leakage),
and have `security-auditor` review the change.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Input's probably fine, it's internal." | Internal boundaries get crossed. Validate anyway. |
| "String-building this query is easier." | That's the injection. Parameterize. |
| "The UI already blocks that." | Client checks are bypassable. Enforce server-side. |
| "I'll rotate the secret later." | A committed secret is already compromised. Never commit it. |

## Red Flags

- Untrusted input reaches a query/command/DOM without validation or encoding.
- Authorization is checked in the client, or not per object.
- Secrets appear in code, logs, or config committed to git.
- New dependencies were added with no vulnerability check.

## Verification

- Inputs validated at boundaries; queries parameterized; output encoded.
- Authorization enforced server-side on every protected operation.
- No secrets in code/logs/VCS; crypto uses vetted libraries.
- Dependencies audited; abuse-case tests pass; `security-auditor` reviewed it.
