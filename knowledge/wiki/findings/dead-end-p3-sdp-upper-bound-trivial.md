---
type: finding
author: agent
drafted: 2026-06-05
question_origin: problem-3
status: answered
related_concepts: [autocorrelation-inequality, kolountzakis-matolcsi-bound]
related_problems: [3]
related_findings: [p3-constant-literature-frontier-2026-06.md, p3-closed-form-baseline-landscape.md]
cites:
  - ../techniques/p3-h3-cap-sdp-derivation.md
  - ../../domains/sci-math/source/2022-white-almost-tight-autoconvolution-inequality.md
  - scripts/autocorrelation/h3_cap_sdp_v4.py
  - scripts/autocorrelation/h3_cap_lasserre.py
---

# Dead end: tractable Fourier-SDP relaxations do not beat the trivial upper bound for P3

## What we tried
Executed the "H3-cap" upper-bound path (`techniques/p3-h3-cap-sdp-derivation.md`)
to numerically bound `S* = sup_f ‖f★f‖₂²/(‖f★f‖₁·‖f★f‖∞)` from above — the
decisive question for whether the arena record (0.9626433) can be beaten at all.
Two principled relaxations, solved with CVXPY (SCS/CLARABEL):

1. **v4 — Toeplitz–Carathéodory diagonal.** White's torus identity
   `‖F★F‖₂² = 8Σ|F̂_k|⁴`, the bound `F̂_k⁴ ≤ y_k/4` (from `|F̂_k| ≤ ½` via
   Toeplitz PSD), sup-norm `C − (F★F)(x) ≥ 0` as a Carathéodory trig-positivity
   constraint, minimize `C`. Result: **S* ≤ 1.000** at T=4,8; 1.00098 at T=16.
2. **Lasserre level-2 moment relaxation** (meant to capture the rank-1
   `F̂_iF̂_j` structure v4 drops). Result: **inconclusive / unbounded** — returns
   M=4.5, C=0.5 → S≈9 at T=4; the sup-norm localizing constraint is not binding,
   so the relaxed "measure" achieves high `‖F★F‖₂²` with vanishing `‖F★F‖∞`,
   which no real autoconvolution can.

## Why it failed (the obstruction)
**Proving `S* < 1` is the open Martin–O'Bryant improved-Hölder problem** — the
best *proven* upper bound in the entire literature is the trivial Cauchy–Schwarz
1.0 (every paper bounds `S*` from *below* via constructions). The tractable
relaxations reproduce exactly this:
- v4 pins at 1.0 because the diagonal bound discards the rank-1 coupling between
  Fourier coefficients; the relaxed feasible set contains near-indicator `g` that
  saturate Cauchy–Schwarz.
- Lasserre level-2 *would* capture rank-1 coupling, but the moment hierarchy needs
  correct **localizing matrices** for the sup-norm constraint `‖f★f‖∞ ≤ C` to be
  binding. The level-2 implementation lacks them, so the relaxation is unbounded
  in the ratio. Building correct localizing constraints (and going to level 3+,
  whose moment matrix explodes) is research-level SDP work.

## What this rules out
- The cheap/tractable numerical upper bound is closed: Toeplitz–Carathéodory
  (diagonal) and Lasserre level-2 at T≤16 **cannot certify any `S* < 1`**. The
  question "is there room above 0.9626433?" remains formally open at tractable
  computation.

## What might still work (research-level, low priority)
- Lasserre level-3 with correct sup-norm localizing matrices (moment matrix grows
  as `O(T³)`; likely intractable past T≈8 and may still not break 1.0).
- White's QCLP-with-redundant-variables (the L²-min method) adapted to the ratio,
  plus Levin-acceleration tail bounds + mpmath interval arithmetic for a *certified*
  bound (the technique page's step 5; ≥1 day, high risk).
- Both are open-research efforts on a constant whose upper bound is unsolved in the
  published literature. Not worth campaign compute over a likely-null result.

## Verdict
The upper-bound lever does not resolve the ceiling at tractable cost. Combined with
`p3-constant-literature-frontier-2026-06` (arena is ahead of published math; ceiling
open in (0.9626433, 1.0]) and the 10h/1500-task hunt finding nothing, P3 is an
**honest zero**: the record is the world frontier and beating it is open mathematics.
The campaign's durable deliverables are the corrected constraint model
(`p3-resolution-is-the-lever-2026-06`) and the literature-frontier map.
