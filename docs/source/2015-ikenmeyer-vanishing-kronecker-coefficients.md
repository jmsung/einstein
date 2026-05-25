---
type: source
kind: paper
title: On vanishing of Kronecker coefficients
authors: Christian Ikenmeyer, K. Mulmuley, M. Walter
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.02955
source_local: ../raw/2015-ikenmeyer-vanishing-kronecker-coefficients.pdf
topic: general-knowledge
cites:
---

# On vanishing of Kronecker coefficients

**Authors:** Christian Ikenmeyer, K. Mulmuley, M. Walter  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.02955

## One-line
Proves that deciding positivity of Kronecker coefficients is NP-hard, and constructs superpolynomially many explicit partition triples in the Kronecker cone where the coefficient vanishes — a saturation failure relevant to Geometric Complexity Theory (GCT).

## Key claim
**Kronecker positivity is NP-hard** (Theorem 1.3), refuting the prior conjecture that it lies in P. For any $0<\varepsilon\le 1$, there exist $0<a<1$ and $\Omega(2^{m^a})$ explicit partition triples $(\lambda,\mu,\mu)$ with $k^\lambda_{\mu,\mu}=0$ inside the Kronecker cone, with $\mathrm{ht}(\mu)=m$, $\mathrm{ht}(\lambda)\le m^\varepsilon$, $|\lambda|\le m^3$, $\lambda$ not a hook (Theorem 1.7).

## Method
Chain of injective polynomial-time many-one reductions: 3-Partition → Machine Flow → RN3DM → RNMTS → Permutation → Special Consistency ($t^\lambda_{\mu,\pi}$ positivity) → Restricted Kronecker, combined with representation-theoretic lower/upper bounds $p^\lambda_{\mu,\pi}\le k^\lambda_{\mu,\pi}\le t^\lambda_{\mu,\pi}$ (pyramids vs. point sets with prescribed marginals on $\wedge^n(\mathbb{C}^r)^{\otimes 3}$). Non-sparseness of NP-hard sets (Fortune 1979) + Bürgisser et al.'s rectangular-membership result $(\lambda,\delta(\lambda),\delta(\lambda))\in\mathrm{Kron}(r)$ converts hardness into superpolynomial existence; an extension via Lemma 5.5 (coNP-hard ≠ sparse union NP∩coNP) handles Theorem 1.8.

## Result
Theorem 1.3: Kronecker positivity is NP-hard (unary input). Theorem 1.5: there is a #P-formula for a subclass whose positivity is NP-hard — first instance of a positive combinatorial rule on a type-NP class, evidence the general Kronecker positivity problem may still be in #P. Theorem 1.7: explicit $\Omega(2^{m^a})$ vanishing triples in the Kronecker cone, computable in $\mathrm{poly}(m)$ time. Theorem 6.9: $t^\lambda_{\delta,\delta}>0$ whenever $\mathrm{ht}(\lambda)\le\min(d^2,r^2)$, supporting the conjecture that rectangular Kronecker positivity is in P.

## Why it matters here
General background; no direct arena tie. Kronecker coefficients and GCT obstructions are far from the 23 Einstein Arena problems (sphere packing, autocorrelation, kissing numbers, etc.) — relevant only as a methodological example of "hardness-into-existence" via injective reductions and saturation-failure constructions.

## Open questions / connections
- Is Kronecker positivity in NP (equivalently, does a #P-formula exist in general)? Theorem 1.5 is evidence yes; still open.
- Saturation property failure for Kronecker — quantify density of vanishing triples in the cone; current $a<1$ leaves the density exponentially small.
- Rectangular case $k^\lambda_{\delta(\lambda),\delta(\lambda)}$ positivity conjectured in P (Mulmuley 2010b); proven only via the $t$-function relaxation here.
- Extends Brunetti et al. (2001) discrete tomography NP-hardness; extends Bürgisser-Ikenmeyer (2013) GCT lower bounds.

## Key terms
Kronecker coefficient, Littlewood-Richardson coefficient, Geometric Complexity Theory, GCT, Kronecker cone, moment polytope, saturation property, NP-hardness, #P-formula, Young diagram, partition triple, rectangular Kronecker, Schur-Weyl duality, Weyl module, 3D Matching reduction, Ikenmeyer, Mulmuley, Walter
