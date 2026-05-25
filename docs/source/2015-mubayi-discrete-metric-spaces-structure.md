---
type: source
kind: paper
title: "DISCRETE METRIC SPACES: STRUCTURE, ENUMERATION, AND 0-1 LAWS"
authors: D. Mubayi, C. Terry
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.01212
source_local: ../raw/2015-mubayi-discrete-metric-spaces-structure.pdf
topic: general-knowledge
cites:
---

# DISCRETE METRIC SPACES: STRUCTURE, ENUMERATION, AND 0-1 LAWS

**Authors:** D. Mubayi, C. Terry  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.01212

## One-line
Approximate-structure and asymptotic enumeration of finite metric spaces on $n$ points with integer distances in $\{1,\dots,r\}$, plus a labeled first-order 0-1 law when $r$ is even.

## Key claim
Let $M_r(n)$ be the set of metric spaces on $[n]$ with distances in $[r]$. Then $|M_r(n)| = \lceil (r+1)/2 \rceil^{\binom{n}{2}+o(n^2)}$; when $r\ge 4$ is even this sharpens to $|M_r(n)| = (r/2+1)^{\binom{n}{2}+o(1)}$ and almost all such metric spaces have every distance in $[r/2, r]$, yielding a labeled first-order 0-1 law for $M_r$ in the language of $r$ binary relations.

## Method
Edge-colored extremal-combinatorics framework: view a metric space as a simple complete $r$-edge-colored graph forbidding triangle-inequality-violating triples, then apply a multi-color Szemerédi regularity lemma (Axenovich–Martin) to prove a stability theorem. Counting and structure follow Erdős–Kleitman–Rothschild / Kolaitis–Prömel–Rothschild templates adapted to the colored setting, with weighted-Turán ideas from Füredi–Kündgen. The 0-1 law is obtained by reducing $M_r$ to the subfamily $C_r$ of $r$-graphs with all colors in $[r/2,r]$ (which has no forbidden configurations), and identifying its almost-sure theory with the theory of the Fraïssé limit of finite complete edge-colored graphs colored in $\{r/2,\dots,r\}$.

## Result
For even $r\ge 4$: $|C_r(n)| = (r/2+1)^{\binom{n}{2}}$ and $|C_r(n)| \ge |M_r(n)|(1 - 2^{-\beta n})$ for some $\beta>0$, so the metric structure is essentially "pick any color in $[r/2,r]$ independently." For odd $r$: a partition-style structure with intra-class colors in $[(r-1)/2, r-1]$ and inter-class colors in $[(r+1)/2, r]$ — and explicit construction shows $|C_r(n)| \le (1 - r^{-66r^2})|M_r(n)|$, so the even-case 0-1 law conjecturally degrades to only a limit law.

## Why it matters here
General background; no direct arena tie — this is enumeration / 0-1 law theory for discrete metric spaces, not an optimization tool. The "all distances concentrate in upper half" phenomenon weakly parallels Kozma–Meyerovitch–Peled–Samotij's continuous metric-polytope result that random metrics on $[0,1]$ concentrate distances in $[1/2,1]$, which could inform priors when sampling metric configurations for combinatorial problems.

## Open questions / connections
- Conjecture 1.8: for odd $r\ge 3$, $M_r$ has a labeled first-order limit law but not a 0-1 law — the partition structure forces non-trivial limiting probabilities.
- Can the discrete results be scaled ($r\to\infty$ with $n$ fixed) to recover the continuous metric-polytope results of Kozma–Meyerovitch–Peled–Samotij [33]?
- Extension to other forbidden-substructure problems in edge-colored complete graphs (weighted-Turán direction of Füredi–Kündgen [22]).

## Key terms
discrete metric space, triangle inequality, edge-colored graph, asymptotic enumeration, first-order 0-1 law, Fraïssé limit, Szemerédi regularity lemma, multi-color regularity, stability theorem, Erdős–Kleitman–Rothschild, Kolaitis–Prömel–Rothschild, metric polytope, weighted Turán, extremal combinatorics, Mubayi, Terry
