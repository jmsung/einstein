---
type: source
kind: paper
title: Bounds for graph regularity and removal lemmas
authors: D. Conlon, J. Fox
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1107.4829
source_local: ../raw/2011-conlon-bounds-graph-regularity-removal.pdf
topic: general-knowledge
cites:
---

# Bounds for graph regularity and removal lemmas

**Authors:** D. Conlon, J. Fox  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1107.4829

## One-line
Establishes tight lower bounds (tower-type, wowzer-type, and $2^{\Omega(\epsilon^{-2})}$) for the number of parts required in Szemerédi's regularity lemma, the strong regularity lemma, and the Frieze–Kannan weak regularity lemma, while giving an improved tower-type proof of the induced graph removal lemma.

## Key claim
For Szemerédi regularity, $M(\epsilon,\delta,\eta)$ grows as a tower of twos of height $\Theta(\eta^{-1})$ (resolving Gowers's question on irregular pairs); the strong regularity lemma requires wowzer-type parts; the Frieze–Kannan weak regularity lemma requires $2^{\Omega(\epsilon^{-2})}$ parts (matching the upper bound, solving a Lovász–Szegedy problem); the induced graph removal lemma admits a tower-of-height-poly$(\epsilon^{-1})$ bound, improving the prior wowzer-type bound.

## Method
Lower bounds use randomized iterated partition constructions: a nested sequence $P_1 \supset \dots \supset P_s$ of refinements with random bipartite graphs $G_i$ between parts of $P_i$ controlling irregular-pair counts (improving on Gowers's deterministic construction). The induced-removal upper bound is obtained via a new "strong cylinder regularity lemma" built on the Duke–Lefmann–Rödl weak cylinder regularity lemma, bypassing the strong regularity lemma entirely. Weak regularity lower bound uses random $\pm\alpha$-perturbations of constant matrices with Chernoff/Hoeffding–Azuma concentration.

## Result
Theorem 1.1: graph with $\geq ck^2/\log^* k$ irregular pairs in any $k$-part partition ($\epsilon = 1/2$, $\delta = 2^{-500}$, $c = 2^{-700}$). Theorem 1.2/Cor 1.2: wowzer in $\Omega(\epsilon^{-1/7})$ lower bound for strong regularity. Theorem 1.3: induced graph removal with $\delta^{-1}$ a tower in $h$ of height poly$(\epsilon^{-1})$. Theorem 1.4: $k(\epsilon) \geq 2^{2^{-60}\epsilon^{-2}}$ for $0 < \epsilon \leq 2^{-50}$ in Frieze–Kannan.

## Why it matters here
General background; no direct arena tie — this is foundational extremal combinatorics on regularity / removal bounds, relevant if the agent encounters problems framed via Szemerédi regularity or property testing (e.g., extremal graph theory subset of the 23 problems), but no current arena problem in scope depends on these specific bounds.

## Open questions / connections
- Tight bound for graph removal lemma: gap remains between tower-of-height-$O(\log \epsilon^{-1})$ upper (Fox 2011) and $\epsilon^{-O(\log \epsilon^{-1})}$ lower.
- Largest single $\epsilon$-regular subset in any graph: conjectured single-exponential in $\epsilon^{-1}$; current bounds are tower (upper) vs $\epsilon^{c\epsilon^{-1}}$ (lower, Peng–Rödl–Ruciński).
- Stable graphs (Malliaris–Shelah): no-half-graph forbidden induced subgraph yields polynomial-in-$\epsilon^{-1}$ regularity with no irregular pairs — connects model-theoretic stability to regularity bounds.

## Key terms
Szemerédi regularity lemma, strong regularity lemma, Frieze–Kannan weak regularity, induced graph removal lemma, irregular pairs, tower function, wowzer function, Ackermann hierarchy, mean square density, Duke–Lefmann–Rödl cylinder regularity, Gowers lower bound, half-graph, property testing, Conlon, Fox
