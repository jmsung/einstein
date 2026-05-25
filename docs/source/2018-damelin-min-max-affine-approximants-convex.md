---
type: source
kind: paper
title: On Min-Max affine approximants of convex or concave real valued functions from $\mathbb R^k$, Chebyshev equioscillation and graphics
authors: Steven B. Damelin, David L. Ragozin, Michael Werman
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1812.02302v10
source_local: ../raw/2018-damelin-min-max-affine-approximants-convex.pdf
ingested_for_concept: equioscillation-escape.md
cites: 
---

# On Min-Max affine approximants of convex or concave real valued functions from $\mathbb R^k$, Chebyshev equioscillation and graphics

**Authors:** Steven B. Damelin, David L. Ragozin, Michael Werman  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1812.02302v10

## One-line
Gives an explicit closed-form best Min-Max affine approximant to any continuous convex/concave $f:\Delta\to\mathbb R$ on a $k$-simplex, generalizing Chebyshev equioscillation to multivariate domains.

## Key claim
For a $k$-simplex $\Delta = \mathrm{CH}(a_1,\dots,a_{k+1})$ and convex (or concave) continuous $f$, the unique best $L^\infty$ affine approximant is $\sigma := (\pi+\rho)/2$, where $\pi$ is the affine interpolant of $f$ at the vertices and $\rho$ is the supporting hyperplane to $\mathrm{graph}(f)$ parallel to $\pi$. The error equioscillates: $f(a_i)-\sigma(a_i)=d$ at all $k+1$ vertices and $\sigma(y)-f(y)=d$ at the contact point $y$.

## Method
Two-line proof using the dual definitions of convexity (graph $\le$ secant; graph $\ge$ supporting hyperplane). Bound the candidate $\mu$ from below at vertices (else max error grows) and from above at the supporting-contact point via the convex combination $y=\sum\gamma_i a_i$ with $\mu(y)=\sum\gamma_i\mu(a_i)$, forcing $\mu=\sigma$. Computationally, solve a $(k+1)\times(k+1)$ linear system for the secant slope $\bar\alpha$, then minimize/maximize $f-\bar\alpha^Tx$ once to locate $\rho$.

## Result
Theorem 2.1 establishes existence, uniqueness, and an explicit formula $\sigma=(\pi+\rho)/2$ for the Min-Max affine approximant on any $k$-simplex when $f$ is convex or concave (Remark 2.2 reduces it to one linear solve plus one convex minimization). Theorem 2.2 strengthens this to any continuous $f$ whose graph lies entirely on one side of the vertex-secant. For $k=1$ it recovers and explicitly solves the Chebyshev equioscillation theorem for degree-1 approximants on $[p,q]$.

## Why it matters here
General background on $L^\infty$ affine approximation; the equioscillation half is directly relevant to arena problems with Chebyshev/Remez-style structure (P14, P15, P16 — equioscillation as an active-triple diagnostic). The multivariate vertex+supporting-hyperplane characterization could inform piecewise-affine envelopes used in LP relaxations and barycentric majorants, though it is not a tight match to any current problem.

## Open questions / connections
- No convex domain other than a simplex is known where this two-hyperplane construction certifies global one-sidedness — what is the right generalization to polytopes or balls?
- Extension beyond affine/linear ($l=1$) to higher-degree multivariate Chebyshev systems on simplices is open (Haar systems exist on intervals only).
- Connection to barycentric-coordinate LP duality on simplices and to flag-algebra-style certificates on extremal-graph problems.
- Computational cost reduces to one convex optimization of $\pm f$ over $\Delta$ — fast enough for in-loop polish?

## Key terms
Min-Max approximation, Chebyshev equioscillation, affine approximant, supporting hyperplane, simplex, convex function, concave function, best uniform approximation, Haar system, Remez, projective transformation, Damelin
