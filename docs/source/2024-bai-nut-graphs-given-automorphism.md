---
type: source
kind: paper
title: Nut graphs with a given automorphism group
authors: Nino Bašić, Patrick W. Fowler
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.04117v1
source_local: ../raw/2024-bai-nut-graphs-given-automorphism.pdf
topic: general-knowledge
cites: 
---

# Nut graphs with a given automorphism group

**Authors:** Nino Bašić, Patrick W. Fowler  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2405.04117v1

## One-line
Proves that every finite group is the automorphism group of infinitely many nut graphs, and of infinitely many $d$-regular nut graphs for $d \in \{8,12,16,20,24\}$.

## Key claim
**Theorem 1:** For every finite group $\mathcal{G}$, there exist infinitely many finite (regular) nut graphs $G$ with $\mathrm{Aut}(G) \cong \mathcal{G}$. **Theorem 2:** The same holds within the class of $d$-regular nut graphs for $d \in \{8,12,16,20,24\}$. Establishes nut graphs as an $f$-universal class in Babai's sense.

## Method
Constructive: start from Sabidussi's $d$-regular graph $H$ realising $\mathcal{G}$, apply the triangle-multiplier $M_3(H)$ (Proposition 4) to produce a nut graph that inherits $\mathrm{Aut}(H)$ plus extra triangle-swap automorphisms $\beta_{i,j}, \gamma_i$. Strip the extras via coalescence (Lemma 3 of Sciriha) with carefully chosen asymmetric "gadget" nut graphs $Q_i$ attached at the degree-2 triangle vertices; orbit-distinct roots prevent reintroduction of symmetry. Infinite families come from the 4-subdivision construction.

## Result
For $|\mathcal{G}|>1$ the nut graph has order $19|V(H)|$ (Theorem 1) or $\omega(d)|V(H)|$ with $\omega(8){=}53, \omega(12){=}99, \omega(16){=}161, \omega(20){=}241, \omega(24){=}337$ (Theorem 2). Census data shows much smaller minima exist: e.g. $G_{288}$ has minimal nut-graph order 10 vs the construction's 109,440. Tabulates $\beta(\mathcal{G})$ vs $\alpha(\mathcal{G})$ for groups of order $\leq 6$.

## Why it matters here
General background; no direct arena tie. Nut graphs are a niche spectral-graph topic (nullity 1, full kernel eigenvector) tied to chemical Hückel theory, not to the sphere-packing / autocorrelation / kissing-number / extremal-graph families on Einstein Arena. Possible weak connection to extremal/spectral graph problems via the eigenvector positivity constraint.

## Open questions / connections
- Problem 7: upper bound on $\beta(\mathcal{G})$ (minimum nut-graph order realising $\mathcal{G}$) in terms of $|\mathcal{G}|$, analogous to Babai/Deligeorgaki bounds $\alpha(\mathcal{G}) \leq |\mathcal{G}|$.
- Problem 8: extend Theorem 2 to all $d \geq 3$, especially $d=3$ (cubic chemical graphs, fullerenes) and $d \not\equiv 0 \pmod 4$.
- Frucht's classical cubic construction fails to yield nut graphs — a direct cubic-nut-graph construction remains open.

## Key terms
nut graph, graph automorphism, $f$-universal, Sabidussi theorem, Frucht theorem, triangle-multiplier construction, coalescence construction, adjacency matrix nullity, kernel eigenvector, regular graph, chemical graph, fullerene, spectral graph theory, Hückel theory
