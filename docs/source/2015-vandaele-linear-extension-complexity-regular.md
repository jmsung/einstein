---
type: source
kind: paper
title: On the Linear Extension Complexity of Regular n-gons
authors: A. Vandaele, Nicolas Gillis, François Glineur
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.08031
source_local: ../raw/2015-vandaele-linear-extension-complexity-regular.pdf
topic: general-knowledge
cites:
---

# On the Linear Extension Complexity of Regular n-gons

**Authors:** A. Vandaele, Nicolas Gillis, François Glineur  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.08031

## One-line
New upper and lower bounds on the linear extension complexity $\mathrm{xc}(P_n)$ of regular $n$-gons via nonnegative factorizations of the slack matrix $S_n$.

## Key claim
For all $n \geq 2$, $\mathrm{rank}_+(S_n) \leq 2\lceil \log_2 n \rceil - 1$ when $2^{k-1} < n \leq 2^{k-1} + 2^{k-2}$, and $2\lceil \log_2 n \rceil$ otherwise — improving Fiorini–Rothvoss–Tiwary's $2\lceil \log_2 n \rceil$ by one in roughly half the regime, and exactly determining $\mathrm{xc}(P_n)$ for $9 \leq n \leq 13$ ($=7,7,7,7,8$) and $21 \leq n \leq 24$ ($=9$).

## Method
**Upper bound:** purely algebraic recursive nonnegative factorization. At each step, subtract a rank-2 nonnegative correction from a circulant $k \times l$ block of $S_n$ to create a "cross" of zeros; symmetry reduces the residual to an upper-left $\lceil k/2 \rceil \times \lceil l/2 \rceil$ block whose factorization extends back; base case ($l \leq 4$) is trivial $B = B I$. Key lemma: matrices $[c_{\alpha-i+j} - c_{\beta-i-j}]$ with $c_k = 2\sin(k\pi/n)\sin((k+1)\pi/n)$ have rank 1 by a trig identity. **Lower bound:** Sperner-style antichain counting refined to exploit that both row supports $\{s_i\}$ and complement-column supports $\{s_i \cup s_{i+1}\}$ form antichains, giving $n \leq \frac{r - \lfloor r/2 \rfloor}{r-1}\binom{r}{\lfloor r/2 \rfloor}$ for the boolean rank $r$.

## Result
The recursive construction yields explicit factorizations $U, V \geq 0$ with $S_n = UV$ achieving the bound (1); Matlab code provided and verified numerically up to $n = 10000$. The new lower bound on the rectangle covering number (boolean rank) improves $n \leq \binom{r}{\lfloor r/2 \rfloor}$ by a factor $\approx 1/2$ and is tight for many small $n$ (e.g. $n = 2$–$6, 8$–$9, 13$–$21, 24$–$32$). Numerical evidence (heuristic exact-NMF solver) suggests the upper bound is tight; gap remains for $n = 14$, $17 \leq n \leq 20$, $25 \leq n \leq 30$, $n \geq 33$.

## Why it matters here
General background; no direct arena tie. Relevant if any problem reduces to bounding nonnegative rank / extension complexity of a polytope, or if slack-matrix / boolean-rank counting arguments are invoked for combinatorial lower bounds.

## Open questions / connections
- Is the conjectured upper bound (1) tight for all $n$? Numerical evidence says yes up to $n = 78$ but no proof.
- Can lower bounds (RRCB, geometric, Sperner-style) be pushed to close the gap for $n \geq 14$ outside the resolved windows?
- Generalizes Yannakakis's slack-matrix / nonnegative-rank correspondence and connects to Fiorini–Rothvoss–Tiwary (geometric reflections), Shitov ($\leq 6\sqrt{7n}$ for rank-3), Ben-Tal–Nemirovski (SOCP approximation).

## Key terms
extension complexity, nonnegative rank, slack matrix, boolean rank, rectangle covering bound, regular n-gon, Sperner theorem, antichain, circulant matrix, Yannakakis, Fiorini-Rothvoss-Tiwary, polytope projection
