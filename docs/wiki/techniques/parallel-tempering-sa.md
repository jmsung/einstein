---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P6, P10, P22]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "minutes (CPU 8 replicas) to GPU-hours (64 replicas, sustained)"
hit_rate: "TBD"
---

# Parallel-Tempering Simulated Annealing

## TL;DR

Run 8–64 SA replicas at geometrically-spaced temperatures with periodic Metropolis exchange. Hot replicas explore (accept worse moves), cold replicas exploit. On kissing-number d=11 this beat single-replica greedy by 730×. The right precondition is gradient-flat-but-stochastically-improvable landscapes; the wrong precondition is a single-funneled global minimum (Thomson n=282 — fails).

## When to apply

- Greedy / micro-perturbation has stalled but the landscape is still stochastically improvable.
- Sphere-packing or constraint-heavy continuous problems with rough loss surfaces and fractal structure (P6 d=11).
- Hinge-loss landscapes where the gradient is zero at SOTA but finite-difference gradients are non-zero (P6, P22).
- You want to scale: GPU fused-batch tempering reaches 131K perturbations/sec on A100 vs ~2.9K/sec CPU.

## Procedure

1. **Set up the temperature ladder**: `T_k = T_min · (T_max / T_min)^(k / (R-1))` for `k = 0..R-1`.
   - P6 sweet spot: `R = 64`, `T_min = 1e-12`, `T_max = 1e-4`.
   - 8 replicas works on CPU; 64 needs GPU fused step.
2. **Contribution-weighted sampling** (lesson #18): weight perturbation probability by each variable's contribution to the loss; recompute every ~50K iters.
3. **Per-replica step**: Metropolis acceptance — accept any improvement; accept worsening with prob `exp(−ΔE / T_k)`.
4. **Replica exchange** every M steps: propose swap of replicas `k, k+1` with prob `min(1, exp((1/T_k − 1/T_{k+1})·(E_k − E_{k+1})))`. Target swap rate 27–37%; tune ladder if outside.
5. **Incremental O(n) eval**: only recompute pairs touching the perturbed variable. Without this, multi-million-iter runs are infeasible.
6. **GPU fused step**: K=5 perturbations per Python step (Jacobi-safe at scale 1e-6); K=50 breaks the approximation.

```python
from einstein.gpu_tempering import run_fused_tempering
result = run_fused_tempering(
    vectors, n_replicas=64, n_steps=200_000,
    k_per_step=5, scale=1e-6, loss_type="hinge",
)
```

## Pitfalls

- **Smooth loss surrogate trap** (lesson #25): `softplus(β·hinge)/β` changes the optimum at low β and flattens gradients at high β. No β works. Stay on the true hinge.
- **Diminishing returns are within-basin** (lesson #27): each round finds ~50–60% less improvement than the previous, exponential decay. This indicates basin exhaustion, NOT plateau across basins. To escape, change starting basin or parameterization, not perturbation scale.
- **Fails on single-funneled landscapes**: Thomson n=282 has a true single global minimum; SA tempering finds nothing because the basin is genuinely unimprovable. Run a cage-structure diagnostic (lesson #28) before committing GPU hours.
- **K too large breaks Jacobi**: at scale 1e-6, K=50 is fine; at scale 1e-5, even K=5 destroys structure.
- **Wrong scale**: P6 scale 1e-6 is the sweet spot; 1e-5 is too aggressive (zero improvement); 1e-12 is too timid (110M iters → 6.45e-10 vs 9.15e-7 in 20M at 1e-6).
- **Stronger GPU does not help when util < 50%** — Python dispatch is the bottleneck. Use fused step / Triton.

## Compute profile

- **Local CPU 8 replicas**: feasible for d=11 n=594 in minutes; explore + diagnose first.
- **Modal A100 64 replicas fused**: 131K p/s; cost-effective for sustained polish races and minImprovement=0 problems (P6).
- **Run benchmark first**: `python -m einstein.gpu_tempering.benchmark` confirms whether the algorithm is GPU-able for the problem.

## References

- `wiki/findings/sa-parallel-tempering.md` (lessons #24, #25, #27, #28).
- `wiki/findings/perturbation-landscape.md` (lessons #17–#20 — fractal scales, contribution-weighted, incremental O(n)).
- `wiki/findings/gpu-modal-compute.md` (lesson #26 — Python overhead).
- knowledge.yaml strategy `simulated_annealing` and pattern `sa-parallel-tempering`.
- `src/einstein/gpu_tempering/` — production module (`core.py`, `fused_step.py`, `triton_kernel.py`).
- `mb/tracking/problem-6-kissing-number/strategy.md`.
