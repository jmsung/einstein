---
type: source
kind: paper
title: Some open problems on permutation patterns
authors: E. Steingrímsson
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1210.7320
source_local: ../raw/2012-steingrmsson-some-open-problems-permutation.pdf
topic: general-knowledge
cites:
---

# Some open problems on permutation patterns

**Authors:** E. Steingrímsson  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1210.7320

## One-line
A survey of open problems in permutation pattern avoidance, centered on the still-unknown Stanley–Wilf limit for the pattern 1324, growth rates of permutation classes, and the Möbius function / topology of the permutation containment poset.

## Key claim
The Stanley–Wilf limit $\mathrm{SW}(1324)$ is the last unknown growth constant among length-4 classical patterns: rigorously bounded in $[9.47,\ 7+4\sqrt{3}\approx 13.93]$, conjecturally $<e\pi\sqrt{2/3}\approx 13.00$, and Monte Carlo estimates suggest the true value is near 11 (Madras–Liu interval $[10.71, 11.83]$).

## Method
Synthesises several techniques: the *insertion encoding* + finite-automata analysis to produce lower bounds (Albert et al.), injective decomposition of 1324-avoiders into pairs (132-avoider, 213-avoider) refined with structural surgery to get upper bounds (Claesson–Jelínek–Steingrímsson, Bóna), and Markov-chain Monte Carlo random sampling of 1324-avoiders (Madras–Liu) for empirical estimates. The Möbius-function results use a sign-counting formula over *normal embeddings* of $\sigma$ in $\tau$; topology results use shellability and discrete Morse theory.

## Result
Bounds for $\mathrm{SW}(1324)$: $9.47 \le \mathrm{SW}(1324) \le 7+4\sqrt{3}\approx 13.9282$, conjecturally $<13.00$. For layered patterns of length $k$, $\mathrm{SW} \le 2.25 k^2$ (Bóna), supporting the conjecture that the most-avoided length-$k$ pattern is layered. Growth-rate spectrum of permutation classes is fully characterised below $\kappa\approx 2.2055$ (root of $x^3-2x^2-1$); every real $\ge \lambda\approx 2.4816$ (root of $x^5-2x^4-2x^2-2x-1$) is realised; gap between $\kappa$ and $\xi\approx 2.32$ remains open. Möbius function $|\mu(\sigma,\tau)|$ is bounded by the number of occurrences of $\sigma$ in $\tau$ for separable permutations.

## Why it matters here
General background; no direct arena tie. Permutation-pattern avoidance is a discrete-combinatorics / extremal-combinatorics neighbour to the arena's autocorrelation, Sidon, and extremal-graph problems — shares the "exponential growth constant of a forbidden-substructure family" motif (Stanley–Wilf ↔ Turán density ↔ packing density) and the technique of bounding such limits via decomposition + injective encoding.

## Open questions / connections
- Exact value (or even tight bounds) for $\mathrm{SW}(1324)$ — does the conjecture $\mathrm{SW}(1324) < e\pi\sqrt{2/3}$ hold, and is the Claesson–Jelínek–Steingrímsson "inversion-count monotonicity" conjecture true?
- Which length-$k$ layered pattern maximises $\mathrm{SW}$? Conjectures for $k\equiv 0,1,2 \pmod 4$ (Kézdy–Snevily, Burstein) remain unrefuted; $k\equiv 3 \pmod 4$ case is irregular.
- Characterise growth rates in $(\kappa, \lambda)$ — is $\xi\approx 2.32$ the threshold from countably-many to uncountably-many realisable growth rates?
- Topology of intervals in the permutation containment poset $\mathcal{P}$: are "nice" intervals shellable / homotopy-equivalent to wedges of spheres? Connection to the Möbius function via reduced Euler characteristic.

## Key terms
permutation patterns, Stanley-Wilf conjecture, Stanley-Wilf limit, 1324-avoiding permutations, Marcus-Tardos theorem, layered patterns, Wilf equivalence, Möbius function, permutation poset, growth rates, permutation classes, mesh patterns, vincular patterns, ascent sequences, (2+2)-free posets, insertion encoding, separable permutations, shellability, Bóna, Vatter, Steingrímsson
