---
type: source
kind: paper
title: Connected Baranyai’s theorem
authors: Amin Bahmanian
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.09643
source_local: ../raw/2014-bahmanian-connected-baranyai-theorem.pdf
topic: general-knowledge
cites:
---

# Connected Baranyai's theorem

**Authors:** Amin Bahmanian  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1909.09643

## One-line
Strengthens Baranyai's hypergraph factorization theorem by showing the factors can additionally be required to be connected, settling a question of Katona.

## Key claim
$\lambda K_n^h$ admits an $(r_1,\dots,r_k)$-factorization iff $h \mid r_i n$ for each $i$ and $\sum_i r_i = \lambda\binom{n-1}{h-1}$; moreover every factor with $r_i \ge 2$ can be taken connected.

## Method
Vertex-amalgamation / detachment technique: start from a single vertex with $\lambda\binom{n}{h}$ $h$-loops colored to match the degree budget, then iteratively split (detach) one vertex into two, distributing incident hinges via a Nash-Williams laminar-family lemma so that degree, multiplicity, and connectivity invariants are preserved. Connectivity is enforced via Lemma 2.1: in each $\alpha$-wing of color $i$ with $d_W(\alpha)\ge 2$, at least one but not all hinges go to the new vertex $\beta$.

## Result
Theorem 1.2 establishes the connected $(r_1,\dots,r_k)$-factorization of $\lambda K_n^h$ under exactly the obvious necessary divisibility/sum conditions. Corollaries: $K_n^h$ has a connected $2$-factorization iff $\binom{n-1}{h-1}$ is even and $h\mid 2n$; and $K_n^h$ always has a connected $\gcd(\binom{n-1}{h-1},h)$-factorization. Specializes to Walecki's Hamiltonian decomposition of $K_n$ when $h=2$, $\lambda=1$, $r_i=2$.

## Why it matters here
General background; no direct arena tie. Hypergraph factorization / Baranyai-style decomposition is adjacent to combinatorial design problems but the 23 Einstein Arena problems (sphere packing, autocorrelation, kissing, Sidon, etc.) don't currently invoke uniform hypergraph factorization machinery.

## Open questions / connections
- Baranyai–Katona conjecture: can $E(K_n^h)$ be decomposed into disjoint wreaths? (Still open; this paper sidesteps via connectivity rather than resolving it.)
- Extends Nash-Williams amalgamation [12] and Johnson [9] from graphs to hypergraphs.
- Whether the detachment technique can enforce structural properties beyond connectivity (girth, diameter, edge-connectivity).

## Key terms
Baranyai's theorem, hypergraph factorization, connected factorization, edge-coloring, detachment, amalgamation, laminar family, Nash-Williams lemma, $\alpha$-wing, Hamiltonian decomposition, Walecki, Katona, complete uniform hypergraph, wreath decomposition
