---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P6, P10]
compute_profile: [local-cpu]
cost_estimate: "minutes to ~1 hour CPU per polish session"
hit_rate: "TBD"
---

# Multi-Scale Micro-Perturbation (Atomic Scales 1e-10 → 1e-14)

## TL;DR

For sphere-packing / kissing-number problems with gradient-flat-but-stochastically-improvable basins, perturb one vector at a time at progressively finer scales `1e-10 → 1e-14` with **contribution-weighted sampling** and **incremental O(n) evaluation**. Finer scales paradoxically find MORE improvements — the landscape has fractal structure invisible to gradient methods. Champion on P6 d=11; FAILED on P10 Thomson (single-funneled basin).

## When to apply

- Gradient methods report zero gradient at SOTA (Riemannian GD on sphere manifold = no improvement).
- Stochastic perturbation finds improvements (the landscape is not gradient-flat — it has finite-difference gradient that the analytical gradient misses, typical of hinge / minimax kinks).
- Sphere packing or constraint-heavy continuous problems with many near-active pairs.
- High-dimensional (n ≥ 100, d ≥ 8) where a smooth surrogate doesn't exist.

## Procedure

1. **Diagnostic**: try `scale = 1e-12` for 100K iters from SOTA. If it finds improvements, the landscape is fractal — proceed. If not, switch to SA parallel tempering (`parallel-tempering-sa.md`).
2. **Contribution-weighted sampling** (lesson #18):
   ```python
   contrib = per_vector_loss(v)                          # weight ∝ contribution
   probs = contrib / contrib.sum()
   i = np.random.choice(n, p=probs)                       # which vector to perturb
   ```
   Recompute weights every ~50K iters to prevent staleness.
3. **Incremental O(n) eval** (lesson #19): after perturbing vector `i`, only recompute the ~n−1 pairs involving `i`. Without this, multi-million-iter runs are infeasible.
4. **Multi-scale alternation** (lesson #17): scales `1e-10, 1e-12, 1e-13, 1e-14`. Finer scales access different geometric features. Alternate to compound improvements.
5. **Stop at diminishing returns**: each scale typically gives ~50% less than the previous. P6 polish curve: 23s → 8.33e-11; 8 min → 2.23e-10; 53 min → 3.38e-10 (severe diminishing past 30 min; 1e-11 dead in 0.156 basin; 1e-13 / 1e-14 productive).

## Pitfalls

- **Coarser scales can be LESS productive than finer** (counter-intuitive but reproducible — lesson #17). 1e-10 → 0.02% rate; 1e-12 → 0.10%; 1e-13 → 0.07%. Don't stop at the coarse scale.
- **Single-funneled basins fail** (P10 Thomson n=282): the landscape is genuinely single-funneled at a global minimum. Run cage-structure diagnostic (`sa-parallel-tempering.md` lesson #28) before committing.
- **Smooth surrogate is a trap** (lesson #25): softplus(β·hinge)/β + cascade does not converge to the hinge optimum at any β. Stay on the true hinge.
- **Wrong scale exhaustion order**: starting at 1e-14 first wastes time on tiny moves before the coarser landscape is exploited. Start at 1e-12 — the productive sweet spot for d=11 — and refine downward only when the coarser scale stalls.
- **Float64 floor at ~1.5e-13**: below this, smooth optimization is dead; switch to ulp coordinate descent (`mpmath-ulp-polish.md`).

## Compute profile

Local CPU. Sequential per-vector perturbation — GPU sits idle without batching. For sustained polish races (`minImprovement=0`), graduate to parallel-tempering on Modal.

## References

- `wiki/findings/perturbation-landscape.md` (lessons #17–#20 — fractal scales, contribution weighting, incremental O(n), gradient failure).
- `wiki/findings/sa-parallel-tempering.md` (lesson #25 smooth-loss trap, #28 cage diagnostic).
- knowledge.yaml strategy `micro_perturbation`; pattern `multi-scale-micro-perturbation`.
- `wiki/techniques/parallel-tempering-sa.md` (the heavier escalation).
- `wiki/techniques/mpmath-ulp-polish.md` (the deeper-precision successor).
- `mb/tracking/problem-6-kissing-number/strategy.md`.
