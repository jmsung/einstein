---
type: source
kind: paper
title: Some open problems on Coxeter groups and unimodality
authors: Francesco Brenti
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.09897
source_local: ../raw/2024-brenti-some-open-problems-coxeter.pdf
topic: general-knowledge
cites:
---

# Some open problems on Coxeter groups and unimodality

**Authors:** Francesco Brenti  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.09897

## One-line
A survey of open conjectures and problems linking Coxeter group combinatorics (Kazhdan–Lusztig polynomials, Bruhat intervals, reflection generating functions) to unimodality, log-concavity, and total positivity, with the partial results and computational evidence currently known.

## Key claim
No single new theorem; the paper consolidates ~12 open problems/conjectures, the most prominent being the Combinatorial Invariance Conjecture (CIC: $P_{u,v}(q)=P_{w,z}(q)$ whenever $[u,v]\simeq[w,z]$ as posets), Marietti's parabolic refinement of CIC, the nonnegativity of the complete $cd$-index $\Phi_{u,v}\in\mathbb{N}\langle c,d\rangle$, total positivity of the Eulerian matrix $A(n+1,k)$, and rank log-concavity of Bruhat intervals in Weyl groups.

## Method
Survey/expository — gathers definitions (parabolic R- and KL-polynomials via Deodhar's "Theorem-Definitions," reflection orderings, complete $cd$-index, $h$-vectors, $\gamma$-nonnegativity), states each conjecture, cites partial proofs (e.g., CIC verified for $\ell(u,v)\le 4$ generally; $\le 8$ in type $A$; type $\tilde A_2$; lattice intervals; Boe/Hermitian symmetric pairs), and reports computer-verified ranges (e.g., Eulerian TP checked for $n,k\le 44$; $L_n(x)$ unimodal for $n\le 11$).

## Result
Catalogues the state of the art: CIC reduces equivalently to $R_{x,y}=R_{u,v}$; an AI-derived hypercube-decomposition algorithm (Blundell et al. 2022) conjecturally computes $P_{u,v}$ for type $A$ from the poset; Plaza's monotonicity $P_{v,w}\le P_{u,w}$ coefficientwise for $u\le v\le w$; parabolic monotonicity $P^{J,q}_{u,v}\le P^{I,q}_{u,v}$ for $I\subseteq J$; the odd-length statistic $L_n(x)=\sum_{\sigma\in S_n} x^{L(\sigma)}$ is conjectured symmetric+unimodal (not log-concave, not $\gamma$-nonnegative). New conjecture 2.4: $Q_{u,v}(t)$ (where $\widetilde R_{u,v}(t)=Q_{u,v}(t^2)$ or $tQ_{u,v}(t^2)$) is log-concave for finite Coxeter systems.

## Why it matters here
General background; no direct arena tie — Einstein Arena problems center on continuous geometric optimization (sphere packing, autocorrelation, kissing), whereas this paper concerns discrete Coxeter combinatorics. Marginal relevance: the unimodality/log-concavity/total-positivity toolkit (Theorem 2.1 linking real-rooted polynomials to TP Hankel-style matrices, $\gamma$-nonnegativity) is the same machinery that underlies LP-bound positivity arguments in Cohn–Elkies sphere packing.

## Open questions / connections
- Is $\sum_{t\in T} x^{\ell(t)}$ rational for every Coxeter system? (Stembridge 1997 — no partial results known.)
- Does every KL polynomial $P_{u,v}$ arise as $P_{e,w}$ in *some* Coxeter system? (Björner; Polo 1999 settled the type-$A$ "any $P\in\mathbb{N}[q]$ with $P(0)=1$" case for $S_n$.)
- Real-rootedness of $\tau$-polynomial $\tau(G;x)=\sum_\pi a(G[\pi])x^{|\pi|}$ for all graphs (yes for connected $G$ on $\le 8$ vertices).
- Does every symmetric monic real-rooted polynomial in $\mathbb{N}[t]$ arise as the $h$-vector of a simplicial convex polytope? (Yes for $d\le 9$, $h_i\le 100$.)
- Total positivity (and "monotone TP") of the Eulerian matrix — strengthens Chen–Deb–Dyachenko–Gilmore–Sokal.

## Key terms
Coxeter group, Bruhat interval, Kazhdan-Lusztig polynomial, parabolic Kazhdan-Lusztig, R-polynomial, Combinatorial Invariance Conjecture, reflection ordering, complete cd-index, hypercube decomposition, unimodality, log-concavity, gamma-nonnegativity, total positivity, Eulerian numbers, h-vector, odd length statistic, Brenti, Stembridge, Marietti, Deodhar, Dyer
