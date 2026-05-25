---
type: source
kind: paper
title: "Fully Dynamic Electrical Flows: Sparse Maxflow Faster Than Goldberg-Rao"
authors: Yu Gao, Yang P. Liu, Richard Peng
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.07233
source_local: ../raw/2021-gao-fully-dynamic-electrical-flows.pdf
topic: general-knowledge
cites:
---

# Fully Dynamic Electrical Flows: Sparse Maxflow Faster Than Goldberg-Rao

**Authors:** Yu Gao, Yang P. Liu, Richard Peng  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.07233

## One-line
First exact maxflow algorithm to break the $O(m^{3/2}\log U)$ Goldberg-Rao barrier on sparse directed graphs with polynomially bounded capacities.

## Key claim
Computes exact $s$-$t$ maximum flow on a graph with $m$ edges and integer capacities in $[1,U]$ in time $\tilde O(m^{3/2 - 1/328}\log U)$ — the first improvement over Goldberg-Rao 1998 in the weakly polynomial sparse regime.

## Method
Wraps Mądry's interior-point method (IPM) for maxflow with dynamic data structures that maintain $s$-$t$ electrical flows under slowly changing edge resistances. A two-level Locator/Checker pair detects edges carrying $\ge \epsilon^2$ fraction of total electric energy: the Locator uses an $\ell_2$ heavy-hitter sketch combined with random-walk-based projections onto a growing terminal set $C$ and spectral vertex sparsifiers (Schur complements), while the Checker independently re-estimates candidate-edge energies to defeat adaptive-adversary leakage between IPM iterations. The IPM is modified to take batched $s$-$t$-only steps (no circulations) with damped step size $k^{-3}/\sqrt m$, recentering every $k = m^{1/328}$ iterations.

## Result
Theorem 1: $\tilde O(m^{2 - 3/328}\log U) = \tilde O(m^{3/2 - 1/656}\log U)$-time exact maxflow (paper's stated exponent $2 - 3/328$). Key structural lemma: over $T$ IPM steps of size $1/\sqrt m$, at most $O(T^2 \gamma^{-2})$ edges have resistance change exceeding $1 \pm \gamma$ multiplicatively (Lemma 6.6) — so on average each edge's resistance changes $O(1)$ times across the $\sqrt m$ iterations, justifying amortized-sublinear updates. Heuristic tradeoff: $\tilde O(m^{1-\eta} k^2)$ data-structure work per batch $\times$ $\sqrt m / k$ batches plus $\tilde O(m \cdot \sqrt m / k)$ recentering, optimized at $k = m^{\eta/2}$.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems in this wiki are continuous geometric/extremal optimization (sphere packing, autocorrelation, kissing); discrete network-flow IPMs do not appear in any of the 23 problem statements. The only loose conceptual transfer is the *dynamic-data-structure-inside-IPM* pattern and the Schur-complement / random-walk vertex sparsifier toolkit — neither currently used by the agent.

## Open questions / connections
- Can the robust central-path / weighted-barrier techniques of [BLN+20, BLL+21] (used for the $\tilde O(m + n^{3/2})$ dense-graph runtime) be combined with this dynamic sparsifier to push the exponent further?
- Does opening up the $\ell_2$ heavy-hitter primitive (Lemma 5.1) so an approximate matrix-vector product suffices generalize to other sketching-inside-optimization settings?
- Pseudo-deterministic adaptive-adversary handling via Locator/Checker separation — does the same trick apply to other randomized graph data structures used inside iterative optimizers?

## Key terms
maximum flow, interior point method, electrical flow, Laplacian solver, Schur complement, spectral vertex sparsifier, $\ell_2$ heavy hitter sketch, random walk projection, dynamic graph data structure, adaptive adversary, Goldberg-Rao, Mądry, augmenting electric flow, central path, Johnson-Lindenstrauss
