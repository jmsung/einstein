---
type: source
kind: paper
title: Eigenfunctions of the Fourier transform with specified zeros
authors: A. Feigenbaum, P. Grabner, D. Hardin
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.08558
source_local: ../raw/2019-feigenbaum-eigenfunctions-fourier-transform-specified.pdf
topic: general-knowledge
cites:
---

# Eigenfunctions of the Fourier transform with specified zeros

**Authors:** A. Feigenbaum, P. Grabner, D. Hardin  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.08558

## One-line
A unifying modular-forms framework that constructs Fourier eigenfunctions with prescribed double zeros at lattice distances, generalizing the Viazovska/Cohn-Gonçalves "magic function" constructions to all dimensions divisible by 4.

## Key claim
For every $d \equiv 0 \pmod 4$, there exist unique weakly holomorphic quasimodular forms (depth 2, weight $4 - d/2$) and modular forms (weight $2 - d/2$ for $\Gamma(2)$) whose Laplace transforms yield $\pm(-1)^{d/4}$-eigenfunctions of the Fourier transform with explicit last-sign-change locations — recovering $A^+(8)=\sqrt 2$, $A^+(12)=\sqrt 2$, $A^+(24)=\sqrt 2$, and giving new bounds $A^\pm(4) \le \sqrt 2$, $A^\pm(16) \le 2$, $A^\pm(20) \le 2$, $A^+(48) \le \sqrt 8$, $A^-(48) \le \sqrt 6$.

## Method
The integral transform $U(s) = -4\sin^2(\pi s/2) \int_0^{i\infty} \psi(z) e^{i\pi s z}\, dz$ produces $F(x) = U(\|x\|^2)$, a radial Schwartz function. Proposition 2.4 reduces the eigenfunction condition to two functional equations on $\psi$; for the $(-1)^{d/4}$ eigenvalue these force $z^{d/2-2}\psi(Sz)$ to be a weakly holomorphic quasimodular form of weight $4-d/2$, depth 2 (decomposable as $\psi_1 - 2E_2\psi_2 + E_2^2\psi_3$), while the $(-1)^{d/4+1}$ case gives a $\Gamma(2)$ modular form of weight $2-d/2$. Differential equations and recurrences then pin down the forms uniquely; Fourier-coefficient positivity is verified explicitly through dimension 312.

## Result
Beyond recovering the $d=8, 12, 24$ optimal functions, the paper produces explicit eigenfunctions in $\theta$-function and $E_2/E_4/E_6$ form for $d = 4, 16, 20, 48$. Theorem 3.2 establishes $F^+(x) \le 0$ for $\|x\|^2 \ge 2n + 2\ell - 2$ for all checked dimensions; Conjecture 1 asserts positivity of the quasimodular Fourier coefficients $a_w(m) > 0$ for $m \ge \lfloor w/4 \rfloor - 1$. The asymptotic packing bounds from this method are weaker than Kabatjanskii–Levenshtein for large $d$.

## Why it matters here
Directly informs the **Cohn–Elkies magic function** technique used for sphere-packing LP bounds and the **uncertainty-principle** problems (last-sign-change of $f$ and $\hat f$) — both core to Einstein Arena problems involving sphere packing, kissing numbers, and Bourgain–Clozel–Kahane-style functional inequalities. Gives the explicit modular-form recipe (with differential equations and recurrences) for constructing extremal radial Schwartz functions in any dimension $\equiv 0 \pmod 4$, not just $8, 12, 24$.

## Open questions / connections
- Conjecture 1: positivity of all but finitely many Fourier coefficients of the quasimodular forms $f_w$ (proved through $w=94$, open in general).
- The modular forms $\phi_w$ appear non-negative on $i\mathbb R_{>0}$ but coefficient positivity fails — proof obstructed by the $\log\lambda$ term except at $w=8,10,14$.
- Extends to $d \equiv 2 \pmod 4$ or odd $d$? The construction is dimension-divisible-by-4 only.
- Connection to Cohn–Kumar–Miller–Radchenko–Viazovska interpolation (arxiv 1902.05438) — uses similar quasimodular ingredients but for interpolation rather than uncertainty bounds.

## Key terms
Cohn–Elkies linear programming bound, magic function, Fourier eigenfunction, quasimodular form, weakly holomorphic modular form, $\Gamma(2)$ principal congruence subgroup, Eisenstein series $E_2$ $E_4$ $E_6$, Jacobi theta functions, modular lambda function, Bourgain–Clozel–Kahane uncertainty principle, last sign change, sphere packing, Viazovska, Cohn–Gonçalves, Laplace transform, Schwartz function
