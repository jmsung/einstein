---
type: source
kind: paper
title: On MAXCUT in strictly supercritical random graphs, and coloring of random graphs and random tournaments
authors: Lior Gishboliner, Michael Krivelevich, Gal Kronenberg
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.04044
source_local: ../raw/2016-gishboliner-maxcut-strictly-supercritical-random.pdf
topic: general-knowledge
cites:
---

# On MAXCUT in strictly supercritical random graphs, and coloring of random graphs and random tournaments

**Authors:** Lior Gishboliner, Michael Krivelevich, Gal Kronenberg  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.04044

## One-line
Determines that the distance-to-bipartiteness of $G(n, (1+\varepsilon)/n)$ in the strictly supercritical regime is $\Theta(\varepsilon^3)n$, resolving a Coppersmith–Gamarnik–Hajiaghayi–Sorkin conjecture, then applies this to settle a Frieze–Pegden odd-cycle homomorphism conjecture and to characterize coloring of biased random tournaments.

## Key claim
For fixed $\varepsilon \in (0,1)$ and $G \sim G(n, (1+\varepsilon)/n)$, w.h.p. $\mathrm{DistBP}(G) = |E(G)| - \mathrm{MAXCUT}(G) = \Theta(\varepsilon^3)n$. As corollaries: (i) for every $\varepsilon > 0$ there exists $\ell_\varepsilon = O(\varepsilon^{-3})$ such that w.h.p. $G$ has no homomorphism to $C_{2\ell+1}$ for any $\ell \geq \ell_\varepsilon$; (ii) the analogous statement holds for $p$-random tournaments — $\mathrm{DistTour\text{-}BP}(T) = \Theta(\varepsilon^3)n$.

## Method
Builds on the Ding–Lubetzky–Peres (2014) contiguity description of the giant component's 2-core as a random multigraph $K$ (with degrees i.i.d. Poisson$(\Lambda)$, $\Lambda \sim N(\lambda-\mu, 1/n)$) whose edges are replaced by i.i.d. Geom$(1-\mu)$ paths. Lower bound: a random partition leaves $\geq \tfrac{1}{2} - O(\varepsilon)$ of each path's edges in the same side, and odd-length paths force a monochromatic edge; counts give $\Omega(\varepsilon^3)n$. Upper bound: each path contributes $\leq 1$ to $\mathrm{DistBP}$, the expected fraction of odd-length paths is $\leq \tfrac{1}{2} - 8\varepsilon$, and $e(K) = (2\varepsilon^3 + O(\varepsilon^4))n$ via Poisson tail computation. Tournament case combines this with a backedge-graph argument using Vizing's theorem and a "long-backedge matching forces transitivity contradiction" lemma.

## Result
$\mathrm{DistBP}(G) = (c\varepsilon^3 + O(\varepsilon^4))n$ with $c \leq 1$ (and the authors note refinement to $c \leq 1/3$); the construction is algorithmic (polynomial-time cut achieving $e(G) - O(\varepsilon^3)n$). Tournament chromatic threshold for $k \geq 3$ is $\Theta((k\log k)/n)$, mirroring the $G(n,p)$ result of Achlioptas–Naor; 2-colorability has a coarse threshold at $p = c/n$.

## Why it matters here
General background; no direct arena tie. The MAXCUT-on-sparse-random-graph framing and the Ding–Lubetzky–Peres giant-component anatomy are relevant if any Einstein Arena problem reduces to extremal cuts / bipartiteness distance on $G(n, c/n)$-like structures, but no current problem in the wiki inventory matches.

## Open questions / connections
- Exact constant in $\mathrm{DistBP}(G) = (c\varepsilon^3 + O(\varepsilon^4))n$ — the authors conjecture $c = 1/3$.
- Minimal $\ell(\varepsilon)$ such that w.h.p. no homomorphism $G(n, (1+\varepsilon)/n) \to C_{2\ell+1}$ exists (their bound $O(\varepsilon^{-3})$ may be loose).
- Conjectured: the $k$-colorability threshold for $T(n,p)$ matches $G(n,p)$'s — proof needs $\mathrm{Dist}_{k\text{-col}}(G(n,c/n)) \geq C(k) n^{3/4}\log^{1/2} n$.
- Connects to Dembo–Montanari–Sen (2017) on extremal cuts; their large-$c$ asymptotic $\mathrm{MC}(c) = c/4 + \gamma\sqrt{c/4} + o(\sqrt c)$ with $\gamma \approx 0.7632$ (Parisi constant from spin-glass) is the dense-regime counterpart.

## Key terms
MAXCUT, distance to bipartiteness, sparse random graph $G(n,p)$, strictly supercritical regime, giant component 2-core, Ding–Lubetzky–Peres, Frieze–Pegden conjecture, odd-cycle homomorphism, biased random tournament, chromatic number threshold, Achlioptas–Naor, Parisi constant, Poisson cloning, Vizing edge coloring
