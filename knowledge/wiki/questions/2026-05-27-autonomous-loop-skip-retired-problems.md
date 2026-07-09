---
type: question
author: agent
drafted: 2026-05-27
status: open
asked_by: autonomous-loop
related_problems: [17]
related_concepts: [float64-ceiling.md]
---

# Should the autonomous loop skip problems with `status: retired` and no manifest entry?

The orchestrator dispatched cycle_id=0 for P17 (retired-17-hexagon-packing) on 2026-05-27. Outcome by inspection alone, before any compute:

- `docs/wiki/problems/retired-17-hexagon-packing.md` declares `status: retired`, retired_at 2026-05-23, arena URL returns HTTP 404, score 3.9416523 at known-optimal float64-ceiling basin (already #1 tied).
- `src/einstein/optimizer_manifest.yaml` has no entry for `17:` (only 14 and 22), so `optimizer_dispatch` can return nothing.
- Existing wisdom in [`findings/float64-ceiling.md`](../findings/float64-ceiling.md) already classifies P17a as "basin rigid at sub-ulp; strict-tol trap nearly cost 500 pts" — further compute cannot improve the score and there is no arena to submit to.

So the cycle is structurally a no-op: it spends an inner-agent invocation budget to re-derive that the problem is retired. Two candidate filters for the orchestrator's problem picker:

1. **Skip on `status: retired`** in the problem wiki frontmatter.
2. **Skip on absent manifest entry** in `optimizer_manifest.yaml`.

The honest answer probably wants both: retired + manifest-present is still a legitimate "compute for the wisdom" path (e.g., a retired problem could still be a test bed). But retired + no-manifest is purely overhead.

## What the right answer would look like

A small change in `scripts/autonomous_loop.py`'s problem picker (or in `docs/agent/skill-library.md`'s scoring) that down-weights or excludes retired+no-manifest problems. Cited evidence: a count of cycles on retired problems in `docs/agent/cycle-log.md` since 2026-05-23 vs cycles on live problems — if non-trivial, the filter pays for itself.

## Suggested sources

- `docs/agent/cycle-log.md` — base rate of retired-problem cycles.
- `scripts/autonomous_loop.py` — picker logic.
- `src/einstein/optimizer_manifest.yaml` — current coverage.
