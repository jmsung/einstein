---
type: source
kind: paper
title: Hypergraph containers
authors: D. Saxton, A. Thomason
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.6595
source_local: ../raw/2012-saxton-hypergraph-containers.pdf
topic: general-knowledge
cites:
---

# Hypergraph containers

**Authors:** D. Saxton, A. Thomason  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.6595

## One-line
For every $r$-uniform hypergraph $G$, there is a small family $\mathcal{C}$ of "containers" (vertex subsets) such that every independent set is contained in some $C \in \mathcal{C}$, with each container itself only mildly large — turning many extremal/counting problems into routine union-bound arguments.

## Key claim
Every $r$-graph $G$ on $n$ vertices of average degree $d$ admits a container family with $\log|\mathcal{C}| \lesssim c_d n$ where $c_d \approx d^{-1/(r-1)}$, constructed algorithmically. Consequences include: simple $r$-graphs satisfy $\chi_\ell(G) \ge (1/(r-1)^2 + o(1))\log_r d$ (tight for $r=2$, improving Alon); for any $\ell$-graph $H$, $H$-free $\ell$-graphs on $[N]$ lie in $\mathcal{C}$ with $\log|\mathcal{C}| \le c N^{\ell-1/m(H)}\log N$ where $m(H) = \max_{H'\subset H}(e(H')-1)/(v(H')-\ell)$.

## Method
A short greedy algorithm operating on a hypergraph $G$ and its co-degree function $\delta(G,\tau)$: vertices are admitted into a "fingerprint" set $T$ based on degree-relative-to-co-degree thresholds, and the container $C(T)$ is determined deterministically from $T$ alone. Because $T$ is small ($\sum |T_i| \le c n^{\ell-1/m(H)}$) and $C$ is a function of $T$, the number of distinct containers is small. The argument is unified across regular/non-regular $r$-graphs, unlike Sapozhenko's earlier graph-only construction.

## Result
- List chromatic bound: $\chi_\ell(G) \ge (1/(r-1)^2 + o(1))\log_r d$ for simple $r$-graphs, tight for $r=2$.
- $H$-free counting: $|\{H\text{-free } \ell\text{-graphs on }[N]\}| = 2^{(\pi(H)+o(1))\binom{N}{\ell}}$ (Corollary 2.4), recovering Erdős–Kleitman–Rothschild / Nagle–Rödl–Schacht.
- $C_4$-free graphs: at most $2^{(300+o(1))N^{3/2}}$ on $[N]$.
- Sidon sets: between $2^{(1.16+o(1))\sqrt{n}}$ and $2^{(55+o(1))\sqrt{n}}$.
- Sparse random / KŁR: counting version of the KŁR conjecture, plus solution-free counts for abundant linear systems $Ax=b$: at most $2^{\mathrm{ex}(F,A,b)+o(|F|)}$.

## Why it matters here
General background; no direct arena tie — but provides the canonical framework for *counting* extremal configurations and for transferring extremal results to sparse random settings, which underlies the random-discrete-structures program (Conlon–Gowers, Schacht). Touches Sidon sets (additive combinatorics, distantly related to autocorrelation problems) and $H$-free counting (relevant if extremal-graph counting ever enters an arena problem).

## Open questions / connections
- Conjectured tightness of the regular-$r$-graph list-chromatic bound $\chi_\ell(G) \ge (1/(r-1)+o(1))\log_r d$ for general (non-simple) $r$-graphs (§8, §12).
- A "single-pass" absolute-threshold variant of the algorithm (§12) yields the online property for all $r$-graphs, not just simple ones — promised in [57], unpublished here.
- Independent parallel development by Balogh–Morris–Samotij (arXiv:1204.6530) — comparing the two methods and their relative strengths is open.
- Whether $|C|$-type and $e(C)$-type container conclusions can be unified beyond the two-variant packaging in Theorems 3.7 / 3.6.

## Key terms
hypergraph containers, independent sets, list chromatic number, choice number, $H$-free graphs, KŁR conjecture, Sidon sets, sum-free sets, Cameron–Erdős conjecture, supersaturation, Erdős–Simonovits stability, Sapozhenko, balanced hypergraph parameter $m(H)$, abundant linear systems, sparse random graphs
