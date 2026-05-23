---
type: source
kind: paper
title: Stochastic Variance Reduction for Variational Inequality Methods
authors: Ahmet Alacaoglu, Yura Malitsky
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.08352
source_local: ../raw/2021-alacaoglu-stochastic-variance-reduction-variational.pdf
topic: general-knowledge
cites:
---

# Stochastic Variance Reduction for Variational Inequality Methods

**Authors:** Ahmet Alacaoglu, Yura Malitsky  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.08352

## One-line
Variance-reduced stochastic variants of extragradient / FBF / forward-reflected-backward for finite-sum monotone variational inequalities that match deterministic convergence assumptions but achieve accelerated complexity.

## Key claim
For finite-sum monotone VIs $F = \sum_{i=1}^N F_i$ with $L$-Lipschitz-in-mean stochastic oracle and $L_F$-Lipschitz full operator, the proposed loopless EG/FBF/FoRB with variance reduction reach $\varepsilon$-accuracy in $O(N + \sqrt{N}L/\varepsilon)$ oracle calls under *mere monotonicity* (no bounded-domain or extra-convexity assumption), improving the prior $O(N\,L_F/\varepsilon)$ deterministic rate whenever $L \le \sqrt{N}\,L_F$.

## Method
Loopless SVRG-style variance reduction grafted onto extragradient: at each step use $\tilde F(z) = F(w_k) + F_{\xi_k}(z) - F_{\xi_k}(w_k)$ with a snapshot $w_k$ refreshed to $z_{k+1}$ with probability $p$ (else kept), and an averaged anchor $\bar z_k = \alpha z_k + (1-\alpha) w_k$ with the key choice $\alpha = 1-p$. The Lyapunov function $\Phi_k(z) = \alpha\|z_k-z\|^2 + \tfrac{1-\alpha}{p}\|w_k-z\|^2$ combined with Lemma 2.4 (a maximal-inequality trick for switching $\max$ and $\mathbb{E}$) yields the $O(1/K)$ expected-gap rate; the framework extends to Bregman/Mirror-Prox (double-loop) and to FBF/FoRB for monotone inclusions.

## Result
Theorem 2.5: $\mathbb{E}[\mathrm{Gap}(\bar z_K)] = O(L/(\sqrt{p}\,K))$ with step $\tau = \sqrt{1-\alpha}\,\gamma/L$; Corollary 2.7: choosing $p = 2/N$ gives total expected complexity $O(N + \sqrt{N}L/\varepsilon)$. For bilinear $\min_x\max_y \langle Ax,y\rangle$: $\tilde O(\mathrm{nnz}(A) + \sqrt{\mathrm{nnz}(A)(m+n)}\,\|A\|_F/\varepsilon)$ Euclidean and $\tilde O(\mathrm{nnz}(A) + \sqrt{\mathrm{nnz}(A)(m+n)}\,\|A\|_{\max}/\varepsilon)$ entropic — recovering [Car+19] under strictly weaker assumptions. Strongly monotone case: $O(N + \sqrt{N}L/\mu \cdot \log(1/\varepsilon))$. Lower-bound matching shown later by [HXZ21].

## Why it matters here
General background; no direct arena tie — current arena problems (sphere packing, autocorrelation, kissing) are not finite-sum saddle-point structures, so this acceleration doesn't apply directly. Could become relevant if an LP/SDP relaxation (e.g. Cohn–Elkies dual, flag-algebra SDP) is recast as a structured min-max with bilinear coupling and sparsity, where $\|A\|_F/\|A\|$ savings would compound — but that's speculative until a concrete reformulation exists.

## Open questions / connections
- Does any Cohn–Elkies-style LP dual for sphere packing admit a sparse bilinear saddle reformulation where $\sqrt{\mathrm{nnz}(A)(m+n)}\,\|A\|_F$ beats deterministic IPM?
- Extends [BB16] (strongly monotone) and [Car+19] (matrix games with extra assumptions); leaves open how to design stochastic oracles satisfying $L \le \sqrt{N}\,L_F$ for nonbilinear constrained optimization (52) — the generic oracle does not.
- Connection to [Car+20] coordinate methods for sparse matrix games — open whether their data-structure tricks port to this framework.

## Key terms
variational inequality, monotone operator, extragradient, mirror-prox, forward-backward-forward, forward-reflected-backward, variance reduction, SVRG, saddle point, min-max, finite-sum, Bregman distance, matrix games, bilinear coupling, Lipschitz-in-mean, Alacaoglu, Malitsky, Carmon
