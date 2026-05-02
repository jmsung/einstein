---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - problem-6-kissing-number/strategy.md
---

# Perturbation Landscape & Stochastic Optimization

## #17: Finer perturbation scales can have HIGHER improvement rates

Problem 6: scale 1e-10 gave 0.02% rate, 1e-12 gave 0.10%, 1e-13 gave 0.07%. The optimization landscape has fractal-like structure where atomic-scale perturbations find structure invisible at larger scales. Always try progressively finer scales when a coarser scale stops improving. The fractal-like structure means that the improvement rate is NOT monotonically decreasing with perturbation scale — finer scales access different geometric features of the loss landscape. The 5x improvement rate jump from 1e-10 to 1e-12 is counterintuitive but reproducible.

## #18: Contribution-weighted sampling beats uniform

Focusing perturbations on high-overlap (high-contribution) vectors finds improvements faster. Recompute weights periodically (every 50K iterations). Rather than uniformly sampling which vector to perturb, weight the sampling probability by each vector's contribution to the total loss. Vectors with high overlap (near the critical distance threshold) have the most room for improvement and the highest probability of yielding a strict improvement when perturbed. The weights drift as the configuration changes, so they must be recomputed periodically — every 50K iterations is a practical frequency that balances overhead against staleness.

## #19: Incremental O(n) evaluation essential

When perturbing one vector at a time, only recompute pairs involving that vector. This turns O(n²) evaluation into O(n) per step, enabling millions of iterations. For Problem 6 with 594 vectors in 11 dimensions: the full pairwise evaluation touches all 176,121 pairs, but a single-vector perturbation only affects ~593 pairs (all pairs involving that vector). The O(n) incremental evaluation is what makes multi-million iteration runs feasible on a single CPU. Without it, each iteration is 593x slower and the improvement-per-wall-clock plummets below the threshold where stochastic perturbation is productive.

## #20: Gradient descent may fail where stochastic perturbation succeeds

Problem 6: Riemannian GD on sphere manifold found zero improvement (gradient is zero at SOTA). But random perturbation at 1e-10 to 1e-14 found thousands of improvements. The landscape has flat gradient but non-zero stochastic gradient. This happens when the objective is piecewise-linear or has kinks at the current point — the gradient is zero (or undefined) in every direction, but the function value does change when perturbed by a finite amount. The stochastic perturbation "sees" the finite-difference gradient that the analytical gradient misses. This is particularly common at maximin/minimax optima where the min/max operation creates kinks.

## #25 (smooth loss): Smooth loss approximation is a trap

Cross-reference to sa-parallel-tempering.md — see #25 there for the full discussion. The key point relevant to perturbation landscape analysis: smooth surrogates (softplus, LogSumExp) change the loss landscape topology. What is optimal under the smoothed loss is NOT optimal under the true loss. This is not a precision issue — the surrogate introduces spurious attractors and removes real ones. At any β, the surrogate either (a) changes the objective enough to move the optimum (low β), or (b) flattens the gradient so much that optimization stalls (high β). No β simultaneously approximates the landscape and maintains useful gradients.
