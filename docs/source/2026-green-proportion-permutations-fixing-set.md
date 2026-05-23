---
type: source
kind: paper
title: The proportion of permutations fixing a $k$-set
authors: Ben Green, Mehtaab Sawhney
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.28116v1
source_local: ../raw/2026-green-proportion-permutations-fixing-set.pdf
topic: general-knowledge
cites: 
---

# The proportion of permutations fixing a $k$-set

**Authors:** Ben Green, Mehtaab Sawhney  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2604.28116v1

## One-line
Establishes a sharp asymptotic for $p(k)$, the limiting probability that a random permutation has an invariant set of size $k$, revealing oscillatory dependence on $\{\log_2 k\}$.

## Key claim
$p(k) = (1+o(1)) f(\{\log_2 k\}) k^{-\delta} (\log k)^{-3/2}$, where $\delta = 1 - (1+\log\log 2)/\log 2 \approx 0.086$ (Erdős–Ford–Tenenbaum constant) and $f \in C^\infty(\mathbb{R}/\mathbb{Z})$ is a smooth, nowhere-zero function expressible as $c_0\, g * \mu * \mu'$ with $\max f / \min f < 1 + 2 \times 10^{-7}$.

## Method
Reduces $p(k)$ via Arratia–Tavaré to $\mathbb{P}(k \in \Sigma(A_0))$ for a Poisson random multiset, then changes measure to a "lower" lacunary process $x$ and an "upper" rate-1 Poisson process $u$. The core analysis conditions random walks (Pois(1)$-$1 increments) to stay almost positive, using Denisov–Tarasov–Wachtel-type local limit theorems and a Poisson-paradigm approximate $\ell$-wise independence + inclusion–exclusion argument to control subset-sum statistics $\tau_x(\ell)$ and $\varrho_u(\ell)$.

## Result
The function $f$ decomposes as a convolution $c_0\, g * \mu * \mu'$ with $c_0 = (\pi/2)^{1/2}(\log 2)^{3/2} e^{\gamma(1/\log 2 - 1)}$ and $g(x) = \sum_{D\in\mathbb{Z}}(\log 2) 2^{D-x}(1 - e^{-2^{D-x}})$. The Fourier coefficients $\hat g(m)$ are values of $\Gamma$ at imaginary part $2\pi m/\log 2$, explaining the extreme near-constancy. As a corollary, along powers of two, $p(k) = (C+o(1)) k^{-\delta} (\log k)^{-3/2}$. Methods adapt to give an asymptotic for Erdős's multiplication table $M(n)$ in forthcoming work.

## Why it matters here
General background; no direct arena tie. Connects to extremal/probabilistic combinatorics and analytic number theory (subset sums, Poisson paradigm, random walks conditioned to stay positive) — techniques potentially relevant to combinatorial counting problems but not directly mapped to current Arena problems.

## Open questions / connections
- Is $f$ non-constant? Equivalently, is $\mu * \mu'$ not the uniform measure on $\mathbb{R}/\mathbb{Z}$?
- Numerical/computational simulation of $\mu, \mu'$ is open — obstructed by subset-sum problem (exponential-in-$\ell$ complexity).
- Extends Ford's $k^{-\delta}(\log k)^{-3/2}$ order-of-magnitude bound (Eberhard–Ford–Green 2016) to a sharp asymptotic; same machinery promised for $M(n)$ (Erdős's multiplication table problem).
- Same function $g$ unexpectedly appears in Granville–Sedunova–Sabuncu (multiplication table constant + sums of two squares) and in Hardy's account of Ramanujan's failed PNT proof.

## Key terms
permutation invariant set, multiplication table problem, Erdős–Ford–Tenenbaum constant, Poisson paradigm, random walks conditioned to stay positive, Denisov–Tarasov–Wachtel local limit, subset sums, Rayleigh distribution, approximate $\ell$-wise independence, inclusion–exclusion, bounded Lipschitz distance, Berry–Esséen, cycle structure random permutations, lacunary sequences
