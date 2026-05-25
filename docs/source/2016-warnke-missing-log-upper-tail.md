---
type: source
kind: paper
title: On the missing log in upper tail estimates
authors: L. Warnke
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.08561
source_local: ../raw/2016-warnke-missing-log-upper-tail.pdf
topic: general-knowledge
cites:
---

# On the missing log in upper tail estimates

**Authors:** L. Warnke  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.08561

## One-line
Closes a long-standing logarithmic gap in upper-tail concentration inequalities for polynomial-type random variables (e.g. counts of arithmetic progressions, Schur triples, additive quadruples) in random subsets of $[n]$.

## Key claim
For $k$-uniform hypergraphs $H$ with $v(H)\le N$, $e(H)\ge\gamma N^q$, $\Delta_q(H)\le D$, and $1\le q<k$, the induced edge count $X=e(H_p)$ satisfies $P(X\ge(1+\varepsilon)\mu)\le\exp\!\bigl(-c\,\min\{\mu,\,\mu^{1/q}\log(e/p)\}\bigr)$, matching the known lower bound up to the constant $c$.

## Method
Replaces pure induction (Kim–Vu, Janson–Ruciński) with a combinatorial **sparsification** scheme: iteratively peel a nested sequence $H_p=J_q\supseteq\cdots\supseteq J_1$ reducing maximum degree, controlled by "good events" $E_{Q,\varepsilon}$ stating that low-degree subhypergraphs have $\le(1+\varepsilon/2)\mathbb{E}X$ edges. Probability bounds use a Chernoff-type inequality for variables with bounded dependencies plus the **BK (van den Berg–Kesten–Reimer) inequality** to handle disjoint-occurrence events from matchings, avoiding union bounds over all subhypergraphs.

## Result
The extra $\log(1/p)$ factor in the exponent (Theorem 1 / Theorem 36) is sharp for $k$-term APs ($q=2$), Schur triples ($q=2$), additive quadruples ($q=3$), $(r,s)$-sums ($q=r+s-1$), and integer solutions of linear homogeneous systems. Also delivers sub-Gaussian estimates $P(X\ge\mu+t)\le C\exp(-ct^2/\mathrm{Var}\,X)$ for strictly balanced subgraph counts $X_H$ in $G_{n,p}$ up to $\mu\le(\log n)^{1+\xi}$, beating the prior $\mu=O(\log n)$ barrier of Vu / Janson–Ruciński / Sileikis.

## Why it matters here
Directly relevant to Einstein Arena problems involving **counts of arithmetic structures in random subsets of $[n]$** — APs, Schur triples, additive quadruples, $(r,s)$-sums — providing sharp concentration bounds (both tails matched up to constants) for the dominant "clustered" deviation regime. Also informs general upper-tail intuition (Poisson term $\exp(-c\mu)$ vs. clustered term $p^{c\mu^{1/q}}$) useful whenever optimizing random combinatorial counts.

## Open questions / connections
- Extends Janson–Ruciński (2011) [16] and Warnke (2017) [36] (which solved $q=2$); the $q=k$ excluded case has no log term (complete hypergraph counterexample).
- Sharper, problem-specific large-deviation methods (Chatterjee, DeMarco–Kahn, Janson–Oleszkiewicz–Ruciński) often beat these general bounds for fixed subgraph counts but lack the generality.
- The dependence of $c=c(\varepsilon,\dots)$ on $\varepsilon$ is left partial (small-$p$ Theorem 41); finer $\varepsilon$-dependence remains open for general $p$.

## Key terms
upper tail, concentration inequality, BK inequality, van den Berg–Kesten, Reimer, Janson–Ruciński, Kim–Vu, sparsification, arithmetic progressions, Schur triples, additive quadruples, $(r,s)$-sums, random induced subhypergraph, subgraph counts, strictly balanced graph, additive combinatorics, large deviations, Chernoff bound
