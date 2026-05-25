---
type: source
kind: paper
title: Equivariant log-concavity and equivariant Kähler packages
authors: Tao Gui, Rui Xiong
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2205.05420v3
source_local: ../raw/2022-gui-equivariant-log-concavity-equivariant-hler.pdf
topic: general-knowledge
cites: 
---

# Equivariant log-concavity and equivariant Kähler packages

**Authors:** Tao Gui, Rui Xiong  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2205.05420v3

## One-line
Constructs explicit $S_n$-equivariant Kähler packages (Poincaré duality + hard Lefschetz + Hodge–Riemann) on the polynomial ring $\mathbb{R}[t_1,\ldots,t_n]$ and the exterior algebra $\Lambda_\mathbb{R}[\alpha_1,\ldots,\alpha_n]$, proving these are equivariantly log-concave for $S_n$.

## Key claim
For $H = H_{n,m}$ (tensor pieces $D^i \otimes R^{m-i}$ of two dual polynomial rings) or $H'_{n,m}$ (tensor pieces $\Lambda^i \otimes (\Lambda^*)^{m-i}$): the Poincaré pairing $\langle -,- \rangle$, the explicit Lefschetz operator $L = \sum_i d_i \otimes \partial/\partial x_i$ (resp. $L = \sum_k e_{\theta_k} \otimes i_{\theta_k}$), and the induced Lefschetz form are all $S_n$-equivariant and satisfy the full Kähler package. Consequently $H^*((\mathbb{CP}^\infty)^n,\mathbb{R})$ and $H^*((S^1)^n,\mathbb{R})$ are strongly $S_n$-equivariantly log-concave: $V^{i-1}\otimes V^{m-i+1} \hookrightarrow V^i \otimes V^{m-i}$ via $L$.

## Method
Reduce equivariant log-concavity to equivariant unimodality, then prove hard Lefschetz by explicitly constructing the lowering operator $F$ (e.g. $F = \sum_i \partial/\partial d_i \otimes x_i$) and verifying the $\mathfrak{sl}_2$ relations $[L,F]=h$, $[h,L]=2L$, $[h,F]=-2F$ via Leibniz/commutator computations. Hodge–Riemann is then transported from classical Hodge theory by decomposing the tensor product as an $\bigoplus_n \mathfrak{sl}_2(\mathbb{R})$-module isomorphic to $\bigoplus_\alpha H^*(\mathbb{CP}^{\alpha_1}\times\cdots\times\mathbb{CP}^{\alpha_n})$ with $L$ corresponding to multiplication by an ample class.

## Result
Establishes Theorem 7 (polynomial ring case) and Theorem 12 (exterior algebra case): PD + HL + HR hold $S_n$-equivariantly, with the Lefschetz form $(a,b) = \langle a, L^{m-2i} b \rangle$ being $(-1)^i$-definite on primitive subspaces $P_L^{-m+2i} = \ker L^{m-2i+1}$. Theorem 16 shows that the "usual" grading on $\Lambda \otimes \Lambda^*$ still satisfies PD + HL but *not* HR (e.g., $n=2$: signature $(2,2)$ on degree $-1$, $(3,3)$ on degree $0$ — disagrees with HR prediction). Corollaries: symmetric and exterior powers of *any* representation $V$ of *any* group $G$ are equivariantly log-concave, with explicit injections given by $L$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the "Kähler package as Hodge-theoretic upgrade of log-concavity" template (Adiprasito–Huh–Katz, Brändén–Huh) is the same machinery cited for matroid and Lorentzian-polynomial proofs, which sits adjacent to LP/SDP bound work on sphere packing and extremal combinatorics.

## Open questions / connections
- Geometric interpretation of these algebraic Kähler packages (Question 19) — currently purely algebraic with no known geometric origin.
- Implications for diagonal coinvariants and fermionic diagonal coinvariants (Question 20; extends Kim–Rhoades [24]).
- Whether the construction extends to prove the Novak–Rhoades conjecture (longest-increasing-subsequence log-concavity, Conjecture 21) and Gui's flag-variety coinvariant conjecture (Conjecture 22).
- Generalizes Lam–Postnikov–Pylyavskyy Schur log-concavity [26] (a special case of Okounkov's conjecture) to an explicit map-level statement for $S_n$.

## Key terms
equivariant log-concavity, Kähler package, hard Lefschetz, Hodge–Riemann bilinear relations, Poincaré duality, symmetric group representation, exterior algebra, polynomial ring cohomology, $\mathfrak{sl}_2$-triple, Lefschetz operator, primitive decomposition, Schur log-concavity, Okounkov conjecture, Littlewood–Richardson coefficients, tensor product representations
