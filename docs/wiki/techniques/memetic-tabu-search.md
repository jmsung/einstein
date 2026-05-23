---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P12]
compute_profile: [local-cpu]
cost_estimate: "tens of minutes (1.26B evals in 30 min on CPU)"
hit_rate: "TBD"
---

# Memetic Tabu Search (Vectorized)

## TL;DR

Vectorized tabu search with population crossover for `±1`-coefficient combinatorial problems. Champion on P12 Flat Polynomials: 1.26B evaluations in 30 minutes of CPU rediscovered SOTA `1.2809` independently — but could not break the proven 4-flip local optimum. Use to confirm exhaustion; recognize when algebraic constructions are required.

## When to apply

- Discrete combinatorics with binary / ±1 / small-integer coefficients (Littlewood / flat polynomials, ±1 sequences).
- Score is local-optimum-rich (small flips give finite improvements; tabu is necessary).
- Population-based crossover gives diversity (memetic = GA + local search).
- Goal: confirm a SOTA is locally optimal under all w-flip neighborhoods, OR independently discover an unknown SOTA.

## Procedure

1. **Vectorize the score** across all neighbors of the current state:
   ```python
   # Score every 1-flip neighbor in one numpy/torch vectorized call
   neighbors_score = score_batch(np.tile(x, (n, 1)) ^ np.eye(n).astype(int))
   ```
2. **Tabu list**: keep recent moves (last K flips); reject revisiting.
3. **Aspiration**: accept a tabu move if it strictly improves the global best.
4. **Population**: maintain ~200 individuals; crossover via uniform mask; local search via tabu within each child.
5. **Restart cadence**: re-seed individuals when no improvement in N iters; helps escape flat plateaus.
6. **Termination**: stop when budget exhausted or all individuals converge to the same score within tolerance.

## Pitfalls

- **4-flip local optimum is a ceiling for stochastic search** (P12): SA, GA, memetic-tabu, and 1.26B-eval brute force all converge to ~1.35; SOTA at 1.2809 is provably 4-flip-local-optimal but algebraically special. Recognizing this stops wasted compute.
- **GA without local search converges to ~1.35 basin** (P12): naive population-based (GA pop=200) hits the same wall as SA — the basin is locally rigid.
- **Memetic tabu independently rediscovers SOTA** but cannot beat it: this is the diagnostic that the SOTA is structurally special (Turyn / Rudin-Shapiro / Fekete construction), not just a deep basin.
- **Vectorization is essential**: scalar tabu loops at <1M evals/sec are infeasible for B-scale searches; vectorized at ~700K evals/sec is the floor.
- **Tabu list size**: too small re-cycles (gets stuck); too large blocks productive moves. K ≈ √n is a working starting point.

## When NOT to use (pivot signal)

- Memetic tabu hits the same local optimum across 1B+ evals → SOTA is probably algebraically special. Pivot to literature search for the special construction (Turyn, Rudin-Shapiro, Fekete, Shapiro polynomials).
- Score gap between stochastic ceiling (~1.35) and algebraic SOTA (1.2809) is a strong signal of the algebraic-construction barrier.

## Compute profile

Local CPU. Vectorized numpy — 16-core multiprocess scales linearly. P12: 1.26B evals in 30 min on a workstation. GPU offers little benefit at the small per-iter tensor sizes.

## References

- `wiki/findings/discrete-optimization.md`.
- knowledge.yaml strategies `memetic_tabu_search`, `genetic_algorithm`, `simulated_annealing`.
- `mb/tracking/problem-12-flat-polynomials/strategy.md`.
