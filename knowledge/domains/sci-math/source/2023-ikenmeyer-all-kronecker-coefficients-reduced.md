---
type: source
kind: paper
title: All Kronecker coefficients are reduced Kronecker coefficients
authors: Christian Ikenmeyer, G. Panova
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.03003
source_local: ../raw/2023-ikenmeyer-all-kronecker-coefficients-reduced.pdf
topic: general-knowledge
cites:
---

# All Kronecker coefficients are reduced Kronecker coefficients

**Authors:** Christian Ikenmeyer, G. Panova  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.03003

## One-line
Every ordinary Kronecker coefficient $k(\lambda,\mu,\nu)$ of the symmetric group equals an explicit reduced Kronecker coefficient $\overline{k}(\cdot,\cdot,\cdot)$ of only modestly larger partitions, collapsing the apparent gap between the two families.

## Key claim
For all partitions $\lambda,\mu,\nu$ of equal size, $k(\lambda,\mu,\nu) = \overline{k}\bigl(\nu_1^{\ell(\lambda)}+\lambda,\ \nu_1^{\ell(\mu)}+\mu,\ (\nu_1^{\ell(\lambda)+\ell(\mu)},\nu)\bigr)$ (Theorem 1). More generally, for $l\geq\ell(\lambda)$, $m\geq\ell(\mu)$, $c\geq\nu_1$: $k(\lambda,\mu,\nu) = \overline{k}(c^l+\lambda,\ c^m+\mu,\ c^{l+m}\diamond\nu)$ (Theorem 2).

## Method
Three independent proofs are given: (i) a $\mathrm{GL}_N$ representation-theoretic argument via the natural interpretation of $k(\lambda,\mu,\nu)$ and 3-dimensional $\{0,1\}$-contingency arrays; (ii) symmetric-function manipulations using the plethysm $s_\lambda[x\cdot y]$, triple Cauchy identities, and an alternating-sum formula over contingency arrays $k(\lambda,\mu,\nu)=\sum \mathrm{sgn}(\sigma)\mathrm{sgn}(\pi)\mathrm{sgn}(\rho)\,C(\cdot,\cdot,\cdot)$; (iii) a Littlewood–Richardson rule argument using multi-LR tableaux and the iterated formula $k(\lambda,\mu,\nu)=\sum_\sigma \mathrm{sgn}(\sigma)\prod c_{\alpha^1\cdots\alpha^k}^\lambda c_{\alpha^1\cdots\alpha^k}^\mu$. A fourth derivation falls out of the Briand–Orellana–Rosas (2011) stability identity.

## Result
The identity reduces all ordinary Kronecker coefficient questions to reduced Kronecker coefficient questions on partitions of size at most a small polynomial factor larger. **Corollary 1:** deciding $\overline{k}(\alpha,\beta,\gamma)>0$ is NP-hard (in unary), settling the conjecture of Pak–Panova 2020 §4.4 by reducing from IMW17. **Corollary 2:** computing $\overline{k}$ is strongly #P-hard under parsimonious many-one reductions (strengthening prior Turing-reduction hardness). Stanley's Problem 10 (2000) and Kirillov's Problem 2.32 (2004) are formally equivalent — equivalently, Pak's Conjectures 9.1 and 9.4 are the same.

## Why it matters here
General background; no direct Einstein Arena tie — Kronecker / reduced Kronecker coefficients are representation-theoretic objects of $S_n$ and do not appear directly in the 23 arena problems (sphere packing, autocorrelation, kissing, etc.). Relevant only as a meta-lesson on complexity/positivity boundaries for combinatorial structure constants and as a cautionary tale that "interpolated" objects (here, reduced Kronecker between LR and Kronecker) can collapse to the harder side.

## Open questions / connections
- Combinatorial interpretation of $k(\lambda,\mu,\nu)$ remains open (Stanley Problem 10); this paper shows attacking $\overline{k}$ is no easier.
- Saturation fails for $\overline{k}$ (Pak–Panova 2020 disproved Kirillov–Klyachko); how far from LR-saturation does it sit?
- Connections to Geometric Complexity Theory (Mulmuley) and the partition algebra (Bowman–De Visscher–Orellana 2015).

## Key terms
Kronecker coefficients, reduced Kronecker coefficients, Littlewood-Richardson coefficients, symmetric group representations, Specht modules, Schur functions, plethysm, contingency arrays, multi-LR tableaux, Murnaghan stability, NP-hardness positivity, #P-hardness, Ikenmeyer, Panova, Stanley Problem 10, Kirillov saturation, partition algebra
