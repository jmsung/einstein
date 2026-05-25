---
type: source
kind: paper
title: A short proof of ℓ2 decoupling for the moment curve
authors: LI Zanekun, Po-Lam Yung, Pavel Zorin-Kranich
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.09798
source_local: ../raw/2019-zanekun-short-proof-decoupling-moment.pdf
topic: general-knowledge
cites:
---

# A short proof of ℓ2 decoupling for the moment curve

**Authors:** LI Zanekun, Po-Lam Yung, Pavel Zorin-Kranich  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.09798

## One-line
A short, elementary bilinear proof of the sharp $\ell^2$ decoupling inequality for the moment curve $\Gamma(\xi)=(\xi,\xi^2,\ldots,\xi^k)$ in $\mathbb{R}^k$, avoiding Kakeya–Brascamp–Lieb machinery.

## Key claim
**Theorem 1.2 (re-proved):** For every $k\in\mathbb{N}$ and $\epsilon>0$, the $\ell^2 L^{p_k}$ decoupling constant satisfies $D_k(\delta)\le C_{k,\epsilon}\delta^{-\epsilon}$ at the critical exponent $p_k=k(k+1)$, for all $\delta\in(0,1)$ — equivalently, the optimal exponents in Vinogradov's mean value theorem.

## Method
Bilinear (not multilinear) decoupling: reduce linear decoupling to a symmetric bilinear constant $B(\delta)$ via a Whitney decomposition of $[0,1]^2$ around the diagonal, then introduce **asymmetric** bilinear constants $B_{l,a,b}(\delta)$ at intermediate scales $\delta^a,\delta^b$. Transversality between $V^{(l)}(\xi_1)$ and $V^{(k-l)}(\xi_2)$ (quantified by a generalized Vandermonde bound $\gtrsim|\xi_1-\xi_2|^{l(k-l)}$) lets Fubini + uncertainty principle reduce to lower-degree decoupling $D_l$ ($l<k$). A Hölder-interpolation lemma plus a Perron–Frobenius-style left eigenvector argument (eigenvector $(1,\ldots,1)$ of the recursion matrix) closes the induction on $k$, giving $\eta=0$.

## Result
The decoupling exponent $\eta := \inf\{\epsilon : D_k(\delta)\lesssim\delta^{-\epsilon}\}$ equals $0$, recovering Bourgain–Demeter–Guth [BDG16] without Kakeya–Brascamp–Lieb. As a corollary (Corollary 1.3), Vinogradov's mean value theorem holds with optimal exponents: $\int|\sum_{n=1}^N a_n e(nx_1+\cdots+n^k x_k)|^{2s}\lesssim_\epsilon N^\epsilon(1+N^{s-k(k+1)/2})(\sum|a_n|^2)^s$. Method extends to curves with torsion (Lemma 3.6).

## Why it matters here
General background; no direct arena tie. Decoupling/Vinogradov are adjacent to the harmonic-analysis toolkit (uncertainty principle, LP duality, transversality arguments) that touches autocorrelation/uncertainty problems (P14, P17) and Cohn–Elkies-style bounds, but the specific machinery here is not directly used in current wiki techniques.

## Open questions / connections
- Can the asymmetric bilinear constant framework simplify decoupling proofs for other model manifolds (cones, paraboloids in higher codimension)?
- The Perron–Frobenius left-eigenvector structure of the recursion (Remark 4.3) — does it generalize to non-curve manifolds where transversality is partial?
- Relation to Wooley's nested efficient congruencing [Woo19] and Heath-Brown's cubic simplification [Hea15] — what is the precise dictionary between counting and decoupling?

## Key terms
ℓ2 decoupling, moment curve, Vinogradov mean value theorem, bilinear decoupling, Bourgain-Demeter-Guth, Wooley efficient congruencing, transversality, Vandermonde determinant, uncertainty principle, Whitney decomposition, critical exponent k(k+1), Perron-Frobenius eigenvector
