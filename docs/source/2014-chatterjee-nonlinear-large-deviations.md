---
type: source
kind: paper
title: Nonlinear large deviations
authors: S. Chatterjee, A. Dembo
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.3495
source_local: ../raw/2014-chatterjee-nonlinear-large-deviations.pdf
topic: general-knowledge
cites:
---

# Nonlinear large deviations

**Authors:** S. Chatterjee, A. Dembo  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.3495

## One-line
A general machinery for computing large-deviation rate functions of nonlinear functions of independent Bernoulli variables, replacing Szemerédi's regularity lemma with a "low-complexity gradient" condition that extends to sparse regimes.

## Key claim
If $f:[0,1]^n\to\mathbb{R}$ is smooth and its gradient $\nabla f(x)$ can be approximately encoded by $o(n)$ bits (the *low-complexity gradient* condition), then $\log P(f(Y)\ge tn) = -\varphi_p(t) + o(n)$, where $\varphi_p(t) = \inf\{I_p(x): f(x)\ge tn\}$ and $I_p$ is the product Bernoulli relative entropy. Applied to $G(N,p)$ triangle counts, this yields the variational formula valid down to $p \gg N^{-1/42}(\log N)^{11/14}$, far below the dense-regime barrier.

## Method
Theorem 1.6 (free-energy / normalizing-constant approximation) is the core; Theorem 1.1 (upper-tail) is derived from it by a smooth indicator approximation, à la Bryc's inverse Varadhan lemma. The proof bounds the free energy via an $\epsilon$-net $D(\epsilon)$ over gradient images plus first/second-derivative smoothness control. For subgraph counts, the low-complexity gradient is verified by a *spectral argument* (replacing regularity lemma); for 3-APs on $\mathbb{Z}/n\mathbb{Z}$, by discrete Fourier transform + Plancherel.

## Result
- Triangle upper tail (with Lubetzky–Zhao's solution of the variational problem): $P(T\ge(1+\delta)\mathbb{E}T) = \exp(-(1+o(1))\min(\tfrac{\delta^{2/3}}{2},\tfrac{\delta}{3}) N^2 p^2 \log(1/p))$ for $p\gg N^{-1/42}(\log N)^{11/14}$.
- General subgraph $H$: error in $\varphi_p(u)/(-\log P)$ is $O((\log N)^{B_1}/(N^{B_2}p^{B_3}))$ with explicit exponents in $m=|E(H)|$, $\Delta$, $k=|V(H)|$.
- 3-term APs in random subsets of $\mathbb{Z}/n\mathbb{Z}$: same-form variational formula valid for $p\gg n^{-1/162}(\log n)^{33/162}$.
- Exponential random graphs: free-energy variational principle holds with error $O(B^{8/5}N^{9/5}(\log N)^{6/5})$.

## Why it matters here
General background; no direct arena tie. Closest relevance is the *low-complexity gradient* heuristic — a transferable diagnostic for when a nonlinear functional admits a clean variational characterization (relevant to autocorrelation inequalities, Sidon-type sum problems, and any extremal-combinatorics problem reduced to optimizing over $[0,1]^n$ with a smooth objective).

## Open questions / connections
- Can the threshold be pushed to $p \gg N^{-1/2}$ (conjectured by Lubetzky–Zhao) or even $N^{-1+\epsilon}$, fully closing the triangle large-deviation problem?
- Does the low-complexity gradient condition hold for longer arithmetic progressions ($k$-APs, $k\ge 4$) — likely yes wherever an averaging structure exists.
- Connects to Bhattacharya–Ganguly–Lubetzky–Zhao [2] which solves the variational problem for general $H$ via independence polynomials $P_{H^*}(\theta)=1+\delta$.

## Key terms
nonlinear large deviations, low-complexity gradient, Bernoulli rate function, subgraph count upper tail, Erdős–Rényi $G(N,p)$, triangle count, Szemerédi regularity lemma, sparse graph limits, exponential random graphs, three-term arithmetic progressions, discrete Fourier transform, variational principle, Chatterjee–Varadhan, Lubetzky–Zhao, independence polynomial, relative entropy, free energy approximation
