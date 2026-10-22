---
type: source
kind: paper
title: An almost-tight $L^2$ autoconvolution inequality
authors: E. White
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2210.16437
source_local: ../raw/2022-white-almost-tight-autoconvolution-inequality.pdf
topic: general-knowledge
cites:
---

# An almost-tight $L^2$ autoconvolution inequality

**Authors:** E. White  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2210.16437

## One-line
Pins down the minimum $L^2$ norm of the autoconvolution $f*f$ over densities $f$ on $[-1/2,1/2]$ to within $\sim 0.0014\%$, yielding improved upper bounds on $B_h[g]$ set sizes for several $(g,h)$.

## Key claim
For $\mathcal{F} = \{f:[-1/2,1/2]\to\mathbb{R}, \int f = 1\}$ and $\mu_2 = \inf_{f\in\mathcal{F}} \|f*f\|_2$, the bounds tighten to $0.574635728 \le \mu_2^2 \le 0.574643711$ (vs prior $0.574575 \le \mu_2^2 \le 0.640733$). A unique minimizer $f_\diamond \in \mathcal{F}$ exists, and $F_\diamond * F_\diamond * F_\diamond$ is constant $= \mu_2^2/4$ on $(-1/2,1/2)$.

## Method
Reformulate $\|f*f\|_2^2 = \|\hat f\|_4^4$ via Parseval; truncate Fourier series to degree $T$ to get a finite **quadratically constrained linear program (QCLP)** with redundant variables $\{w_k, x_k, y_m, z_m\}$ enforcing $x_k \ge \hat f(k)^4$, solved by CPLEX at $R=4000, T=30000$. Upper bound: evaluate $\|f_P*f_P\|_2^2$ on the numerical optimizer with explicit tail estimates using $|\hat F(m)| \le 2/(m\pi)\sum|\hat f(k)|$. Lower bound: a Hölder-duality trick (Lemma 8) — for any periodic $g$ with $\int g = 2$, $\mu_2^2 \ge 1/(2\sum|\hat G(m)|^{4/3})^3$, tight when $\hat g(k) \propto \hat f_\diamond(k)^3$; choosing $g_P$ from the cubed Fourier coefficients of $f_P$ converts the good upper-bound construction into a good lower bound.

## Result
$\mu_2^2 \in [0.574635728, 0.574643711]$. Via Green's methods (Theorem 10 with $\gamma(g) = 2\mu_2^2 - 1$ replacing the old $1/7$), improved Sidon-type asymptotics:
$$\sigma_2(g) \le \left(\frac{2-1/g}{\mu_2^2}\right)^{1/2}, \quad \sigma_3(1) \le (2/\mu_2^2)^{1/3}, \quad \sigma_4(1) \le (4/\mu_2^2)^{1/4}.$$
Also: additive energy $\sum_{a+b=c+d} H(a)H(b)H(c)H(d) \ge \mu_2^2 N^3$ for any $H:[N]\to\mathbb{R}$ with $\sum H = N$. Appendix: the family $f_c(x) = \alpha_c (1/4 - x^2)^c$ (arcsine-like, $c \approx 0.4942$) attains $\|f*f\|_2^2 \approx 0.5746482$ — within $4.5\times 10^{-6}$ of the QCLP bound, a closed-form near-optimizer.

## Why it matters here
Direct relevance to P14 / autoconvolution-norm problems and to Sidon / $B_h[g]$ counting (P-family using extremal set theory). The QCLP-from-Fourier-truncation pattern is a portable template: any convolution-type extremal problem with Parseval structure can be attacked this way, complementing the LP / SDP / basin-hopping methods already in the wiki. The upper-bound-feeds-lower-bound duality (Lemma 8) is a methodological lesson worth importing: a good construction yields *both* bounds simultaneously via Hölder.

## Open questions / connections
- Extends Green 2001 (the prior $\mu_2$ bound holder) and Martin–O'Bryant 2007; complements Cloninger–Steinerberger / Matolcsi–Vinuesa on the $\|f*f\|_\infty$ side (still wide: $0.64 \le \inf \|f*f\|_\infty \le 0.75496$).
- Analogous QCLP approach for $\mu_p$, $p \ne 2$ — explicitly suggested by the author; the $L^\infty$ case is the obvious next target.
- Is the true $\mu_2^2$ closer to the upper or lower end of $[0.574635728, 0.574643711]$? The $f_c$ family hits the upper bound to $10^{-6}$, suggesting the QCLP upper bound is essentially tight.
- Convergence rate $O(R^{-1/6})$ of the program is slow — better truncation / preconditioning could enable higher $T$.

## Key terms
autoconvolution, $L^2$ norm, Sidon set, $B_h[g]$ set, Fourier truncation, quadratically constrained linear program, Parseval identity, Hölder duality, Bose–Chowla, Green, Martin–O'Bryant, arcsine distribution, additive energy, three-fold convolution flatness
