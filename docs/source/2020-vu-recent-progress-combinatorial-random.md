---
type: source
kind: paper
title: Recent progress in combinatorial random matrix theory
authors: V. Vu
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.02797
source_local: ../raw/2020-vu-recent-progress-combinatorial-random.pdf
topic: general-knowledge
cites:
---

# Recent progress in combinatorial random matrix theory

**Authors:** V. Vu  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.02797

## One-line
Survey of progress on discrete random matrix problems — singularity probability, rank/co-rank, determinant/permanent magnitude, spectral gap, simple spectrum, normality, and sandpile groups — focused on $\pm 1$ matrices and random (regular and Erdős–Rényi) graphs.

## Key claim
Tikhomirov (2018) resolved the folklore singularity conjecture: for the $n\times n$ Rademacher matrix $M_n$, $p_n = P(M_n\text{ singular}) = (1/2 + o(1))^n$, matching the trivial two-equal-rows lower bound. Symmetric and random-regular analogs are now known to satisfy $p_n^{sym}\le \exp(-n^{1/2})$ (Campos–Mattos–Morris–Morrison) and $P(A_{n,d}\text{ singular})\le n^{-c}$ for fixed $d\ge 3$ (Huang, Mészáros).

## Method
The dominant technique is **anti-concentration** of random walks $S=\sum\xi_i v_i$ via Erdős–Littlewood–Offord small-ball inequalities ($p_v\le \binom{n}{\lfloor n/2\rfloor}2^{-n}=O(n^{-1/2})$) and **inverse Littlewood–Offord theorems** (Tao–Vu, Rudelson–Vershynin) that force additive structure on coefficients when concentration is large. Tikhomirov's proof adds an "inversion of randomness" double-counting argument reducing the problem to random walks with **random** coefficients. Other tools: Talagrand concentration for distance-to-subspace (Lemma 6.4), martingale methods for permanents, Wigner semicircle + least-singular-value bounds for $|\det M_n^{sym}|$, and Cohen–Lenstra-style heuristics for sandpile p-Sylow distributions.

## Result
- Singularity: $p_n=(1/2+o(1))^n$; symmetric $p_n^{sym}\le\exp(-n^{1/2})$; $A_{n,d}$ non-singular w.h.p. for fixed $d\ge 3$.
- Determinant magnitude: $|\det M_n|, |\det M_n^{sym}|, |\text{Per }M_n| = n^{(1/2-o(1))n}$ w.h.p. (matches Turán identity $E(\det M_n)^2 = n!$).
- Spectral: Friedman's theorem $\lambda(G_{n,d})=2\sqrt{d-1}+o(1)$ w.h.p.; Babai's simple-spectrum conjecture proved for $G(n,1/2)$ (Tao–Vu); Marcus–Spielman–Srivastava bipartite Ramanujan existence for all $d\ge 3$.
- Rank threshold: $\text{corank}\,A(n,p)=0$ exactly when $p\ge \log n/n + \gamma(n)/n$ (Addario-Berry–Eslava hitting-time version).
- Normality: $\nu_n\le 2^{-(0.302+o(1))n^2}$ (Deneanu–Vu), conjectured $2^{-(0.5+o(1))n^2}$.

## Why it matters here
General background; no direct arena tie. Could inform discrete-combinatorics problems via anti-concentration + inverse Littlewood–Offord machinery, which underlies many extremal-combinatorics small-ball / forbidden-configuration arguments; the spectral-gap / Ramanujan threshold $2\sqrt{d-1}$ is a canonical extremal bound worth citing if any arena problem touches expander-like graphs.

## Open questions / connections
- Sharp constant $c$ in $P(A_{n,d}\text{ singular})\le n^{-c}$ for fixed $d$ (Huang gives $\min\{1/8,(d-2)/(5d-6)\}$; lower bound $n^{-d+2}$).
- Conjecture 6.8: $P(\det M_n = x)\le n^{-(1/2+o(1))n}$ for any $x\ne 0$; only exponential bound known.
- Conjecture 11.3: $M_n$ has $\Theta(\sqrt n)$ real eigenvalues w.h.p. — even "≥2 real eigenvalues" is open.
- Limiting distribution of $\lambda_2(G_{n,d})$ — exact Ramanujan probability still unknown.
- Permanent zero-probability: super-exponentially small? Currently only polynomial bound.

## Key terms
random matrix, singularity probability, Rademacher matrix, Bernoulli matrix, anti-concentration, Littlewood-Offord, inverse Littlewood-Offord, Tikhomirov, Komlós, Kahn-Komlós-Szemerédi, random regular graph, Ramanujan graph, Friedman theorem, Alon-Boppana, simple spectrum, sandpile group, Cohen-Lenstra, permanent, determinant, Erdős-Rényi, Wigner semicircle, least singular value, Talagrand concentration
