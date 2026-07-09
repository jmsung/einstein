---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-12
status: answered
answer_finding: self
related_concepts: [equioscillation, triple-verify, discretization-as-structure]
related_problems: [12]
cites:
  - ./dead-end-p12-grid-sampling-drift.md
  - src/einstein/flat_poly/evaluator.py
  - src/einstein/triple_verify/problems/p12_flat_poly.py
  - knowledge/wiki/questions/2026-06-04-p12-headroom-razborov-grid-drift-bound.md
---

# P12 grid-drift resolution: certify the continuous sup, not the grid max

## The question
The P12 SOTA ±1 vector scored **1.2809320520721** through our 1e6-point grid
evaluator but the arena reports **1.2809320527988** for the *same* coefficients
(`dead-end-p12-grid-sampling-drift.md`). Until reconciled, P12 was "tie-at-SOTA,
non-submittable": any local Δ on the coarse grid could be sampling noise, and —
now that auto-submit is armed — a coarse-grid false improvement could trip a
false submission.

## The resolution
The arena score is a **grid maximum**, which underestimates the true
`sup_{|z|=1} |p(z)|/√71` because the peak rarely lands on a node. The fix is to
score the **continuous supremum**, which is grid-independent.

`g(θ) = |p(e^{iθ})|²` is an exact real trig polynomial of degree n−1:

    g(θ) = r₀ + 2·Σ_{m≥1} r_m cos(mθ),   r_m = Σ_j a_j a_{j+m}   (integer autocorrelation)

so g, g′, g″ are closed forms. A flat polynomial has *many* near-equal peaks, so
we seed Newton from the top-K local-max nodes of a fine FFT grid (not just the
single argmax) and refine each to machine precision. Implemented as
`continuous_sup_score` (float64 FFT+Newton) and `continuous_sup_score_mpmath`
(arbitrary precision) in `src/einstein/flat_poly/evaluator.py`.

### The numbers (SOTA seed)

| quantity | value | vs continuous sup |
|---|---|---|
| our 1e6 grid (`compute_score`) | 1.2809320520721 | −8.0e-10 |
| arena reported | 1.2809320527988 | −7.6e-11 |
| **certified continuous sup** | **1.2809320528750** | — |

Three independent certifications — FFT(2²⁰)+Newton, FFT(2²²)+Newton (more
peaks), and mpmath dps=50 Newton — agree to **2.2e-16** (machine epsilon). The
continuous sup is stable to ~1e-13 across FFT seeding density.

**Both the 1e6 grid and the arena value sit below the true sup, and every gap is
< minImprovement (1e-8).** The arena is simply a finer grid than our 1M-from-k=0
grid; it samples the same basin's peak more closely but still underestimates it.

## What this rules out / what it enables
- **The drift cannot manufacture a false P12 improvement.** grid ≤ continuum
  always, and the worst gap (8e-10) is two orders below minImprovement. A
  coarse-grid "improvement" that doesn't survive the continuous-sup certifier is
  sampling noise.
- **Safe submission rule:** compare a candidate's *continuous sup* against arena
  #1's *reported grid* score. Since grid ≤ continuum, a continuous sup below the
  arena grid value is a genuine improvement on the arena's own metric and can
  never over-claim. This is now the authoritative P12 comparison.
- The triple-verify registration (`triple_verify/problems/p12_flat_poly.py`) now
  certifies the continuous sup three ways; the 1e6 grid (`compute_score`) is
  retained as a fast pre-filter only.

## Post-fix strategy attempt (Goal 2, last sub-task)
With the drift dissolved, ran one bounded memetic-tabu search (3 seeds × 40 pop
× 60 rounds) warm-started from the SOTA basin + algebraic seeds (Fekete, Turyn,
Rudin–Shapiro, period-3), certifying finalists by `continuous_sup_score`.

**Outcome: honest-zero.** The search re-converges to the SOTA basin — best
candidate's continuous sup is **1.2809320528750419**, bit-identical to the SOTA
basin's own continuous sup. No candidate has a continuous sup below arena #1's
1.2809320527988 by minImprovement. This confirms (now rigorously, not on a
drifting grid) that **we hold the SOTA basin and the visible Δ was sampling
noise** — P12 is tied-at-SOTA. Algebraic seeds (Fekete 1.966, Turyn 1.515,
Rudin–Shapiro 1.720) are all far worse, consistent with the SOTA being a
non-classical search optimum.

## What might still work
- Beating P12 requires a *different* ±1 vector with a strictly lower continuous
  sup — open question whether one exists (Erdős second-moment estimate,
  `2026-06-04-p12-headroom-erdos-is-sota-truly-global.md`). The certifier now
  makes any future claim drift-proof.
