---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
synthesized_into: ../concepts/basin-rigidity.md
cites:
  - ../concepts/basin-rigidity.md
  - ../concepts/reduced-hessian.md
---

> **See also**: [`concepts/basin-rigidity.md`](../concepts/basin-rigidity.md) — the abstract concept distilled from the lessons below. This finding is the **provenance**: the per-problem empirical episodes (with specific lesson IDs and dates) that the concept page abstracts. Read the concept first; come here for the receipts.

# Basin Rigidity Proofs & Locking Diagnostics — empirical lessons

Methods and thresholds for determining when an optimization basin is mathematically rigid — meaning no local method will ever improve the current score. These diagnostics prevent wasting compute on provably locked problems.

## Lesson #29: Basin Locking Threshold — <2% of minImprovement After 12+ Approaches Means Pivot

Problem 6: 44 experiments across 12+ fundamentally different approaches (micro-perturbation, SA tempering, GPU brute-force, cage escape, smooth gradient, eigenvalue, remove-readd) yielded only 1.92% of the needed improvement. When exhaustive breadth search produces <2% of target, the problem requires a different starting configuration or mathematical breakthrough, not more compute. Pivot to higher-value targets.

## Lesson #84: 44K Multi-Start Search Is Gold Standard for Proving Global Optimality

Problem 5 Min Distance Ratio (2D, n=16, 2026-04-10): after 30 random restarts suggested single-basin, a 44,018-config massive multi-start SLSQP search (8 diverse initialization strategies: uniform random, disk, concentric rings, grids, hex lattice, Halton, topology perturbation; 200 parallel Modal containers; 205s wall time) found 11 distinct basins but none below 12.889228 (the minImprovement threshold). This definitively proved the (22,8) David Cantrell configuration is the global optimum and P5 is permanently frozen. The 1400x scale-up from 30 to 44K starts cost only ~3 min wall time but converts "probably single-basin" into "definitively single-basin."

**Rule**: before permanently closing a frozen problem, invest the 3-minute Modal multi-start search — it prevents future returns to the problem.

## Lesson #85: Over-Constrained Reduced Hessian = Fully Rigid Basin

Problem 5 (2D, n=16): the (22,8) minimum has 30 active constraints (22 min-edge equality + 8 max-edge equality) on 28 DOF (32 coords - 4 affine gauges), making it over-constrained by 2. The reduced Hessian has no zero eigenvalues — no infinitesimal motion improves the objective while maintaining all active constraints. This is a stronger proof of basin rigidity than "44K starts found no alternative" because it's analytical, not empirical.

**Diagnostic**: for any constrained geometric optimization, count `active_constraints - (coords - gauges)`. If positive, the basin is fully rigid and no local method will ever improve it.

## Lesson #88: KKT Exact Solve (mpmath) Definitively Confirms Basin Ceiling

Problem 18 (2026-04-10): 80-digit mpmath KKT solve found the exact optimum at 2.365832375910832741572... with 64 active constraints for 64 variables (0 DOF — fully determined system). This proves the basin ceiling is not a numerical artifact but a mathematical certainty.

**Diagnostic**: for any constrained packing, count active constraints vs variables. If active_constraints >= variables, the system is fully determined (0 DOF) and the KKT solution is unique — no local method can improve it. Pair with lesson #85 (over-constrained reduced Hessian) for a complete rigidity proof.

## Lesson #96: Three-Way Convergence Proof for Minimax Local Optimality

Problem 1 Erdos Minimum Overlap (2026-04-17, feat/auto-p1): established a definitive local-optimality proof via three independent convergence tests, each targeting a different optimality condition:

1. **First-order (gradient = 0)**: PyTorch LBFGS with strong Wolfe line search at float64 gives ZERO improvement in 200 steps — the gradient is numerically zero.
2. **Second-order (covariance collapse)**: CMA-ES starting from SOTA with pop_size=50 collapsed sigma to 1e-15 in 50k evaluations with ZERO improvement — no direction at any scale reduces the objective.
3. **Minimax optimality (equioscillation)**: Remez exchange algorithm converges immediately with zero exchanges — the SOTA satisfies the Chebyshev equioscillation necessary conditions at 437 active shifts.

**When to use**: for any discretized-function minimax problem (max_k f(k) or min_k f(k)) where the solution is suspected to be a local optimum but not provably so. The three tests cover complementary failure modes: gradient methods miss non-smooth structure, CMA-ES misses gradient-accessible improvements, and Remez misses higher-order structure. All three converging is the strongest computational proof of local optimality short of an analytical certificate.

**Contrast with lessons #85/#88**: those apply to constrained geometric problems where you count active constraints vs DOF. This lesson applies to unconstrained or minimax problems where the "constraints" are implicit (the max over shifts). The diagnostic cost is ~10 minutes total (3 min LBFGS, 5 min CMA-ES, 2 min Remez).
