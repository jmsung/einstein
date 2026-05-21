---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - ../source/repos/jmsung-einstein.md
  - ../source/repos/jmsung-einstein-codebase.md
  - ../concepts/bourgain-clozel-kahane.md
---

# Verification Patterns & Quality Gates

## Strategic #6: Verification > optimization {#strategic-6}

A wrong score is worse than no score. Build exact verifiers first, then optimize. Problem 18: 90% of "improvements" from the fast evaluator were fake. The fast evaluator's false positives cost more time than they save when they propagate into submissions.

## Two-Tier Verification {#two-tier-verification}

Fast scorer for the optimization loop + exact verifier as a quality gate. Used across multiple problems.

- **Fast**: FFT/numpy, ~milliseconds — drives the inner optimization loop where throughput matters
- **Exact**: sympy/np.convolve, ~seconds-minutes — serves as the quality gate before any submission
- **Rule**: never submit without exact verification

The two tiers serve fundamentally different purposes. The fast scorer maximizes iterations per second in the search loop. The exact verifier catches the false positives that the fast scorer inevitably produces. Collapsing them into one tier either cripples search speed (exact-only) or lets false positives through to submission (fast-only).

## #25: Hybrid verifier (sympy + numpy.roots) is 8x faster than full sympy {#lesson-25}

For polynomial quotient problems, build the polynomial with exact sympy arithmetic, then use `numpy.roots` (companion matrix eigenvalues) to find ALL roots in O(n^3). For k=13 (degree-27 quotient): 12s vs 96s for full sympy. Catches all far sign changes with no grid sampling.

The key insight is separating exact coefficient computation (sympy) from root-finding (numpy). The coefficients need exact arithmetic to avoid cancellation errors in the quotient polynomial. But once the coefficients are exact, root-finding via the companion matrix eigenvalue method is both faster and more reliable than sympy's symbolic root-finding.

## #27: Fast evaluator false positives concentrate in far-field sign changes {#lesson-27}

Problem 9 (Uncertainty Principle): the fast evaluator (grid-based) has a 90%+ false positive rate for improvements because sign changes at x >> max(roots) are invisible to finite grids. The far-field region where the polynomial has large magnitude but may still cross zero is exactly where a fixed grid undersamples.

**Rule**: always use a root-finding verifier (numpy.roots or sympy) that finds ALL roots analytically, not grid sampling that can miss distant sign changes. The root-finding approach is both more reliable (zero false negatives for polynomial problems) and provides exact root locations for downstream analysis.

## #94: Numerical precision alone is not sufficient — enforce mathematical constraints {#lesson-94}

Problem 9 (Uncertainty Principle, 2026-04-19): our poly_evaluate was triple-verified at dps=80/100/150 with agreement to 1.3e-15 — yet the score of 1.07e-13 was invalid. The proven lower bound is S >= 0.2025 (Georgiev et al., 2025, p.24, C_{6,11} bounds). Root cause: the evaluator computed the polynomial correctly but never checked that the solution satisfied the problem's mathematical constraints (f must be even, f(0) < 0, f_hat(0) < 0). Without constraint enforcement, the optimizer trivially minimized the product A(f)A(f_hat) by violating sign conditions.

**Rule**: for every problem, the local evaluator must enforce ALL mathematical constraints from the problem statement, not just compute the objective function. Precision verification (triple-check at multiple dps) catches numerical errors but cannot catch constraint violations. Before claiming any result, verify: (1) the computation is numerically accurate (multi-precision agreement), AND (2) the solution satisfies every stated constraint. When a score falls below a known theoretical bound, suspect constraint violation before suspecting a mathematical breakthrough.

## #95: Always check theoretical bounds before claiming results {#lesson-95}

Problem 9 (Uncertainty Principle, 2026-04-19): a score of 1.07e-13 was celebrated and posted to GitHub before discovering it was below the proven lower bound of 0.2025. The theoretical bounds (0.2025 <= C_{6,11} <= 0.3102) from Georgiev et al. / Bourgain-Clozel-Kahane / Cohn-de Laat-Goncalves were publicly available in the reference paper (arXiv:2511.02864, p.24) cited by the arena operator.

**Rule**: before investing significant optimization effort or claiming a breakthrough score, search the literature for known theoretical bounds on the problem's objective. If a score violates a proven bound, the evaluator is wrong, not mathematics. This check takes minutes (search arXiv + problem statement for "lower bound" / "upper bound") and would have saved 2 days of optimization on an invalid objective.
