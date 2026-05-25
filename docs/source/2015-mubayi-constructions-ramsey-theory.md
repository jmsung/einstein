---
type: source
kind: paper
title: Constructions in Ramsey theory
authors: D. Mubayi, Andrew Suk
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.07082
source_local: ../raw/2015-mubayi-constructions-ramsey-theory.pdf
topic: general-knowledge
cites:
---

# Constructions in Ramsey theory

**Authors:** D. Mubayi, Andrew Suk  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.07082

## One-line
New constructive lower and upper bounds for several hypergraph Ramsey-type quantities, including the off-diagonal Ramsey number $r_k(k+1, n)$, the Erdős–Rogers function $f^k_{k+1,k+2}(N)$, and Ramsey numbers for $k$-half-graphs versus cliques.

## Key claim
For $k \geq 4$: $r_4(5,n) > 2^{n^{c \log \log n}}$ (first super-exponential lower bound), and $r_k(k+1,n) > \mathrm{twr}_{k-2}(n^{c\log\log n})$. For $k \geq 14$: $g(k,N) = f^k_{k+1,k+2}(N) < O(\log^{(k-13)} N)$, an iterated-logarithm upper bound replacing the prior $O((\log N)^{1/(k-2)})$. For $k$-half-graphs $B_k$: $r(B_k, K_n^k) > 2^{\Omega(n)}$ while $r(B_k, K_n^k) \leq (n!)^{k-1}$.

## Method
Three main techniques. (1) Variants of the Erdős–Hajnal **stepping-up lemma**: encode vertices in binary, use $\delta(a,b) =$ highest differing bit, and color $k$-tuples based on monotonicity / local extrema patterns of the $\delta$-sequence to lift a $(k-1)$-uniform coloring to a $k$-uniform one. (2) For Erdős–Rogers: an inductive stepping-up recurrence $g(k, 2^N) < k \cdot g(k-1, N)$ via a clever edge rule based on the number of local extrema $m(e) \in \{k-4, k-3\}$. (3) For $k$-half-graph lower bounds: random tournament construction (odd $k$) and random proper edge-coloring (even $k$), combined with partial Steiner $(n,k,2)$-systems for first-moment calculation.

## Result
$r_4(5,n) \geq 2^{r_3(4, \lfloor \log n/2 \rfloor) - 1} > 2^{n^{c \log\log n}}$, established by Theorem 2.4 + Conlon–Fox–Sudakov's $r_3(4,t) > 2^{ct \log t}$. The recursive Lemma 2.5 gives $r_k(k+1,n) \geq 2^{r_{k-1}(k, \lfloor n/6\rfloor) - 1}$, extending to all $k \geq 5$. Theorem 3.2 gives $g(k,N) < 2^k k! \log^{(k-13)} N$. Theorem 4.3 gives $r(B_k, K_n^k) > 2^{\Omega(n)}$ via probabilistic constructions avoiding red $B_k$ by forcing structural rigidity (regular tournaments / proper edge-colorings).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are hypergraph Ramsey number computations. The stepping-up lemma technique (encoding vertices in binary, then defining colorings via patterns of the highest-differing-bit function) is a general combinatorial construction primitive that could conceivably inform extremal-graph or combinatorial arena problems, but no current problem matches.

## Open questions / connections
- Determine the correct number of iterations in $g(k,N)$ — conjectured $k-2$, paper achieves $k-13$.
- Improving either bound on $r(K_4^3 \setminus e, K_n^3)$ — exponential lower vs $(n!)^2$ upper — remains open.
- Extends Erdős–Hajnal 1972 conjecture program (Conjecture 2.1: $r_k(s,n) \geq \mathrm{twr}_{k-1}(\Omega(n))$ for $s \geq k+1$).

## Key terms
hypergraph Ramsey numbers, stepping-up lemma, Erdős–Hajnal, Erdős–Rogers function, off-diagonal Ramsey, $k$-half-graph, $K_4^3$ minus edge, tower function, iterated logarithm, Conlon–Fox–Sudakov, Spencer's lemma, partial Steiner system, regular tournament, Mubayi–Suk
