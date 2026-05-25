---
type: source
kind: paper
title: Polarization Problem on a Higher-Dimensional Sphere for a Simplex
authors: S. Borodachov
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.02165
source_local: ../raw/2020-borodachov-polarization-problem-higher-dimensional-sphe.pdf
topic: general-knowledge
cites:
---

# Polarization Problem on a Higher-Dimensional Sphere for a Simplex

**Authors:** S. Borodachov  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.02165

## One-line
Proves that the regular $d$-simplex inscribed in $S^{d-1}$ is the optimal $(d{+}1)$-point configuration for the maximal discrete polarization problem under a broad class of convex potentials.

## Key claim
For $d \ge 2$ and $f:[0,4]\to(-\infty,\infty]$ non-increasing and convex on $(0,4]$ with $f'$ either concave or convex on $(0,4)$, the vertices $\omega_d^*$ of a regular $d$-simplex inscribed in $S^{d-1}$ maximize $P_f(\omega_d, S^{d-1}) := \min_{x\in S^{d-1}} \sum_{i=0}^d f(|x-v_i|^2)$ over all $(d{+}1)$-point configurations, with $P_f(S^{d-1}) = f(4) + d\cdot f(2 - 2/d)$ (concave $f'$ case) or $f(0) + d\cdot f(2 + 2/d)$ (convex $f'$ case). Strict convexity of $f$ implies uniqueness up to isometry.

## Method
Reduces $p_f(x, \omega_d^*)$ to a one-variable sum $\sum g(t_i)$ with $g(t)=f(2-2t)$ under the constraints $\sum t_i = 0$, $\sum t_i^2 = (d+1)/d$ (Proposition 6.1, the "regular simplex identity"). Applies tangent-line / secant-line interpolation of the convex derivative $g'$ to bound the sum at extremal configurations $t_i \in \{-1, 1/d\}$ or $\{1, -1/d\}$. Combines with barycentric-coordinate geometry (averaging argument: some $b_i \le 1/(d+1)$) to handle arbitrary configurations via Lemmas 5.3–5.5.

## Result
$P_f(S^{d-1}) = f(4) + d\cdot f(2 - 2/d)$ when $f'$ is concave (Theorem 2.1); $P_f(S^{d-1}) = f(0) + d\cdot f(2 + 2/d)$ when $f'$ is convex (Theorem 2.2). Covers all completely monotone potentials (Riesz $s>0$, shifted Riesz $-2<s<0$, log, Gaussian $e^{-\sigma t}$). Also locates absolute min/max of $p_f(x,\omega_d^*)$ at antipodes $-\omega_d^*$ / vertices $\omega_d^*$ themselves (Theorem 2.4), and yields a short barycentric-coordinate proof of the optimal covering property: $\eta_{d+1}(S^{d-1}) = \sqrt{2 - 2/d}$ (Theorem 3.1).

## Why it matters here
Direct relevance to sphere-packing / kissing-number / energy-minimization problems where the regular simplex is the conjectured extremal small-$N$ configuration — establishes simplex optimality under a strictly broader class of potentials than Riesz-only prior work. The barycentric averaging argument ("some $b_i \le 1/(d+1)$" + secant-bound on $u(t) = f(2+2dt) + d\cdot f(2-2t)$) is a transferable proof technique for $(d{+}1)$-point extremal problems on $S^{d-1}$.

## Open questions / connections
- Extends Stolarsky 1975, Nikolov–Rafailov 2011/2013, Su 2015 (regular simplex for Riesz/shifted-Riesz only) to general convex-derivative potentials including Gaussian and log on $S^{d-1}$, $d \ge 3$.
- Open: $N > d+1$ on $S^{d-1}$ for $d \ge 2$ — the simplex argument breaks; only $N=4,6,12$ on $S^2$ (and a few more) have known exact polarization optima.
- The concavity-direction transition of $f'$ at $s=-2$ and $s=-4$ (where minimizer flips between $\omega_d^*$ and $-\omega_d^*$) explained structurally — useful diagnostic for other potential families.
- The polynomial-interpolation-of-$g'$ technique parallels Cohn–Elkies LP duality witnesses; potential cross-pollination with magic-function constructions.

## Key terms
maximal polarization, Chebyshev constant, regular simplex, sphere $S^{d-1}$, Riesz $s$-kernel, completely monotone, Gaussian kernel, logarithmic kernel, barycentric coordinates, optimal covering, convex derivative, Borodachov, Stolarsky, Nikolov-Rafailov
