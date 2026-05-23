---
type: source
kind: paper
title: Revisiting Jacobi-Trudi identities via the BGG category $\mathcal{O}$
authors: Tao Gui, Arthur L. B. Yang
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2209.12632v3
source_local: ../raw/2022-gui-revisiting-jacobi-trudi-identities-bgg.pdf
topic: general-knowledge
cites: 
---

# Revisiting Jacobi-Trudi identities via the BGG category $\mathcal{O}$

**Authors:** Tao Gui, Arthur L. B. Yang  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2209.12632v3

## One-line
Reproves the Jacobi–Trudi identity and Schur-positivity of certain Jacobi–Trudi truncations by reinterpreting Kostka numbers as tensor-product composition-factor multiplicities in the BGG category $\mathcal{O}$ of $\mathfrak{sl}_n(\mathbb{C})$.

## Key claim
For partitions $\mu,\nu$ of length $\le n$ and $0 \le k \le \binom{n}{2}$, the truncations $g^k_{\mu/\nu} = (-1)^k \sum_{w \in S_n, \ell(w) \ge k} (-1)^{\ell(w)} h_{\mu+\delta-w(\nu+\delta)}$ of the Jacobi–Trudi expansion of $s_{\mu/\nu}$, and analogous truncations $t^k_{\mu,\nu}$ of the product expansion $s_\mu s_\nu$, are Schur-positive; explicitly, the $s_\lambda$-coefficient equals $[L(\lambda) \otimes V(\nu,k) : L(\mu)]$ where $V(\nu,k) = \mathrm{Im}(d_k)$ in the BGG resolution of $L(\nu)$.

## Method
Interpret the Kostka number $K_{\lambda,\mu+\delta-w(\nu+\delta)}$ as the multiplicity $[L(\lambda)\otimes\Delta(w\cdot\nu):L(\mu)]$ in the BGG category $\mathcal{O}$ (Proposition 5), proved via Weyl character formula, Verma module characters $\mathrm{ch}\,\Delta(\lambda) = x^\lambda / \prod(1-x^{-\alpha})$, Kostant partition function, and uni-triangularity of $\mathrm{ch}\,L(\mu)$ vs $\mathrm{ch}\,\Delta(\mu)$. Then truncate the BGG resolution at degree $k$, take formal characters of the resulting short exact sequence so $\mathrm{ch}\,V(\nu,k)$ is the alternating tail sum; positivity follows because $V(\nu,k)$ is an honest module.

## Result
New algebraic proof of Jacobi–Trudi (1.3) and its product variant (1.4) directly from the Weyl character formula, recovering Akin–Zelevinskii's Schur-positivity (Theorem 1) without their GL$_n$-resolution construction, and extending it to product-Schur truncations (Theorem 2). Provides a representation-theoretic formula for the Schur expansion coefficients as $\mathcal{O}$-multiplicities, giving an algebraic — though not yet combinatorial — interpretation of these non-negative coefficients (the combinatorial interpretation remains open, Stanley EC2 p. 461).

## Why it matters here
General background; no direct arena tie. Schur polynomials, Kostka numbers, and BGG-style resolutions are far from the Einstein Arena problem set (sphere packing, autocorrelation, kissing, sieve); only tangential relevance via the noted Lorentzian-polynomial conjecture (Huh–Matherne–Mészáros–St. Dizier) if log-concavity ever surfaces in a problem.

## Open questions / connections
- Are normalized truncations $g^k_{\mu/\nu}$ Lorentzian for all $\mu,\nu$? (Checked for $|\mu|+|\nu|\le 9$; cf. Huh et al. [9, Conjecture 19].)
- Find a combinatorial (tableaux) interpretation of $[L(\lambda)\otimes V(\nu,k):L(\mu)]$, open since Stanley EC2 p. 461.
- What other Schur-positivity problems reduce to virtual-character positivity in category $\mathcal{O}$?

## Key terms
Jacobi-Trudi identity, Schur positivity, Kostka numbers, BGG category O, BGG resolution, Weyl character formula, Verma modules, special linear Lie algebra sln, skew Schur polynomial, Akin-Zelevinskii theorem, Kostant partition function, Lorentzian polynomials
