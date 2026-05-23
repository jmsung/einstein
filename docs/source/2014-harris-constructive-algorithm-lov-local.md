---
type: source
kind: paper
title: A constructive algorithm for the Lovász Local Lemma on permutations
authors: David G. Harris, A. Srinivasan
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.02663
source_local: ../raw/2014-harris-constructive-algorithm-lov-local.pdf
topic: general-knowledge
cites:
---

# A constructive algorithm for the Lovász Local Lemma on permutations

**Authors:** David G. Harris, A. Srinivasan  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1612.02663

## One-line
Gives the first randomized polynomial-time algorithm (the "Swapping Algorithm") that constructively realizes the lopsided Lovász Local Lemma on random permutations, with applications to Latin transversals, rainbow Hamiltonian cycles, strong coloring, and hypergraph packing.

## Key claim
Under the same hypothesis as the permutation-LLL existence theorem (existence of $\mu : \mathcal{B} \to [0,\infty)$ with $\mu(B) \geq P_\Omega(B) \prod_{B' \sim B}(1+\mu(B'))$), a Moser–Tardos-style swap-resampling procedure terminates in expected polynomial (often near-linear) time and admits an RNC parallel version; this yields a constructive proof that every $n\times n$ matrix with each value appearing $\leq (27/256)n$ times has a Latin transversal, and the new bound $L(s;n,n) \geq (s - O(\sqrt{s}))n$, asymptotically optimal in $s$.

## Method
Replace Moser–Tardos variable resampling with a Fisher–Yates-style **Swap subroutine**: when a bad event $B$ fires, for each involved permutation $\pi_k$ swap the relevant domain entries with uniformly random partners outside the already-touched set. Analysis introduces a **witness subdag** $\mathrm{Proj}_k(\tau)$ per permutation (a flattening of the witness tree to one permutation's $(x,y)$ pairs), and proves a permutation-flavored **Witness Tree Lemma** $P(\tau \text{ appears}) \leq \prod_i P_\Omega(B_i)$ by tracking how swaps must be constrained to remain consistent with the subdag history (Prop. 3.2: any change $\pi^{t_0}_k(X)=Y \to \pi^{t_2}_k(X)\neq Y$ forces an intermediate bad event touching row $X$ or column $Y$). Symmetry of the swap subroutine under domain/range permutations and reordering (Appendix A) lets the analysis treat each permutation independently.

## Result
- Latin transversals: constructive $\Delta \leq (27/256)n$ (matches Bissacot et al.); generalized to arbitrary cycle structures with $\Delta \leq 0.027n$ (Thm 8.3).
- $s$-transversals: $L(s;n,n) \geq (s-O(\sqrt{s}))n$, beating the LLL's $s/e$ even non-constructively.
- Strong chromatic number: block size $b \geq (256/27)\Delta$ gives a strong coloring in $O(n\Delta)$ expected time, with RNC variant for $b \geq (256/27 + \varepsilon)\Delta$.
- Edge-disjoint hypergraph packing of $r$-uniform $H_1,H_2$: constructive whenever $(d_1+1)m_2 + (d_2+1)m_1 < \binom{n}{r}/e$.
- Inherits Moser–Tardos extensions: output-distribution characterization, partial resampling, adversarial bad-event choice, RNC parallelism.

## Why it matters here
General background; no direct arena tie. The lopsided-LLL-on-permutations machinery could inform any discrete-combinatorics arena problem framed as injection-with-forbidden-patterns (rainbow / Latin / hypergraph-packing flavors), and provides a constructive existence-to-algorithm bridge whenever a non-constructive LLL bound is the current best — but none of the 23 arena problems are currently mapped to this framework.

## Open questions / connections
- Can the $(27/256)n$ Latin transversal constant be pushed toward the conjectured $n-1$? Gap between LLL-style $\Theta(n)$ bounds and the Ryser–Brualdi–Stein conjecture.
- Is there a truly generalized constructive LLLL that subsumes Moser–Tardos, Swapping, Achlioptas–Iliopoulos [1], Harvey–Vondrák [22], and Kolmogorov [27]? (Open: Section 9.)
- Does the partial-resampling/commutativity property (Kolmogorov [27]) extend to all permutation-LLL applications, including the $s$-transversal optimal bound (Thm 8.2)?

## Key terms
Lovász Local Lemma, lopsided LLL, Moser-Tardos resampling, random permutations, Latin transversal, Fisher-Yates swap, witness tree, witness subdag, rainbow Hamilton cycle, strong chromatic number, hypergraph packing, negative dependence graph, RNC parallel algorithm, Harris, Srinivasan, Erdős-Spencer, Bissacot
