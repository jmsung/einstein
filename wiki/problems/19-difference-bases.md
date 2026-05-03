---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 19
arena_url: https://einsteinarena.com/problems/difference-bases
status: shelved
score_current: 2.6390274695
tier: S
concepts_invoked: [sidon-sets.md, kronecker-decomposition.md, probabilistic-method.md, basin-rigidity.md]
techniques_used: [bnb-exhaustive-w3.md, kronecker-search-decomposition.md, memetic-tabu-search.md]
findings_produced: [discrete-optimization.md]
private_tracking: ../../mb/tracking/problem-19-difference-bases/
---

# Problem 19 — Difference Bases

## Statement
Find a set B of non-negative integers (0 in B, |B| <= 2000) maximizing v = the largest integer such that every integer in {1, ..., v} occurs as a positive difference b_i - b_j; minimize |B|^2 / v.

## Approach
SOTA atom A has the Kronecker-product structure A oplus 8011 * {0, 1, 4, 6} — recognizing this product decomposition shrinks the search space dramatically. Approaches: 1-swap exhaustive (47M evaluations), 2-swap random, 3-swap LNS, simulated annealing, ILP via CP-SAT, Singer/Bose/Paley algebraic constructions. Final negative result: a full BnB exhaustive sweep over C(90,3) = 117,480 triples on Modal proves no 3-swap of the SOTA atom achieves c(A) >= 1044 (1.22T branch nodes, 0 hits). Partial w=4 sweep (3.45T nodes, 25% coverage, 0 hits) consistent. A formal BnB negative lemma is rare and high-value.

## Result
- **Score**: 2.6390274695 (7-way tied at SOTA)
- **Rank**: would land #8; not submitted
- **Date**: as of 2026-04-09
- **Status**: shelved with formal negative lemma; resume requires CP-SAT or larger w sweep

## Wisdom hook
Kronecker product structures in combinatorics reduce search space dramatically — decompose before brute-force enumeration; formal BnB negatives are rarer and more valuable than positive discoveries.

## Concepts invoked
- [sidon-sets.md](../concepts/sidon-sets.md)
- [kronecker-decomposition.md](../concepts/kronecker-decomposition.md)
- [probabilistic-method.md](../concepts/probabilistic-method.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [bnb-exhaustive-w3.md](../techniques/bnb-exhaustive-w3.md)
- [kronecker-search-decomposition.md](../techniques/kronecker-search-decomposition.md)
- [memetic-tabu-search.md](../techniques/memetic-tabu-search.md)

## Findings
- [discrete-optimization.md](../findings/discrete-optimization.md)
- [p19-kronecker-bridging-threshold.md](../findings/p19-kronecker-bridging-threshold.md) — conditional identity v = L·λ + c(A); 2-axis (c, max) Pareto (corrected by cycle 4)
- [dead-end-p19-different-k-local-search.md](../findings/dead-end-p19-different-k-local-search.md) — different-k local search around SOTA
- [dead-end-p19-4mark-sidon-rulers.md](../findings/dead-end-p19-4mark-sidon-rulers.md) — 4-mark Sidon R uniquely {0,1,4,6}
- [dead-end-p19-imperfect-5mark-sidon.md](../findings/dead-end-p19-imperfect-5mark-sidon.md) — H1 sub-cases closed
- [dead-end-p19-bose-chowla.md](../findings/dead-end-p19-bose-chowla.md) — Bose-Chowla family fails
- [dead-end-p19-extended-span-1-swap.md](../findings/dead-end-p19-extended-span-1-swap.md) — 1-swap of SOTA atom with extended y
- [dead-end-p19-from-scratch-extended-span.md](../findings/dead-end-p19-from-scratch-extended-span.md) — direct BnB at S_max=8010 + Wichmann correction (cycle 4)

## References
- Gyarmati, "Sums and differences of finite sets" (2007).
- Vinuesa, Sidon set thesis (2010).
- Singer, Bose, Paley algebraic difference-set constructions.

## Private tracking
For owner's reference: `mb/tracking/problem-19-difference-bases/` contains the BnB w=3 exhaustive summary, partial w=4 results, and Kronecker decomposition diagnostic. Not part of the public artifact.
