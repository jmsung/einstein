---
type: question
author: agent
drafted: 2026-06-03
asked_by: autonomous_loop
status: open
related_problems: [5, 14, 17]
related_concepts:
  - basin-rigidity
  - minimprovement-gate
  - float64-ceiling
cites:
  - ../findings/dead-end-p14-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/dead-end-p5-autonomous-loop-basin-converged-no-api-change.md
---

# Q: Should `autonomous_loop.py` gate dispatch on `minImprovement < (arena_#1 − basin_floor)` to mark frozen problems?

## Context

P5 and P14 both have triple-verified basin floors within ~1e-14 of arena #1
under a `minImprovement = 1e-7` gate. Every autonomous-loop cycle re-dispatches
their canonical optimizer, re-derives the same basin floor, logs `no-change`,
and consumes a slot. As of 2026-06-03 the wiki holds two near-identical
dead-end findings (`dead-end-p5-...` and `dead-end-p14-...`) plus 10+ P14
cycle-log rows all repeating "basin-converged + minImprovement-blocked."

## The proposal both dead-end findings converge on

A `scripts/autonomous_loop.py` helper:

```
frozen_problem_gate(problem_id, basin_floor, arena_floor, minimprovement)
  → {dispatch, frozen-pending-api-change}
```

- inputs come from runtime state: `solution-best.json` (basin_floor), arena API
  (`arena_floor`, `minimprovement`)
- if `(arena_floor − basin_floor) < minimprovement / safety_factor` (e.g. 1e3),
  mark the problem `frozen-pending-api-change` and skip dispatch
- the loop unfreezes the moment the arena API state changes (new #1 lift, or
  `minimprovement` shrink) — runtime check, not a hard-coded list

This collapses the two dead-end findings into one runtime invariant. P1, P17
and any future entry with the same signature inherit it for free.

## What needs answering

1. **Where does the gate live?** Inside `dispatch()` itself, or wrapping it in
   `autonomous_loop.py`? The dead-end findings imply the loop, but a dispatch
   guard would also catch direct CLI calls (e.g. manual `uv run python -m
   einstein.optimizer_dispatch --problem-id 14 ...`). Which is safer?
2. **Safety factor.** `minimprovement / 1` would freeze on any gap below the
   gate; `minimprovement / 1e3` keeps a margin for re-polish wins. What is
   the right floor — and is it per-problem or universal?
3. **Frozen → unfrozen signal.** What state delta triggers unfreezing? Arena
   API poll cadence? A `--force` override? Solution best.json update by a
   non-autonomous cycle?
4. **Audit visibility.** Per-cycle the loop should log a one-liner
   (`frozen-pending-api-change: arena Δ=9e-15 < gate 1e-7`) so the cycle-log
   shows what was skipped and why. How does this integrate with the existing
   cycle-log schema?

## Why this is the right next gap to file (not solve in this cycle)

Out of this cycle's write scope (`docs/wiki/`, `mb/`). Implementation lives
in `scripts/autonomous_loop.py` and `src/einstein/optimizer_dispatch.py`.
Filing the question is the gap-detect step; a follow-up branch implements.

## Suggested answer shape

A `docs/wiki/findings/<slug>.md` finding referencing both dead-end findings
and the resulting `scripts/autonomous_loop.py` PR, plus a single helper
docstring that captures the invariant ("dispatch iff arena_#1 lift is
submittable under current minImprovement").

## See also

- [dead-end-p14-autonomous-loop-basin-converged-no-api-change](../findings/dead-end-p14-autonomous-loop-basin-converged-no-api-change.md)
- [dead-end-p5-autonomous-loop-basin-converged-no-api-change](../findings/dead-end-p5-autonomous-loop-basin-converged-no-api-change.md)
- [arena-proximity-guard](../findings/arena-proximity-guard.md)

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"basin rigidity" OR all:"minimprovement gate" OR all:"Q Should `autonomous_loop.py` gate dispatch on") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
