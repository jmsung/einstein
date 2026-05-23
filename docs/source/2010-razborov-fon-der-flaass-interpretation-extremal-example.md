---
type: source
kind: paper
title: On the Fon-der-Flaass Interpretation of Extremal Examples for Turan's (3,4)-problem
authors: Alexander Razborov
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1008.4707v1
source_local: ../raw/2010-razborov-fon-der-flaass-interpretation-extremal-example.pdf
topic: general-knowledge
cites: 
---

# On the Fon-der-Flaass Interpretation of Extremal Examples for Turan's (3,4)-problem

**Authors:** Alexander Razborov  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1008.4707v1

## One-line
Razborov uses flag algebras to push the Fon-der-Flaass construction's edge-density lower bound from $3/7$ toward the conjectured optimal $4/9$ for Turán's (3,4)-problem, achieving $7/16$ unconditionally and $4/9$ under mild structural assumptions.

## Key claim
For any $C_4$-free orgraph $\Gamma$, the 3-graph $\mathrm{FDF}(\Gamma)$ has edge density $\geq 7/16(1-o(1))$ unconditionally, and $\geq 4/9(1-o(1))$ whenever (a) $\Gamma$ orients a complete multipartite graph, or (b) the underlying graph density is $\geq 2/3 - \epsilon$ for an absolute $\epsilon > 0$.

## Method
Flag-algebra calculus in theories $T_{\text{FDF}}$ (C4-free orgraphs), $T_{\text{Graph}}$, and Z3-colored extensions $T^*_{\text{FDF}}$. The $7/16$ bound combines Goodman's triangle inequality with the Lovász–Simonovits–Fisher optimal triangle bound $\delta_{K_3} \leq \delta_\rho + \tfrac{\sqrt 6}{3}\delta_\rho^{3/2}$ via "tangential coordinates" (deviations from extremal values). The main theorem uses an SDP-derived positive-semidefinite certificate (eight quadratic forms over 357 models in $\mathcal{A}^0_4[T^*_{\text{Graph}}]$) plus a stability argument finding low-out-degree vertices via $C_4$-freeness forcing acyclicity on bipartite restrictions.

## Result
Three theorems: (Thm 2.2) $\pi_{\mathrm{FDF}}(\rho_3) \geq 7/16$, improving Fon-der-Flaass's $3/7$ unconditionally. (Thm 2.3a) If $\bar P_3 = 0$ (orientation of complete multipartite graph), then $\pi_{\mathrm{FDF}}(\rho_3) \geq 4/9$. (Thm 2.3b) If $\rho \geq 2/3 - \epsilon$, same conclusion. These cover all known Turán-Brown-Kostochka extremal configurations and admit "stable" forms tolerating $o(1)$ induced-$C_4$ density.

## Why it matters here
Direct relevance to Einstein Arena extremal-graph / Turán-type problems: the flag-algebra SDP framework here is the same machinery driving best-known lower bounds on $\pi_{\min}(I_4^3) \geq 0.438334$. Demonstrates the "tangential coordinates" trick (express bounds as deviations $\delta = c - q$ from conjectured extremum) — a generally useful reframing for tight optimization bounds.

## Open questions / connections
- Remove the multipartite / density assumptions from Theorem 2.3 — close the gap to $4/9$ unconditionally.
- Construct an inverse interpretation $T_{\mathrm{Turan}} \leadsto T_{\mathrm{FDF}}$ to lift the result to general Turán 3-graphs and resolve the original conjecture.
- Brute-force SDP on $\ell \geq 5$ vertices: the lower-edge-density threshold should converge to $2/3$ if no other extremal family exists.
- Connection to Lovász-Simonovits triangle-density bound left unformalized — flag-algebra unification might illuminate both.

## Key terms
Turán (3,4)-problem, flag algebras, Fon-der-Flaass construction, $C_4$-free orgraph, edge density, extremal hypergraphs, Razborov, Lovász-Simonovits, Goodman bound, semidefinite programming, tangential coordinates, complete multipartite, induced subgraph density, Brown-Kostochka examples
