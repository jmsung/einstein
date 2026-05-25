---
type: source
kind: paper
title: Generation and properties of nut graphs
authors: K. Coolsaet, P. Fowler, J. Goedgebeur
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.04254
source_local: ../raw/2017-coolsaet-generation-properties-nut-graphs.pdf
topic: general-knowledge
cites:
---

# Generation and properties of nut graphs

**Authors:** K. Coolsaet, P. Fowler, J. Goedgebeur  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.04254

## One-line
Exhaustive computer-generation of nut graphs (graphs with nullity 1 and a zero-free kernel eigenvector), extending known catalogues and tabulating chemical properties of the kernel eigenvector.

## Key claim
New canonical-construction algorithm enumerates all nut graphs up to $n=13$, all chemical nut graphs up to $n=22$, all cubic-polyhedral nut graphs up to $n=34$, and all nut fullerenes up to $n=250$; proves every chemical nut graph satisfies $r \geq 2$ (ratio of max to min $|$kernel entry$|$), with $r=2$ attained for every $n \geq 9$ except $n=10$.

## Method
Canonical construction path (McKay) augmented with two algebraic filters from Theorem 2.1: keep order-$(n-1)$ parents only if $B$ is non-singular (cache $B^{-1}$), then accept the child of order $n$ iff $bB^{-1}b^T=0$ and $bB^{-1}$ is zero-free. To avoid floating-point ambiguity in detecting zeros, rank and adjugate are computed modulo several primes $p \lesssim 2^{31}$ and CRT-lifted via Hadamard's bound $\Delta_n \leq 2^{-n}(n+1)^{(n+1)/2}$. Integrated with `geng`, `plantri`, and `buckygen`.

## Result
Nut-graph counts grow rapidly: $3, 13, 560, 12\,551, 2\,060\,490, 208\,147\,869, 96\,477\,266\,994$ for $n=7,\dots,13$. Only $173$ of the $\sim2.16 \times 10^{10}$ fullerene isomers up to $n=250$ are nut graphs; no IPR-nut-fullerene exists up to $n=320$. Theorem 3.1: any chemical nut graph has $r^2 \geq 4$ (from a degree-3 vertex with kernel entries $\{1,x,-1-x\}$). Theorem 3.2: $P_4$-insertion on an edge preserves nut status and $r$, so $r=2$ propagates to all $n\geq 9$, $n\neq 10$.

## Why it matters here
General background; no direct arena tie. Closest touch is the modular-arithmetic / CRT trick for exact rank detection on integer matrices, which is a useful template whenever an einstein workload needs to certify singularity / nullspace structure without float-precision hazards (echoes the `triple-verify` rule and the kind of integer/rational pitfalls flagged in `findings/sdp-relaxation-uselessness`).

## Open questions / connections
- No known lower bound on the smallest nonzero eigenvalue of a 0–1 adjacency matrix that would let plain float eigensolvers safely classify nut graphs.
- Extends Sciriha–Gutman (1998) and Fowler et al. (2014); fullerene counts piggyback on Brinkmann–Goedgebeur–McKay generators.
- Open: characterise $r$-distribution at scale; classify uniform vs balanced vs "just" cubic nuts; explain near-absence of IPR nut fullerenes below $n=320$.

## Key terms
nut graph, nullity 1, kernel eigenvector, adjacency matrix rank, Hadamard determinant bound, modular arithmetic CRT, canonical construction path, McKay isomorph-free generation, fullerene enumeration, cubic polyhedral graph, Hückel theory non-bonding orbital, source-and-sink-potential, omniconductor, chemical graph
