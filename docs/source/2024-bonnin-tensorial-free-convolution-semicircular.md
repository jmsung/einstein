---
type: source
kind: paper
title: Tensorial free convolution, semicircular, free Poisson and R-transform in high order
authors: Remi Bonnin
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2412.02572
source_local: ../raw/2024-bonnin-tensorial-free-convolution-semicircular.pdf
topic: general-knowledge
cites:
---

# Tensorial free convolution, semicircular, free Poisson and R-transform in high order

**Authors:** Remi Bonnin  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.02572

## One-line
Extends free probability theory from random matrices to random tensors of order $p \geq 2$, defining higher-order semicircular and free Poisson laws and a tensorial free convolution with associated $R$-transform.

## Key claim
For order-$p$ tensors, the moments and free cumulants of a tensor $T$ obey the analytic moment-cumulant formula $M_T(z) = C_T(z M_T(z)^{p/2})$, from which the higher-order semicircular law $\mu_p$ has moments equal to Fuss-Catalan numbers $F_p(k) = \frac{1}{pk+1}\binom{pk+1}{k}$, and the higher-order free Poisson law $\nu_{p,t}$ has constant free cumulants $\kappa_n = t$ with moments given by Fuss-Narayana polynomials.

## Method
Combinatorial maps (pairs of permutations $(\pi,\alpha)$) encode tensor contractions; a "non-crossing poset" on these maps via edge-switches that increase connectivity yields free cumulants by Möbius inversion. Convergence theorems are proved by classifying $\Delta$-graphs into three categories (paired-tree, unpaired-multiedge, residual) and showing only the paired-tree graphs $\Delta_1(n,b)$ — in bijection with non-crossing partitions of $[np/2]$ into $b$ blocks of sizes divisible by $p/2$ — contribute at leading order in $N$. Free convolution is then defined via additivity of free cumulants on the poset, proven well-posed via exponential bounds.

## Result
Three convergence theorems: (i) Wigner tensor $W_N^p \to \mu_p$ in moments (rate $O(1/N)$, variance $O(1/N^2)$); (ii) Wishart tensor $W_N^{p,k}$ with $k_N/N^{p/2} \to t$ converges to $\nu_{p,t}$; (iii) free CLT — averages $T_k = k^{-1/2}\sum T_i$ of even-order tensors with bounded moments converge to $\mu_p$. Corollaries: $\mu_p \oplus_p \mu_p = \mu_p^{(\sqrt 2)}$ (semicircular stable under sum-dilation), $\nu_{p,t} \oplus_p \nu_{p,t'} = \nu_{p,t+t'}$ (free Poisson additive in parameter). $R$-transform $R_\mu(z) = (C_\mu(z)-1)/z$ is additive under $\oplus_p$.

## Why it matters here
General background; no direct arena tie. Closest adjacency is to optimization-theoretic problems involving random-tensor spectra or trace invariants (P1 sphere packing via Cohn–Elkies, problems with symmetric-tensor decompositions); the Fuss-Catalan / Fuss-Narayana moment formulas could provide closed-form references if a future problem touches large-$N$ symmetric-tensor norm distributions, but none of the 23 current Einstein Arena problems are tensor-spectral.

## Open questions / connections
- Existence of a direct (non-moment-derived) proof of the probability measure $\mu_T$ for general real symmetric tensors — Gurau showed existence, direct construction is open.
- Characterization of freeness by vanishing mixed cumulants is only proven for **even** families; odd-order case is open (multiple minimal maps in the poset block the argument).
- Subordination functions / analytic free convolution for general (non-compactly-supported) tensor measures — flagged as future work; the $Q$-transform $Q_\mu(z) = (C_\mu(z)^{p/2}-1)/z$ is introduced as the analytic handle.
- Link between this distribution-on-trace-invariants and the actual eigenvalue distribution of a given tensor remains unclear (cited as open).

## Key terms
free probability, tensor freeness, Voiculescu, Wigner tensor, Wishart tensor, semicircular law, free Poisson, Marčenko-Pastur, Fuss-Catalan numbers, Fuss-Narayana polynomials, R-transform, non-crossing partitions, free cumulants, moment-cumulant formula, random tensors
