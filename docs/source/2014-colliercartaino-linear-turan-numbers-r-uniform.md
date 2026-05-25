---
type: source
kind: paper
title: Linear Turan numbers of r-uniform linear cycles and related Ramsey numbers
authors: Clayton Collier-Cartaino, Nathan Graber, T. Jiang
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1404.5015
source_local: ../raw/2014-colliercartaino-linear-turan-numbers-r-uniform.pdf
topic: general-knowledge
cites:
---

# Linear Turan numbers of r-uniform linear cycles and related Ramsey numbers

**Authors:** Clayton Collier-Cartaino, Nathan Graber, T. Jiang  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1404.5015

## One-line
Proves the conjectured Bondy–Simonovits-style upper bound $\mathrm{ex}_L(n, C_\ell^r) = O(n^{1+1/\lfloor \ell/2\rfloor})$ for linear Turán numbers of $r$-uniform linear cycles, and uses it to bound cycle-vs-clique hypergraph Ramsey numbers.

## Key claim
For all $r,\ell \geq 3$, there exists $\alpha_{r,\ell} > 0$ such that $\mathrm{ex}_L(n, C_\ell^r) \leq \alpha_{r,\ell} n^{1+1/\lfloor \ell/2\rfloor}$. Concretely: $\mathrm{ex}_L(n, C_{2m}^r) \leq c_{m,r} n^{1+1/m}$ and $\mathrm{ex}_L(n, C_{2m+1}^r) \leq c'_{m,r} n^{1+1/m}$. This answers a question of Kostochka–Mubayi–Verstraëte and extends Bondy–Simonovits's even-cycle bound to linear hypergraphs.

## Method
Builds "leveled linear $r$-trees" greedily inside a dense linear $r$-graph via a BFS-style expansion (Lemma 4.1), using vertex covers, cross-cuts (random halving), and strongly proper edge-colorings on the 2-shadow $\partial_2(G)$ with the "default edge-coloring" $\phi(\{a,b\}) = e\setminus\{a,b\}$. Strongly rainbow paths are extracted via Lemma 3.4 (induction on path length), giving disjoint expansion vertices needed to close a linear cycle. The odd-cycle case requires substantially more bookkeeping (Section 6) than even. For Ramsey bounds: reduce a $C_\ell^r$-free hypergraph to a linear one via the sunflower lemma (Lemma 7.5–7.7) and apply Alon's independence-number bound (Lemma 7.9) plus Caro–Wei on neighborhood subgraphs.

## Result
- $\mathrm{ex}_L(n, C_\ell^r) = O(n^{1+1/\lfloor \ell/2\rfloor})$, matching the graph-case exponent for all $r \geq 3$.
- $R(C_{2m}^r, K_t^r) \leq a_{m,r} (t/\ln t)^{m/(m-1)}$ and $R(C_{2m+1}^r, K_t^r) \leq b_{m,r} t^{m/(m-1)}$.
- Lower bound (Prop 8.1, via random subgraph of a Steiner-type linear $r$-graph): $\mathrm{ex}_L(n, C_\ell^r) > c''_{r,\ell} n^{1+1/(\ell-1)}$ — leaving a gap between $1/\lfloor\ell/2\rfloor$ and $1/(\ell-1)$ for $\ell\geq 4$.

## Why it matters here
General background; no direct arena tie. Linear hypergraph Turán bounds inform extremal-graph and discrete-combinatorics problem families (e.g., problems framed around forbidden configurations or Sidon-set / triple-system constructions), but no current Einstein Arena problem is directly a linear-cycle Turán problem.

## Open questions / connections
- Tighten the constant: is there $c_r$ with $\mathrm{ex}_L(n, C_{2m}^r) \leq c_r m \cdot n^{1+1/m}$ (graph-case analogue from Bukh–Jiang)?
- Closing the lower-bound gap — Verstraëte's random-subgraph-of-Steiner-system construction gives only $n^{1+1/(\ell-1)}$; can generalized Sidon / $B_k^*$ sets push this toward $n^{1+1/\lfloor\ell/2\rfloor}$?
- Sharper Ramsey: Kostochka–Mubayi–Verstraëte conjecture $R(C_\ell^r, K_t^r) = \Theta^*(t^{\ell/(\ell-1)})$; current bound off by polynomial factors.
- Connection to rainbow Turán number $\mathrm{ex}^*(n, C_{2m})$ — same conjectured exponent $1+1/m$, open beyond $C_4, C_6$.

## Key terms
linear Turán number, linear hypergraph, linear cycle, $r$-expansion, Bondy–Simonovits, even cycle, cycle-complete Ramsey number, sunflower lemma, 2-shadow, strongly proper edge-coloring, leveled linear tree, Sidon set, Brown–Erdős–Sós, Behrend, Roth, Ruzsa–Szemerédi, Alon independence bound
