---
type: source
kind: paper
title: Ramanujan graphs
authors: A. Lubotzky, R. Phillips, P. Sarnak
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.06558
source_local: ../raw/2017-lubotzky-ramanujan-graphs.pdf
topic: general-knowledge
cites:
---

# Ramanujan graphs

**Authors:** A. Lubotzky, R. Phillips, P. Sarnak  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.06558

## One-line
A short expository note explaining what Ramanujan graphs are, why they are named after Ramanujan, and how their construction reduces to the Ramanujan–Petersson conjecture via $p$-adic representation theory.

## Key claim
A finite connected $k$-regular graph $X$ is Ramanujan iff every adjacency eigenvalue $\lambda$ satisfies $|\lambda|=k$ or $|\lambda|\le 2\sqrt{k-1}$; this bound is optimal (Alon–Boppana) because $[-2\sqrt{k-1},2\sqrt{k-1}]$ is exactly the spectrum of the adjacency operator on the universal cover $T_k$ (Kesten).

## Method
Survey/expository. Connects the spectral condition to representation theory: for $G=\mathrm{PGL}_2(\mathbb{Q}_p)$ acting on its Bruhat–Tits tree $T_{p+1}$, $X=\Gamma\backslash T$ is Ramanujan iff every infinite-dim $K$-spherical sub-representation of $L^2(\Gamma\backslash G)$ is tempered. Existence then follows from Deligne's proof of Ramanujan–Petersson plus Jacquet–Langlands (LPS/Margulis), or non-constructively from interlacing families (Marcus–Spielman–Srivastava).

## Result
Recovers the LPS/Margulis construction of infinite families of $(q+1)$-regular Ramanujan graphs for $q$ prime, and cites MSV (2015) for bipartite Ramanujan graphs of every degree $k\ge 3$. Records the Cheeger–spectral inequality $h(X)^2/(2k)\le k-\lambda_1(X)\le 2h(X)$ tying Ramanujan-ness to optimal expansion, and notes Ihara/Sunada's reformulation: $X$ is Ramanujan iff its Ihara zeta function satisfies the Riemann hypothesis.

## Why it matters here
General background; no direct Einstein Arena tie. Provides reference framing for extremal-graph / expander problems and for spectral-bound thinking (Alon–Boppana, Cheeger) that may inform discrete combinatorics or graph-density problems in the inventory.

## Open questions / connections
- Are random $k$-regular graphs Ramanujan? (Known to be expanders; Ramanujan-ness open.)
- Higher-dimensional analogues: Ramanujan complexes from $\mathrm{GL}_d$ generalizations of RP.
- Extends Lubotzky–Phillips–Sarnak (Combinatorica 1988) and Margulis (1988); MSV (2015) gives existence at every degree but no explicit construction.

## Key terms
Ramanujan graph, expander graph, Alon–Boppana bound, Cheeger constant, Kesten spectrum, $k$-regular tree, Bruhat–Tits building, Ramanujan–Petersson conjecture, Hecke eigenform, tempered representation, Jacquet–Langlands, Ihara zeta function, Lubotzky, Sarnak, Margulis, Deligne
