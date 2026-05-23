---
type: source
kind: paper
title: Optimal Size of Linear Matrix Inequalities in Semidefinite Approaches to Polynomial Optimization
authors: G. Averkov
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.08656
source_local: ../raw/2018-averkov-optimal-size-linear-matrix.pdf
topic: general-knowledge
cites:
---

# Optimal Size of Linear Matrix Inequalities in Semidefinite Approaches to Polynomial Optimization

**Authors:** G. Averkov  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.08656

## One-line
Proves that the standard SOS-to-SDP reduction is size-optimal — you cannot represent the SOS cone $\Sigma_{n,2d}$ using any finite number of LMIs smaller than $\binom{n+d}{n}$.

## Key claim
For all $n, d$: $\mathrm{sxdeg}(\Sigma_{n,2d}) = \mathrm{sxc}(\Sigma_{n,2d}) = \binom{n+d}{n}$. Consequently $\mathrm{sxdeg}(\mathcal{S}^k_+) = k$ (the PSD cone of $k \times k$ matrices needs LMIs of size $\geq k$), and the SONC cone has $\mathrm{sxdeg}(C_{n,2d}) = 2$ (second-order-cone representable, independent of $n,d$).

## Method
Combines the Gouveia–Parrilo–Thomas slack-matrix criterion for $K$-lifts with Ramsey's theorem for $k$-uniform hypergraphs. Main theorem: if a cone $C \subseteq P_{n,2d}(X)$ admits arbitrarily large sets $S$ such that for every $k$-element subset $T \subset S$ some $f \in C$ vanishes on $T$ and is positive on $S \setminus T$, then $\mathrm{sxdeg}(C) > k$. Vandermonde-style general-position arguments produce the required vanishing polynomials (squares of degree-$d$ interpolants) for SOS cones; Ben-Tal–Nemirovski's weighted geometric-mean SOCP construction handles SONC.

## Result
Beyond the SOS exact value, the paper determines: $\mathrm{sxdeg}(P_{n,2d}) = \binom{n+d}{n}$ when $n=1$, $d=1$, or $(n,d)=(2,2)$, else $\infty$ (combining with Hilbert + Scheiderer); truncated quadratic modules $C = \Sigma_{n,2d_0} + g_1\Sigma_{n,2d_1} + \cdots$ have $\mathrm{sxdeg}(C) = \binom{n+d}{n}$ with $d = \max d_i$ (Lasserre hierarchy levels are size-tight); copositive and completely positive cones satisfy $\mathrm{sxdeg}(CP_k) = \mathrm{sxdeg}(CP^*_k) \geq k$, with equality for $k \leq 4$; $\Sigma_{n,2d} + C_{n,2d} \neq P_{n,2d}$ whenever $n,d \geq 2$, $(n,d)\neq(2,2)$.

## Why it matters here
Directly informs the SDP-flag/Lasserre cost analysis used in arena problems where SOS hierarchies are an obvious-looking attack — confirms the "SDP relaxation uselessness" dead-end is structural, not a tooling artifact, and that pushing the hierarchy level $d$ blows up LMI size as $\binom{n+d}{n}$ with no smaller-LMI workaround. The $\mathrm{sxdeg}(C_{n,2d}) = 2$ result motivates SONC/SOCP as a cheap alternative for non-negative polynomial certificates (relevant when SOS is too large to fit).

## Open questions / connections
- Exact $\mathrm{sxdeg}(CP_k)$ for $k > 4$ — even finiteness unknown.
- Sparsity / symmetry exploitation (Lasserre §8, Nie) as the only escape from the size lower bound — when does it actually shrink LMIs in practice?
- $\mathrm{sxc}(C_{n,2d})$ (number of SOCP constraints) for SONC remains open even though degree is settled at 2.
- Extends Fawzi's $\mathrm{sxdeg}(\mathcal{S}^3_+) = 3$ and Ahmadi et al.'s $\mathrm{sxdeg}(\Sigma_{1,4}) = 3$ to the full parameter range via hypergraph-Ramsey generalization.

## Key terms
semidefinite extension degree, SOS hierarchy, Lasserre relaxation, linear matrix inequality, LMI size lower bound, sum of squares, SONC, sums of nonnegative circuit polynomials, copositive cone, completely positive cone, truncated quadratic module, Gouveia-Parrilo-Thomas slack matrix, Ramsey theorem, second-order cone programming, Scheiderer spectrahedral shadows, Hilbert 1888, moment cone, Fawzi, Averkov
