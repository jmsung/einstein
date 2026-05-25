---
type: source
kind: paper
title: Equivariant Semidefinite Lifts and Sum-of-Squares Hierarchies
authors: Hamza Fawzi, J. Saunderson, P. Parrilo
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1312.6662
source_local: ../raw/2013-fawzi-equivariant-semidefinite-lifts-sum-of-squares.pdf
topic: general-knowledge
cites:
---

# Equivariant Semidefinite Lifts and Sum-of-Squares Hierarchies

**Authors:** Hamza Fawzi, J. Saunderson, P. Parrilo  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1312.6662

## One-line
Proves that any symmetry-respecting SDP lift of a symmetric polytope is essentially a low-degree sum-of-squares relaxation, yielding exponential lower bounds for the parity polytope and the cut polytope.

## Key claim
Any $G$-equivariant psd lift of size $d$ of a $G$-orbitope $P = \mathrm{conv}(G\cdot x_0)$ is a sum-of-squares lift drawn from a $G$-invariant subspace $V \subseteq F(X,\mathbb{R})$ with $\dim V \le d^3$; specializing gives lower bounds $\ge \binom{n}{\lfloor n/4 \rfloor}$ on equivariant psd lifts of both $\mathrm{PAR}_n$ and $\mathrm{CUT}_n$.

## Method
Representation-theoretic structure theorem: combine the Gouveia–Parrilo–Thomas factorization theorem for psd lifts with isotypic decomposition of $F(X,\mathbb{R})$ under $G$, showing the certifying subspace can be chosen $G$-invariant. For specific orbitopes, classify low-dimensional invariant subspaces (here, of functions on $\{x \in \{\pm 1\}^n : \prod x_i = 1\}$ and on $\{\pm 1\}^n$) and show they contain only low-degree polynomials, then invoke Laurent's $\lceil n/2 \rceil$ SOS lower bound for $\mathrm{CUT}_n$ and a parallel $n/4$ bound proved here for $\mathrm{PAR}_n$.

## Result
- Structure theorem (Thm 1): equivariant psd lifts ↔ $G$-invariant SOS certificates, with $\dim V \le d^3$ (improvable for product-structure groups).
- Parity polytope (Thm 2): any $G_{\text{parity}}$-equivariant psd lift of $\mathrm{PAR}_n$ has size $\ge \binom{n}{\lfloor n/4 \rfloor}$ for $n \ge 8$ (exponential).
- Cut polytope (Thm 3): any $G_{\text{cube}}$-equivariant psd lift of $\mathrm{CUT}_n$ has size $\ge \binom{n}{\lfloor n/4 \rfloor}$ (exponential), broader than the permutation-only symmetry of Lee–Raghavendra–Steurer–Tan.
- Approximation versions (Thm 10): small equivariant $(c,s)$-approximations of $\mathrm{CUT}_n$ are matched by a constant number of SOS rounds on $\mathrm{CUT}_{\lfloor n/2 \rfloor}$.

## Why it matters here
Direct relevance to any arena problem reaching for SDP relaxations (cut-like extremal-graph problems, autocorrelation/uncertainty problems framed as moment SDPs): if the problem has symmetry and you write an equivariant SDP, you cannot beat the Lasserre/theta-body hierarchy of comparable degree — so equivariant SDP shortcuts to better bounds are ruled out a priori. Extends the wiki's existing `findings/sdp-relaxation-uselessness` (P1) by giving a general structural reason rather than a one-problem dead end.

## Open questions / connections
- Does the $d^3$ bound tighten to $d^2$ (matching the non-equivariant converse to Theorem A)?
- For non-polyhedral orbitopes like $\mathrm{conv}(SO(n))$, what is the matching upper bound (only the parity-induced lower bound is transferred)?
- Follow-up [FSP15] gives $O(\log N)$ equivariant lifts of regular $N$-gons — does an analogous sparse-SOS construction exist for other low-symmetry-rank orbitopes relevant to packing problems?
- Connects to Lee–Raghavendra–Steurer (2014) breakthrough: non-equivariant exponential lower bound on $\mathrm{CUT}_n$ subsumes Thm 3 but uses very different (psd-rank) machinery.

## Key terms
equivariant psd lift, symmetric SDP lift, sum-of-squares hierarchy, Lasserre hierarchy, theta-body, orbitope, parity polytope, cut polytope, hyperoctahedral group, isotypic decomposition, Laurent lower bound, Yannakakis, Fawzi, Parrilo, representation theory of finite groups
