---
type: source
kind: paper
title: Nonnegative k-sums, fractional covers, and probability of small deviations
authors: N. Alon, Hao-wei Huang, B. Sudakov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1104.1753
source_local: ../raw/2011-alon-nonnegative-k-sums-fractional-covers.pdf
topic: general-knowledge
cites:
---

# Nonnegative k-sums, fractional covers, and probability of small deviations

**Authors:** N. Alon, Hao-wei Huang, B. Sudakov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1104.1753

## One-line
Proves the Manickam–Miklós–Singhi conjecture for $n \geq 33k^2$ by reducing nonnegative $k$-sum counting to a fractional-matching/covering problem on hypergraphs and applying Feige's small-deviation inequality.

## Key claim
For $n \geq 33k^2$, any $n$ real numbers with nonnegative sum admit at least $\binom{n-1}{k-1}$ subsets of size $k$ with nonnegative sum — a polynomial bound replacing the prior exponential $n \geq e^{ck\log\log k}$ (Tyomkyn).

## Method
Reduce to bounding edges in a $(k-1)$-uniform hypergraph $H$ whose edges encode negative $k$-sums containing $x_1$; show the fractional matching number $\nu^*(H) \leq n/k$, dualize to fractional cover $\tau^*(H)$, then use Feige's inequality $\Pr[\sum X_i < m + \delta] \geq \min(\delta/(1+\delta), 1/13)$ on independent nonnegative variables to lower-bound the missing edges by a constant fraction of $\binom{n-1}{k-1}$. A simpler combinatorial argument via random partitions plus Baranyai's theorem gives the weaker $n \geq 2k^3$ bound.

## Result
**Theorem 1.2:** $f(k) \leq 33k^2$ where $f(k)$ is the threshold for the MMS conjecture. **Theorem 1.3 (Hilton–Milner-type stability):** if no $x_i$ is "large" (sum with any $k-1$ others is nonnegative), then there are at least $\binom{n-1}{k-1} + \binom{n-k-1}{k-1} - 1$ nonnegative $k$-sums, asymptotically $(2+o(1))\binom{n-1}{k-1}$, with two extremal configurations characterized. **Theorem 1.4:** if no $x_i$ is $(1-\delta)$-moderately large, then $\geq g(\delta,k)\binom{n}{k}$ nonnegative $k$-sums exist, with $g(\delta,k) = \delta(1-\delta)/(14k)$.

## Why it matters here
General background on extremal combinatorics, fractional LP duality, and small-deviation probability inequalities — techniques (LP duality, Feige-type tail bounds, Kruskal–Katona) that recur in Einstein Arena problems involving discrete extremal structures and sum constraints. No direct arena tie to any of the 23 problems unless an MMS-type or Erdős matching-conjecture instance appears.

## Open questions / connections
- Can MMS be verified in the linear range $n \geq ck$ (the conjectured $4k$)? Authors suggest algebraic or structural-extremal methods.
- Feige's constant $1/13$ conjecturally improvable to $1/e$; Samuels's general problem on $\inf \Pr(\sum X_i < m)$ open for $k \geq 5$.
- Erdős's $r$-uniform matching conjecture (equation (1)) and its fractional version (equation (22)) — would give direct constant edge-density bound without fractional matchings; related to perfect-matching Dirac thresholds via Alon–Frankl–Huang–Rödl–Ruciński.

## Key terms
Manickam-Miklós-Singhi conjecture, nonnegative k-sums, fractional matching, fractional cover, hypergraph matching number, Erdős matching conjecture, Erdős-Ko-Rado, Hilton-Milner theorem, Feige inequality, small deviation probability, Kruskal-Katona, Baranyai partition theorem, LP duality, Johnson scheme, Samuels inequality
