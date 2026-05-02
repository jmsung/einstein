---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P1, P9, P13]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "minutes (small pop) to GPU-hours (pop ≥ 256, sustained)"
hit_rate: "TBD"
---

# CMA-ES with Warm-Start

## TL;DR

Covariance Matrix Adaptation Evolution Strategy is the workhorse for medium-dimensional continuous optimization with exploration. Two complementary uses: (1) **second-order local-optimality proof** — start from SOTA with `pop_size=50`; if `sigma` collapses to 1e-15 with zero improvement, the basin is provably local-optimal at second order; (2) **gap-space CMA-ES with soft repair** for ordered-roots problems (P9 k=15, lesson #67).

## When to apply

- Medium-dimensional continuous problem (10–500 variables).
- Need exploration beyond what SLSQP / L-BFGS finds (gradient-flat basins, multi-modal).
- Goal A: prove SOTA is second-order local-optimal (sigma collapse).
- Goal B: ordered-roots problem (gap-space CMA-ES with linear penalty + soft repair).

## Procedure

### A. Second-order local-optimality proof

```python
import cma
es = cma.CMAEvolutionStrategy(sota_solution, sigma0=0.05,
                              {'popsize': 50, 'maxfevals': 50000})
while not es.stop():
    solutions = es.ask()
    es.tell(solutions, [-score(s) for s in solutions])
# If es.sigma < 1e-12 and no improvement → second-order local-optimal.
```

P1 Erdős: pop_size=50, sigma collapsed to 1e-15 in 50K evals, zero improvement → second-order local-optimality proven.

### B. Gap-space CMA-ES for ordered roots (P9 lesson #67)

```python
# In gap-space (g_i > 0), with linear penalty + soft repair
def loss(g):
    g_repaired = np.maximum(g, eps)             # soft repair, eps ~ 1e-6
    z = np.cumsum(g_repaired)
    return true_loss(z) + lambda_pen * np.sum(np.maximum(0, eps - g))
es = cma.CMAEvolutionStrategy(g0, sigma0=0.05, {'popsize': 14})
# Phase 1: sigma=0.05 broad
# Phase 2: sigma=0.005 refine
```

P9 k=15: this recipe reached the basin floor where pure position-space NM and unrepaired CMA both failed.

## Three-way local-optimality proof (lesson #96)

For minimax problems, combine three independent tests:
1. **First-order** (PyTorch L-BFGS, zero gradient).
2. **Second-order** (CMA-ES sigma collapse).
3. **Minimax / equioscillation** (Remez exchange).

All three converging in ~10 min total = strongest computational proof of local optimality short of an analytical certificate. Do this BEFORE declaring "frozen" or investing GPU.

## Pitfalls

- **Hard clamping in gap space**: zeros the gradient on the constraint, kills CMA. Use linear penalty instead.
- **Quadratic penalty**: dominates the true objective at the boundary; the wrong basin is found.
- **Population too small**: pop=11 is the scipy default; pop=50 is the floor for serious second-order proofs. Pop=256+ for hard problems.
- **CMA on GPU is rarely worth it**: pop ≤ 50 → kernel-launch dominated. Need pop ≥ 256 + float64 to justify Modal A100.
- **Don't trust CMA "improvements" without constraint verification** (lesson #87): P9 CMA-ES drove the score to 1.07e-13 on a missing-constraint evaluator — invalid below the proven lower bound 0.2025. Verify all constraints in the evaluator FIRST.
- **Wrong sigma0**: too small → trapped in initial basin; too large → wastes evals on infeasible. Sigma0 ≈ 5–10% of variable range is a working default.

## Compute profile

- Local CPU: pop ≤ 50, ≤ 1000 variables. Minutes per run.
- Local MPS: float32 only — useful for big-pop CMA where precision is not the bottleneck.
- Modal A100/H100: pop ≥ 256, float64 needed → sustained parallel evaluation. Run benchmark first.

## References

- `wiki/findings/basin-rigidity.md` (lesson #96 — three-way local-optimality proof).
- `wiki/findings/optimizer-recipes.md` (#67 — CMA-ES gap-space recipe).
- knowledge.yaml strategy `cma_es`.
- `wiki/techniques/gap-space-parameterization.md` (companion).
- `mb/wiki/problem-1-erdos-overlap/strategy.md` (sigma collapse), `mb/wiki/problem-9-uncertainty-principle/strategy.md` (gap-space).
