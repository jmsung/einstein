---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 12
arena_url: https://einsteinarena.com/problems/flat-polynomials
status: rank-8
score_current: 1.3539
tier: B
concepts_invoked: [discretization-as-structure.md, basin-rigidity.md, probabilistic-method.md]
techniques_used: [memetic-tabu-search.md, basin-hopping-multistart.md, multistart-with-rotation-lottery.md]
findings_produced: [discrete-optimization.md]
private_tracking: ../../mb/tracking/problem-12-flat-polynomials/
---

# Problem 12 — Flat Polynomials (degree 69, +/-1 coefficients)

## Statement
Find a degree-69 polynomial with +/-1 coefficients that minimizes max|p(z)| / sqrt(71) on the unit circle, evaluated at 1M sample points (Littlewood / flat polynomials problem).

## Approach
SOTA (1.2809) is a proven 4-flip local optimum — three independent searchers converge to the identical solution, suggesting it is the true minimum reachable by any local-search procedure. Memetic tabu search (vectorized, 18K rounds, 1.26B evaluations on M5 Max) independently rediscovered SOTA from random init. Simulated annealing (single-bit-flip neighborhood, 2M iters x 10 restarts) cannot escape: SOTA's 4-flip basin is wider than 2-flip moves can cross. Algebraic constructions explored — Turyn, Rudin-Shapiro, Fekete polynomials — none match SOTA. The 0.06 gap to rank #2 indicates an algebraic barrier that stochastic search cannot bridge.

## Result
- **Score**: 1.3539 (best from-scratch; rediscovered SOTA 1.2809)
- **Rank**: #8
- **Date**: as of 2026-05-02
- **Status**: stochastic-search exhausted; algebraic breakthrough required

## Wisdom hook
Discrete +/-1 combinatorics problems often have algebraically special optima unreachable by stochastic search — recognize when local-optimality exploration is exhausted.

## Concepts invoked
- [discretization-as-structure.md](../concepts/discretization-as-structure.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)
- [probabilistic-method.md](../concepts/probabilistic-method.md)

## Techniques used
- [memetic-tabu-search.md](../techniques/memetic-tabu-search.md)
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)
- [multistart-with-rotation-lottery.md](../techniques/multistart-with-rotation-lottery.md)

## Findings
- [discrete-optimization.md](../findings/discrete-optimization.md)
- [float64-ceiling.md](../findings/float64-ceiling.md) — P12 added to cross-problem inventory 2026-05-02 (byte-identical SOTA pattern, sha256 `992570de7873` shared by Together-AI, GaussAgent3615, alpha_omega_agents)

## Open questions
- [2026-05-02-p12-flat-poly-sota-uniqueness.md](../questions/2026-05-02-p12-flat-poly-sota-uniqueness.md) — is the byte-identical SOTA at deg-69 the unique global optimum over `{-1, +1}⁷⁰`? Empirically yes (3-agent byte-convergence + MTS rediscovery + 4-flip local optimality); formally unproven.
- Littlewood, "On polynomials with +/-1 coefficients."
- Rudin-Shapiro polynomial constructions.
- Turyn sequences and Fekete polynomials.
- Erdős's flat polynomial conjectures.

## Private tracking
For owner's reference: `mb/tracking/problem-12-flat-polynomials/` contains the memetic tabu run log and algebraic-construction comparison. Not part of the public artifact.
