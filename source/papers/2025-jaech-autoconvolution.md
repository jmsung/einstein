---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2508.02803
source_drive: https://drive.google.com/file/d/1nA9WKzR7RCnf87a4ur5MqnsEdZp3aj7J
source_local: sources/2025-jaech-autoconvolution.pdf
cites:
  - problem-3-autocorrelation/strategy.md
  - problem-3-autocorrelation/literature.md
  - problem-4-third-autocorrelation/strategy.md
  - ../papers/2025-boyer-autoconvolution.md
  - ../papers/2026-rechnitzer-autoconvolution-digits.md
---

# Jaech & Joseph (2025) — Further Improvements to the Lower Bound for an Autoconvolution Inequality

**Authors**: Aaron Jaech, Alan Joseph
**arXiv**: [2508.02803](https://arxiv.org/abs/2508.02803)
**Date**: August 4, 2025

## Summary

This paper advances the known lower bound for the second autoconvolution inequality constant from c ≥ 0.9016 (Boyer & Li, 575 intervals) to **c ≥ 0.94136** (2,399 intervals), closing ~40% of the gap to the trivial upper bound c ≤ 1.

The core contribution is a two-stage optimization pipeline: (1) batch Adam gradient ascent with noise-annealed exploration at moderate resolution (N=559–768), then (2) linear-interpolation upsampling to 4× resolution followed by a second round of gradient ascent. The upsampling breaks resolution-specific local optima and unlocks fresh degrees of freedom at higher N — a technique that proved decisive in our subsequent P3 and P4 arena campaigns.

The paper also identifies a structural property of optimal solutions: the denominator placement of ‖f∗f‖_∞ creates a "peak-flattening" dynamic where gradients naturally push down sharp peaks, preventing the "peak-locking" failure mode that plagues the first and third autocorrelation problems (where ‖f∗f‖_∞ appears in the numerator).

## Key Techniques

- **Four-phase Adam optimizer**: (1) High-LR exploration (lr=3e-2, Gaussian gradient noise σ=η/(t+1)^γ), (2) Low-LR exploitation (lr=5e-3, no noise), (3) Elitist respawn (retain top-κ% every 20K iters, replace rest with random), (4) Upsampling + re-optimize. Batch size B=1024.
- **Upsampling cascade**: Optimize at N=559, linearly interpolate to N=2,399, re-optimize with Adam at lr=3e-2 for ~200K iterations. The interpolation preserves basin structure while exposing sub-interval degrees of freedom.
- **Peak-flattening dynamic**: ‖f∗f‖_∞ in the denominator creates gradients that flatten the autoconvolution globally, preventing convergence to narrow-peak local optima. This is unique to the second autocorrelation — the first and third variants suffer from the opposite (peak-locking).
- **Non-negativity via projection**: Simple h ← max(0, h) after each Adam step. No reparameterization (contrast with our w² parameterization in Dinkelbach approach).

## Structural Observations

- **Spike + comb**: Optimal f has a tall narrow spike near x ≈ −0.24, a sharp drop to zero, then a sparse comb of smaller periodic peaks to the right.
- **Flat autoconvolution plateau**: The resulting f∗f has a wide, nearly flat central plateau (boosting L²) with gentle ripples at the right edge.
- **Resolution matters**: The 559-interval optimum (c=0.9265) and 2,399-interval optimum (c=0.9414) live in different effective basins — upsampling creates a new optimization landscape.

## Relevance to Einstein Arena

### P3 Second Autocorrelation (our #1, C=0.963)
This paper's upsampling idea was the conceptual precursor to our Dinkelbach + LogSumExp + L-BFGS cascade at n=1,600,000. Our approach differs in three ways: (1) Dinkelbach fractional programming instead of direct ratio optimization, (2) LogSumExp smooth L∞ proxy with β-cascade instead of raw max, (3) w² parameterization for strict non-negativity. But the core insight — optimize at moderate N, upsample, re-optimize at larger N — came from this paper.

### P4 Third Autocorrelation (our #1, C=1.4525)
The "block-repeat + perturb + re-optimize" breakthrough that broke the n=400 equioscillation basin is a direct adaptation of Jaech & Joseph's upsampling technique. All top-9 agents were stuck at n=400 piecewise-constant local minima. Block-repeating to n=100,000 + noise + L-BFGS unlocked 15× minImprovement (Δ=1.52e-3).

### Peak-locking vs peak-flattening
The peak-flattening observation explains why P3 (second autocorrelation, ‖f∗f‖_∞ in denominator) has a smoother optimization landscape than P2 (first autocorrelation, ‖f∗f‖_∞ in numerator) and P4 (third autocorrelation, abs(max) in numerator). This structural insight guided our choice of β-cascade schedules across all three problems.

## Limitations

- Adam + projection is simple but may miss basins that require reparameterization
- No theoretical analysis of why upsampling works — purely empirical
- Peak-flattening observation is qualitative, not formalized
- Batch size 1024 is feasible for N≤2,399 but doesn't scale to N=1.6M (our arena resolution)

## See Also

- [[problem-3-autocorrelation/strategy]]
- [[problem-3-autocorrelation/literature]]
- [[problem-4-third-autocorrelation/strategy]]
- [[cross-problem-lessons]]
