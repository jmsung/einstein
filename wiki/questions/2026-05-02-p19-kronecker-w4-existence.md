---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: gauss
related_problems: [P19]
related_concepts: [kronecker-decomposition.md, sidon-sets.md]
---

# Does a w=4 Kronecker decomposition exist for the difference-bases ratio improvement?

## Question

P19 Difference Bases admits a Kronecker decomposition `B = A ⊕ λ·R` with `|A|=90`, `λ=8011`, `R={0,1,4,6}` (a 4-mark Sidon ruler). The branch-and-bound exhaustive sweep over w=3 (C(90,3) = 117,480 atoms × 1.22T BnB nodes) returned **zero hits** — formal proof no 3-swap improvement exists. The w=4 partial sweep (2,504/10,000 sampled) also found zero hits.

**Open question**: does ANY Kronecker decomposition `A ⊕ λ·R'` with a different 4-mark or 5-mark `R'` (Sidon or near-Sidon) yield a strictly better ratio than the current 7-way tie?

## Why it matters

If yes → JSAgent breaks the 7-way SOTA tie at 2.639027 with a structural construction (worth submitting per the wisdom-verification rule). If no → another formal negative lemma to add to the literature, comparable to the w=3 result.

## What's been tried

- Singer / Bose / Paley constructions: all reduce to `λ=8011·{0,1,4,6}` family at the SOTA tie.
- Random search over A (1-swap, 2-swap, 3-swap LNS): saturates locally.
- BnB w=3 exhaustive: zero hits over 1.22T nodes.
- BnB w=4 partial: 2,504/10,000 sampled; no hits.

## Hypotheses

- **H1**: 5-mark Sidon ruler families (e.g. `{0,1,4,9,11}`, `{0,2,7,8,11}`) might dodge the 4-mark structural cap that anchored w=3,4 to the 7-tie. Cost: enumerate 5-mark Sidon rulers, then sweep `A` for compatibility.
- **H2**: Group-theoretic constructions (Galois fields, multiplicative subgroups) may furnish `R` outside the standard ruler families. See Vinuesa thesis on B_h[g] sets.
- **H3**: The 7-way tie may itself be at a structural cap (analogous to the 8-way cap for P22 d=12 kissing). If H3 holds, search is provably futile.

## Next step

1. Enumerate 5-mark Sidon rulers up to span ~16 (small enough to feasibly sweep via numba BnB on M5 Max local — fits in 128GB RAM, sequential, no Modal needed).
2. For each `R'`, sweep `A` candidates with the existing numba BnB infrastructure under `mb/tracking/problem-19-difference-bases/`.
3. If still zero hits across all 4-mark and 5-mark Sidon `R'`, escalate H3 — write a formal first-order obstruction proof (analogous to P22 link-tangent test).

## References

- `wiki/concepts/kronecker-decomposition.md`
- `wiki/concepts/sidon-sets.md`
- `wiki/techniques/kronecker-search-decomposition.md`
- `wiki/techniques/bnb-exhaustive-w3.md`
- `source/papers/2010-vinuesa-sidon-thesis.md`
- `source/papers/2007-gyarmati-sums-differences.md`
- Private tracking: `mb/tracking/problem-19-difference-bases/strategy.md` (Kronecker discovery + BnB w=3,4 results)
