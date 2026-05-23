---
type: source
kind: paper
title: Restriction of averaging operators to algebraic varieties over finite fields
authors: Doowon Koh, Seongjun Yeom
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1601.07677
source_local: ../raw/2016-koh-restriction-averaging-operators-algebraic.pdf
topic: general-knowledge
cites:
---

# Restriction of averaging operators to algebraic varieties over finite fields

**Authors:** Doowon Koh, Seongjun Yeom  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1601.07677

## One-line
Establishes sharp $L^p \to L^r$ bounds for the restricted averaging operator $A_V f = (f * \sigma)|_V$ on regular algebraic varieties (spheres, paraboloids, cones) in $\mathbb{F}_q^d$.

## Key claim
For a *regular variety* $V \subset \mathbb{F}_q^d$ ($|V| \sim q^{d-1}$, $|\sigma^\vee(m)| \lesssim q^{-(d-1)/2}$ for $m \ne 0$), $A_V(p \to r) \lesssim 1$ iff $(1/p, 1/r)$ lies in the convex hull of $(0,0), (0,1), ((d-1)/d, 1), ((d-1)/d, 1/d)$. For cones in even $d \ge 4$ with $-1$ a square in $\mathbb{F}_q$, sharp bounds hold on the same region except at two endpoints $P_1 = ((d-1)/d, 1/(d-2))$ and $P_2 = ((d^2-3d+2)/(d^2-2d+2), (d-2)/(d^2-2d+2))$.

## Method
Decompose $\sigma = K + \delta_0$ where $K(m) = \sigma^\vee(m) - \delta_0(m)$; bound $f * 1$ trivially and $f * K$ by interpolating an $L^1 \to L^\infty$ bound (from $\max |\widehat{K}| \lesssim q$) against an $L^2 \to L^2$ bound using the restriction estimate $\|g\|_{L^2(V,\sigma)} \lesssim q^{1/2} \|g\|_{L^2}$ plus Fourier decay $|K(m)| \lesssim q^{-(d-1)/2}$. For the cone, Gauss-sum identities give explicit $C^\vee(m)$ depending on whether $\Gamma_4(m) := m_1^2 + \cdots + m_{d-2}^2 - 4 m_{d-1} m_d$ vanishes, yielding two decay regimes that require Lemma 4.5's split-sum bound. Necessity at $P_2$ uses that $C$ contains a $d/2$-dimensional affine subspace $\Pi = \{(t_1, it_1, \ldots, t_{(d-2)/2}, it_{(d-2)/2}, s, 0)\}$ when $i^2 = -1 \in \mathbb{F}_q$.

## Result
Sharp Riesz-Thorin region for regular $V$ (Theorem 1.4). For cones in even $d \ge 4$: strong-type on the interior of $\Omega$, restricted-type at $P_1$, weak-type at $P_2$ (Theorem 1.5). Necessary conditions: $1/p \le (d-1)/d$, $1/(p(d-1)) \le 1/r$, and if $V \supset \Pi$ with $|\Pi| = q^\alpha$ then $(d-\alpha)/(p'(d-1-\alpha)) \le 1/r' + 1$.

## Why it matters here
General background; no direct arena tie. The finite-field restriction/Kakeya machinery (Mockenhaupt-Tao, Dvir polynomial method, Guth restriction) is adjacent to extremal-set techniques but the arena problems are continuous/Euclidean; this paper's specific bounds don't plug into any of the 23 problems.

## Open questions / connections
- Two endpoint cases $P_1, P_2$ for the cone in even dimensions when $-1$ is a square remain open at strong-type.
- Behavior when $-1$ is a non-square in $\mathbb{F}_q$ (the embedded $\Pi$ argument fails) — full sharp region unknown.
- Extends Koh's earlier 2D result (curves not containing lines) to higher dimensions; natural next: non-quadratic varieties, varieties of codimension $\ge 2$.

## Key terms
finite field harmonic analysis, restriction operator, averaging operator, regular variety, Fourier decay, Gauss sum, paraboloid $\mathbb{F}_q^d$, sphere $\mathbb{F}_q^d$, cone $\mathbb{F}_q^d$, Mockenhaupt-Tao, polynomial method, Riesz-Thorin interpolation
