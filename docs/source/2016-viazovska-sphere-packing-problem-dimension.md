---
type: source
kind: paper
title: The sphere packing problem in dimension 8
authors: Maryna Viazovska
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1603.04246v2
source_local: ../raw/2016-viazovska-sphere-packing-problem-dimension.pdf
topic: general-knowledge
cites: 
---

# The sphere packing problem in dimension 8

**Authors:** Maryna Viazovska  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1603.04246v2

## One-line
Viazovska proves that the $E_8$ lattice gives the densest sphere packing in $\mathbb{R}^8$ by constructing an explicit Cohn–Elkies magic function from modular forms.

## Key claim
$\Delta_8 = \pi^4/384 \approx 0.25367$, attained by the $E_8$-lattice packing; no packing of unit balls in $\mathbb{R}^8$ exceeds this density, and (combined with [4, §8]) the $E_8$ packing is the unique periodic densest packing.

## Method
Applies the Cohn–Elkies linear programming framework: finds a radial Schwartz function $g:\mathbb{R}^8\to\mathbb{R}$ with $g(x)\le0$ for $|x|\ge\sqrt{2}$, $\hat g\ge0$, and $g(0)=\hat g(0)=1$. The function is built as $g = \frac{\pi i}{8640}a + \frac{i}{240\pi}b$, where $a$ (Fourier $+1$-eigenfunction) and $b$ (Fourier $-1$-eigenfunction) are Laplace-transform-like contour integrals of weakly-holomorphic quasi-modular forms ($\phi_0,\phi_{-2},\phi_{-4}$ built from $E_2,E_4,E_6,j$; and $\psi_I,\psi_T,\psi_S$ built from theta functions $\theta_{00}^4,\theta_{01}^4,\theta_{10}^4$). Sign positivity of integrands $A(t),B(t)$ on $(0,\infty)$ is verified via truncated asymptotic expansions plus interval-arithmetic tail bounds.

## Result
Closes the Cohn–Elkies 2003 gap (previously a factor of only $1.000001$) exactly: the LP bound equals the $E_8$ density. The constructed $g$ has $g$ and $\hat g$ with double zeroes at every nonzero $\Lambda_8$ vector (forced by Poisson summation), proving Cohn–Elkies' Conjecture 8.1 in dimension 8 and yielding uniqueness of the densest periodic packing.

## Why it matters here
This is the canonical Cohn–Elkies magic-function construction — the single most important technique for any sphere-packing / kissing-number / LP-bound problem on Einstein Arena, especially anything touching $E_8$, $\Lambda_{24}$, autocorrelation-style $\hat f\ge0$ constraints, or Fourier-eigenfunction sign design. Templates the modular-form $\to$ Laplace-transform $\to$ Fourier eigenfunction pipeline that the Cohn–Kumar–Miller–Radchenko–Viazovska $d=24$ companion paper extends.

## Open questions / connections
- Direct sequel: Cohn–Kumar–Miller–Radchenko–Viazovska prove the analogous $d=24$ result for the Leech lattice using the same architecture.
- Generalization to "universal optimality" of $E_8$ and $\Lambda_{24}$ (energy minimization for all completely monotone potentials) — proved later by the same authors.
- Open: any other dimensions ($d=4,12,16$?) where a sharp LP magic function exists; current bounds in $4\le d\le 36$ remain non-sharp except $d=1,8,24$.
- Open: a conceptual / non-computational proof that avoids the interval-arithmetic positivity check of $A(t),B(t)$.

## Key terms
sphere packing, $E_8$ lattice, Cohn–Elkies linear programming bound, magic function, Fourier eigenfunction, Poisson summation, modular forms, Eisenstein series $E_2,E_4,E_6$, $j$-invariant, theta functions $\theta_{00},\theta_{01},\theta_{10}$, quasi-modular form, weakly holomorphic modular form, Laplace transform, Schwartz function, double zeroes on lattice, Viazovska, kissing number, LP bound
