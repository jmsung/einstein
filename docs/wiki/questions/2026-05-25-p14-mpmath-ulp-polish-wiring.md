---
type: question
author: agent
drafted: 2026-05-25
asked_by: autonomous_loop
status: answered
answer_finding: docs/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity, arena-tolerance-drift]
cites:
  - docs/wiki/findings/p14-manifest-wire-fix-verified.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - docs/wiki/techniques/mpmath-ulp-polish.md
---

# Wire an mpmath-ulp-polish optimizer block into the P14 manifest

## The question

Cycle 52 confirmed that `slsqp_polish` (float64 SLSQP) and the
strict-disjoint `newton_max` both saturate at score
`2.6359830849175245` — the AlphaEvolve basin's float64 ceiling, rank #2.
Arena #1 sits `8e-14` above that, beyond float64 ulp resolution. The
`mpmath-ulp-polish.md` technique (skill-library: tried 8 / top3 5 /
hit_rate 0.62 on float64-ceiling family) is the only remaining
dispatchable lever, but P14 has no manifest entry pointing at an
mpmath-grade strict-disjoint polish wrapper.

**Question**: Can a `mpmath_polish` optimizer block — wrapping
`scripts/circle_packing_square/mpmath_polish.py` (new) at dps=60 with
strict-disjoint pair + wall constraints, warm-started from the held
`solution-best.json` — push the score past `2.6359830849175245` while
remaining within arena verifier tolerance? Or does the AlphaEvolve
construction itself sit ulp-precise at the rank-#1 ceiling such that
no in-basin polish can close the gap?

## Why this matters

- It is the only remaining auto-runnable lever for P14 rank improvement.
- It tests whether the AE basin admits a strict-disjoint sub-ulp
  refinement, which (if it does) generalizes to every other
  float64-ceiling packing problem.
- If it does NOT improve, that closes the P14 rank-#1 door cleanly with
  an articulated obstruction (basin is float64-ulp-optimal under arena
  verifier rules).

## Search hooks

- mpmath ulp polish for nonlinear constrained packing (no off-the-shelf
  solver — must implement Newton at high dps with explicit constraint
  active set).
- AlphaEvolve P14 published configuration: is its rank-#1 score
  reproducible by re-rounding to float64 (suggests arena verifier
  internal precision > float64), or is it a genuine sub-ulp construction?

## Next step

A wiring task (NOT a research task): write
`scripts/circle_packing_square/mpmath_polish.py`, append a `mpmath_polish`
block to `src/einstein/optimizer_manifest.yaml#14.optimizers`, dispatch
end-to-end. If the result file's `score` exceeds `2.6359830849175245`,
file a finding. If not, file a dead-end with the obstruction articulated.
