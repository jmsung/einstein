---
type: source
kind: paper
title: A note on the natural density of product sets
authors: Sandro Bettin, Dimitris Koukoulopoulos, Carlo Sanna
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.13356v1
source_local: ../raw/2020-bettin-note-natural-density-product.pdf
topic: general-knowledge
cites: 
---

# A note on the natural density of product sets

**Authors:** Sandro Bettin, Dimitris Koukoulopoulos, Carlo Sanna  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2006.13356v1

## One-line
Resolves two questions of Hegyvári–Hennecart–Pach on natural density of product sets: density-1 sets multiply to density-1, but for any $\alpha<1$ one can construct $A$ with $d(A)=\alpha$ and $d(A^2)$ arbitrarily small.

## Key claim
**Theorem 1:** If $A,B \subseteq \mathbb{N}$ with $d(A)=d(B)=1$, then $d(A\cdot B)=1$ (hence $d(A^k)=1$ for all $k\geq 2$). **Theorem 2:** $\inf_{A:\,d(A)=\alpha} d(A^2) = 0$ for every $\alpha\in[0,1)$, and $=1$ at $\alpha=1$. So the density-1 hypothesis in Theorem 1 is sharp.

## Method
Smooth/rough factorization: split each $n\leq x$ as $n = n_{\text{smooth}}\cdot n_{\text{rough}}$ at threshold $y^{1/u}$, then bound the "bad" set by separately controlling the smooth part (via Rankin's trick + Mertens estimates) and the rough part (via the density-0 deficit of $\mathbb{N}\setminus B$). Quantitative: choose $u=\alpha(y)^{-1/2}$, $y=\min(x^{1/2}, \exp\beta(x^{1/2})^{-1/2})$ where $\alpha,\beta$ are the deficit rates. For Theorem 2, construct $A=B_{y,k,\mathcal{P}} = \{n:\Omega_y(n)\geq k,\;(n,p)=1\;\forall p\in\mathcal{P}\}$ so that $A^2 = B_{y,2k,\mathcal{P}}$, then tune $k\asymp \tfrac{3}{4}\log\log y$ via Lemma 2.3 (Rankin-style $\Omega$-tail bound with rate function $Q(\lambda)=\lambda\log\lambda-\lambda+1$) and use Lemma 2.4 to fix the density at $\alpha$ by adjoining primes.

## Result
Quantitative form: if $\#\{n\leq x:n\notin A\}\ll x(\log x)^{-a}$ for $a\in(0,1)$, then $\#\{n\leq x:n\notin A\cdot B\}\ll x(\log x)^{-a^2/(1+a)+o(1)}$, with optimal exponent left open. Theorem 2's construction uses $y=\exp(\exp(4k/3))$ and chooses primes $p_1<p_2<\cdots>y$ greedily so $\prod(1-1/p_i)\cdot d(B_{y,k,\emptyset})=\alpha$ exactly, while $d(B_{y,2k,\emptyset})<\varepsilon$ by tail decay of the Erdős–Kac-type distribution of $\Omega$.

## Why it matters here
General background; no direct arena tie. Closest contact is sieve-theoretic asymptotics ($\Omega(n)$ distribution, Rankin's trick, Mertens estimates) which could surface for any density-based combinatorial problem; the smooth/rough decomposition trick is a clean template for "most of the mass lives in unbalanced products."

## Open questions / connections
- Optimal exponent of $\log x$ in the quantitative bound for $\#\{n\leq x:n\notin A\cdot B\}$ given polylog-density deficits.
- Extends Hegyvári–Hennecart–Pach (2019) and parallels random-set product results of Cilleruelo–Ramana–Ramaré and Sanna (extension to many factors).
- Continuous analog to Erdős multiplication-table problem (Ford 2008, Tenenbaum 1987, Koukoulopoulos 2014): infinite-density vs finite-cardinality regimes share the same unbalanced-products mechanism but yield opposite-looking asymptotics.

## Key terms
natural density, product set, multiplication table problem, Erdős, Ford, smooth-rough decomposition, Rankin's trick, Mertens estimates, $\Omega(n)$ distribution, sieve theory, Hegyvári–Hennecart–Pach, Koukoulopoulos
