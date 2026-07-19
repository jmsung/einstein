---
type: source
kind: paper
title: Extremal results in sparse pseudorandom graphs
authors: D. Conlon, J. Fox, Yufei Zhao
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.6645
source_local: ../raw/2012-conlon-extremal-results-sparse-pseudorandom.pdf
topic: general-knowledge
cites:
---

# Extremal results in sparse pseudorandom graphs

**Authors:** D. Conlon, J. Fox, Yufei Zhao  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.6645

## One-line
Proves a counting lemma for fixed subgraph copies in regular subgraphs of sparse $(p,\beta)$-jumbled (pseudorandom) graphs, unlocking sparse analogues of removal, Erdős–Stone–Simonovits, and Ramsey theorems.

## Key claim
For every graph $H$ and $\epsilon>0$, if $\Gamma$ is $(p,\beta)$-jumbled on $n$ vertices with $\beta \leq c\, p^{d_2(H)+3} n$ (where $d_2(H)$ is the 2-degeneracy), then sparse versions of the graph removal lemma (Thm 1.1), Erdős–Stone–Simonovits / Turán property (Thm 1.4), stability (Thm 1.5), and $(H,r)$-Ramsey (Thm 1.6) all hold relative to $\Gamma$.

## Method
Functional/Gowers-style counting strategy combined with the Kohayakawa–Rödl sparse regularity lemma. Core moves: two-sided counting via doubling + densification, $C_4$-count-implies-DISC inheritance, subdivision densification for cycles, and one-sided counting via $K_{1,2,2}$ regularity inheritance. Jumbledness condition $|e(X,Y)-p|X||Y|| \leq \beta\sqrt{|X||Y|}$ is the sole structural input.

## Result
The exponent $d_2(H)+3$ in $\beta \leq c p^{d_2(H)+3} n$ is best possible up to a constant factor (lower bound $\beta = \Omega(p^{(d(H)+2)/4} n)$ from random graph construction). For $H=K_t$ the threshold is $\beta \leq c p^t n$; conjecturally tight at $p^{t-1}n$ for $t\geq 4$ (Alon's construction gives sharp $p^2 n$ for $K_3$). Sparse Roth-type corollary: $(p,\beta)$-jumbled subsets $B \subseteq G$ of a group are $(\epsilon,m)$-Roth when $\beta \leq c p^{k_m} n$ with $k_m \to 1$.

## Why it matters here
General background; no direct arena tie. Pseudorandomness / jumbledness machinery is adjacent to extremal-graph and additive-combinatorics tools occasionally invoked in council dispatch (Szemerédi, Erdős, Tao, Razborov), but no current Einstein Arena problem reduces to subgraph counting in pseudorandom hosts.

## Open questions / connections
- Existence of $(p, c p^{t-1} n)$-jumbled $K_t$-free graphs for $t \geq 4$ (would tighten Theorem 1.4 by an additive 1 in the exponent).
- Extends Kohayakawa–Rödl–Schacht–Skokan triangle removal in sparse pseudorandom graphs (Thm in §1.2) to arbitrary $H$.
- Improving the tower-type dependence in $c^{-1}$, $\delta^{-1}$ via cylinder/Duke–Lefmann–Rödl-style weak regularity (Prop 9.7).

## Key terms
sparse regularity lemma, counting lemma, pseudorandom graphs, jumbledness, $(n,d,\lambda)$-graph, 2-degeneracy, graph removal lemma, Erdős-Stone-Simonovits, Ramsey property, KŁR conjecture, Kohayakawa-Rödl, quasirandomness, Sidorenko conjecture, Cayley graph removal
