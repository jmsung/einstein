---
type: finding
author: agent
drafted: 2026-06-01
question_origin: docs/wiki/findings/p14-mpmath-slack-budget-analysis.md
status: partially-answered
related_concepts: [float64-ceiling, basin-rigidity, contact-graph-rigidity, arena-tolerance-drift]
cites:
  - mb/problems/14-circle-packing-square/experiment-log.md
  - docs/wiki/findings/p14-mpmath-slack-budget-analysis.md
  - docs/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
  - docs/wiki/techniques/mpmath-ulp-polish.md
  - docs/wiki/concepts/contact-graph-rigidity.md
---

# Cycle-53 result lands in the slack-budget finding's middle prediction

## Closes (partially)

`p14-mpmath-slack-budget-analysis.md` predicted three outcomes for the
mpmath ulp-polish wiring cycle:

1. Σr ≥ rank-2 + 7.55e-14 → AE basin admits strict sub-ulp refinement
2. Σr ∈ (rank-2, AE) but short of AE → stiffness map converts only PART of slack
3. Σr ≤ rank-2 → polisher cannot move

Cycle 53 (autonomous_loop, branch `js/feat/p14-mpmath-ulp-polish-body`, PR
#111, wrote `scripts/circle_packing_square/mpmath_ulp_polish.py`) ran the
dual-gated ulp-step coordinate descent on the submitted rank-2 seed at
dps=80, 100 max-iter, 2217 accepted moves over 65 sweeps. Result, triple-
verified per axiom A1:

| Quantity | Value |
|---|---|
| Submitted rank-2 strict | 2.6359830849175245 |
| Cycle-53 ulp-polish best (strict tol=0) | **2.6359830849175907** |
| AlphaEvolve arena #1 | 2.6359830849176 |
| Δ over rank-2 | +6.617e-14 |
| Remaining gap to AE | ≈ 9.3e-15 |
| Worst exact pair gap (mpmath dps=100) | +1.44458e-19 |

Σr lands inside (rank-2, AE) but short of AE by ≈9.3e-15. **This is
the middle prediction.**

## What this confirms

1. **Float64 representability is not the wall.** A 7.55e-14 gap is ~130
   Σr-ulp and was partially recoverable in float64. The basin admits
   sub-ulp refinement; the question was always "how much."

2. **SLSQP-leaves-slack hypothesis is empirically true.** The 1.1e-12 of
   tightest-pair slack was real, recoverable headroom — cycle 53 reclaimed
   ~6% of it (6.617e-14 / 1.1e-12), the rest stays inside the contact
   graph's stiffness map.

3. **Stiffness is the binding constraint, not precision.** Cycle 53's
   dual-gate (arena float64 strict AND mpmath ≥0) ran to coordinate-
   descent saturation at +1.44e-19 worst exact gap — moves can no longer
   be accepted without violating one gate. The remaining 9.3e-15 to AE
   is unreachable from this contact graph by coordinate moves.

## What stays open

The disjunction at the bottom of `p14-mpmath-slack-budget-analysis.md`
remains undecided between:

- **(2a) AE-basin stiffness lock**: AE is a strict-feasible
  configuration of a *different* contact graph (or a near-rigid
  deformation our coordinate descent can't reach), and the residual
  9.3e-15 needs a topology change to claim.
- **(2b) AE-not-strict**: AE's published `2.6359830849176` itself
  relies on sub-tolerance overlaps and would FAIL `evaluate_strict(tol=0)`.
  In that case the door to rank #1 is closed by the *verifier*, not by
  our optimizer, and no honest polish can match it.

A 5-minute test — round AE's published n=26 coordinates to float64 and
call `evaluate_strict` — discriminates (2a) from (2b). Filed as
`docs/wiki/questions/2026-06-01-p14-ae-reround-strict-test.md` for the
next cycle / wiring path.

## What this rules out

- The pessimistic framing in `dead-end-newton-max-strict-tol-lockout-p14.md`
  ("float64-ceiling-locked regardless"): empirically false at 1-ulp resolution.
  P14 was locked at the SLSQP-saturation level, not the basin's float64-floor
  level. The two differ by ~6.6e-14.
- Outcome (1) and outcome (3) of the slack-budget prediction (no strict
  sub-ulp refinement / polisher cannot move). Cycle 53 falsifies both.

## What might still work

- The AE-re-round strict test (next cycle, ~5 min) — settles 2a/2b.
- If (2a): per-topology coordinate descent — pick a near-rigid one-edge-flip
  of the AE contact graph and run dual-gate on each variant. Combinatorial
  cost: ~26²/2 = 338 single-edge flips, each ~30s, parallelizable.
- If (2b): close the door, write a dead-end on "AE rank #1 is not strict-
  feasible; rank-2 is the strict-disjoint optimum on this basin."

## See also

- [p14-mpmath-slack-budget-analysis](p14-mpmath-slack-budget-analysis.md) (parent, status: open → now partially-answered)
- [mpmath-ulp-polish-dual-gate-p14](mpmath-ulp-polish-dual-gate-p14.md) (cycle 53's implementation finding)
- [float64-ceiling](../concepts/float64-ceiling.md)
- [contact-graph-rigidity](../concepts/contact-graph-rigidity.md)
