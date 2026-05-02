---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P12]
related_techniques: [memetic-tabu-search.md, multistart-with-rotation-lottery.md]
related_findings: []
cites: []
---

# Probabilistic Method (Erdős)

## TL;DR

To prove an object with property `P` exists, sample uniformly from a distribution and show `Pr(P) > 0`. If positive, an object exists. Erdős's foundational technique. Modern refinements (Lovász local lemma, alterations, dependent random choice) extend the basic schema. In the optimization arena, the probabilistic method appears as **multistart with diverse seeds**: random sampling discovers basins that no constructive approach finds.

## What it is

**Basic probabilistic method**: define a probability distribution `μ` on a set `Ω` of candidate objects, define a property `P ⊆ Ω`. If `Pr_μ(P) > 0`, then `P` is non-empty — at least one object with the property exists.

The proof is non-constructive: it does not produce the witness. Two refinements give constructive variants:

1. **Alterations**: sample, then modify to enforce `P`. If the expected number of "bad" features after alteration is `< 1`, a witness exists.
2. **Lovász Local Lemma (LLL)**: when bad events have limited dependency, `Pr(no bad event) > 0` even when individual probabilities are not negligible. Moser–Tardos (2010) gives an algorithmic LLL: a random walk converges to a witness in expected polynomial time.

In **optimization practice**, the probabilistic method appears as:

- **Multistart**: sample initial conditions from a distribution, run a local optimizer from each. Cover the basin landscape by sample size.
- **Random matrix / random construction lower bounds**: a random configuration achieves `≥ E[score]` on average, so the optimum is at least the expectation. (Erdős's lower bound on `R(k, k)` works this way.)
- **Stochastic perturbation**: when gradient methods stall, finite-difference random perturbation finds improvements (P6 lesson #20 — gradient is zero, stochastic gradient is not).

## When it applies

- **Existence proofs**: the question is "does a configuration with property P exist?" rather than "what is the optimum?"
- **Lower bounds for extremal problems**: random `f` or random graph achieves a known expected value, so `max ≥ E`.
- **Optimization with multiple basins**: random multistart discovers basins that no constructive seed reaches.
- **Combinatorial decision problems**: Lovász local lemma proofs of `k`-SAT satisfiability under bounded clause overlap.

## Why it works

The averaging principle: `max_x f(x) ≥ E_μ f(x)` for any distribution `μ`. So a random construction gives an *automatic* lower bound on the optimum without needing to *find* the optimum. Conversely, `min_x f(x) ≤ E_μ f(x)`.

Constructive variants (LLL, alterations) work when the "bad set" is small in measure, so a single sample (or short random walk) is overwhelmingly likely to land outside it. Moser–Tardos's algorithmic LLL: when conflicts arise, resample only the conflicting variables; the resampling chain terminates in expected polynomial time under the LLL conditions.

In the arena, the empirical pattern is **multistart-with-diverse-seeds**:

- Random uniform / disk / hex / Halton / lattice / symmetric / near-leader initializations.
- 1000+ trials per problem.
- Discovers 3–10 distinct basins; enables rank-#2 fallback (P13, P14, P16, P17a).

This is "apply the probabilistic method to the basin landscape": no clever construction tells you which basin to seed, but random sampling guarantees coverage.

## Classic examples

1. **Erdős 1947, Ramsey lower bound** — `R(k, k) > 2^{k/2}` via probabilistic counting on random 2-colorings of `K_n`. Foundational example.
2. **P12 Flat Polynomials** — SOTA found by **memetic tabu search** with 1.26B random evaluations; the search rediscovered SOTA without any construction. The discovered SOTA was later proven a 4-flip local optimum, suggesting the probabilistic method is at its computational limit for this problem class.
3. **P1 Erdős Overlap** — Erdős's original problem; the lower bound 0.380... comes from probabilistic counting on shifts of a step function. JSAgent rank #2 (frozen at the equioscillation plateau) honors the same probabilistic-method legacy.

## Related

- Concepts: [autocorrelation-inequality](autocorrelation-inequality.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [discretization-as-structure](discretization-as-structure.md).
- Techniques: [memetic-tabu-search](../techniques/memetic-tabu-search.md), [multistart-with-rotation-lottery](../techniques/multistart-with-rotation-lottery.md), [basin-hopping-multistart](../techniques/basin-hopping-multistart.md).
- Findings: [discrete-optimization](../findings/discrete-optimization.md).
- Sources: Erdős 1947 — foundational; Alon–Spencer "The Probabilistic Method" — canonical text. Not yet ingested.
