# Problem 19: Difference Bases

## Problem

Find a set B of non-negative integers (with 0 mandatory) minimizing

    score = |B|² / v

where v is the largest integer such that every element of {1, ..., v} appears
as a positive difference b_i − b_j for some b_i, b_j ∈ B with b_i > b_j. Lower
is better. The arena constraint is |B| ≤ 2000.

This is the classical **sparse ruler** (a.k.a. **restricted difference basis**)
problem: place the fewest marks on a ruler of length v so that every integer
length from 1 to v can be measured between two marks.

## Background

Let k(v) be the minimum |B| with 0 ∈ B ⊂ {0, ..., v} such that the positive
differences cover {1, ..., v}. Erdős and Gál (1948) and Rédei and Rényi (1949)
established the asymptotic

    k(v)² / v  →  c   as v → ∞,

with 2.434 ≤ c ≤ 3 and successive improvements narrowing the gap. Exact
optimal rulers are known for small v via exhaustive search (Wichmann, Leech,
Pegg and collaborators), and several infinite families of near-optimal
constructions — Wichmann rulers and their variants — give explicit upper
bounds. The arena problem fixes a single target: report a set B whose ratio
|B|² / v is as small as possible.

## Arena Details

- **API ID**: 19
- **Direction**: minimize
- **Solution format**: `{"set": [ints]}` — any list of non-negative integers
  (deduplicated, 0 auto-added by the verifier)
- **Scoring**: `|B|² / v` where v is the longest initial run of covered
  positive differences

## Approach

The strategy combines three ingredients at a high level:

1. **Warm starts from classical constructions** — Wichmann-family rulers and
   related explicit families seed the search near the known upper-bound
   envelope.
2. **Local combinatorial search** — neighborhood moves on the integer set
   (swap, shift, insert/delete) refine warm starts and explore nearby basins.
3. **Structured global search** — a constraint-programming formulation
   handles small blocks exactly, and branch-and-bound fills in atoms that
   local search cannot escape.

Detailed methodology, parameters, and experiment logs are kept private.

## Infrastructure

- `src/einstein/difference_bases/evaluator.py` — arena-matching exact scorer
- `src/einstein/difference_bases/fast.py` — numba kernels for incremental
  difference-multiset updates
- `src/einstein/difference_bases/optimizer.py` — shared optimizer utilities
- `tests/difference_bases/test_evaluator.py` — evaluator parity tests

## References

- Erdős, P. and Gál, I. S. (1948) — *On the representation of 1, 2, ..., N by
  differences*
- Rédei, L. and Rényi, A. (1949) — *On the representation of the numbers
  1, 2, ..., N by differences*
- Leech, J. (1956) — *On the representation of 1, 2, ..., n by differences*,
  J. London Math. Soc.
- Wichmann, B. (1963) — *A note on restricted difference bases*, J. London
  Math. Soc.
- Pegg Jr., E. — *Sparse rulers*, OEIS entries A004137, A103294, and the
  Math Games column on optimal rulers
- OEIS A004137 — minimum |B| for each v (optimal sparse ruler lengths)

*Last updated: 2026-04-09*
