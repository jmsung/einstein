---
type: source
kind: paper
title: On eigenvalues of random complexes
authors: Anna Gundert, Uli Wagner
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1411.4906
source_local: ../raw/2014-gundert-eigenvalues-random-complexes.pdf
topic: general-knowledge
cites:
---

# On eigenvalues of random complexes

**Authors:** Anna Gundert, Uli Wagner  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1411.4906

## One-line
Proves that random $k$-dimensional simplicial complexes are a.a.s. spectrally expanding, but exhibits an infinite family of spectrally-expanding complexes whose coboundary expansion tends to zero — refuting the "easy" higher-dimensional Cheeger inequality.

## Key claim
For the Linial–Meshulam random complex $X^k(n,p)$ with $p \ge (k+\gamma)\log n / n$, all nontrivial eigenvalues of $\Delta^{up}_{k-1}$ concentrate in $[1 - C/\sqrt{d}, 1 + C/\sqrt{d}]$ a.a.s. where $d = p(n-k)$; and there exist $k$-complexes $Y^k_n$ with all nontrivial Laplacian eigenvalues in $[1 - O(1/\sqrt{n}), 1 + O(1/\sqrt{n})]$ yet with a cochain $a$ of normalized Hamming weight $\ge 1/2 - o(1)$ and $\|\delta a\| = O(\log n / n)$.

## Method
Reduces higher-dimensional spectral problems to graph spectra on links of $(k-2)$-faces via Garland's estimate (for the Laplacian) and a novel analogue developed here (for the adjacency matrix $A_{k-1}$). The Cheeger counterexample uses a two-stage probabilistic construction: first sample a random 2-cocycle $a$, then include only "good" $k$-faces (those with even count of $a$-active $(k-1)$-faces) with probability $p$, plus a Linial-Meshulam overlay $X^k(n,q)$ to kill cohomology. Concentration follows from second-moment / Chernoff bounds.

## Result
**Theorem 2:** For $p \ge (k+\gamma)\log n /n$, the largest $\binom{n-1}{k-1}$ eigenvalues of $A_{k-1}$ lie in $[d - C\sqrt{d}, d + C\sqrt{d}]$, the rest in $[-C\sqrt{d}, C\sqrt{d}]$; the nontrivial Laplacian eigenvalues lie in $[1 \pm C/\sqrt{d}]$. **Theorem 4:** For every $k > 1$, an infinite family $Y^k_n$ exists with spectral gap $1 \pm O(1/\sqrt{n})$ but coboundary expansion $O(\log n / n) \to 0$, and with $\tilde H_i(Y; \mathbb{Z}) = 0$ for $i \le k-1$. Concentration is essentially optimal: $1 - \lambda \ge k/d_{\max} \cdot (n - d_{\max})/(n-k)$ for some nontrivial $\lambda$.

## Why it matters here
General background; no direct arena tie — relevant only to discrete-geometry / extremal-combinatorics problems that might invoke higher-dimensional expander structure (none of the current 23 arena problems are spectral-complex problems).

## Open questions / connections
- Is there a complex with coboundary expansion bounded away from zero AND spectral expansion tending to zero? (Dual direction, still open.)
- Extends Coja-Oghlan, Feige-Ofek, Friedman-Kahn-Szemerédi spectral bounds for $G(n,p)$ to random simplicial complexes; precursor to Hoffman-Kahle-Paquette sharp thresholds.
- Connects to Gromov / Linial-Meshulam coboundary expansion, Property (T) for random 2-complexes, and Parzanchevski-Rosenthal-Tessler's weaker higher Cheeger inequality.

## Key terms
random simplicial complex, Linial-Meshulam model, normalized Laplacian, generalized adjacency matrix, Garland's method, coboundary expansion, Cheeger inequality, spectral expander, link of a face, cohomology, eigenvalue concentration, Gundert-Wagner
