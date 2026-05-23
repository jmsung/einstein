---
type: source
kind: paper
title: Computing the Lambert W function in arbitrary-precision complex interval arithmetic
authors: Fredrik Johansson
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1705.03266v1
source_local: ../raw/2017-johansson-computing-lambert-function-arbitrary-precisio.pdf
topic: general-knowledge
cites: 
---

# Computing the Lambert W function in arbitrary-precision complex interval arithmetic

**Authors:** Fredrik Johansson  ·  **Year:** 2017  ·  **Source:** http://arxiv.org/abs/1705.03266v1

## One-line
Describes a rigorous algorithm — implemented in the Arb library — for evaluating all complex branches $W_k(z)$ of the Lambert W function in arbitrary-precision complex interval arithmetic with certified error bounds.

## Key claim
All branches $W_k(z)$ can be enclosed rigorously at any precision with cost only a constant factor over $\exp/\log$, by combining a Halley iteration with backward-error a posteriori certification, plus explicit truncation bounds for the Taylor, Puiseux, and asymptotic expansions (notably $|c_{l,m}| \le 4^{l+m}$ for the asymptotic coefficients, and $|c_n| \le 1$ for the Puiseux series coefficients around the branch point $-1/e$).

## Method
Three-stage scheme: (i) detect asymptotic regimes ($|z|$ tiny, huge, or near $-1/e$) and use bounded Taylor/Puiseux/asymptotic series; (ii) compute a floating-point approximation $\tilde w$ via Halley iteration with precision doubling; (iii) certify by backward error — set $\tilde z = \tilde w e^{\tilde w}$ and bound $|W_k(\tilde z) - W_k(z)| \le |z-\tilde z|\sup_\gamma |W'_k|$, with a branch-membership test using the curves $-\eta\cot\eta + \eta i$ from Corless et al. Alternative branch cuts ($W_{\text{left}|k}$, $W_{\text{middle}}$) are introduced so output intervals converge across the standard cuts.

## Result
Explicit constants are derived where prior work gave only big-O: Lemma 3 gives $|c_{l,m}| \le 4^{l+m}$ for the asymptotic Stirling-coefficients; Theorem 4 gives effective tail bound $|\varepsilon_{L,M}(z)| \le \frac{4|\tau|(4|\sigma|)^L + (4|\tau|)^M}{(1-4|\sigma|)(1-4|\tau|)}$ when $|\sigma|,|\tau|<1/4$; Theorems 5–9 give piecewise rigorous bounds on $|W'_k(z)|$ including $|W'_k(z)| \le 1/|z|$ when $|z| \ge 4(|k|+1)$, and $|W'_0(z)| \le 2.25/(t(1+t))$ near $-1/e$ with $t=|ez+1|$. Benchmarks show $W$ is ~1.5–4× cost of $\exp$ at 100–10000 digits; 10000 Taylor terms of $W_0(e^{1+x})$ at 256-bit take 2.8 s.

## Why it matters here
General background; no direct arena tie. Closest relevance is as a template for **interval-arithmetic certification of transcendental optima** — the backward-error-then-bound-derivative pattern is reusable wherever the arena agent needs rigorous enclosures (e.g. mpmath polish on $P_5, P_6, P_{11}, P_{14}, P_{17}$ float-precision-critical problems, or triple-verify check #2).

## Open questions / connections
- Tighter / simpler bounds for $|W^{(n)}(z)|$ for small $n$ would sharpen higher-order error propagation on wide intervals — left open.
- Rigorous floating-point (non-interval) error analysis for complex $W$ remains feasible but unproven; would unlock Ziv-strategy correct rounding without interval overhead.
- For wide $z$, optimal enclosures via evaluation at extremal points (monotonicity conditions for complex case) not yet characterized.
- Extends Corless–Gonnet–Hare–Jeffrey–Knuth 1996 by replacing heuristic numerics with certified bounds; complements Kalugin–Jeffrey 2012 (asymptotic convergence) and Johansson 2015 (medium-precision elementary functions).

## Key terms
Lambert W function, interval arithmetic, Arb library, arbitrary precision, Halley iteration, backward error analysis, branch cuts, Puiseux series, asymptotic expansion, Stirling numbers first kind, complex analysis, Johansson, Corless, certified enclosure, mpmath polish
