---
type: source
kind: paper
title: Forbidden Subgraphs for Graphs of Bounded Spectral Radius, with Applications to Equiangular Lines
authors: Zilin Jiang, A. Polyanskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.02317
source_local: ../raw/2017-jiang-forbidden-subgraphs-graphs-bounded.pdf
topic: general-knowledge
cites:
---

# Forbidden Subgraphs for Graphs of Bounded Spectral Radius, with Applications to Equiangular Lines

**Authors:** Zilin Jiang, A. Polyanskii  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.02317

## One-line
Characterizes which spectral-radius bounds $\lambda$ admit a finite forbidden-subgraph description of $\mathcal{F}(\lambda)$, and uses this to pin down the linear coefficient $c_\alpha$ in $N_\alpha(n) = c_\alpha n + O(1)$ for equiangular lines.

## Key claim
$\mathcal{F}(\lambda)$ (connected graphs with spectral radius $\leq \lambda$) has a finite forbidden-subgraph characterization iff $\lambda < \lambda^* := \sqrt{2+\sqrt{5}} \approx 2.058$ and $\lambda \notin \{\alpha_2, \alpha_3, \ldots\}$, where $\alpha_m = \beta_m^{1/2} + \beta_m^{-1/2}$ and $\beta_m$ is the largest root of $x^{m+1} = 1 + x + \cdots + x^{m-1}$. Consequently, for $\alpha \in (0,1)$ with $\lambda := \tfrac{1-\alpha}{2\alpha} \leq \lambda^*$, $N_\alpha(n) = \tfrac{k(\lambda)}{k(\lambda)-1} \cdot n + O(1)$, where $k(\lambda)$ is the spectral radius order (smallest $n$ admitting a graph of spectral radius exactly $\lambda$); $k(\lambda)=\infty$ gives $N_\alpha(n)=n+O(1)$.

## Method
Combines spectral graph theory (Hoffman/Shearer limit points of graph spectral radii, Perron–Frobenius for multiplicity-one largest eigenvalue) with the Balla–Dräxler–Keevash–Sudakov "projection-to-orthogonal-complement of a Ramsey-large independent set" framework. The pivot is Lemma 8: bounding a spherical $L(\alpha,t)$-code's underlying graph by forbidden subgraphs of spectral radius $> \lambda$ via Weyl's inequality applied to $M = (1-\alpha)(I - A/\lambda) + \alpha J$. Theorem 1 supplies the finite forbidden family; Corollary 12 (rank bound from Perron–Frobenius) converts spectral-radius order into the linear coefficient.

## Result
Recovers $N_{1/3}(n) = 2n+O(1)$, $N_{1/5}(n) = \tfrac{3}{2}n+O(1)$; **new** result $N_{1/(1+2\sqrt{2})}(n) = \tfrac{3}{2}n + O(1)$ (refuting part of BDKS Conjecture 6.1). For $\lambda > \lambda^*$, improves the universal bound to $N_\alpha(n) \leq 1.49n + O(1)$ for $\alpha \neq 1/3, 1/5, 1/(1+2\sqrt{2})$, beating BDKS's $1.93n$. Asymptotic formula $N_{1/7}(n) \leq (4/3 + 1/36 + o(1))n$ for the open Bukh case.

## Why it matters here
Direct algebraic-graph-theory tooling for equiangular-line and spherical-code problem families (kissing numbers, two-distance sets) — the Gram-matrix-as-$(1-\alpha)(I-A/\lambda)+\alpha J$ trick converts an unit-vector packing into a spectral constraint on a 0/1 matrix. Provides the canonical $k(\lambda)/(k(\lambda)-1)$ linear coefficient that any Einstein-Arena equiangular-line attack should match before claiming improvement.

## Open questions / connections
- Conjecture B: does $N_\alpha(n) = \tfrac{k(\lambda)}{k(\lambda)-1} \cdot n + O(1)$ hold for **all** $\lambda$, not just $\lambda \leq \lambda^*$? (Open beyond $\lambda^*$.)
- Conjecture C: forbidden-subgraph control on multiplicity of the second-largest eigenvalue — would close Conjecture B.
- Extends Bukh [Buk16], BDKS [BDKS18], Glazyrin–Yu [GY18]; predates the full Jiang–Tidor–Yao–Zhang–Zhao 2021 resolution.
- $N_{1/7}(n)$ remains the cleanest unresolved odd-$1/\alpha$ instance.

## Key terms
equiangular lines, spectral radius, forbidden subgraphs, Perron–Frobenius, Weyl inequality, spherical L-code, Gram matrix, Ramsey, Hoffman limit points, Shearer, Cvetković–Doob–Gutman, $\lambda^* = \sqrt{2+\sqrt{5}}$, spectral radius order, equiangular line maximum $N_\alpha(n)$, Balla–Dräxler–Keevash–Sudakov
