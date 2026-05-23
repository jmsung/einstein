---
type: source
kind: paper
title: A note on the random greedy independent set algorithm
authors: Patrick Bennett, T. Bohman
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1308.3732
source_local: ../raw/2013-bennett-note-random-greedy-independent.pdf
topic: general-knowledge
cites:
---

# A note on the random greedy independent set algorithm

**Authors:** Patrick Bennett, T. Bohman  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1308.3732

## One-line
Generalizes the H-free process analysis to arbitrary $D$-regular $r$-uniform hypergraphs, lower-bounding the size of the maximal independent set produced by the random greedy algorithm.

## Key claim
For a $D$-regular $r$-uniform hypergraph $H$ on $N$ vertices with $D > N^\epsilon$, bounded sub-degrees $\Delta_\ell(H) < D^{(r-\ell)/(r-1)-\epsilon}$ for $\ell=2,\dots,r-1$, and bounded $(r-1)$-codegree $\Gamma(H) < D^{1-\epsilon}$, the random greedy independent-set algorithm w.h.p. produces an independent set of size $|I| = \Omega\big(N \cdot ((\log N)/D)^{1/(r-1)}\big)$.

## Method
Differential-equations method for dynamic concentration: parametrize time by $t = (D^{1/(r-1)}/N)\cdot i$ and track $|V(i)|$ and the residual-edge degrees $d_\ell^\pm(v)$ against their idealized trajectories under the binomial heuristic $\Pr[v \in S(i)] = i/N$. Variation equations on error functions $f_\ell, f_v$ make the deviation sequences $Z_V, Z_\ell^\pm$ supermartingales; Hoeffding-type concentration (Lemmas 4.4–4.5) then bounds the failure probability by $\exp(-N^{\Omega(1)})$. A second-moment / Wolfovitz argument (Lemma 5.1, Theorem 1.2) extends to subgraph counts.

## Result
Independent set of size $\Omega(N(\log N/D)^{1/(r-1)})$ with probability $1 - \exp(-N^{\Omega(1)})$. Theorem 1.2: any "compatible" auxiliary $s$-uniform hypergraph $G$ has $X_G(i) = |G|p^s(1+o(1))$ copies inside $I(i)$, where $p = i/N$. Corollary 3.1 yields Turán-type lower bounds $\mathrm{ex}(n,H) = \Omega\big(n^{k-(v_H-k)/(e_H-1)}(\log n)^{1/(e_H-1)}\big)$ for strictly $k$-balanced $k$-uniform $H$ with no degree-1 vertex. Corollary 2.1: the $k$-AP-free process on $\mathbb{Z}_N$ produces $I$ with $\|\nu_I - 1\|_{U^d} = o(1)$ for $2^{d-1} = k-1$, proving $s(k) > 1 + \log_2(k-1)$ for the Gowers-norm question.

## Why it matters here
Directly relevant to autocorrelation / Sidon-like and combinatorial-packing problems on Einstein Arena — the random-greedy lower bound and its subgraph-count companion give baseline existence results for sparse structures (independent sets, $H$-free configurations, $k$-AP-free subsets) when only degree/codegree control is available. Anchors the wiki's treatment of probabilistic / nibble methods and connects to LP-bound / extremal-graph framings.

## Open questions / connections
- Is the lower bound $\Omega(N(\log N/D)^{1/(r-1)})$ tight for a broad hypergraph class? Bohman–Keevash conjecture this for strictly 2-balanced $H$-free processes; open beyond $K_3$, $K_4$, $C_\ell$.
- Self-correcting / critical-interval methods (Telcs–Wormald–Zhou; Bohman–Frieze–Lubetzky) are deliberately not used here — sharper constants/lower-order terms remain accessible via that route.
- Conditions fail for diamond-free (Picollelli) and sum-free (Bennett) processes, yet the bound still holds — what is the right relaxation of the codegree hypothesis?
- Does the Gowers $s(k) > 1 + \log_2(k-1)$ lower bound for arithmetic-progression detection match the true threshold?

## Key terms
random greedy algorithm, independent set, hypergraph, H-free process, differential equations method, dynamic concentration, supermartingale, Bohman–Keevash, Turán number, strictly k-balanced, k-AP-free process, Gowers uniformity norm, codegree condition, Hoeffding inequality, Wormald, Ajtai–Komlós–Pintz–Spencer–Szemerédi
