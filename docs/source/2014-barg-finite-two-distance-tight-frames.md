---
type: source
kind: paper
title: Finite two-distance tight frames
authors: A. Barg, A. Glazyrin, Kasso Okoudjou, Wei-Hsuan Yu
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1402.3521
source_local: ../raw/2014-barg-finite-two-distance-tight-frames.pdf
topic: general-knowledge
cites:
---

# Finite two-distance tight frames

**Authors:** A. Barg, A. Glazyrin, Kasso Okoudjou, Wei-Hsuan Yu  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1402.3521

## One-line
Classifies all non-equiangular two-distance finite unit-norm tight frames (FUNTFs) in $\mathbb{R}^n$ as spherical embeddings of strongly regular graphs (SRGs).

## Key claim
Every non-equiangular two-distance FUNTF in $\mathbb{R}^n$ is a spherical two-distance 2-design (or shifted 2-design) arising as a Delsarte–Goethals–Seidel spherical embedding of an SRG; each SRG yields exactly three such 2-designs and hence six two-distance tight frames (two of which are regular simplices). Combined with Waldron (2009) for the equiangular case, this completes the classification.

## Method
Gram-matrix spectral analysis: for $S$ a two-distance FUNTF with inner products $a,b$, write $G = I + a\Phi_1 + b\Phi_2$ and exploit $G^2 = (N/n)G$. Show $\mathbf{1}$ is an eigenvector with eigenvalue $0$ or $N/n$, splitting into "2-design" vs "shifted 2-design" cases (Prop. 3.1). Prove the indicator graph $\Gamma_1$ is strongly regular by counting common-neighbor structure (Prop. 3.2), then parameterize all spherical embeddings via convex combinations $(\alpha,\beta,\gamma)$ over the three DGS eigenspace projections (Prop. 3.3, Thm 3.4).

## Result
- Theorem 2.4: regularity of $S$ and the algebraic constraint $-n(a+b) - nab(N-1) = N-n$ or $(N-n)(a+b) - nab(N-1) = N-n$ on $(a,b)$.
- Theorem 3.4: any spherical two-distance 2-design with graph $\Gamma_1$ is either $S_1(\Gamma_1)$, $S_2(\Gamma_1)$, or the regular $(N-1)$-simplex.
- Explicit FUNTF examples from SRG(10,6,3,4), SRG(15,8,4,4), SRG(16,10,6,6), e.g. FUNTF$(5,10,3,1/3,-1/3)$, FUNTF$(6,15,8,3/8,-1/4)$.

## Why it matters here
General background for spherical-code / equiangular-line problems: gives a clean SRG↔frame dictionary useful when arena problems involve few-distance configurations or tight-frame constructions. No direct tie to a current arena problem, but informs any future kissing-number / equiangular-lines / spherical-design approach.

## Open questions / connections
- Extends Waldron (2009) for ETFs; together they fully characterize two-distance tight frames — what about three-distance?
- Connects to general problem of which spherical designs come from association schemes (Delsarte–Goethals–Seidel).
- Relates to spherical-two-distance-set upper bounds $g(n)$ studied in Barg–Yu [3,4]; classification narrows the search space.

## Key terms
two-distance set, tight frame, FUNTF, equiangular tight frame, ETF, strongly regular graph, SRG, spherical 2-design, Delsarte-Goethals-Seidel embedding, Gram matrix, frame potential, Larman-Rogers-Seidel, Waldron, harmonic-index design, spherical code
