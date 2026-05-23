---
type: source
kind: paper
title: Non-Three-Colourable Common Graphs Exist
authors: Hamed Hatami, J. Hladký, D. Král, Sergey Norin, A. Razborov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1105.0307
source_local: ../raw/2011-hatami-non-three-colourable-common-graphs-exist.pdf
topic: general-knowledge
cites:
---

# Non-Three-Colourable Common Graphs Exist

**Authors:** Hamed Hatami, J. Hladký, D. Král, Sergey Norin, A. Razborov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1105.0307

## One-line
Proves the 5-wheel $W_5$ is a common graph, giving the first known common graph with chromatic number $> 3$.

## Key claim
**Theorem 3.1:** $W_5$ is common, i.e. $\liminf_{n\to\infty} \min_{G\in\mathcal{M}_n}(t(W_5;G)+t(W_5;G^*)) \geq 2^{1-|E(W_5)|} = 2^{-9}$, matching the random-graph value. This resolves the Jagger–Šťovíček–Thomason (1996) question and refutes the suggestion (implicit in prior gluing constructions) that common graphs are confined to chromatic number $\leq 3$.

## Method
Flag algebra calculation (Razborov 2007): express $\widetilde{W_5}+\widetilde{W_5}^* - 2^{-9}$ as a sum of squares $\sum_i Q_i^\sigma + Q_i^{-\sigma}$ over five types $\sigma_0,\ldots,\sigma_4$ of size 4, with quadratic forms defined by explicit symmetric matrices $M_i^{\pm}$ and basis vectors $g_i^{\pm}$ of $\mathrm{Aut}(\sigma)$-invariant flags. Positive-definiteness of $M_i^{\pm}$ (verified by standard math software) plus the averaging-operator inequality from flag algebras gives the bound; the algebraic identity (3.2) reduces to checking coefficients on 156 flags in $\mathcal{M}_6$, done by a published C program. The matrices were found via SDP.

## Result
The exact rational identity $\widetilde{W_5}+\widetilde{W_5}^* = 2^{-9} + R + R^*$ holds in the flag algebra $\mathcal{A}^0$, where $R$ is a positive combination of squared flag-algebra elements. Random graphs $G_{n,1/2}$ asymptotically minimize $t(W_5;G)+t(W_5;G^*)$; the authors argue (numerically, to accuracy $10^{-10}$, via inequality (3.3) involving $C_4$) that $G_{n,1/2}$ is essentially the unique minimizer, though this uniqueness is not made rigorous.

## Why it matters here
Directly informs **extremal_graph / common-graph** problems on the arena where one must minimize monochromatic-copy counts: shows the flag-algebra + SDP machinery can certify tight Cauchy-Schwarz bounds even on non-bipartite, non-3-colourable graphs. Adds a concrete worked SDP-certified extremal identity ($2^{-9}$, 156 flags, 5 types of size 4) and a uniqueness-via-$C_4$-quasirandomness argument template.

## Open questions / connections
- Do common graphs of arbitrarily large chromatic number exist? (Explicit conclusion question.)
- Can the floating-point inequality (3.3) be converted to a rigorous proof of uniqueness of the minimizing homomorphism $\varphi$?
- Extends the Jagger–Šťovíček–Thomason / Sidorenko gluing operations, which could not increase chromatic number above 3 — what new constructions could?
- Relates to Erdős–Simonovits–Sidorenko conjecture (known for $C_4$ via [Sid91]); $W_5$ is a vertex-of-full-degree extension of a non-bipartite graph, answering Sidorenko's 1996 question negatively.

## Key terms
common graph, 5-wheel $W_5$, flag algebra, Razborov, semi-definite programming, Cauchy-Schwarz, Sidorenko conjecture, Erdős-Simonovits-Sidorenko, quasi-random graphs, Goodman bound, chromatic number, Burr-Rosta conjecture, monochromatic subgraph density, homomorphism density, Jagger-Šťovíček-Thomason
