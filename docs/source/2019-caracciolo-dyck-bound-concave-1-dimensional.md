---
type: source
kind: paper
title: The Dyck bound in the concave 1-dimensional random assignment model
authors: S. Caracciolo, Matteo D’Achille, Vittorio Erba, A. Sportiello
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.10867
source_local: ../raw/2019-caracciolo-dyck-bound-concave-1-dimensional.pdf
topic: general-knowledge
cites:
---

# The Dyck bound in the concave 1-dimensional random assignment model

**Authors:** S. Caracciolo, Matteo D'Achille, Vittorio Erba, A. Sportiello  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.10867

## One-line
Introduces and analyzes the "Dyck matching" — a deterministic, combinatorially-defined matching for random bipartite points on an interval — as a tractable upper bound for the 1D random Euclidean assignment problem with concave cost $|x-y|^p$, $0<p<1$.

## Key claim
The average cost of the Dyck matching has scaling $\mathbb{E}_N(H_{\text{Dyck}}) \asymp N$ for $0\le p<\tfrac12$, $\asymp N\ln N$ at $p=\tfrac12$, and $\asymp N^{1/2+p}$ for $\tfrac12<p\le 1$, universal across independent-spacing models (US, ES, PPP); conjectured to share the same scaling exponent (but not constant) as the optimal matching.

## Method
Exploits two structural lemmas: optimal matchings under concave cost are **non-crossing** and **sliced** (Lemmas 1–2), proven via the subadditivity inequality $(a+b)^p+(b+c)^p > (a+b+c)^p+b^p$ for $0<p<1$. The Dyck matching is canonically defined by pairing up/down steps within each excursion of the Dyck bridge encoding the red/blue color sequence $\sigma$. Combinatorial enumeration of edge lengths $v_{N,k}$ via generating functions + singularity analysis (Flajolet–Sedgewick) extracts the large-$N$ asymptotics; the ES case is resummed exactly via $_2F_1$ hypergeometrics and Gauss's inversion formula.

## Result
Explicit two-term expansion: $\mathbb{E}_N(H_{\text{Dyck}}) = \frac{2^p\Gamma(p-1/2)}{4\Gamma(p+1)} N^{1/2+p} + \frac{A_p}{2}N + \ldots$ with $A_p^{\text{ES}} = \frac{\Gamma(1/2-p)\Gamma(p+1)}{2^{p-1}\sqrt{\pi}\Gamma(2-p)}$; logarithmic correction at $p=1/2$: $\frac{1}{\sqrt{2\pi}}N\log N + A^*N/2 + \tilde A^*N$ with $\tilde A^* = \frac{\gamma_E+2\log 2-2}{\sqrt{2\pi}}$. PPP reduces to ES via Poissonization (Lemma 4) with relative error $O(N^{-1})$. Edge-length distribution exhibits universal $k^{-3/2}$ tail (planar-secondary-structure exponent).

## Why it matters here
General background for 1D Euclidean optimization with concave cost — informs the [[non-crossing-matchings]] concept and singularity-analysis technique. No direct Einstein Arena problem tie, but the non-crossing/sliced structural lemmas and the generating-function+singularity-analysis method are reusable for any 1D matching/packing problem; the Dyck-matching idea (deterministic combinatorial proxy as upper bound) is a transferable trick.

## Open questions / connections
- Conjecture 1: do $\mathbb{E}_N(H_{\text{opt}})$ and $\mathbb{E}_N(H_{\text{Dyck}})$ share the same scaling exponent? Proof would need a matching lower bound on $H_{\text{opt}}$.
- Extension to Gamma-distributed spacings $\alpha g_\alpha(\alpha s)$ for half-integer $\alpha$ (yields $_kF_{k-1}$ generating functions; US is $\alpha\to\infty$ limit).
- Ground-state degeneracy at $p=1$ and cycle decomposition of optimal matchings remain open.
- Connection to RNA secondary structure folding (planar matchings, glassy phases) — same $k^{-3/2}$ universal tail.

## Key terms
random assignment, concave cost, non-crossing matching, sliced matching, Dyck path, Dyck bridge, Catalan numbers, Poisson point process, exponential spacings, singularity analysis, hypergeometric function, generating functions, Caracciolo, Sportiello, RNA secondary structure, 1D Euclidean matching
