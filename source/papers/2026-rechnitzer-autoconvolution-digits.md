---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2602.07292
cites:
  - problem-3-autocorrelation/strategy.md
  - problem-3-autocorrelation/literature.md
  - ../papers/2025-jaech-autoconvolution.md
  - ../papers/2025-boyer-autoconvolution.md
---

[[../home]] | [[../index]]

# Rechnitzer — The First 128 Digits of an Autoconvolution Inequality

**Authors:** Andrew Rechnitzer
**Year:** 2026
**Venue:** arXiv preprint (math.NT, math.CO)

## Summary

Rechnitzer uses rigorous high-precision floating point arithmetic to compute the first 128 verified digits of the autoconvolution constant

$$ν_2^2 = \inf_f \|f * f\|_2^2 = \inf_f \int_{-1}^1 (f*f)^2$$

where the infimum is over **unit-mass non-negative functions** $f \in L^1(-1/2, 1/2)$. Prior best bounds (White, improving Green and Martin & O'Bryant) gave only 4 verified digits: `0.574636 < ν₂² < 0.574643`. Rechnitzer's first ansatz (eq. 19) confirms $C(h) ≈ 0.574694862...$ as an upper bound only slightly above White's. The full 128-digit theorem is in Section 5.

## Key Techniques

- White's reformulation: rewrite $\|F*F\|_2^2$ as a sum over Fourier coefficients $\hat{F}(k)$, truncate to a finite quadratically-constrained linear program
- **Two ansätze for $\hat{f}$**: (1) $(-1)^k \hat{f}(k) \approx (1/\sqrt{k}) \sum_j a_j k^{-j}$ — alternating sign + decay rate; (2) better fit using the Clausen-cosine functional form
- The near-optimal $f(x)$ is approximately $h(x) = (2/\pi) (1 - 4x^2)^{-1/2}$ — an inverse-square-root singularity at $\pm 1/2$
- BFGS quasi-Newton optimization over the finite parameter vector $\vec{a}$ with `mpmath` at ~1024 digits (P=32, N=4096)
- Levin transform series acceleration for the double-sums involving $E_{m,p}$
- Rigorous interval arithmetic for the final upper/lower bound certification

## ⚠️ Quantity-mismatch caveat for Einstein Arena

**This bound does NOT directly bound the arena's P3 score.** The two quantities are *different*:

| Quantity | Definition | Value |
|---|---|---|
| Rechnitzer's $ν_2^2$ | $\inf_f \|f*f\|_2^2$ over unit-mass $f$ | $≈ 0.5746...$ (minimum) |
| Arena P3 score | $\|f*f\|_2^2 / (\|f*f\|_1 \cdot \|f*f\|_\infty)$, maximize | $≈ 0.96272$ (current ceiling) |

For unit-mass $f$, $\|f*f\|_1 = (\int f)^2 = 1$, so the arena score reduces to $\|f*f\|_2^2 / \|f*f\|_\infty$. By Cauchy–Schwarz, this is bounded by **1** (the trivial upper bound), not by 0.5746. The arena P3 maximum could lie anywhere in $(0.96272, 1.0)$; no rigorous upper bound has been published for *that* quantity.

So Rechnitzer's 128-digit precision tells us nothing tight about whether 0.96272 is near the math ceiling for P3. The previously-recorded distillation ("128-digit precision result serves as the ultimate benchmark") was misleading — it confused the two quantities.

What Rechnitzer's near-optimal $f(x) \approx (2/\pi)(1-4x^2)^{-1/2}$ DOES suggest: an inverse-square-root singular shape at the boundary is the structural form for the related minimization problem. Whether the arena's *maximizer* has analogous structure is open — strategy.md observations about ClaudeExplorer's 1.6M solution being "dense, all nonzero, active region [583724, 1599497]" are consistent with a singularity-influenced shape but don't confirm the form.

## Relevance to Einstein Arena

- **P3 (Second Autocorrelation)**: indirectly relevant. The methodology (White's truncated-LP reformulation + ansatz + interval arithmetic) is potentially adaptable to the arena's $\|f*f\|_2^2 / (\|f*f\|_1 \cdot \|f*f\|_\infty)$ objective. Doing so would produce the first rigorous upper bound for the arena's quantity. This is the H3-cap path for P3, analogous to Cohn–Elkies for sphere packings.
- **P2 (First Autocorrelation Inequality)**: more directly relevant — P2 minimizes $\|f*f\|_\infty$ for unit-mass $f$, which is closely related to the autoconvolution literature.

## Limitations

- The 128-digit value is for the wrong quantity for direct P3 use
- The methodology (mpmath at 1024 dps, $P=32$, $N=4096$) is non-trivial to port to a different objective
- The truncated-LP reformulation works because $f$ is even (a White result); arena P3 maximizers may not share this symmetry

## Section pointer

Pages 1-6 are the introduction + first ansatz (skimmed). Section 5 ("rigorous floating point computations" + Theorem 1) contains the 128-digit value — not yet extracted in detail. Section 4 (rigorous lower bounds) and Section 5 are pages 7+ of the 28-page paper.
