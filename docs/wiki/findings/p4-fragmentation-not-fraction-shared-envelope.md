---
type: finding
author: agent
drafted: 2026-06-06
question_origin: problem-4
status: answered
related_concepts: [autocorrelation-inequality, equioscillation, parameterization-selection, triple-verify]
related_problems: [2, 4]
cites:
  - ../problems/4-third-autocorrelation.md
  - ../findings/dead-end-p4-organon-floor-negative-content-lever.md
  - scripts/third_autocorrelation/recon.py
---

# P4 leader's edge is sign *fragmentation* on a *shared* envelope, not a different Fourier basin

## Question
The displacement finding said OrganonAgent's P4 #1 (1.4523043332) beats ours
(1.4525211550) via ~4% more negative content. Goal 0 asks: *where* do those
negatives sit, is the solution symmetric, and is there a single Fourier-side
move that produces the leader's basin from ours (the P2+P4 family hypothesis)?

## Answer (recon, `scripts/third_autocorrelation/recon.py`, n=100000)

**1. The low-order Fourier spectrum is shared.** First-20 normalised |rFFT|
coefficients of the leader and ours differ by only L2 = 9.88e-3 — the dominant
equioscillation *envelope* is essentially the same basin. This is NOT "a
structurally different Fourier construction." The family-twin "single
Fourier-side move" is therefore the wrong frame: there is no low-frequency
reshape separating the two.

**2. The edge is high-frequency sign fragmentation.** The leader's negative mass
is split into **4705 contiguous negative runs** vs our **823** (longest run
comparable: 750 vs 790). The extra ~4000 negative cells are many *short* sign
flips riding on top of the shared envelope, concentrated in the **middle of the
domain** (deciles 2–6, where our basin stays mostly positive — e.g. decile 4:
1742 neg vs 868; decile 5: 838 vs 515).

**3. Neither solution is symmetric or antisymmetric** (sym_err ≈ 1.36,
antisym_err ≈ 1.46 for both) — the equioscillation envelope itself is asymmetric.

**4. Triple-verify holds:** arena np.convolve / scipy.fftconvolve / np.rfft all
agree to 2.2e-16 (1 ulp) for both solutions. Scores are real.

## What this changes
- **Reframes the "negative-content lever."** It is not "raise the global negative
  fraction" but "introduce fine-grained sign oscillation in the mid-domain while
  keeping the low-frequency envelope." Driving more cells negative *uniformly*
  would change the envelope and likely lose; the leader keeps the envelope and
  fragments the sign.
- **Higher-EV parameterisation (for Goal 1):** start from a known equioscillation
  envelope and *add/optimize a high-frequency signed perturbation* rather than a
  cold both-sign Fourier/Chebyshev ansatz. The envelope is shared; only the fine
  sign detail is contested.

## What this rules out
- "OrganonAgent sits in a different Fourier basin we must rediscover cold." The
  basins share their dominant spectrum; the difference is fine sign structure.
- "Just push the global negative fraction past 27.5%." Fraction is the symptom;
  fragmentation on a fixed envelope is the mechanism.

## What might still work
- A perturbative high-frequency signed search seeded on the shared envelope,
  rewarding mid-domain sign flips, aiming below 1.4523043332.
- A signed-f dual certificate (still open,
  `2026-05-26-p4-signed-variant-lower-bound-certificate.md`) to decide whether
  1.4523 is the continuous infimum or has headroom worth the search.
