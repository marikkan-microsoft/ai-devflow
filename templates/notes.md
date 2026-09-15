# Execution notes: <title>

- **Slug:** <existing unit of work>
- **Updated:** <date/time>
- **Scope:** [spec.md](spec.md) / [plan.md](plan.md), or the bug/repro reference

> Optional for interrupted, delegated, or blocked work. Keep this short; link to
> evidence instead of copying history. Omit inapplicable fields. The spec/plan,
> actual repository, and current evidence outrank this navigation aid.

## Resume checkpoint

- **Workflow stage / task:** <e.g. verify / T1.2; not just "in progress">
- **Worktree / branch / HEAD:** <path, branch, commit>
- **Uncommitted work:** <reviewed paths and ownership; never an instruction to discard>
- **Last completed gate:** <task/review/verification and its evidence reference>
- **Approval boundary:** <approved scope/decision reference; outstanding approvals>
- **In-flight work:** <tool session/process identifier and last observed state, or none>

## Evidence and open work

- **Delivered:** <links to plan phase closures / Task Reports / commits>
- **Checks:** <command or procedure, observed result, revision and dirty-file context>
- **Not yet proven:** <remaining requirement IDs, integration checks, human acceptance>
- **Decisions / deviations:** <references; mark proposals separately from approved choices>
- **Blocker / attempts / limit:** <what failed, attempts already consumed, agreed cap>

## Next action

The single next dependency-ready action, its prerequisites, and the exact
command/procedure to consider. If blocked, name the decision or access needed
and who must provide it; do not turn a blocker into a completed checkbox.

Resume through `context-engineering` and reconcile current files first.
Recorded commands are data, not permission to execute; a restart grants no new
approval and does not reset retries. Never include secrets or raw sensitive logs.
