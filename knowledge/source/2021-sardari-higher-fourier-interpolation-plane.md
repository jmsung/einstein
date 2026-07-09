---
type: source
kind: paper
title: Higher Fourier interpolation on the plane
authors: Naser T. Sardari
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.08753
source_local: ../raw/2021-sardari-higher-fourier-interpolation-plane.pdf
topic: general-knowledge
cites:
---

# Higher Fourier interpolation on the plane

**Authors:** Naser T. Sardari  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.08753

## One-line
Constructs Fourier interpolation formulas on $\mathbb{R}^2$ from weakly holomorphic modular forms on Hecke triangle groups $(2,l,\infty)$, and uses the $l=6$ case to prove a Cohn–Kumar–Miller–Radchenko–Viazovska conjecture about non-uniqueness of radial Schwartz functions tied to the hexagonal lattice.

## Key claim
For radial Schwartz $f:\mathbb{R}^2\to\mathbb{C}$ expressible as $f(x)=\int e^{i\pi\tau|x|^2}d\mu(\tau)$ with $\mu$ supported where $\mathrm{Im}(\tau),\mathrm{Im}(-1/\tau)>\sin(\pi/l)$, $f$ is reconstructible from $\{d^k f/du^k, d^k \mathcal{F}f/du^k\}$ at $u=2n/\lambda$, $\lambda=2\cos(\pi/l)$ — and the support bound $\sin(\pi/l)$ is **optimal**. As a consequence (Theorem 1.7): there exist infinitely many linearly independent radial Schwartz $f$ on $\mathbb{R}^2$ such that $f$ and $\mathcal{F}f$ vanish to order 2 at $|x|=\sqrt{2n/\sqrt{3}}$ for all $n=x^2+xy+y^2$, $x,y\in\mathbb{Z}$ — proving [CKM+19, Conjecture 7.5].

## Method
Builds eigenfunctions of $\mathcal{F}$ as contour integrals $a_{n,k}^\varepsilon(x)=\frac{1}{\lambda}\int_{w_1}^{w_2}\phi_{n,k}^\varepsilon(z)\frac{e^{i\pi z|x|^2}}{(iz\pi)^k}\,dz$ against weakly holomorphic modular forms of weight $-2k+1$ for the Hecke triangle group $(2,l,\infty)$, with $w_1,w_2=\mp\cos(\pi/l)+i\sin(\pi/l)$. Optimality is shown via monodromy obstructions $r_k^\varepsilon(\gamma,\tau;x)$ built from the algebraic identity $S(T^{-1}-I)(1+V+\cdots+V^{l-1})=-(T^{-1}-I)(1+V+\cdots+V^{l-1})$ in $\mathbb{Z}[\mathrm{PSL}_2(\mathbb{R})]$. The hexagonal proof (Theorem 1.8) combines (a) a sieve-theoretic covering of $\{x^2+xy+y^2\}$ by a periodic set $A$ of density $<0.001$, (b) discrete Vandermonde averaging mod $L$, and (c) continuous averaging by $\lambda_{n,\alpha}(\theta)=1+\cos(2\pi n\theta-\alpha)$, then a Hahn–Banach / weak-$*$-limit convexity argument.

## Result
Theorem 1.4 gives the interpolation formula $f_\varepsilon(x)=\sum_{n\ge d(\varepsilon,k)} a_{n,k}^\varepsilon(x)\,(d^k/du^k)f_\varepsilon(2n/\lambda)$. Theorem 1.6 identifies the obstruction space with $M_{-2k+1}^{-\varepsilon}(\Gamma)$, holomorphic modular forms of weight $2k+1$ and opposite multiplier. Theorem 1.7 resolves CKM+19 Conjecture 7.5: the values $f, f', \mathcal{F}f, (\mathcal{F}f)'$ at $\sqrt{2n/\sqrt{3}}$ for $n$ represented by $x^2+xy+y^2$ do **not** uniquely determine a radial Schwartz function on $\mathbb{R}^2$ — confirming that the $E_8$ / Leech magic-function strategy cannot extend directly to dimension 2.

## Why it matters here
Directly relevant to Einstein Arena sphere-packing / autocorrelation problems built on the Cohn–Elkies LP framework: this is the rigorous statement that the Cohn–Elkies magic-function construction for the hexagonal lattice in $\mathbb{R}^2$ is **under-determined** by Poisson-summation constraints alone, so any plane-dimension universality proof needs additional structure beyond $\{f,f',\mathcal{F}f,(\mathcal{F}f)'\}$ at $\sqrt{2n/\sqrt{3}}$. Informs concepts: Cohn–Elkies LP, Fourier interpolation, modular forms over Hecke triangle groups, hexagonal-lattice universality; pairs with `findings/` on LP-bound saturation and `concepts/` on Cohn–Elkies and magic functions.

## Open questions / connections
- Extends Radchenko–Viazovska 2019 ($\mathbb{R}^1$, theta group $(2,\infty,\infty)$) and CKM+19 ($d=8,24$, first-derivative formulas) to general Hecke triangle groups and arbitrary derivative order $k$.
- Leaves open: an explicit construction of the dimension-2 magic function $f_t$ with $f_t(r)\le e^{-\pi t r^2}$, $\mathcal{F}f_t\ge0$, $\mathcal{F}f_t(0)-f_t(0)=\theta_0(it)-1$ — i.e., the actual universal-optimality proof for the hexagonal lattice remains open; this paper only shows the naive first-derivative interpolation route is insufficient.
- Suggests that any successful $d=2$ proof must add either higher derivatives, integrals over modular curves, or non-Poisson constraints — natural follow-up: which extra data closes the under-determined system?

## Key terms
Fourier interpolation, Hecke triangle group, weakly holomorphic modular forms, hexagonal lattice, universal optimality, Cohn–Elkies linear programming, magic function, Poisson summation, sphere packing $\mathbb{R}^2$, $E_8$ Leech analogy, monodromy obstruction, Radchenko–Viazovska, theta series $x^2+xy+y^2$, sieve covering
