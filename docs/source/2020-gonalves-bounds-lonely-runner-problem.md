---
type: source
kind: paper
title: Bounds for the Lonely Runner Problem via Linear Programming
authors: Felipe Gonçalves, João P. G. Ramos
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2010.02271v2
source_local: ../raw/2020-gonalves-bounds-lonely-runner-problem.pdf
topic: general-knowledge
cites: 
---

# Bounds for the Lonely Runner Problem via Linear Programming

**Authors:** Felipe Gonçalves, João P. G. Ramos  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2010.02271v2

## One-line
Develops a linear programming framework using even trigonometric polynomials to produce upper and lower bounds for the gap of loneliness in the Lonely Runner Conjecture.

## Key claim
For any vector $v = (v_1,\ldots,v_{n-1})$ of increasing positive integer speeds, $\lambda_-(v) \le \text{gap}(v) \le \lambda_+(v)$, where $\lambda_\pm(v)$ are LP values over classes $\Lambda_\pm(v)$ of even trigonometric polynomials of degree $\le \max(v_i)$ with constrained Fourier support $\{0, v_1, \ldots, v_{n-1}\}$ and one-sided positivity conditions; equality in the upper bound is characterized in three explicit cases (all $v_i$ odd; arithmetic-progression-of-multiples structure; integer dilation thereof).

## Method
LP-duality / Selberg-Beurling-style extremal problem in Fourier analysis: minimize/maximize $\hat f(0)/f(0)$ over even trig polynomials $f$ supported on speed indices, with sign constraint $f \ge 0$ on $[0, 1/2]$ (upper bound) or $f \ge 0$ on $[1/(v_{n-1}+v_{n-2}), 1/2]$ (lower bound). Proof pairs $f$ against the hat-function $h(x)=(\delta-|x|)_+$ whose Fourier transform is $(\sin(\pi\delta k)/\pi k)^2 \ge 0$, mirroring Montgomery's analytic proof of Dirichlet's approximation theorem. Solved numerically with Gurobi using sampling for the sign condition; Fejér's kernel $K_n$ realizes optimality for $v=(1,\ldots,n-1)$.

## Result
Theorem 1 establishes the LP sandwich $\lambda_-(v) \le \text{gap}(v) \le \lambda_+(v)$. Theorem 2 characterizes tight upper-bound cases with explicit optimizers ($\cos(\pi v_i x)^2$ when all $v_i$ odd; $K_m(ax)$ for Fejér-kernel-type structure). Theorem 3 improves the lower bound on $v \in V_q$ (vectors whose $t \mapsto \mu(tv)$ attains its max at $t=p/q$) via a stronger sign constraint $f \ge 0$ on $[1/q, 1/2]$, with optimizer $K_q(ax)\cdot(1-\cos(\pi/q))^{-2}(\cos(\pi a x)^2-\cos(\pi/q)^2)$. Computer search ($n \le 20$, $|v|_\infty \le 40$) finds no equality cases outside Theorem 2, motivating an "iff" conjecture.

## Why it matters here
Provides a clean LP/Fourier-extremal template — sign-constrained trig polynomial with prescribed Fourier support paired against a positive-Fourier-transform test function — that generalizes Cohn–Elkies / Selberg-style bounds and could plug into autocorrelation, sphere-packing, or kissing-number LP formulations on the arena. The dual structure (upper bound via $\ge 0$ on $[0,1/2]$, lower via complementary interval) is a transferable design pattern for two-sided extremal bounds.

## Open questions / connections
- Is the conjectured iff-characterization of upper-bound tightness (Theorem 2 cases only) provable, perhaps via the rigidity argument that forced Fejér's kernel as unique optimum for $v=(1,\ldots,n-1)$?
- Can the weak $\lambda_-(v)$ bound be strengthened uniformly (not just on $V_q$) by a smarter sign-region or a polynomial-degree boost — and what determines feasibility/degree trade-offs?
- Connections: Montgomery (1994) analytic Dirichlet proof; Bohman–Holzman–Kleitman (2001) $n=6$ resolution; Tao (2018) remarks; Goddyn–Wong (2006) tight-instance characterizations.

## Key terms
lonely runner conjecture, linear programming bounds, Fejér kernel, trigonometric polynomial extremal problem, Fourier sign constraint, Selberg-Beurling extremal, Dirichlet approximation, Montgomery, Cusick, view obstruction, gap of loneliness, autocorrelation inequality, LP duality, Gurobi
