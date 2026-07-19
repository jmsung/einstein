---
type: source
kind: paper
title: Three-point bounds for sphere packing
authors: Henry Cohn, David de Laat, Andrew Salmon
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.15373
source_local: ../raw/2022-cohn-three-point-bounds-sphere-packing.pdf
topic: general-knowledge
cites:
---

# Three-point bounds for sphere packing

**Authors:** Henry Cohn, David de Laat, Andrew Salmon  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.15373

## One-line
Extends the Cohn–Elkies two-point LP sphere-packing bound to a truncated three-point SDP bound, yielding the best known upper bounds on sphere-packing density in dimensions 4–7 and 9–16.

## Key claim
Theorem 1.1 introduces a truncated three-point bound: given $f_2 \geq 0$ continuous integrable with $f_2 \geq 0$ on $|x|\geq R$, and $f_3$ positive-definite-as-a-kernel with $f_2(x)+f_3(x,0)+f_3(0,x)+f_3(x,x)\leq 0$ for $r\leq|x|\leq R$ and $f_3(x,y)\leq 0$ on the truncated region, the packing density is bounded by $\mathrm{vol}(B^n_{r/2})(f_2(0)+f_3(0,0))$. Corollary 1.3: the LP bound is **not sharp** in $n\in\{12,16\}$ (their bound dips below the Cohn–Triantafillou dual lower bound on the LP bound itself).

## Method
Truncation radius $R$ confines $f_3$'s support, sidestepping Lemma 1.2's no-go (polynomial-times-Gaussian $f_3$ on all of $\mathbb{R}^n\times\mathbb{R}^n$ forces $f_3\equiv 0$). Two derivations: (i) truncated Poisson summation over periodic packings; (ii) limit of de Laat–Machado–Oliveira–Vallentin $k$-point bounds on growing compact sets $rC$. The SDP formulation parametrizes $f_3$ via $p_3(|x|^2,|y|^2,\langle x,y\rangle)\cdot e^{-\pi(|x|^2+|y|^2)}$ with sum-of-squares certificates over a semialgebraic set; a Taylor truncation $T(u)$ of $e^{-\pi u}$ handles the non-polynomial mixed constraint rigorously, verified via SDPA-GMP + Arb interval arithmetic.

## Result
With $r=1$, $d_2=24$, $d_3=9$, $d_{\text{taylor}}=24$: $n=3$ gives 0.770270 (vs LP 0.779747), $n=4$ gives 0.636108 (vs LP 0.647705), $n=12$ gives 0.079712, $n=16$ gives 0.024995 — strictly improving the LP and the de Laat–Oliveira–Vallentin strengthening in every dimension computed. Theorem 1.4 gives a *separate* three-point bound for **lattice** packing on the set $S_{\text{lat},n}=\{(x,y):|x|,|y|,|x\pm y|\in\{0\}\cup[r,\infty)\}$; at $d=13$ in $n=4$ it agrees with the $D_4$ density to 5 decimals (0.616858 vs 0.616850), motivating Conjecture 6.1 — a Viazovska-style magic function for $D_4$.

## Why it matters here
Directly relevant to sphere-packing problems on the arena: gives the current SOTA *upper bound* benchmark (any optimizer claiming to approach SOTA in $n\in\{4..7,9..16\}$ is bounded above by these numbers, not the LP bound). The truncation trick — and the Lemma 1.2 obstruction that motivates it — is a paradigmatic example of why "polynomial × Gaussian" parametrizations have a structural ceiling, informing parametrization-selection wisdom on any LP/SDP-bound problem.

## Open questions / connections
- Conjecture 6.1: does a Viazovska-style Schwartz function exist matching $D_4$ via the lattice three-point bound? (Open; would be a fourth sharp case after $n=1,8,24$.)
- Is the high-degree limit of $R(d_3)$ bounded, or does it diverge? Empirically $R$ stays small — "three-point interactions are most relevant over short distances."
- Extends Bachoc–Vallentin (kissing/spherical codes) and de Laat–Vallentin $k$-point hierarchy to the Euclidean (non-compact) sphere-packing setting for the first time.
- Li (2206.09876) subsequently ruled out LP sharpness in $n=3,4$ via dual bounds — complementary to Corollary 1.3.

## Key terms
sphere packing, three-point bound, semidefinite programming, Cohn-Elkies bound, linear programming bound, Delsarte, positive definite kernel, sum-of-squares, truncation radius, Poisson summation, lattice packing, D4 lattice, Bachoc-Vallentin, Viazovska, magic function, Lovász theta
