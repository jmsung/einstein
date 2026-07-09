---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-3
status: answered
related_concepts: [autocorrelation-inequality, cross-resolution-basin-transfer, discretization-as-structure, triple-verify]
related_problems: [3]
cites:
  - ./dead-end-p3-resolution-inflation.md
  - ./p3-closed-form-baseline-landscape.md
  - src/einstein/autocorrelation/evaluator.py
  - ../questions/2026-06-04-p3-headroom-tao-antialias-kernel.md
  - ../questions/2026-06-04-p3-headroom-cohn-basin-class.md
  - ../questions/2026-06-04-p3-headroom-hilbert-agreement-test.md
---

# Dead end: no anti-aliased downsample of the 1.6M P3 solution survives to 100k

## What we tried
Goal 3's primary strategy was a *valid* cross-resolution transplant: take our
1.6M-point P3 solution (scores C2 = 0.9627189978 at 1.6M — above SOTA 0.962643)
and downsample to the arena's 100k resolution with a band-limited / anti-aliased
kernel, hoping to land a 100k-native f above SOTA. The resolution-inflation
dead-end (`dead-end-p3-resolution-inflation.md`) had ruled out *naive* decimation;
this tests whether *any* proper kernel preserves the score.

Re-scored every downsample at the arena's 100k evaluator:

| kernel (1.6M → 100k, factor 16) | C2 @ 100k |
|---|---|
| decimate (every 16th) | 0.2356 |
| max-pool | 0.1332 |
| band-limit (FFT low-pass + subsample) | 0.7816 |
| average-pool (box) | 0.8612 |
| Gaussian σ=8 + subsample | 0.9549 |
| **Gaussian σ=16 + subsample** | **0.9596** |
| Gaussian σ=32 + subsample | 0.9561 |

Best downsample: **0.9596** — *below* our own 100k-native reclaim basin
(0.96227) and far below SOTA (0.962643).

## Why it failed (the obstruction — answers Tao's question)
**Yes, the quadratic ★ injects above-Nyquist energy that no f-side downsample can
pre-empt** (`2026-06-04-p3-headroom-tao-antialias-kernel`). The 0.9627 at 1.6M is
produced by *fine* structure in f whose autoconvolution f★f is flat only at 1.6M
resolution. Any downsample of f to 100k smooths exactly that fine structure away;
the 100k f★f is no longer flat, so the L²/(L¹·L∞) ratio drops. The score lives in
the high-frequency content that downsampling necessarily destroys — it is a
*resolution artifact*, not a transferable construction. The map f ↦ down(f) and
the scoring map do not commute through the quadratic ★; `down(f)★down(f) ≠
down(f★f)` is irreducible here.

## What this rules out
- **Cross-resolution transplant as a P3 record path — fully, not just naive
  decimation.** Box, max, Gaussian (3 widths), and band-limit kernels all fail.
  The 1.6M→100k pipeline cannot beat a 100k-native solution; native optimisation
  at the arena resolution is strictly better (our 0.96227 native > 0.9596 best
  transplant).
- **Promoting any high-resolution P3 score as "beats SOTA."** Confirmed
  empirically: the arena quantity is only meaningful at the arena's resolution.

## Cohn's question (is P3 literature-capped?) — NO
Rechnitzer 2026's 128-digit value bounds `inf ‖f★f‖₂²` (≈0.5746), a *different*
quantity; it does not cap the arena ratio (`p3-closed-form-baseline-landscape`).
So P3 is not proven-capped — but all 11 leaderboard agents plateau at the SOTA
cluster (~0.96264) and our strategy.md verdict is "solved to practical limit."
The math ceiling lies in (0.96264, 1.0], unpinned.

## Hilbert's question — the cross-resolution agreement predicate (gate-2 design)
Any future P3 (or P4) submission must pass: **score stability under
re-discretisation.** Concretely, for candidate f at 100k, require

    |C2_100k(f) − C2_100k(resample(f, 100k via a different phase / 200k↓100k))| < minImprovement

i.e. the score must be a continuum property, stable to how f is sampled, not an
artifact of one grid. A candidate whose score *rises* at higher resolution is
inflated and must be rejected. (Not wired now — there is no P3 candidate; stated
here as the prerequisite for when one exists.)

## What might still work (low EV)
- **100k-native new-basin search** (Dinkelbach + L-BFGS from diverse 100k seeds)
  to beat 0.962643 directly — the only live path, but 11 agents cluster at the
  ceiling and our basin plateaus at 0.96227, so EV is low. P3 is honest-zero for
  this branch; the transplant obstruction is the wisdom.
