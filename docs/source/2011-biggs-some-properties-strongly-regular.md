---
type: source
kind: paper
title: Some Properties of Strongly Regular Graphs
authors: N. Biggs
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1106.0889
source_local: ../raw/2011-biggs-some-properties-strongly-regular.pdf
topic: general-knowledge
cites:
---

# Some Properties of Strongly Regular Graphs

**Authors:** N. Biggs  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1106.0889

## One-line
A systematic method for enumerating feasible parameter sets $(n,k,a,c)$ of strongly regular graphs using the structural parameters $(a,c,e)$, where $e=\lambda_1$ is the positive eigenvalue, with Krein bounds capping $c$ and integrality conditions filtering further.

## Key claim
Fixing $a$ and $e$, the Krein bound forces $c \le e^2 + e + 2a$ (or $e^2+e+3a$ for $e\in\{1,2\}$); combined with the divisibility conditions $c \mid D$ and $c+2e-a \mid F$ (where $D=e(e+1)(e-a)(e-a-1)$, $F=(e+1)(e^2+2e-a)(e^2+3e-a)$), this yields a finite, tractable enumeration. The "algebraically feasible" case $c=e(e+1)$ is the unique non-trivial divisor in $\mathbb{Z}[e]$ for any $a\ge 1$, and Theorem 6.1 shows that for such graphs with $e>a$, the closed neighbourhood $N=\{v\}\cup X_1(v)$ is always a star complement for $e$.

## Method
Reformulate the classical SRG parameter conditions in $(a,c,e)$ coordinates so that $k=(e+1)c+e(e-a)$ and $s=c+2e-a$ become explicit. Express the Krein parameter $K_2$ as a quadratic in $c$, bounding feasible $c$. Apply the Reconstruction Theorem $eI - A_P = B^T(eI - A_Q)^{-1}B$ for star-complement analysis, reducing graph construction to finding a $(0,1)$-matrix $B$ with $BB^T = R = cJ + e(e+c-a)I + (a-c)A_Q - A_Q^2$.

## Result
Closed-form Krein bounds and divisibility conditions allow tabulation up to any $n$; e.g. for SRNT graphs ($a=0$) the bounds $n_{\min}, n_{\max}$ are computed for $1\le e\le 10$ (covering all SRGs up to $n\le 6024$ by checking only those $e$). For $a=1, e=4$: only $c\in\{2,8,20\}$ feasible, giving $(n,k)=(243,22),(378,52),(729,112)$, all realised. The algebraically feasible family with $a=e-1$, $c=e(e+1)$, $k=e(e^2+2e+2)$, $n=(e+1)^4$ includes the Clebsch graph $(16,5,0,2)$ and the $(81,20,1,6)$ graph, and admits a Hermitian-matrix Cayley construction whenever $e=q-1$ for $q$ a prime power.

## Why it matters here
General background; no direct arena tie — strongly regular graphs are not among the 23 Einstein Arena problem families, though the eigenvalue-integrality + Krein-bound enumeration template is methodologically adjacent to extremal-graph and discrete-geometry techniques in the wiki.

## Open questions / connections
- Does the Brouwer-Haemers structure theorem (partition of $(e+1)^4$ vertices into $e+1$ subsets each inducing $(e+1)^2$ copies of $K_{e+1}$) yield graphs when $e+1$ is *not* a prime power?
- Are the numerical Krein + divisibility conditions asymptotically sufficient, or do "accidental" feasibles persist whose graphs never exist (cf. the ruled-out $(63,22,1,11)$)?
- Extends the SRNT line (Biggs 2009, arXiv:0911.2160, 0911.2455) and connects to two-weight codes / affine polar graphs (Calderbank-Kantor, Brouwer).

## Key terms
strongly regular graph, Krein bound, star complement, Reconstruction Theorem, eigenvalue multiplicity, integrality condition, feasible parameters, SRNT, Clebsch graph, Higman-Sims graph, Brouwer-Haemers, Hermitian forms Cayley graph, affine polar graph, two-weight code, closed neighbourhood, algebraic feasibility
