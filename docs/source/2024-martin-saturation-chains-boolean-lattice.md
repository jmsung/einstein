---
type: source
kind: paper
title: Saturation of $k$-Chains in the Boolean Lattice
authors: Ryan R. Martin, Nick Veldt
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2402.14113
source_local: ../raw/2024-martin-saturation-chains-boolean-lattice.pdf
topic: general-knowledge
cites:
---

# Saturation of $k$-Chains in the Boolean Lattice

**Authors:** Ryan R. Martin, Nick Veldt  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2402.14113

## One-line
Tightens both the upper and lower bounds for the minimum size $\mathrm{sat}(k)$ of a saturated $k$-Sperner system in the Boolean lattice $\mathcal{P}(X)$ for sufficiently large $|X|$.

## Key claim
For $k \ge 7$, $\mathrm{sat}(k) \le 2^{(1-\varepsilon)k}$ with $\varepsilon = 1 - \tfrac{1}{5}\log_2 28 \approx 0.038529$ (improving the prior $\approx 0.023277$); and for $k \ge 497$, $\mathrm{sat}(k) > \sqrt{k}\, 2^{k/2}$ (improving the prior $2^{k/2 - 0.5}$).

## Method
Upper bound: explicit construction of a saturated 7-Sperner system of size 56, built from a layered sequence of disjoint saturated antichains whose middle layer is the Fano plane $\cup$ its complement family (using $\chi(\text{Fano}) = 3$ for saturation), then bootstrapped via the Morrison–Noel–Scott composition lemma to arbitrary $k$. Lower bound: probabilistic / first-moment argument — pick each element of $[n]$ independently with probability $1/2 - \varepsilon$, count sub/supersets in each canonical antichain layer $\mathcal{A}_i$, require expectation $\ge 1$ for saturation, then sum over layers using an integral approximation that reduces to the error function $\mathrm{erf}$.

## Result
Construction: layered antichain family $\mathcal{F} = \bigcup_{i=0}^{6} \mathcal{A}_i$ of size 56 (vs. previous 60) for $k=7$; via composition lemma yields $\mathrm{sat}(k) \le 2^{s+1} \cdot 28^{j}$ for $k = 5j + 2 + s$, $0 \le s \le 4$. Lower bound: $|\mathcal{F}| \ge 2^{k/2 + (1/2)\log_2 k - 1.66}$ for $k \ge 7$ and $\ge 2^{k/2 + (1/2)\log_2 k}$ for $k \ge 497$. Combined: $\sqrt{k}\, 2^{k/2} < \mathrm{sat}(k) < 2^{0.961471 k}$.

## Why it matters here
General background; no direct arena tie — the Einstein Arena problems cover sphere packing / autocorrelation / kissing, not poset saturation. Tangentially informs **extremal set theory / Sperner-type** intuition (Boolean lattice antichains, LYM-style counting, probabilistic lower bounds via biased product measure) which could brush against discrete-combinatorics problems if any arise.

## Open questions / connections
- Is $\mathrm{sat}(7) = 56$ exactly, or does a smaller construction exist?
- Can the gap between $\sqrt{k}\,2^{k/2}$ and $2^{0.961471 k}$ be closed for large $k$?
- Are all optimal saturated $k$-Sperner systems "flat" — i.e., within each $\mathcal{A}_i$ do small (resp. large) elements share a common size?
- Extends Gerbner et al. (2013) and Morrison–Noel–Scott (2014); relates to induced poset saturation literature (Ferrara et al., Keszegh et al., Ivan).

## Key terms
saturated k-Sperner system, Boolean lattice, antichain saturation, Sperner's theorem, Erdős k-chain theorem, LYM-style probabilistic lower bound, Fano plane chromatic number, layered antichain decomposition, homogeneous atom, poset saturation, extremal set theory, Turán-type problem
