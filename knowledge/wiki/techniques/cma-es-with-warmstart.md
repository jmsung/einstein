---
type: technique
author: agent
drafted: 2026-05-02
revised: 2026-05-23
related_concepts: [parameterization-selection.md, basin-rigidity.md]
related_problems: [P1, P9, P13, P15, P16]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "minutes (small pop) to GPU-hours (pop ≥ 256, sustained)"
hit_rate: "TBD"
cites:
  - ../../domains/ai-ml/source/2016-hansen-cma-evolution-strategy-tutorial.md
  - ../../domains/ai-ml/source/2014-loshchilov-maximum-likelihood-based-online-adaptation.md
  - ../../domains/ai-ml/source/2016-akimoto-quality-gain-analysis-weighted.md
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

## Theory anchors

Three primary sources in `knowledge/source/` ground the heuristics above:

- **Hansen 2016 — *The CMA Evolution Strategy: A Tutorial*** ([`domains/ai-ml/source/2016-hansen-cma-evolution-strategy-tutorial.md`](../../domains/ai-ml/source/2016-hansen-cma-evolution-strategy-tutorial.md)) — the canonical derivation. The covariance $C$ is a stochastic quasi-Newton approximation of $H^{-1}$ on convex quadratic $f_H = \tfrac12 x^T H x$, making CMA-ES *affine-invariant*. The updates split into a **rank-$\mu$** term (outer products $y_{i:\lambda} y_{i:\lambda}^T$ from selected offspring) and a **rank-one** term along the cumulated evolution path $p_c$; step-size $\sigma$ follows cumulative step-size adaptation (CSA), comparing $\|p_\sigma\|$ to $E\|\mathcal{N}(0,I)\|$. Defaults: $\lambda = 4 + \lfloor 3\ln n\rfloor$, $\mu = \lfloor\lambda/2\rfloor$, $w_i \propto \ln\tfrac{\lambda+1}{2} - \ln i$. **Sigma-collapse interpretation**: when $C$ converges to $H^{-1}$ near a strict local minimum, $p_c$ becomes uncorrelated and $\sigma$ exponentially shrinks under CSA — this is the *theoretical* basis for the "sigma → 1e-15 with no improvement = second-order local-optimal" diagnostic, not a heuristic.
- **Akimoto–Auger–Hansen 2016** ([`domains/ai-ml/source/2016-akimoto-quality-gain-analysis-weighted.md`](../../domains/ai-ml/source/2016-akimoto-quality-gain-analysis-weighted.md)) — derives the finite-dimensional quality-gain bound for the weighted-recombination ES family on arbitrary convex quadratic $f(x) = \tfrac12(x-x^*)^T A (x-x^*)$. Two key takeaways: (a) optimal recombination weights $w_k^* \propto -E[N_{k:\lambda}]$ are **Hessian-independent** — the default expected-order-statistic weights are already optimal; (b) the optimal step-size scales with $\|\nabla f(m)\| / \mathrm{Tr}(A)$, so step-size collapse is informative about gradient-trace ratio, not just function value. Justifies trusting CMA-ES's default weights even on ill-conditioned arena landscapes.
- **Loshchilov–Schoenauer–Sebag–Hansen 2014 — self-CMA-ES** ([`domains/ai-ml/source/2014-loshchilov-maximum-likelihood-based-online-adaptation.md`](../../domains/ai-ml/source/2014-loshchilov-maximum-likelihood-based-online-adaptation.md)) — the default learning rates $(c_1, c_\mu, c_c)$ are derived as fixed functions of $n$ and $\lambda$, but become substantially sub-optimal when $\lambda$ is enlarged (e.g. $\lambda = 100$, ~10× default). Self-CMA-ES runs an auxiliary CMA-ES on the hyper-parameter triple, using a rank-agreement surrogate for log-likelihood. Reports up to $1.5\times$ speedup on Sharp Ridge, matches default elsewhere on BBOB. **Arena reading**: when pop-size is bumped to 256+ for a hard problem (P15 / P16-class), the default learning rates leak performance — self-CMA-ES is worth a try before committing GPU hours.

## See also

- `wiki/findings/basin-rigidity.md` (lesson #96 — three-way local-optimality proof).
- `wiki/findings/optimizer-recipes.md` (#67 — CMA-ES gap-space recipe).
- knowledge.yaml strategy `cma_es`.
- `wiki/techniques/gap-space-parameterization.md` (companion).
- `mb/problems/1-erdos-overlap/strategy.md` (sigma collapse), `mb/problems/9-uncertainty-principle/strategy.md` (gap-space).
- Concepts: [basin-rigidity](../concepts/basin-rigidity.md), [parameterization-selection](../concepts/parameterization-selection.md).
