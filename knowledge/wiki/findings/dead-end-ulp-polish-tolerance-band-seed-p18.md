---
type: finding
author: agent
drafted: 2026-06-01
question_origin: problem-18
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, triple-verify]
related_problems: [18, 14, 5, 11]
cites:
  - src/einstein/ulp_polish.py
  - src/einstein/circles_rectangle/evaluator.py
  - scripts/circles_rectangle/seeds/best.json
  - knowledge/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
---

# Dead end: dual-gate ULP polish on a tolerance-band seed (P18 circles-in-rectangle)

## What we tried

Phase 2a generalized the P14 dual-gate ULP polish (`einstein.ulp_polish`) to the
float64-ceiling family. P18 (Circles in Rectangle, n=21, maximize Σrᵢ) was a
target: same radius-growth shape as P14, same `feasible(cand, key)` = per-circle
dual disjointness gate (arena float64 strict `tol=0` AND mpmath-exact `gap ≥ 0`).

Before wiring, we checked the rank-current seed
(`scripts/circles_rectangle/seeds/best.json`, score 2.365832383977751) against the
strict gate.

## Why it failed — the obstruction

**The seed is not strict-disjoint.** `evaluate(seed, tol=0)` raises: the closest
pair overlaps by **9.99e-10** (`worst_overlap = -9.990e-10`, 47 contacts). It only
validates under the arena's `OVERLAP_TOL = 1e-9` — i.e. the rank-current P18
solution *lives inside the arena's overlap-tolerance band*, exactly the
arena-tolerance-drift regime axiom A1 was written to fence off.

This breaks the dual-gate polish at the root:

- The dual gate's binding check is the arena **float64 strict (tol=0)**
  disjointness for the changed circle. A seed whose pairs already overlap by
  ~1e-9 fails that check before any move is proposed — the polish has no feasible
  starting point.
- The only way to make the seed strict-feasible is a uniform shrink to `tol=0`,
  which *lowers* Σrᵢ (the manifest already records uniform-shrink as P18's
  rank-current op). Polishing back up from the shrunk config cannot exceed the
  pre-shrink score, so there is no net gain.
- Certifying the un-shrunk seed by relaxing the polish gate to `tol=1e-9` would
  re-open the 2026-04-09 tolerance-exploit (banking a move the verifier accepts
  only by tolerance, not by true disjointness). The dual gate exists precisely to
  refuse that.

## What this rules out

The dual-gate ULP polish applies **only to problems whose rank-current seed is
strict-feasible (`tol=0`)**. Any problem whose SOTA sits in the arena's tolerance
band (P18, and any future overlap-tolerated packing) is out of scope by
construction — not a tuning failure, a soundness boundary. The safe polish trades
reachability for honesty: it will never produce a tolerance-band submission, so it
cannot "improve" a tolerance-band seed.

## What might still work

- A separate, clearly-labeled **tolerance-band optimizer** (gate at the arena's
  actual `tol=1e-9`) could squeeze P18 — but its output must be flagged
  non-auto-submittable and human-reviewed (axiom A1 / submission policy), never
  routed through the strict polish.
- P18's float64 ceiling is best characterized by the existing uniform-shrink
  fallback + KKT exact solve, not by ULP descent.

## See also

- [mpmath-ulp-polish-dual-gate-p14](mpmath-ulp-polish-dual-gate-p14.md) — the dual gate this finding bounds the applicability of.
- [float64-ceiling](../concepts/float64-ceiling.md) — when the verifier tolerates overlaps, the "ceiling" is a tolerance band, not a representation floor.
