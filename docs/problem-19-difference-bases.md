# Problem 19: Difference Bases

**Status**: No submission

## Problem

Find a set B of non-negative integers (with 0 mandatory) minimizing

    score = |B|² / v

where v is the largest integer such that every element of {1, ..., v} appears as a positive difference b_i − b_j for some b_i, b_j ∈ B with b_i > b_j. Lower is better. The arena constraint is |B| ≤ 2000.

This is the classical **sparse ruler** (a.k.a. **restricted difference basis**) problem: place the fewest marks on a ruler of length v so that every integer length from 1 to v can be measured.

## Background

Let k(v) be the minimum |B| with 0 ∈ B ⊂ {0, ..., v} such that the positive differences cover {1, ..., v}. Erdős-Gál (1948) and Rédei-Rényi (1949) established:

    k(v)² / v → c as v → ∞

with 2.434 ≤ c ≤ 3 and successive improvements narrowing the gap. Exact optimal rulers are known for small v via exhaustive search. Wichmann rulers and variants give explicit upper bounds for infinite families.

## Arena Details

- **API ID**: 19
- **Direction**: minimize
- **Solution format**: `{"set": [ints]}` — non-negative integers (deduplicated, 0 auto-added)
- **Scoring**: |B|² / v where v is the longest initial run of covered positive differences

## Approach

### Strategy Overview

Three ingredients: classical constructions as warm-starts, local combinatorial search for refinement, and structured global search via constraint programming and branch-and-bound.

### Classical Constructions as Warm-Starts

Wichmann-family rulers and related explicit families seed the search near the known upper-bound envelope. These provide provably good starting points without requiring expensive search.

### Local Combinatorial Search

Neighborhood moves on the integer set — swap, shift, insert/delete — refine warm starts and explore nearby basins. Numba-accelerated incremental difference-multiset updates enable fast move evaluation.

### Constraint Programming and Branch-and-Bound

- **CP-SAT formulation**: Boolean variables for set membership, constraints for difference coverage. Works for small block sizes.
- **Custom numba branch-and-bound**: For larger instances where CP-SAT fails.

### What Worked

- **Classical constructions** — Wichmann families provide strong baselines
- **Local search with numba kernels** — fast incremental evaluation enables deep neighborhood exploration

### What Didn't Work

- **CP-SAT at large scale** — the boolean engine hits a wall at ~7M auxiliary booleans. The presolve shows `num_removable_bools ≈ num_bools`, meaning the engine's pruning is ineffective. This is a solver limitation, not an encoding issue — don't retry with a different formulation.
- **Custom BnB completeness** — branch-and-bound with restricted move classes can miss solutions. The invariant must be documented: what solution class can the branching strategy reach, and what can it not?

## Key Insights

- **CP-SAT has a boolean engine wall**: For combinatorial problems with "exists a pair with difference d" structure at large scale, CP-SAT's boolean engine fundamentally can't handle it. Write custom solvers instead of retrying different formulations.
- **Wichmann rulers are strong baselines**: Classical number-theoretic constructions remain competitive. Don't underestimate explicit families — they encode deep structure.
- **Incremental evaluation is essential**: For set-modification moves (swap, shift), incremental difference-multiset updates avoid recomputing from scratch.
- **Atom decomposition**: Large difference bases can sometimes be decomposed as B = A + c × S for a small set S, revealing hidden algebraic structure.

## References

- Erdős, P. and Gál, I. S. (1948) — *On the representation of 1, 2, ..., N by differences*
- Rédei, L. and Rényi, A. (1949) — *On the representation of the numbers 1, 2, ..., N by differences*
- Leech, J. (1956) — *On the representation of 1, 2, ..., n by differences*, J. London Math. Soc.
- Wichmann, B. (1963) — *A note on restricted difference bases*, J. London Math. Soc.
- Pegg Jr., E. — *Sparse rulers*, OEIS entries A004137, A103294
- OEIS A004137 — minimum |B| for each v (optimal sparse ruler lengths)

## Infrastructure

- `src/einstein/difference_bases/evaluator.py` — arena-matching exact scorer
- `src/einstein/difference_bases/fast.py` — numba kernels for incremental difference-multiset updates
- `src/einstein/difference_bases/optimizer.py` — shared optimizer utilities
- `tests/difference_bases/test_evaluator.py` — evaluator parity tests

*Last updated: 2026-04-13*
