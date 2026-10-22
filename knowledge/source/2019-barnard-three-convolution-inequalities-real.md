---
type: source
kind: paper
title: Three convolution inequalities on the real line with connections to additive combinatorics
authors: R. Barnard, S. Steinerberger
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.08731
source_local: ../raw/2019-barnard-three-convolution-inequalities-real.pdf
topic: general-knowledge
cites:
---

# Three convolution inequalities on the real line with connections to additive combinatorics

**Authors:** R. Barnard, S. Steinerberger  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.08731

## One-line
Proves three sharp-ish convolution inequalities on $\mathbb{R}$ whose optimal constants encode hard open problems in additive combinatorics (generalized Sidon sets and difference bases).

## Key claim
Three results: (1) $\int_{-1/2}^{1/2}\!\int_\mathbb{R} f(x)f(x+t)\,dx\,dt \le 0.91\,\|f\|_{L^1}\|f\|_{L^2}$ (lower bound $\ge 0.8$); (2) $\min_{0\le t\le 1}\int_\mathbb{R} f(x)f(x+t)\,dx \le 0.411\,\|f\|_{L^1}^2$ (cannot be replaced by $0.37$); (3) review/restatement of the Cloninger–Steinerberger $1.28$ lower bound on $\max_t (f*f)(t)$ for $g$-Sidon sets (vs upper $1.52$).

## Method
Fourier analysis (Wiener–Khintchine: $\int f(x)f(x+t)dx = \int e^{-2\pi i\xi t}|\hat f(\xi)|^2 d\xi$) combined with the Hardy–Littlewood symmetric decreasing rearrangement inequality. For Theorem 1: case-split on $\|f\|_{L^2}^2/\|f\|_{L^1}^2 \gtrless 0.88$ and reduce to an ODE involving $\mathrm{Si}(x)=\int_0^x\!\sin(y)/y\,dy$. For Theorem 2: write $g(t)=\tfrac12\chi_{[-1,1]}+h$ and use $|\hat g(\xi)|\ge 0$ with the key constant $\inf_x \sin x/x \approx -0.217234$. Lower-bound constructions use the arcsine distribution $f(x)=\chi_{[-1/2,1/2]}/\sqrt{1-4x^2}$ — boundary singularity $\sim |1/2-|x||^{-1/2}$ exactly cancels the shrinking support as $t\to\pm 1$.

## Result
Theorem 1: $0.8 \le c_1 \le 0.91$ for the mixed $L^1$–$L^2$ averaged-autocorrelation constant; Gaussian-times-linear trial $(a,b,c)=(15,0.51,8.55)$ attains $0.802$. Theorem 2: $0.37 \le c_2 \le 0.411$ for the minimum autocorrelation; lower bound from a modified arcsine distribution with mass removed in the middle. Both constants connect to asymptotic densities of $g$-Sidon sets and (conjecturally) $g$-difference bases $\gamma_g(n) \sim \sigma(g)\sqrt{gn}$.

## Why it matters here
Direct background for autocorrelation-inequality problems (P15/P16-style) and difference-basis questions: identifies the arcsine distribution with $|1/2-|x||^{-1/2}$ boundary blow-up as the conjectured extremal density profile, and pinpoints $\inf_x \sin x/x \approx -0.217234$ as the universal constant emerging in autoconvolution sharp-constant problems. Extends prior wiki content on Cohn–Elkies / Bourgain–Clozel–Kahane uncertainty-principle constants by exhibiting the same constant in a dual additive-combinatorics setting.

## Open questions / connections
- Closed form for $c$ in $\min_t (f\star f)(t) \le c^{-1}\|f\|_{L^1}^2$? Golay conjectured "never in closed form" for the discrete analogue.
- Do $g$-difference bases have an asymptotic density profile with $\sim |1/2-|x||^{-1/2}$ boundary blow-up matching the extremal continuous function?
- Martin–O'Bryant improved-Hölder conjecture: $\|f*f\|_{L^2}^2 \le (1-c)\|f*f\|_{L^1}\|f*f\|_{L^\infty}$ with $c \le 0.1107$ (Matolcsi–Vinuesa); related to Bourgain–Clozel–Kahane $A(f)A(\hat f) \ge 0.2025$.
- Existence of an extremizer for Theorem 2; numerical attack on lower-bound constructions remains hard.

## Key terms
convolution inequality, autocorrelation, $g$-Sidon set, $g$-difference basis, arcsine distribution, Hardy–Littlewood rearrangement, Wiener–Khintchine, $\inf \sin x/x$, Bourgain–Clozel–Kahane, Cilleruelo–Ruzsa–Vinuesa, Steinerberger, Cloninger, Matolcsi–Vinuesa, Golay, sinc function, additive combinatorics
