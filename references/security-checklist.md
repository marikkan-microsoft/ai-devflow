# Security Checklist

Pulled in by `security-hardening` and the `security-auditor` persona. Maps to the
OWASP Top 10. Not exhaustive — a floor, not a ceiling.

## Input handling

- [ ] Validate/normalize untrusted input **at the boundary**; prefer allow-lists.
- [ ] Enforce type, length, range, and format before use.
- [ ] Treat all external data as untrusted: request bodies, params, headers,
      cookies, file uploads, and third-party API responses.

## Injection

- [ ] **Parameterize** every database query — never string-concatenate SQL/NoSQL.
- [ ] Avoid shell-outs with user data; if unavoidable, use argument arrays, not
      string commands.
- [ ] **Encode output** for its sink (HTML, attribute, URL, JS, shell) to prevent
      XSS/injection.
- [ ] Avoid `eval`/dynamic template rendering on untrusted input.

## Authentication & session

- [ ] Strong, standard auth; no home-rolled crypto or password hashing.
- [ ] Session tokens are random, expiring, and invalidated on logout.
- [ ] Sensitive actions re-verify identity; rate-limit auth endpoints.

## Access control

- [ ] Authorization enforced **server-side** on every protected operation.
- [ ] Check ownership per object (prevent IDOR); never trust client-supplied IDs
      or roles.
- [ ] Fail **closed** (deny by default).

## Secrets & data

- [ ] No secrets in code, logs, error messages, or version control.
- [ ] Secrets come from env/secret managers; rotate on exposure.
- [ ] Encrypt sensitive data in transit (TLS) and at rest where required.
- [ ] Least-privilege credentials for services and databases.

## Configuration & headers

- [ ] Security headers set (CSP, HSTS, X-Content-Type-Options, etc. as applicable).
- [ ] CORS scoped to known origins; no wildcard with credentials.
- [ ] Errors don't leak stack traces, versions, or internal paths to users.

## Dependencies & supply chain

- [ ] New/updated dependencies scanned for known CVEs.
- [ ] Pin versions; review what a dependency actually does before adding it.
- [ ] Minimize the dependency surface.

## Verification

- [ ] Abuse-case tests exist: rejected malformed input, denied access, no secret
      leakage.
- [ ] `security-auditor` reviewed changes touching a trust boundary.
