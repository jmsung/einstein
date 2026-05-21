---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P19]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "hours (decomposition discovery) to GPU-hours (search after decomposition)"
hit_rate: "TBD"
---

# Kronecker / Direct-Sum Decomposition for Combinatorial Search

## TL;DR

For combinatorial problems whose ostensible search space is huge, look for a **Kronecker-product / direct-sum decomposition** first: `A ⊕ λ·R` where `A` is a small base set and `λ·R` is a scaled "shift" set. P19 Difference Bases SOTA decomposes as `A ⊕ 8011·{0,1,4,6}` — searching the small base + the small shift is dramatically cheaper than searching the full set. Decompose before brute-force.

## When to apply

- Combinatorial problem with a sum / difference / additive structure in ℤ (sparse rulers, Sidon sets, B_h sets).
- Current search budget is exhausted on direct enumeration / SA / GA.
- A multiplicative or block structure is suspected (looking at top scores reveals a periodicity or divisibility).
- Group-theoretic or algebraic constructions (Singer, Bose, Paley) are known but haven't been tried.

## Procedure

1. **Check the SOTA for additive structure**: `gcd` of differences; periodicity in the support; multiplicative shifts.
   - P19: `B = {0, 1, 2, 7, ..., 8019, 8023, 8025, 8030, ...}` — gcd of large jumps = 8011.
2. **Conjecture decomposition**: `B = A ⊕ λ·R = { a + λ·r : a ∈ A, r ∈ R }` for small `A`, `R`, scalar `λ`.
3. **Verify**: `|B| = |A| · |R|`; `(B − B) = (A − A) ⊕ λ·(R − R)`; the score factorizes (or bounds nicely).
4. **Search in (A, R, λ)** instead of (B):
   - `|A| ~ 30`, `|R| ~ 4`, `λ` from a few candidates → search space is dramatically smaller.
   - Use ILP (CP-SAT) on the small subproblems, OR custom numba BnB if CP-SAT walls (lesson #62).
5. **Combine with formal BnB** (`bnb-exhaustive-w3.md`) for negative lemmas at small sizes.

## Pitfalls

- **CP-SAT walls at large `|B|`**: the boolean engine blows up to ~7M aux booleans for "exists a pair with difference d" at S_max=6967. Decomposition reduces both `|B|` and the boolean encoding cost. If you must use ILP, do it in (A, R) space.
- **Kronecker isn't always exact**: sometimes the decomposition is approximate (`B ≈ A ⊕ λ·R`) with small additive correction. Check whether the approximation preserves the score within tolerance.
- **Group-theoretic constructions** (Singer / Bose / Paley) often don't give Kronecker structure but rather field-element structure — not the same thing. Try both.
- **Branching factor pitfall**: even after decomposition, naive BnB can have branching factor `≤ 2 · depth`. Use goal-directed branching ("the new mark must be `existing_a ± d_star`" — lesson #62).
- **Negative lemma scoping** (lesson #64): if BnB rules out only configurations where each new mark immediately covers the smallest uncovered `d*`, the lemma is "no w=3 swap with that property" — NOT "no w=3 swap". Document the soundness boundary.

## Compute profile

- Local CPU: decomposition discovery + small-`(A, R)` ILP. Custom numba BnB at ~10M nodes/sec.
- Modal: w=3 exhaustive sweep over C(90,3)=117,480 atom triples → 88 wall-min, 100 concurrent containers, ~$4 (lesson #63). Single-digit USD for formal negative lemmas.

## References

- knowledge.yaml: P19 strategy notes.
- `wiki/findings/discrete-optimization.md` (lesson #62 — "When to write your own solver"; CP-SAT wall diagnostic).
- `wiki/findings/gpu-modal-compute.md` (lesson #63 — Modal BnB economics).
- `wiki/techniques/bnb-exhaustive-w3.md` (companion: formal BnB negative lemmas).
- `mb/tracking/problem-19-difference-bases/strategy.md` (Kronecker structure A ⊕ 8011·{0,1,4,6}).
