---
type: question
author: agent
drafted: 2026-05-27
asked_by: autonomous_loop (P14 cycle, attempt 1)
related_problems: [14, 22]
status: open
related_concepts: []
cites:
  - src/einstein/optimizer_dispatch.py
  - scripts/autonomous_loop.py
---

# The inner-agent's prescribed EXECUTE command (`python -m einstein.optimizer_dispatch …`) is a silent no-op

## The question

The autonomous inner-agent task prompt instructs the LLM to execute optimizers with:

```
uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish
```

But `src/einstein/optimizer_dispatch.py` has **no `__main__` block, no argparse, no CLI**
(grep for `__main__|argparse|def main` → no matches). Running it as a module imports the
file, defines `dispatch()`, and exits 0 with **no output** — the `--problem-id`/`--strategy`
args land in `sys.argv` and are never read. What is the minimal fix so the prescribed
command actually dispatches?

## Why this is open (and why it bites)

- The *production* loop is fine: `scripts/autonomous_loop.py` calls `dispatch()` in-process,
  not via the `-m` CLI. So this is a **prompt ↔ tooling mismatch**, not a loop bug.
- The *inner agent* following the task literally cannot run an optimizer through the one
  Bash channel it's allowed (`Bash(uv run python -m einstein.optimizer_dispatch:*)`). Worse,
  the no-op **exits 0 with empty stdout**, which an agent could misread as "ran, no result"
  or even "succeeded." Silent-success-on-no-op is the dangerous failure mode (cf. axiom A1
  spirit: never trust a number — here, never trust a *silence*).
- This visit's P14 attempt 1 hit exactly this: the `-m` call returned nothing; the direct
  script run (`scripts/.../slsqp_polish.py`) is outside the allowlist and gated. Net: no
  sanctioned way for the inner agent to re-run compute. The score was recovered from the
  deterministic result file + test, not from a fresh dispatch.

## What an answer looks like

One of:

1. **Add a thin `__main__` CLI** to `optimizer_dispatch.py`:
   `argparse` for `--problem-id` (int, required), `--strategy` (str, optional),
   `--dry-run`; call `dispatch(...)`; print the `DispatchResult` as JSON to stdout and
   exit non-zero on `ok=False`. Smallest change; makes the documented command real.
2. **OR** change the inner-agent prompt + allowlist to invoke the per-problem script
   directly (`scripts/<slug>/<optimizer>.py`) — but that re-introduces the
   heterogeneous-CLI problem the dispatch layer was built to hide. Option 1 is preferred.
3. **OR** have the orchestrator pre-run the chosen dispatch and hand the inner agent the
   result file path, so the inner agent verifies rather than executes. Cleanest separation,
   but changes the loop contract.

Add a test asserting `python -m einstein.optimizer_dispatch --problem-id 14 --dry-run`
exits 0 and prints JSON with `optimizer == "slsqp_polish"`.

## Suggested next step

Land in a sibling branch (not this autonomous-loop branch). Until then, inner agents
should treat empty `-m optimizer_dispatch` output as "command is a no-op, fall back to the
deterministic result file + dispatch test," not as a successful run.

## Cross-refs

- [p14-strict-tol-wire-fix-confirms-float64-ceiling](../findings/p14-strict-tol-wire-fix-confirms-float64-ceiling.md)

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"The inner-agent's prescribed EXECUTE command `python") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
