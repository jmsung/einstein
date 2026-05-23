---
type: source
kind: paper
title: Extension theorems for spheres in the finite field setting
authors: A. Iosevich, Doowon Koh
year: 2007
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/0712.1627
source_local: ../raw/2007-iosevich-extension-theorems-spheres-finite.pdf
topic: general-knowledge
cites:
---

# Extension theorems for spheres in the finite field setting

**Authors:** A. Iosevich, Doowon Koh  ·  **Year:** 2007  ·  **Source:** https://arxiv.org/abs/0712.1627

## One-line
Improves the Tomas–Stein exponents for the Fourier extension operator on spheres $S_j \subset \mathbb{F}_q^d$ in even dimensions $d \geq 4$, by bounding additive-energy / incidence counts on spheres.

## Key claim
For even $d \geq 4$ and any sphere $S_j = \{x \in \mathbb{F}_q^d : x_1^2+\cdots+x_d^2 = j\}$ with $j \neq 0$, the extension estimate $R^*(p \to 4) \lesssim 1$ holds for all $p \geq \frac{12d-8}{9d-12}$, strictly better than the Tomas–Stein threshold $p \geq \frac{4d-4}{3d-5}$. In odd $d \geq 3$ with $-1$ a square, the Tomas–Stein "$p$" exponent is sharp at $r \geq \frac{2d+2}{d-1}$ (cannot be improved without restrictions), because $S_j$ contains a $\frac{d-1}{2}$-dimensional affine subspace.

## Method
Reduces the $L^4$ extension bound to controlling the additive energy $\Lambda_4(E) = \#\{(x,y,z,k)\in E^4 : x+y = z+k\}$ for $E \subset S_j$. Expands via the explicit Fourier transform of the sphere indicator (Lemma 4: $\widehat{S_j}(m) = q^{-1}\delta_0(m) + Kq^{-(d+2)/2}\sum_{r\neq 0}\chi(jr + \|m\|^2/4r)$ when $d$ even, using that $\eta^d \equiv 1$ and Gauss sum $G^d(\eta,\chi) = Kq^{d/2}$), then bounds the resulting exponential sums via Weil/Salié estimates for (twisted) Kloosterman sums. A key auxiliary (Theorem 5) bounds $\#\{(x,y) \in E^2 : x\cdot y = j\} \lesssim q^{-1}|E|^2 + q^{(d-2)/2}|E|$.

## Result
Theorem 7: for even $d \geq 4$ and $E \subset S_j$,
$$\Lambda_4(E) \lesssim \min\{|E|^3,\; q^{-1}|E|^3 + q^{(d-2)/4}|E|^{5/2} + q^{(3d-4)/4}|E|^{3/2}\}.$$
Plugging into the dyadic / pigeonhole reduction yields $R^*\!\left(\frac{12d-8}{9d-12} \to 4\right) \lesssim 1$. Necessary-condition analysis (Theorem 2, Corollary 3) caps affine subspaces in $S_j$ at dimension $\leq (d-2)/2$ when $d$ even, leaving a conjectured optimum $r \geq p(d+2)/((p-1)d)$.

## Why it matters here
General background for finite-field harmonic analysis / extension theory; no direct Einstein Arena tie among the 23 problems. Relevant tangentially to discrete-geometry / incidence-counting problems where additive-energy bounds on algebraic varieties are used as an auxiliary tool, and to sphere-incidence reasoning over discrete structures.

## Open questions / connections
- Conjectured bound $r \geq p(d+2)/((p-1)d)$ in even $d \geq 4$ — Theorem 1 only partially supports it; gap to closure remains.
- Extension of the "$p$"-improvement to odd dimensions when $-1$ is a non-square (where the affine-subspace obstruction vanishes) — left open.
- Extends Mockenhaupt–Tao (paraboloids/cones, 2004) and Iosevich–Koh (non-degenerate quadrics, 2008); analogous techniques may apply to other quadratic-surface families.

## Key terms
extension theorem, restriction conjecture, finite field, sphere, Tomas–Stein exponent, Fourier transform, Gauss sum, Kloosterman sum, Salié sum, Weil bound, additive energy, incidence theorem, Mockenhaupt–Tao, quadratic surface, $\mathbb{F}_q^d$
