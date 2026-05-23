---
type: source
kind: paper
title: SPHERE PACKING BOUNDS VIA SPHERICAL CODES
authors: Henry Cohn, Yufei Zhao
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1212.5966
source_local: ../raw/2012-cohn-sphere-packing-bounds-spherical.pdf
topic: general-knowledge
cites:
---

# SPHERE PACKING BOUNDS VIA SPHERICAL CODES

**Authors:** Henry Cohn, Yufei Zhao  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1212.5966

## One-line
Improves the Kabatiansky–Levenshtein (KL) sphere-packing upper bound by a constant factor via a simpler geometric reduction, proves the Cohn–Elkies LP bound always dominates KL, and extends both to hyperbolic space.

## Key claim
For all $n \ge 1$ and $\pi/3 \le \theta \le \pi$, $\Delta_{\mathbb{R}^n} \le \sin^n(\theta/2)\, A(n,\theta)$ (vs. the old $A(n+1,\theta)$); the Cohn–Elkies LP bound $\Delta^{LP}_{\mathbb{R}^n} \le \sin^n(\theta/2)\, A^{LP}(n,\theta)$ subsumes KL; hyperbolic packing density obeys $\sup_{r>0} \Delta_{\mathbb{H}^n}(r) \le 2^{-(0.5990\ldots + o(1))n}$, exponentially improving Böröczky/Rogers.

## Method
Geometric: place a sphere of radius $R \le 2$ in $\mathbb{R}^n$ (not $\mathbb{R}^{n+1}$) containing many packing centers, project radially, and use a law-of-cosines lemma to show projected centers are still $\theta$-separated where $\sin(\theta/2)=1/R$. LP comparison: given any KL auxiliary $g$ on the sphere, construct a Cohn–Elkies $f$ on $\mathbb{R}^n$ by $f(x-y) = \int_{B_R(x)\cap B_R(y)} g(\langle \widehat{x-z}, \widehat{y-z}\rangle)\,dz$, which is automatically positive-definite (via $\chi_R$ kernel trick) and matches the bound. Hyperbolic case uses the Bowen–Radin ergodic packing framework plus the Selberg pre-trace formula in place of Poisson summation.

## Result
Constant-factor improvement: replacing $A(n+1,\theta)$ with $A(n,\theta)$ saves a factor $A_{n+1}/A_n$ with geometric mean $\approx 1.2635$ (exponential rate $0.5990\ldots$ unchanged). Theorem 3.4: $\Delta^{LP}_{\mathbb{R}^n} \le \sin^n(\theta/2) A^{LP}(n,\theta)$ for $\pi/3 \le \theta \le \pi$, settling that Cohn–Elkies $\ge$ KL asymptotically (analogue of Rodemich's theorem). Theorem 4.1 (hyperbolic): $\Delta_{\mathbb{H}^n}(r) \le \sin^{n-1}(\theta/2) A(n,\theta)$, radius-independent. Theorem 5.7: periodic hyperbolic packings obey a Cohn–Elkies-style LP bound $\Delta \le \mathrm{vol}(B_r^n)\, \hat f(0)/f(0)$ provided $\hat f \ge 0$ everywhere (not just on the Plancherel support — Selberg eigenvalue obstruction).

## Why it matters here
Directly informs sphere-packing strategy (P1 and related): clarifies the LP-vs-KL hierarchy (Cohn–Elkies is provably $\ge$ KL, so LP magic functions are the right asymptotic frontier) and tightens the high-dimensional upper bound numerically (Appendix A gives explicit $n=12\ldots600$ numbers, correcting [CS99] errors). The $f(x-y) = \int g(\cos\angle)$ construction is a reusable "geometric lift" template for translating spherical positive-definite kernels into Euclidean ones.

## Open questions / connections
- Can the analogue of Theorem 3.4 be proved for the *full* Cohn–Elkies bound in hyperbolic space (Conjecture 5.1 — open for non-periodic packings; obstruction is the Plancherel measure not containing $0$).
- Selberg's eigenvalue conjecture controls whether the $\hat f \ge 0$ everywhere hypothesis can be weakened to "on $[(n-1)^2/4, \infty)$" for arithmetic groups.
- Lower-bound side remains stuck at $2^{-(1+o(1))n}$ despite Vance/Venkatesh improvements — exponential gap with the $0.5990\ldots$ upper bound persists.
- Improving the Rogers bound conceptually in low $n$ (LP does it numerically with 8 forced double roots but no clean explanation).

## Key terms
sphere packing, Kabatiansky-Levenshtein bound, Cohn-Elkies linear programming bound, spherical codes, Gegenbauer polynomials, Delsarte-Goethals-Seidel, positive-definite functions, Schoenberg theorem, Bochner theorem, Rodemich theorem, hyperbolic sphere packing, Bowen-Radin density, Böröczky bound, Selberg trace formula, Plancherel measure, magic function
