---
type: source
kind: paper
title: On expansion and topological overlap
authors: Dominic Dotterrer, T. Kaufman, Uli Wagner
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.04558
source_local: ../raw/2015-dotterrer-expansion-topological-overlap.pdf
topic: general-knowledge
cites:
---

# On expansion and topological overlap

**Authors:** Dominic Dotterrer, T. Kaufman, Uli Wagner  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.04558

## One-line
A streamlined, elementary proof of Gromov's Topological Overlap Theorem: sufficiently strong higher-dimensional coboundary expansion of a $d$-complex $X$ forces a topological point-overlap property for every continuous map $X \to M^d$.

## Key claim
If a finite $d$-dimensional polyhedral cell complex $X$ satisfies (i) an $L$-cofilling (coisoperimetric) inequality in dimensions $1,\ldots,d$, (ii) $\vartheta$-large cosystoles in dimensions $0,\ldots,d-1$, and (iii) local $\varepsilon$-sparsity with $\varepsilon \le \varepsilon_0(d,L,\vartheta)$, then for every continuous $f: X \to M$ into a compact connected $d$-dimensional PL manifold there exists $p \in M$ hit by a $\mu(d,\varepsilon,L,\vartheta) > 0$ fraction of $d$-cells.

## Method
PL approximation + general-position perturbation reduces to a PL map $f$ in general position with respect to a sufficiently fine triangulation $T$ of $M$. The core argument builds, by induction on simplex dimension, a chain–cochain homotopy $H$ between the intersection-number map $f^\pitchfork$ and a constant map $G$; at each step the inductive cocycle is cofilled using the coisoperimetric assumption, while large cosystoles rule out nontrivial cohomology obstructions. Applying $H$ to the fundamental cycle $\zeta_M$ yields a contradiction unless some vertex $v$ has $\|f^\pitchfork(v)\| \ge \mu$.

## Result
The overlap constant satisfies $\mu \ge \vartheta / (2(k+1)! L^k) + o(1)$ as local sparsity $\varepsilon \to 0$ (e.g. for the $d$-skeleton of $\Delta^n$ with $\varepsilon = O(1/n)$). The proof works for arbitrary monotone norms on cochains and generalizes to coefficient rings $R$ (under $R$-orientability and sign-invariance of the norm). The argument also extends conceptually to homology manifolds, modulo a general-position chain map substitute.

## Why it matters here
General background; no direct arena tie — this is high-dimensional expander / topological-combinatorics machinery, useful as conceptual scaffolding for problems where coboundary expansion or simplicial-complex isoperimetry might enter (extremal graph / hypergraph density, Tverberg-type incidence problems), but none of the 23 Einstein Arena problems currently invokes topological overlap.

## Open questions / connections
- Can the theorem be extended to homology manifolds via a general-position chain-map analogue (authors flag this as future work)?
- Sharper overlap constants $\mu$ via Gromov's cofilling profiles or Matoušek–Wagner pagodas — what is the optimal $\mu(d)$ for $\Delta^n_{(d)} \to \mathbb{R}^d$?
- Bounded-degree complexes with the topological overlap property (Kaufman–Kazhdan–Lubotzky, Evra–Kaufman) — explicit Ramanujan-complex constructions.

## Key terms
topological overlap theorem, coboundary expansion, cofilling inequality, coisoperimetric inequality, cosystole, cellular cochains, simplicial complex, PL manifold, intersection number, chain-cochain homotopy, point selection problem, Gromov, Linial-Meshulam, high-dimensional expander, general position
