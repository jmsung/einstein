---
type: source
kind: paper
title: Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid
authors: R. Quilodrán
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1108.6324
source_local: ../raw/2011-quilodrn-nonexistence-extremals-adjoint-restriction.pdf
topic: general-knowledge
cites:
---

# Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid

**Authors:** R. Quilodrán  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1108.6324

## One-line
Proves sharp constants and nonexistence of extremizers for the $L^2 \to L^p$ adjoint Fourier restriction inequality on the hyperboloid $\mathbb{H}^d$ in the three even-integer endpoint cases $(d,p) \in \{(2,4),(2,6),(3,4)\}$.

## Key claim
The best constants are $H_{2,4} = 2^{3/4}\pi$, $H_{2,6} = (2\pi)^{5/6}$, $H_{3,4} = (2\pi)^{5/4}$, and no extremizer exists in any of these three cases; analogous nonexistence holds for the two-sheeted hyperboloid with $\bar H_{d,4} = (3/2)^{1/4} H_{d,4}$.

## Method
Adapts Foschi's convolution-form argument (originally for the cone / wave equation): rewrite $\|Tf\|_{L^{2k}}^{2k}$ as $\|(f\sigma)^{*k}\|_{L^2}^2$, compute the $n$-fold convolution $\sigma^{*n}$ of the hyperboloid measure explicitly, then bound it pointwise using Lorentz invariance to reduce to a 1D inequality. Cauchy–Schwarz / Hölder against $\|\sigma^{*n}\|_\infty$ gives a sharp constant; strict inequality on a Gaussian-like family $f_a(y)=e^{-a\sqrt{s^2+|y|^2}}$ (with explicit Ei-function asymptotics as $a\to 0^+$ or $\infty$) rules out extremizers by showing the supremum is only attained in a limit.

## Result
Sharp constants above are established with strict inequality $\|Tf\|_{L^p} < H_{d,p}\|f\|_{L^2}$ for every nonzero $f$. Extremizing sequences concentrate in frequency (escape to infinity) — analogous to the cone limit $s \to 0$ where extremizers do exist (Carneiro, Foschi). For the two-sheeted hyperboloid at $p=6$, only an upper bound $\bar H_{2,6} < (5/2)^{1/3} H_{2,6}$ (refined to $\bar H_{2,6} \le (\tfrac{5}{8}(4+3\sqrt 2))^{1/6} H_{2,6}$) is obtained.

## Why it matters here
General background; no direct arena tie. Relevant only as exemplar of the "convolution-form + sharp pointwise bound on $\sigma^{*n}$ + Lorentz invariance" template for sharp Fourier-extension inequalities, which could inform any future arena problem framed as a sharp $L^2 \to L^{2k}$ extension estimate.

## Open questions / connections
- Extension to $d=1$ for $p \ge 6$ even — blocked by combinatorial complexity of $\sigma^{*n}$ for $n \ge 3$.
- Existence of extremizers for non-even $p \in (4,6)$ on $\mathbb{H}^2$ — interpolation only gives upper bounds.
- Closes Foschi-type loop for hyperboloid; complements Carneiro (cone, $d=2,3$), Fanelli–Vega–Visciglia (existence for truncated/$p>$endpoint), Ramos (wave/cone $r=1/2$).

## Key terms
adjoint Fourier restriction, hyperboloid, Strichartz inequality, Klein-Gordon equation, sharp constants, extremizers nonexistence, Foschi method, convolution of measures, Lorentz invariance, concentration at infinity, exponential integral Ei, Quilodrán, Carneiro
