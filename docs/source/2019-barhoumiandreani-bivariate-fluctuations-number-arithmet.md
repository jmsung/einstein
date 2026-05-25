---
type: source
kind: paper
title: Bivariate fluctuations for the number of arithmetic progressions in random sets
authors: Yacine Barhoumi-Andr'eani, Christoph Koch, Hong Liu
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.04176
source_local: ../raw/2019-barhoumiandreani-bivariate-fluctuations-number-arithmet.pdf
topic: general-knowledge
cites:
---

# Bivariate fluctuations for the number of arithmetic progressions in random sets

**Authors:** Yacine Barhoumi-Andr'eani, Christoph Koch, Hong Liu  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.04176

## One-line
Determines the limiting joint distribution of the counts of $\ell$-APs and $\ell'$-APs in a binomial random subset $[n]_p$ of $\{1,\ldots,n\}$, for sparse $p=o(1)$ and lengths up to $\ell=o(\log n)$.

## Key claim
Let $X_\ell$ count $\ell$-APs in $[n]_p$. Univariately, $X_\ell \to \mathrm{Po}(c/2)$ when $n^2 p^\ell/(\ell-1)\to c$, and $(X_\ell-\mathbb{E}X_\ell)/\sigma_\ell \to N(0,1)$ when $n^2 p^\ell/(\ell-1)\to\infty$. Bivariately, $(X_{\ell_1},X_{\ell_2})$ (rescaled) converges to a centered Gaussian with covariance $\kappa_{\ell_1,\ell_2}\in\{0,(0,1),1\}$ determined by the threshold $\psi_{\ell_1}=np^{\ell_1-1}\ell_1$.

## Method
Method of moments + Cramér–Wold: show joint centered moments of $(X_{\ell_1},X_{\ell_2})$ match Gaussian moments via a perfect-matching combinatorial expansion on the dependency graph. The dominant contributions come from "loose pairs" ($|T\cap T'|=1$) vs "overlap pairs" ($T'\subset T$); a BFS-style algorithmic exploration of components in the dependency graph bounds non-matching configurations. Auxiliary: a Lebesgue–Stieltjes integral representation $h_\ell(x)$ converging in $L^2$ to the binary entropy $h_\infty(x)=x\log(1/x)+\bar x\log(1/\bar x)$ supplies sharp loose-pair counts.

## Result
The "overlap pair regime" ($\psi_{\ell_1}\to 0$) and "loose pair regime" ($\psi_{\ell_1}\to\infty$) are separated by $\psi_{\ell_1}=np^{\ell_1-1}\ell_1$: in the former, overlap pairs dominate the second moment and the correlation $\kappa_{\ell_1,\ell_2}$ can be nontrivial; in the latter with both $\ell_i\to\infty$, $\kappa\in\{0,1\}$ (asymptotically uncorrelated, or collapse to the same Gaussian). The CLT range covers $0<p=o(1)$ with $p\ell_1^9\to 0$ and $n^2 p^{\ell_1}\ell_1^{-9}\to\infty$; conjectured to extend to the full sparse Gaussian range.

## Why it matters here
General background; no direct arena tie. Relevant peripherally to sieve-theory / autocorrelation problems where one counts arithmetic structures in sparse random sets, and to extremal-combinatorics intuition about loose-vs-overlap pair regimes that recurs in subgraph-count CLTs.

## Open questions / connections
- Extension to $r\ge 3$-variate joint CLT for $(X_{\ell_1},\ldots,X_{\ell_r})$; functional CLT for $(X_{\lfloor s\ell\rfloor})_{s\in[0,1]}$.
- Conjectured Log-normal limit for $\ell/\log n\to\infty$ with $p\to 1$ (analogue of Gao–Sato matching-count transition).
- Behavior of higher joint cumulants and whether the BFS-exploration coding gives asymptotic expansions; coupling process $X_\ell([\lfloor tn\rfloor]_p)$ for $t\ge 0$.

## Key terms
arithmetic progression, central limit theorem, bivariate fluctuations, method of moments, dependency graph, loose pair, overlap pair, Poisson approximation, Chen-Stein, Janson, random subset $[n]_p$, Szemerédi, sparse random sets
