---
type: source
kind: paper
title: The Complexity of Positive Semidefinite Matrix Factorization
authors: Yaroslav N. Shitov
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1606.09065
source_local: ../raw/2016-shitov-complexity-positive-semidefinite-matrix.pdf
topic: general-knowledge
cites:
---

# The Complexity of Positive Semidefinite Matrix Factorization

**Authors:** Yaroslav N. Shitov  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1606.09065

## One-line
Proves that computing the positive semidefinite (PSD) rank of a nonnegative integer matrix is polynomial-time equivalent to the existential theory of the reals ($\exists\mathbb{R}$).

## Key claim
**Theorem 2.3:** PSD RANK is $\exists\mathbb{R}$-complete. This settles a long-standing open conjecture (Problem 9.6 of Fawzi–Gouveia–Parrilo–Robinson–Thomas) that PSD rank is NP-hard, and strengthens it: PSD rank computation is at least as hard as deciding any quantifier-free first-order formula over $(\mathbb{R},+,-,\cdot,0,1)$.

## Method
Reduction from a restricted ETR problem (single polynomial equation in standard monomial form, no solutions outside $[-1,1]^n$, via Grigoriev–Vorobjov radius bound $2^{2^{CL}}$) to PSD RANK. Constructs an incomplete matrix $B(f)$ whose entries encode dot-product squares $(u\cdot v)^2$ over a vector set $H(f) \subset \sigma^3$; uses the "sqrt condition" plus Lemma 5.2 to convert PSD-rank-3 completions to rank-3 sign-square completions; a delicate geometric argument (Steps 1–13 of Lemma 6.6) recovers a real root $f(y)=0$ from collinearity/orthogonality patterns of the factorization vectors. A matrix-completion gadget $M(S,K)$ built from copies of the $3\times 3$ matrix $P(\alpha)$ (which has PSD rank 2 for $\alpha \in [0,4]$) converts the completion problem back to a single PSD rank decision.

## Result
PSD RANK $\in \exists\mathbb{R}$-complete. Corollary: PSD rank is NP-hard (the original conjecture). Bonus result: for any irrational algebraic $r \in \mathbb{R}$, the PSD rank over $\mathbb{Q}$ and over $\mathbb{Q}(r)$ are genuinely different functions on rational matrices — generalizing Fawzi–Gouveia–Robinson 2016. Key technical lemma (4.8): if a bordered matrix $G$ has $\mathrm{PSDrank}\le r+2$, the inner block $A(x) = \binom{S\,b}{c\,x}$ has $\mathrm{PSDrank}\le r$ for some $x \ge 0$.

## Why it matters here
General background; no direct arena tie. Reinforces the wiki's "SDP relaxation uselessness" finding (P1) — exact PSD-rank certification is computationally intractable in the $\exists\mathbb{R}$ sense, so any optimizer hoping to use PSD-factorization bounds as a tractable subroutine is implicitly working inside an $\exists\mathbb{R}$-hard landscape and must rely on heuristic relaxations rather than exact computation.

## Open questions / connections
- Is nonnegative rank also $\exists\mathbb{R}$-complete? Only NP-hardness known (Vavasis 2009; Shitov 2016 short proof).
- Quantitative gap between rational and real PSD rank — how large can it be for fixed matrix size?
- Implications for the size of semidefinite extended formulations (Lee–Raghavendra–Steurer 2015): exact lower bounds via PSD rank are uncomputable in polynomial time unless $\exists\mathbb{R} = \mathsf{P}$.
- Extends Fiorini–Massar–Pokutta–Tiwary–de Wolf 2012 (LP extension complexity) into the SDP regime.

## Key terms
PSD rank, positive semidefinite factorization, existential theory of the reals, $\exists\mathbb{R}$-complete, nonnegative rank, semidefinite extension complexity, matrix completion, sqrt rank, Cholesky decomposition, Grigoriev–Vorobjov bound, semialgebraic sets, Shitov, Fawzi–Gouveia–Robinson, extended formulations
