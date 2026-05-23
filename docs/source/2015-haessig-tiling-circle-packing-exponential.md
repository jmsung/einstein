---
type: source
kind: paper
title: Tiling, Circle Packing and Exponential Sums over Finite Fields
authors: C. Haessig, A. Iosevich, Jonathan Pakianathan, S. Robins, L. Vaicunas
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.05861
source_local: ../raw/2015-haessig-tiling-circle-packing-exponential.pdf
topic: general-knowledge
cites:
---

# Tiling, Circle Packing and Exponential Sums over Finite Fields

**Authors:** C. Haessig, A. Iosevich, Jonathan Pakianathan, S. Robins, L. Vaicunas  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.05861

## One-line
Develops a Fourier/polynomial-method theory of multi-tilings and circle packings in vector spaces over finite fields $\mathbb{F}_q^d$, with structural classification in low dimensions and a near-optimal isotropic circle packing in the plane.

## Key claim
(i) $E$ $k$-tiles $\mathbb{F}_q^d$ by $A$ iff $|A|\cdot|E|=kq^d$ and $\widehat{E}(m)\widehat{A}(m)=0$ for all $m\neq 0$; (ii) every $1$-tiling of $\mathbb{F}_p^2$ (and every $1$-tiling of $\mathbb{F}_p^3$ with $|E|\in\{p,p^{d-1}\}$) is *graphical* — one side is the graph of a polynomial $f:\mathbb{F}_p\to\mathbb{F}_p$ of degree $\le p-1$; (iii) for $q\equiv 1\pmod 4$ and any $c\ne 0$, the unit-circle packing number satisfies $q \le P(q,c) \le q+1$, realized by placing $q$ radius-$c$ circles on an isotropic line.

## Method
Three intertwined tools. (1) **Discrete Fourier on $\mathbb{F}_q^d$** with additive character $\chi$, plus a *rational-valued* refinement: Galois action $g_r:\xi\mapsto\xi^r$ on $\mathbb{Q}(\xi)$ forces $\widehat{f}(rm)=g_r(\widehat{f}(m))$, so a single Fourier zero kills a whole line through the origin. (2) **Equidistribution lemma**: $\widehat{E}(m)=0$ iff $E$ is evenly distributed across the $p$ hyperplanes $\{x\cdot m=t\}$, proved via Eisenstein-irreducibility of the cyclotomic polynomial. (3) **Polynomial-ring encoding** in $(\mathbb{Z}/q\mathbb{Z})[z_1,\dots,z_d]/(z_i^q-1)$: $\sum_{e\in E}z^e \cdot \sum_{a\in A}z^a \equiv k\prod_i \frac{z_i^q-1}{z_i-1}$, then differentiate $z_j\partial_{z_j}$ to extract moment identities. Circle packing uses a triangle-completion lemma counting $\#\{x_3: \|x_2-x_3\|=\ell_2, \|x_3-x_1\|=\ell_3\}$ via the discriminant $4\sigma_2-\sigma_1^2$.

## Result
- **Fourier characterization** (Thm 1.2) of multi-tilings.
- **Plane classification** (Thm 1.7/1.8): a $k$-tiling set $E\subset\mathbb{F}_p^2$ with $|E|=sp$, $1\le s\le p-1$, decomposes into $s$ disjoint polynomial graphs; $s\mid k$.
- **3-space classification** (Thm 1.10): every $1$-tiling of $\mathbb{F}_p^3$ is graphical; first uncovered case is $|E|=|A|=p^2$ in $\mathbb{F}_p^4$.
- **Two-circle intersection criterion** (Cor 1.17): radius-$c$ circles at distance $R$ meet in $\mu\in\{0,1,2\}$ points according to whether $R(4c-R)$ is a nonsquare / zero / nonzero square.
- **Isotropic packing** (Thm 1.21): for $q\equiv 1\pmod 4$, $q$ disjoint radius-$c$ circles centered on an isotropic line; their complement is exactly that line, giving $q\le P(q,c)\le q+1$.
- **Moment identities** (Cor 1.27/1.28): $|A|\sum_E e + |E|\sum_A a \equiv 0$ and a second-moment analog in $(\mathbb{Z}/q\mathbb{Z})^d$.
- **Algebraic tiling** (Thm 1.25): over algebraically closed $k$, $\dim X+\dim Y=d$; when $X,Y\cong\mathbb{A}^i,\mathbb{A}^j$ the tiling map is a *regular automorphism* of $\mathbb{A}^d$, linking to the Jacobian conjecture.

## Why it matters here
General background — no direct arena tie. The Fourier-zero ⇒ equidistribution dictionary, the rational-valued Galois constraint $\widehat{f}(rm)=g_r(\widehat{f}(m))$, and the polynomial-method moment identities are *technique transfer candidates* for any arena problem cast over $\mathbb{F}_p$ (Sidon-set / autocorrelation / discrete-geometry variants), and the isotropic-line trick is a vivid reminder that "degenerate" symmetric subspaces can saturate packing bounds.

## Open questions / connections
- Does the graphical classification extend to $\mathbb{F}_p^d$ for $d\ge 4$? The smallest unsettled case is $(E,A)\subset\mathbb{F}_p^4$ with $|E|=|A|=p^2$.
- Is $P(q,c)=q$ or $q+1$ exactly for $q\equiv 1\pmod 4$? The isotropic packing is maximal but a non-isotropic $(q+1)$-packing is not ruled out.
- Higher-order moment identities (beyond Cor 1.28) — what tiling obstructions do they encode?
- Connects to: Kolountzakis–Matolcsi non-spectral tilings of $\mathbb{Z}_{56}\times\mathbb{Z}_{15}$, Gravin–Robins–Shiryaev multi-tilings, Bennett–Iosevich–Pakianathan three-point configurations, Jacobian conjecture for $d\ge 2$.

## Key terms
multi-tiling, finite field Fourier transform, equidistribution on hyperplanes, graphical tiling, cyclotomic Galois action, Eisenstein irreducibility, polynomial method, moment identities, isotropic line, circle packing in $\mathbb{F}_q^2$, packing number $P(q,c)$, Jacobian conjecture, algebraic 1-tiling, Iosevich, Pakianathan, Robins
