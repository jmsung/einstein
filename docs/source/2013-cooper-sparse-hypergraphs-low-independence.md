---
type: source
kind: paper
title: Sparse hypergraphs with low independence number
authors: Jeff Cooper, D. Mubayi
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.0813
source_local: ../raw/2013-cooper-sparse-hypergraphs-low-independence.pdf
topic: general-knowledge
cites:
---

# Sparse hypergraphs with low independence number

**Authors:** Jeff Cooper, D. Mubayi  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.0813

## One-line
Constructs a $K_4^{(3)}$-free 3-uniform hypergraph whose independence number is only $O(N/d^{1/2})$, refuting a 1981 Ajtai–Erdős–Komlós–Szemerédi conjecture that forbidding $K_4^{(3)}$ should buy a $\log$-factor improvement over Spencer's Turán-type bound.

## Key claim
There exists a 3-uniform, $K_4^{-(3)}$-free hypergraph $H$ on $N$ vertices with average degree $d$ such that $\alpha(H) < 2N/d^{1/2}$ — so no $\omega(d) \to \infty$ improvement factor exists. Generalizes to $(k+1)$-uniform hypergraphs with $\alpha(H_k) \le 2k(k+1)^{1/k}\, N/\Delta^{1/k}$, disproving the Frieze–Mubayi chromatic-number conjecture and de Caen's sparse-hypergraph conjecture.

## Method
Algebraic/combinatorial construction. Vertices = edges of $K_{n,n}$; hyperedges = "increasing-opening" 3-edge paths $\{ab, ac, db\}$ with $c>b$, $d>a$. Link graphs are stars plus one bipartite component, ruling out $K_4^{-(3)}$; any vertex set $\ge 2n$ contains a 4-cycle in $K_{n,n}$, which forces a forbidden 3-edge path. Generalized via "positive strong $k$-simplices" $S_k^+$ and Zarankiewicz bound $z(n,S_k^+) \le 2k n^{k-1}$ proved by induction on link-graph degrees.

## Result
- $\alpha(H) < 2N/d^{1/2}$ for the $K_4^{-(3)}$-free 3-uniform $H$ (settles Question 1 negatively).
- $\alpha(H_k) \le 2k(k+1)^{1/k} N/\Delta^{1/k}$, so $\chi(H_k) \ge \Delta^{1/k}/(2k(k+1)^{1/k})$ — disproves Frieze–Mubayi $(\Delta/\log\Delta)^{1/k}$ chromatic conjecture and the Bohman–Frieze–Mubayi independent-neighborhoods variant.
- Ramsey: $r(P_s, t) = \Theta(t^2)$ for the tight 3-uniform path $P_s$, $s \ge 4$ (improved lower bound).
- $H_2$ is 1-sparse, killing de Caen's 1986 conjecture; a special-$k$-cluster $J_k$ construction kills the $k$-uniform generalization.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to extremal-graph/hypergraph problems in the inventory (independence-number lower bounds via Lovász Local Lemma / Spencer-Turán are tools the council may invoke for combinatorial arena problems), and as a cautionary tale that forbidden-subgraph hypotheses do not automatically yield $\log$-factor improvements.

## Open questions / connections
- Order of $r(P_3, t)$ remains open (this paper handles $s \ge 4$).
- Question 1 if both $K_4^{-(3)}$ and $C_3 = \{abc, cde, efa\}$ are forbidden — open.
- Cooper–Mubayi [6] answered Question 1 positively when $K_4^{-(3)}$, $F_5$, AND $C_3$ are all forbidden — suggests intermediate forbidden-family regimes.
- Sudakov's denser "L-shaped" $(k+1)$-uniform variant gives stronger counterexamples for $k \ge 3$.

## Key terms
hypergraph independence number, Turán-type bound, Spencer bound, Ajtai-Erdős-Komlós-Szemerédi, $K_4^{(3)}$-free, Frieze-Mubayi conjecture, de Caen conjecture, Zarankiewicz number, strong $k$-simplex, tight path Ramsey number, chromatic number hypergraph, $c$-sparse hypergraph
