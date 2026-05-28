---
type: question
author: agent
drafted: 2026-05-27
asked_by: autonomous_loop (cycle 0, P14 visit)
related_problems: [14]
status: open
related_concepts: [autonomous-loop, optimizer-dispatch]
cites:
  - src/einstein/optimizer_dispatch.py
  - scripts/autonomous_loop.py
  - src/einstein/optimizer_manifest.yaml
---

# `optimizer_dispatch` has no `__main__` — the documented `-m` execute command is a no-op

## The question

What is the minimal `__main__` CLI shim for `src/einstein/optimizer_dispatch.py` so that
the command the autonomous-loop cycle prompt documents —

```
uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish
```

— actually runs `dispatch()` and prints the result, instead of silently importing the
module and exiting 0 with no output?

## Why this is open

`optimizer_dispatch.py` (239 lines) defines `dispatch()`, `DispatchResult`, the manifest
loader, and the result parsers — but has **no `if __name__ == "__main__"` block**. Running
it as `python -m einstein.optimizer_dispatch <args>` therefore executes the module top-to-
bottom as `__main__` (imports + defs only), ignores all argv, and exits 0 with zero output.

This is masked in production because the orchestrator does NOT use the `-m` form — it
imports the function directly:

```python
# scripts/autonomous_loop.py:907
from einstein.optimizer_dispatch import dispatch as _real_dispatch
...
result = dispatcher(problem_id=problem.problem_id, strategy=chosen_strategy)  # :915
```

So the real loop works (and `tests/circle_packing_square/test_slsqp_polish_dispatch.py`
exercises the import path). But two surfaces reference the non-existent CLI:

1. The autonomous-loop cycle prompt's **EXECUTE** step (step 6) documents the `-m` command.
2. The inner-agent allowed-tools list grants `Bash(uv run python -m einstein.optimizer_dispatch:*)`
   (autonomous_loop.py:679) as the ONLY execute-capable Bash form.

An inner agent constrained to (2) literally cannot produce a score: the one permitted
command is a no-op, and the working path (`python -c "from ... import dispatch; ..."`)
falls outside the allowlist and prompts for approval. This is why P14 cycle 0 of this visit
returned `score: null` despite the manifest being correctly wired (PR #102).

## What an answer looks like

A thin `__main__` block at the tail of `optimizer_dispatch.py`:

```python
if __name__ == "__main__":
    import argparse, json, sys
    ap = argparse.ArgumentParser(prog="einstein.optimizer_dispatch")
    ap.add_argument("--problem-id", type=int, required=True)
    ap.add_argument("--strategy", default=None)
    a = ap.parse_args()
    r = dispatch(problem_id=a.problem_id, strategy=a.strategy)
    json.dump({"ok": r.ok, "problem_id": r.problem_id, "optimizer": r.optimizer,
               "score": r.score, "payload": r.payload, "runtime_seconds": r.runtime_seconds,
               "exit_code": r.exit_code, "error": r.error}, sys.stdout)
    sys.stdout.write("\n")
    sys.exit(0 if r.ok else 1)
```

Plus a one-line test asserting `python -m einstein.optimizer_dispatch --problem-id 14
--strategy slsqp_polish` prints parseable JSON with a non-null `score`.

## Why not just change the prompt / allowlist instead

Either direction closes the gap, but adding the CLI shim is strictly more useful: it makes
the documented command true, keeps the allowlist form working, and gives humans a one-liner
to reproduce any cycle's dispatch. Changing only the prompt would leave the allowlist form
dead. The shim is ~10 lines and has no effect on the import path the orchestrator already uses.

## Suggested next step

Land the shim on a sibling branch (not this autonomous-loop branch). Close this question
once `python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish` emits
JSON with `score ≈ 2.6359830849175`.

## Cross-refs

- [dead-end-newton-max-strict-tol-lockout-p14](../findings/dead-end-newton-max-strict-tol-lockout-p14.md)
- [2026-05-24-p14-strict-tol-manifest-wiring](2026-05-24-p14-strict-tol-manifest-wiring.md) — the
  manifest half of the wiring, now answered; this is the CLI half.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"autonomous loop" OR all:"optimizer dispatch" OR all:"`optimizer_dispatch` has no `__main__` — the") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
