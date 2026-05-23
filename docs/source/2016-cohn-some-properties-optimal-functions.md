---
type: source
kind: paper
title: Some properties of optimal functions for sphere packing in dimensions 8 and 24
authors: Henry Cohn, Stephen D. Miller
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.04759
source_local: ../raw/2016-cohn-some-properties-optimal-functions.pdf
topic: general-knowledge
cites:
---

# Some properties of optimal functions for sphere packing in dimensions 8 and 24

**Authors:** Henry Cohn, Stephen D. Miller  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.04759

## One-line
Constructs explicit sequences of Gaussian-times-polynomial functions, with a priori (perturbed) forced root locations at lattice vector lengths, conjectured to converge to the Cohn–Elkies magic functions for $E_8$ and the Leech lattice.

## Key claim
If the sequences $f_k$ defined by forcing single/double roots at the modified locations $r_m^2 = m + \frac{1}{4}\left(\frac{m - \lceil 2k/3\rceil}{k - \lceil 2k/3\rceil}\right)^2 \cdot m$ (for $m \geq 2k/3$) converge uniformly on a neighborhood of $\mathbb{R}$ and have no non-forced real roots, then the Cohn–Elkies conjecture (and hence exact sphere packing optimality of $E_8$ and Leech) follows in dimensions 8 and 24.

## Method
Cohn–Elkies linear-programming framework: seek admissible $f$ with $\hat f \geq 0$, $f \leq 0$ outside ball of radius $r$. Take $f(x) = p(|x|^2)e^{-\pi|x|^2}$ with $p$ a polynomial of degree $4k-1$ subject to $4k$ linear constraints — forced roots of $f$ and $\hat f$ at the (modified) lattice vector lengths. Diagonalize via Laguerre polynomials $L_j^{n/2-1}$ which are radial Fourier eigenfunctions with eigenvalue $(-1)^j$; split into $\pm 1$ eigenspaces for ~4× speedup. The key insight: using *exact* lattice lengths fails (Runge-like phenomenon — unwanted oscillations emerge by $k \approx 40$ for $n=8$); perturbing the top third of roots outward by up to 25% restores convergence.

## Result
Numerical bounds sharp to >50 decimal places: at $k=600$, density bound is $1 + 6.32 \times 10^{-60}$ times optimal in $\mathbb{R}^8$ and $1 + 7.28 \times 10^{-51}$ in $\mathbb{R}^{24}$ (vs. $10^{-14}$ and $10^{-30}$ in Cohn–Kumar 2009). Lemma 5.1: $f'(r_1) = -\frac{n}{N r_1} \hat f(0)$ where $N$ = kissing number (240 for $E_8$, 196560 for Leech). Conjecture 5.2: quadratic Taylor coefficients are rational — $-27/10$ and $-3/2$ for $n=8$; $-14347/5460$ and $-205/156$ for $n=24$. Conjecture 5.3: $Mf(4) = M\hat f(4) = 1/15$ for $n=8$.

## Why it matters here
Direct input to the Cohn–Elkies magic-function technique used across arena LP-bound problems (sphere packing, kissing number, autocorrelation). The "perturb the top third of forced roots" recipe is a transferable optimization heuristic when naive lattice-length root forcing causes Runge-style oscillations. Predates Viazovska's $n=8$ proof (March 2016, [V]) by days; the $n=24$ case remained open at publication.

## Open questions / connections
- Closed-form power series for $f, \hat f$ — quadratic Taylor coefficients are rational, but higher coefficients (quartic onward) remain mysterious.
- Why do complex roots of $f_k$ and $\hat f_k$ nearly coincide far from origin? They lie on visible curves accumulating on a domain-of-holomorphy boundary.
- Conjecture 6.1 extends the framework to Gaussian-core energy minimization on $E_8$ / Leech; duality $h \leftrightarrow \phi - h$ preserves optimality.
- Section 7 "forced single roots" $g_{n,k}^\varepsilon$ — closed forms exist when $4 \mid n$ via $\sin(\pi|x|^2/2) e^{-\pi\sqrt 3 |x|^2/2}$ shifted by $(\sqrt 3/2 + i/2)$ being a 12th root of unity; the other eigenfunction has mysterious near-integer imaginary roots.
- Conjectures appear to hold for $0 < n < 10$ (E8 roots) and $0 < n < 26$ (Leech roots) — suggests proof need not depend on dimension-specific modular-form magic.

## Key terms
Cohn-Elkies conjecture, magic function, sphere packing, E8 lattice, Leech lattice, Poisson summation, Laguerre polynomials, Fourier eigenfunctions, Hermite interpolation, Runge phenomenon, forced roots, Gaussian-times-polynomial, Viazovska, Mellin transform, kissing number, universal optimality, Gaussian core model, LP bounds
