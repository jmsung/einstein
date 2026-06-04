---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-12
status: answered
related_concepts: [equioscillation, triple-verify]
cites:
  - scripts/flat_poly/seeds/best.json
  - src/einstein/flat_poly/evaluator.py
  - src/einstein/triple_verify/problems/p12_flat_poly.py
  - mb/logs/leaderboard-audit-2026-06.md
---

# P12 flat-polynomials: local↔arena grid-sampling drift (~7e-10)

## The question
While wiring P12 (Phase 6, Goal 3) the SOTA ±1 coefficient vector scored
**1.2809320520721** through our evaluator, but the arena reports
**1.2809320527987977** for the *same coefficients*. Why the ~7.3e-10 gap?

## What we found
The score is `max_k |p(z_k)| / √71` over a **finite grid** of N = 1,000,000
N-th roots of unity — *not* the continuous supremum. The grid max underestimates
the true `max_{|z|=1} |p(z)|` because the peak rarely lands exactly on a grid
node. Re-evaluating the same polynomial on a denser/shifted grid:

| grid | score |
|---|---|
| 1e6 uniform (k=0…N−1), our evaluator | 1.2809320520721 |
| 4e6 uniform, half-step offset | 1.2809320528463 |
| arena reported | 1.2809320527987977 |

The denser grid (1.28093205285) is closer to the true sup and brackets the
arena value, so arena is sampling the peak more finely (or at a different phase)
than our 1M-from-k=0 grid. The drift is **a property of the discretisation, not
a bug** in either evaluator — three independent in-grid methods (np.poly1d,
np.fft, mpmath at the argmax node) agree to <1e-15 that *our* 1M-grid max is
1.2809320520721.

## What this rules out / implies
- **Our 1M-grid triple-verify is internally sound** but verifies the *grid*
  quantity, not arena's quantity. A P12 submission claim cannot trust gate 1
  (strict improvement ≥ minImprovement = 1e-7) naively: a 7e-10 drift is small
  vs minImprovement, but a genuinely better basin reported on our coarse grid
  could be a sampling artefact rather than a real improvement, or vice-versa.
- This is the same class as P14/P17 local↔arena drift (triple-verify rule):
  single-grid scores are not trustworthy to sub-1e-9 without matching arena's
  exact sampling.

## What might still work (Phase 7)
- Match arena's grid exactly (probe N, starting phase, k-range) so the local
  evaluator and arena agree bit-for-bit, OR
- Use a continuous upper-bound (Bernstein / FFT-zero-padding refinement, or
  mpmath peak-bracketing) as the authoritative score and treat the 1M grid as a
  fast pre-filter only.
- Until reconciled, treat P12 as **tie-at-SOTA, non-submittable** (our basin ==
  the arena leader's basin; the visible Δ is sampling noise).
