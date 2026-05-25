---
type: source
kind: paper
title: The structure of low-complexity Gibbs measures on product spaces
authors: Tim Austin
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.07278
source_local: ../raw/2018-austin-structure-low-complexity-gibbs-measures.pdf
topic: general-knowledge
cites:
---

# The structure of low-complexity Gibbs measures on product spaces

**Authors:** Tim Austin  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.07278

## One-line
Proves that any Gibbs measure $\mu \propto e^{f}\,d\lambda_1\cdots d\lambda_n$ on a product space whose discrete-gradient set $\{\nabla f(x,\cdot)\}$ has small covering number can be decomposed as a mixture of few near-product measures.

## Key claim
**Theorem A:** if a partition $\mathcal{P}$ of $\prod K_i$ has $|\nabla f(x,\cdot)-\nabla f(y,\cdot)|<\delta n$ within parts, then (a) $\mathrm{DTC}(\mu)<H_\mu(\mathcal{P})+\delta n$, (b) $\sum_P \mu(P)\int D(\mu|_P\,\|\,\xi_{\nabla f(y,\cdot)})\,\mu|_P(dy)<H_\mu(\mathcal{P})+\delta n$, and (c) the same with KL replaced by $\bar d_n$ transportation distance bounded by $\sqrt{H_\mu(\mathcal{P})/n}+\sqrt{\delta}\,/2$. **Corollary A′:** if $\mathrm{cov}_{\delta n}(\{\nabla f(x,\cdot)\},\|\cdot\|_\infty)\le e^{\varepsilon n}$, then $\mu$ is a mixture of at most $e^{\varepsilon n}$ conditioned measures, most close to product measures in $\bar d_n$.

## Method
Four information-theoretic ingredients glued together: a modified KL chain rule (Lemma 2.1), Gibbs' variational principle, Marton's transportation–entropy inequality $\bar d_n(\mu,\nu)\le\sqrt{D(\mu\|\nu)/(2n)}$ for product $\nu$, and Han's dual-total-correlation (DTC) identity. The pivotal step is Lemma 3.1 — a tower-property identity $\int \nabla f(x,x)\,d\mu = \iint \nabla f(x,y)\,\xi_{\nabla f(x,\cdot)}(dy)\,\mu(dx)$ — yielding the master identity (17) $\mathrm{DTC}(\mu)+\sum_P \mu(P)\int D(\mu|_P\|\xi_{\nabla f(y,\cdot)})\mu|_P(dy)=H_\mu(\mathcal{P})+(\text{error}<\delta n)$.

## Result
Generalizes Chatterjee–Dembo nonlinear large deviations and Eldan's Gaussian-width structure theorem from $\{-1,1\}^n$ to arbitrary bounded complete separable metric product spaces (diameter $\le 1$). Yields partition-function approximation (Prop. 5.1): $\log\int e^f d\lambda \le \sup_\xi\{\int f\,d\xi - D(\xi\|\lambda)\} + (\varepsilon+\delta)n + \sqrt{(\varepsilon+\delta)/2}\,L$ over product measures $\xi$, where $L$ is the $\bar d_n$-Lipschitz constant of $f$. Proposition 4.1 gives an approximate fixed-point characterization of mixture components: $g_P \approx \int \nabla f(x,\cdot)\,\xi_{g_P}(dx)$ — on $\{-1,1\}^n$ this becomes $m_P\approx\tanh(D\tilde f(m_P))$.

## Why it matters here
General background — no direct Einstein Arena problem ties, but provides the information-theoretic toolkit (DTC, Marton transportation–entropy, Gibbs variational principle) that underlies LP-bound and mean-field analyses used in extremal combinatorics and random-graph upper-tail problems related to autocorrelation / sieve / extremal-graph problems. The covering-number-of-gradients framing is a cleaner alternative to Gaussian-width complexity when bounding partition functions in high-dimensional optimization landscapes.

## Open questions / connections
- Question 3.2: can structure be sharpened for highly biased reference measures $\lambda_i\{1\}=p\ll 1$?
- Question 3.3: can the proof be modified to benefit from $\delta<\gamma^{2/3}$ — the regime where Eldan's Gaussian-width bound still gives useful estimates but Austin's does not?
- Extension to continuous $K_i=[0,1]$ with classical gradient $Df$ replacing discrete $\nabla f$ — Lemma 3.1 fails to transfer; requires new control likely involving second derivatives.
- Direct extension of Yan (arXiv:1703.08887) and Augeri (arXiv:1810.01558) to Banach-space-valued / Fréchet-derivative settings.

## Key terms
Gibbs measure, partition function, nonlinear large deviations, dual total correlation, DTC, Han's inequality, Marton transportation-entropy inequality, Kullback-Leibler divergence, Gibbs variational principle, discrete gradient complexity, covering number, mixture of product measures, Gaussian width, Eldan, Chatterjee-Dembo, mean-field decomposition
