---
type: source
kind: paper
title: The large $N$ factorization does not hold for arbitrary multi-trace observables in random tensors
authors: Razvan Gurau, Felix Joos, Benjamin Sudakov
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2506.15362v1
source_local: ../raw/2025-gurau-large-factorization-does-not.pdf
topic: general-knowledge
cites: 
---

# The large $N$ factorization does not hold for arbitrary multi-trace observables in random tensors

**Authors:** Razvan Gurau, Felix Joos, Benjamin Sudakov  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2506.15362v1

## One-line
Disproves a standing conjecture by showing that Gaussian random tensors of order $D \geq 3$ do not satisfy the large-$N$ factorization of multi-trace expectations that random matrices ($D=2$) enjoy.

## Key claim
For $D \geq 3$, the Gaussian scaling of cumulants is *not* strictly subadditive: there exist connected edge-$D$-colored graphs $M_1,\dots,M_q$ whose joint connected expectation $\langle \mathrm{Tr}_{M_1}(T)\cdots\mathrm{Tr}_{M_q}(T)\rangle_{\mathrm{con.}}$ scales in $N$ *strictly higher* than $\prod_\rho \langle \mathrm{Tr}_{M_\rho}(T)\rangle$. Quantitatively, for $\epsilon>0$ and $n$ large enough (e.g. $n\sim 76$ at $D=3$), at least a $1-\epsilon$ fraction of edge-$D$-colored graphs on $2n$ vertices violate $\max_{M_0} F_n(M_0,M) > Dn/2$.

## Method
Probabilistic/counting argument over uniformly random edge-$D$-colored graphs (unions of $D$ independent uniform perfect matchings). The key technical lemma reduces factorization to the inequality $\max_{M_0}F_n(M_0,M) > Dn/2$ for every connected $M$ (via a boundary-graph construction that lifts component-wise matchings to global ones). A tail bound $\Pr[F_n(M_0,M)\geq t] \leq 7^n/(2n)^t$ on cycles in two random matchings (Markov + induction on $m^{F_n}$) then shows almost all $D$-colored graphs fail the inequality.

## Result
Theorem 1: for $D\geq 3$ and $n$ such that $(D-2)n/2 > (D\ln 7 - \ln 2)\ln n/n + D$, a $(1-\epsilon)$-fraction of edge-$D$-colored graphs on $2n$ vertices have a connected component $M_\rho$ with $\max_{M_0} F_{2n_\rho}(M_0, M_\rho\sqcup M_\rho) \geq Dn_\rho > 2\max F_{n_\rho}(M_0,M_\rho)$. Factorization *does* hold when restricted to melonic observables (the dominant family) for any $D$, and the bound $\max_{M_0}F_n(M_0,M) > n + n/2 + q$ holds for ribbon-planar $D=3$ graphs (though factorization itself is not established for the planar subfamily).

## Why it matters here
General background; no direct arena tie. Relevant only as cautionary context for any agent strategy that invokes large-$N$ free-probability heuristics on tensor-structured optimization landscapes — naive multi-trace factorization fails outside the melonic subfamily.

## Open questions / connections
- Which *other* restricted families beyond melonic (e.g. ribbon-planar $D=3$) actually satisfy factorization, not just the necessary scaling bound?
- Does a refined moments–cumulants relation (analog of free cumulants on non-crossing partitions) exist for tensors that captures the non-factorizing terms?
- Extends/refutes the Collins–Gurau–Lionni conjecture [arXiv:2410.00908] on Gaussian-tensor freeness; how must the proposed free-cumulant framework be modified?

## Key terms
random tensors, large $N$ limit, multi-trace factorization, Gaussian cumulants, melonic graphs, edge-colored graphs, perfect matchings, free probability, Wick contractions, ribbon-planar graphs, Gurau, SYK model
