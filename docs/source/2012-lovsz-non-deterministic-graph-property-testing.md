---
type: source
kind: paper
title: Non-Deterministic Graph Property Testing
authors: L. Lovász, K. Vesztergombi
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1202.5337
source_local: ../raw/2012-lovsz-non-deterministic-graph-property-testing.pdf
topic: general-knowledge
cites:
---

# Non-Deterministic Graph Property Testing

**Authors:** L. Lovász, K. Vesztergombi  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1202.5337

## One-line
Proves that any dense-graph property whose certificate (a node/edge coloring) is testable by random local sampling is itself directly testable — a "P = NP" theorem for dense-graph property testing.

## Key claim
**Theorem 1.1:** A graph property $P$ is nondeterministically testable if and only if it is testable. Equivalently, if $P = Q'$ for some testable property $Q$ of $k$-colored digraphs (where $Q'$ is the "shadow" projection forgetting colors/orientation), then $P$ is testable in the usual oblivious sense.

## Method
Uses the graph-limits framework (graphons, digraphons, $k$-digraphons) of Lovász–Szegedy and Borgs–Chayes–Lovász–Sós–Vesztergombi. Key technical lemma (3.2): given a sequence $F_n \to U$ of simple graphs converging to the "shadow" of a $k$-digraphon $W$, one can lift each $F_n$ to a $k$-colored digraph $J_n$ with $J_n' = F_n$ and $J_n \to W$. The lift is built via averaged conditional weights $\beta_h(i,j)$ and randomized rounding (Lemma 3.1 controls cut-norm error by $O(k/\sqrt{n})$); convergence in cut norm uses Frieze–Kannan cut norm $\|\cdot\|_\square$ and a key bilinear bound (Prop. 2.3). The characterization of testability via $\delta_\square \to 0 \Rightarrow d_1 \to 0$ (Prop. 2.6) closes the argument.

## Result
Establishes Theorem 1.1 nonconstructively (no explicit sample-size bound). Corollaries: (4.1) max-cut $\geq c|V|^2$ is testable; (4.2) any property expressible as $\exists S_1 \dots \exists S_c \exists x_1 \dots \exists x_a \forall y_1 \dots \forall y_b \Phi$ with $S_i$ ranging over unary/binary relations is testable — a strict generalization of the Alon–Fischer–Krivelevich–Szegedy first-order condition; (4.3) upward closure of any testable property is testable; (4.4) "within $|V|^2/100$ edits of $P$" is testable. Theorem 5.1 gives the parameter-estimation analogue: $g'(G) = \max\{g(L): L' = G\}$ is estimable whenever $g$ is. Result fails for bounded-degree graphs (expander vs. 2× expander counterexample).

## Why it matters here
General background for the extremal-graph / property-testing corner of the arena (e.g., problems involving graph density, max-cut, $k$-colorability, or hereditary-style certificates); the "lift via graphon + randomized rounding" pattern is a candidate tool whenever a problem's optimum admits a low-information combinatorial certificate. No direct arena tie to the current 23 problems.

## Open questions / connections
- Effective (quantitative) version of Theorem 1.1 with explicit sample-size bounds — current proof is pure existence.
- Extension to hypergraphs (Elek–Szegedy limits) — auxiliary tools not yet generalized.
- Extension to compact-decorated graphs (e.g., threshold graphs certified by $[0,1]$-valued node labels) — limit theory exists [15], lifting argument plausibly extends.
- Bounded-degree analogue is FALSE (expander counterexample), highlighting that the dense-graph regularity machinery is essential.

## Key terms
property testing, graph limits, graphon, digraphon, $k$-colored digraph, cut norm, Frieze-Kannan, cut distance $\delta_\square$, edit distance, oblivious testing, nondeterministic certificate, Lovász, Szegedy, Alon-Shapira, hereditary property, max-cut testability, randomized rounding, regularity lemma, dense graphs
