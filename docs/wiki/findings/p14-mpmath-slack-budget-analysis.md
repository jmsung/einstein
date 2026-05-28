---
type: finding
author: agent
drafted: 2026-05-27
question_origin: docs/wiki/questions/2026-05-25-p14-mpmath-ulp-polish-wiring.md
status: open
related_concepts: [float64-ceiling, basin-rigidity, contact-graph-rigidity, arena-tolerance-drift]
cites:
  - mb/problems/14-circle-packing-square/experiment-log.md
  - docs/wiki/findings/p14-manifest-wire-fix-verified.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - docs/wiki/techniques/mpmath-ulp-polish.md
  - docs/wiki/concepts/contact-graph-rigidity.md
---

# P14 rank-#1 gap is a slack-budget question, not a float64-representability wall

## Context

Autonomous cycle (2026-05-27, attempt 2/3) found P14 agent-side converged: the
only two manifest-dispatchable optimizers (`slsqp_polish` default, `newton_max
--pair-gap 0`) both saturate at the held rank-#2 strict score
**2.6359830849175245** (cycle 52 verified). The one remaining lever —
`mpmath-ulp-polish` — needs a new `scripts/circle_packing_square/mpmath_polish.py`
+ manifest block, which is **outside the autonomous loop's write-scope** (it may
only write `docs/wiki/{findings,questions,concepts}/` and the mb experiment log).
So no execution this cycle; instead, an analysis that the wiring cycle can act on.

Two prior findings frame the gap pessimistically:
- `p14-manifest-wire-fix-verified.md` (l.73–75): arena #1 is "unreachable without
  mpmath ulp polish **AND** a verifier with mpmath-grade tolerance handling on the
  arena side."
- `dead-end-newton-max-strict-tol-lockout-p14.md` (l.80): "the score is
  float64-ceiling-locked regardless."

This finding **partially corrects** that framing. The binding constraint is not
float64 representability of the gap — it is (a) contact-graph stiffness and
(b) arena strictness. Those are different, and testable.

## The three numbers that matter

| Quantity | Value | Source |
|---|---|---|
| Held strict score (rank #2) | 2.6359830849175245 | experiment-log final submission |
| Arena #1 (AlphaEvolve) | 2.6359830849176 | recon, 2026-04-08 |
| **Gap to close** | **≈ 7.55e-14** | difference of the two above |
| Held config **min pair gap** (tightest contact slack) | **+1.1e-12** | experiment-log "pair-gap margin +1.1e-12" |
| float64 worst-case post-rounding overlap, coords O(1) | **≈ 3–5e-16** | 2–3 ulp on unit-square coordinates |

Read these as a budget, smallest to largest:

```
float64 back-off floor   gap to AE #1      SLSQP interior slack
   ~5e-16          ≪      ~7.55e-14    ≪       ~1.1e-12
   (hard wall)            (target)             (available headroom)
```

## The argument

1. **SLSQP leaves slack on the table.** The held config's *tightest* contact is
   +1.1e-12 from tangency — SLSQP stops at an interior-feasible KKT point with a
   small positive margin on the active inequalities, so radii sit slightly below
   the exact-tangent configuration of this (rigid, Packomania-optimal) contact
   graph. That 1.1e-12 is recoverable slack, not noise.

2. **The float64 floor is ~4 orders below the gap.** To survive a strict (tol=0)
   verifier after rounding exact-tangent coords back to float64, each contact only
   needs a back-off of ~2× the worst-case rounding overlap, i.e. ~1e-15. That floor
   (~5e-16–1e-15) is **~150× smaller** than the 7.55e-14 we need and **~1000× smaller**
   than the 1.1e-12 of slack already present. So "float64 can't represent the gap"
   is false: the gap is 130+ float64-ulp on Σr, comfortably above representability.

3. **Therefore the gate is stiffness, not precision.** Whether tightening the
   1.1e-12 of slack toward the ~1e-15 floor actually buys ≥7.55e-14 of Σr depends
   on the contact graph's rigidity/stiffness map: closing one gap in a rigid graph
   can open another, so the recoverable Σr is *some fraction* of the raw slack, set
   by the equilibrium stress matrix — not a free 1.1e-12. This is the genuine
   unknown, and it is measurable.

## Falsifiable prediction for the wiring cycle

When `mpmath_polish.py` is wired (dps≈60, strict-disjoint equality solve on the
held active set, warm-started from `solution-best.json`, then rounded to float64
with a ~1e-15 strict-feasibility margin):

- **If** Σr(rounded, strict-verified) **> 2.6359830849175245 by ≥ 7.55e-14** → the AE
  basin admits a strict sub-ulp refinement; this generalizes to every float64-ceiling
  packing problem. File a finding + (gated) submit.
- **If** Σr lands **in (2.6359830849175245, AE)** but short of AE → the stiffness map
  converts only part of the slack; rank #2 is the strict-disjoint optimum and AE's
  published 2.6359830849176 must itself rely on sub-tol overlaps. Close the door with
  this obstruction.
- **Cheapest first test (do this before writing the polisher):** re-round AlphaEvolve's
  published n=26 config (`ae_original_notebook.ipynb` in mb solutions) to float64 and
  run `evaluate_strict` (tol=0). If AE's own config **fails strict**, the rank-#1 door
  is closed by the *verifier*, not by our optimizer — and no mpmath polish can claim it
  safely. This is a 5-minute test that may settle the whole question.

## What this rules out

- The claim that P14 rank #1 is "float64-ceiling-locked regardless of optimizer."
  The 7.55e-14 gap is ~130 ulp on Σr and sits inside a 1.1e-12 slack budget — it is
  representable and there is headroom. The lock, if real, is a *stiffness* or
  *arena-strictness* lock, which the prediction above distinguishes.

## What might still work

- The wiring task in [`2026-05-25-p14-mpmath-ulp-polish-wiring`](../questions/2026-05-25-p14-mpmath-ulp-polish-wiring.md)
  (kept open — this finding sharpens its target, does not close it).
- Run the cheap AE-re-round strict test first; it may convert the open question to a
  dead-end without writing any polisher.

## See also

- [p14-manifest-wire-fix-verified](p14-manifest-wire-fix-verified.md)
- [dead-end-newton-max-strict-tol-lockout-p14](dead-end-newton-max-strict-tol-lockout-p14.md)
- [float64-ceiling](float64-ceiling.md)
- [contact-graph-rigidity](../concepts/contact-graph-rigidity.md)
