---
type: source
kind: paper
title: "Chernoff-Hoeffding Bounds for Markov Chains: Generalized and Simplified"
authors: Kai-Min Chung, H. Lam, Zhenming Liu, M. Mitzenmacher
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1201.0559
source_local: ../raw/2012-chung-chernoff-hoeffding-bounds-markov-chains.pdf
topic: general-knowledge
cites:
---

# Chernoff-Hoeffding Bounds for Markov Chains: Generalized and Simplified

**Authors:** Kai-Min Chung, H. Lam, Zhenming Liu, M. Mitzenmacher  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1201.0559

## One-line
Proves the first Chernoff-Hoeffding concentration bounds for random walks on general (irreversible) finite-state Markov chains parameterized directly by the $L_1$ mixing-time $T$, plus a simplified elementary proof of the spectral-expansion version.

## Key claim
For an ergodic chain $M$ with stationary $\pi$, $\varepsilon$-mixing time $T = T(\varepsilon)$ with $\varepsilon \le 1/8$, weight functions $f_i:[n]\to[0,1]$ all with $\mathbb{E}_\pi f_i = \mu$, and $X = \sum_{i=1}^t f_i(V_i)$ along a $t$-step walk from $\varphi$:
$$\Pr[|X - \mu t| \ge \delta \mu t] \le c\|\varphi\|_\pi \cdot \begin{cases} \exp(-\delta^2 \mu t / 72T) & 0\le\delta\le 1 \\ \exp(-\delta\mu t / 72T) & \delta > 1 \end{cases}$$
matching the i.i.d. Chernoff exponent up to the $1/T$ factor, and tight up to constants among mixing-time-based bounds.

## Method
Partition the walk into $T$ interleaved sub-walks of step-$T$ powers $M^T$; each sub-walk has unit mixing time, so via reversiblization $R = M^T \tilde M^T$ and Sinclair-style mixing↔spectral lemma one gets $\lambda(M^T) \le \sqrt{2\varepsilon}$ (Claim 3.1). Then bound each sub-walk's MGF via a spectral Chernoff bound (Claim 3.2) proved by directly tracking the $\pi$-parallel/perpendicular decomposition $z_i = z_{i-1}P_iM$ through coupled recurrences for $\|z_i^\|\|_\pi, \|z_i^\perp\|_\pi$ — avoiding Kato perturbation theory and the reversiblization black box of Lezaud/Wagner. Combine sub-walk MGFs via Jensen + Markov.

## Result
Discrete-time bound above with constant $1/72$ in the exponent (improvable to $(1-\sqrt{2\varepsilon})/36$); a unified elementary proof of the spectral-expansion bound $\exp(-\Omega(\delta^2(1-\lambda)\mu t))$ valid for both reversible and irreversible chains and for distinct $f_i$ sharing mean $\mu$; continuous-time analog via $b\to 0$ discretization (Theorem 3.5) — the latter only possible because the leading $T$ factor of a naive union-bound proof is shaved off. Optimality witnessed by a 2-state lazy chain with flip-prob $p = \Theta(1/T)$.

## Why it matters here
General background; no direct arena tie. Could inform MCMC-based optimizers (parallel tempering, basin-hopping with Markov proposals) where one needs honest concentration guarantees on time-averaged observables when the chain mixes slowly but has poor spectral gap — a regime that arises in float64 SA on rugged landscapes.

## Open questions / connections
- Are the bounds still tight when $\varepsilon = o(1)$? (Optimality example only works for constant $\varepsilon$.)
- Can the requirement that all $f_i$ share the same mean $\mu$ be removed in the mixing-time (not just spectral) version?
- Extends Gillman (1997), Lezaud (1998), Leon-Perron (2004), Wagner (2008), Healy (2008); generalizes Healy's regular-graph trace approach to arbitrary ergodic chains.
- Connects to Sinclair (1992) mixing↔spectral inequality and Aldous (1982) continuous-time reversible bounds.

## Key terms
Chernoff-Hoeffding bound, Markov chain concentration, mixing time, total variation distance, spectral gap, spectral expansion, reversiblization, irreversible chain, moment generating function, MCMC, stationary distribution, Lezaud bound
