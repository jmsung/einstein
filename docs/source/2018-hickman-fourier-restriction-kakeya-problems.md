---
type: source
kind: paper
title: The Fourier restriction and Kakeya problems over rings of integers modulo N
authors: J. Hickman, James Wright
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.03176
source_local: ../raw/2018-hickman-fourier-restriction-kakeya-problems.pdf
topic: general-knowledge
cites:
---

# The Fourier restriction and Kakeya problems over rings of integers modulo N

**Authors:** J. Hickman, James Wright  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.03176

## One-line
Formulates and partially resolves the Fourier restriction and Kakeya conjectures over the ring $\mathbb{Z}/N\mathbb{Z}$, showing the numerology and methods mirror the Euclidean case far more closely than the finite-field model does.

## Key claim
With the scale-aware norm $|x|:=N/\gcd(x,N)$, the discrete Stein–Tomas restriction estimate for the paraboloid $\Sigma=\{(\omega,\omega_1^2+\cdots+\omega_{n-1}^2)\}\subset[\mathbb{Z}/N\mathbb{Z}]^n$ holds (with $N^\varepsilon$ loss) at $s=2$ iff $1\le r\le 2(n+1)/(n+3)$ — exactly the Euclidean range, up to endpoints.

## Method
A "correspondence principle" lifts restriction problems on $\mathbb{Z}/p^\alpha\mathbb{Z}$ to the $p$-adic field $\mathbb{Q}_p$, exploiting that the $p$-adic unit ball is a subgroup (sharp uncertainty principle). Divisors of $N$ supply multiple scales, enabling a discrete Knapp example, wave-packet decomposition, $d$-tubes, and a Kakeya maximal operator on $[\mathbb{Z}/N\mathbb{Z}]^n$ via projective directions $P^{n-1}(\mathbb{Z}/N\mathbb{Z})$. Gauss-sum decay $|G_N(a,b)|=|b|^{-1/2}$ when $|a|\preceq|b|$ plays the role of stationary phase.

## Result
Establishes (i) the $s=2$ Stein–Tomas range for the paraboloid mod $N$, (ii) full $r$–$s$ restriction for the parabola ($n=2$) matching Fefferman–Zygmund (Thm 7.11: $r\ge 4$, $r\ge 3s$), (iii) a Kakeya maximal/set conjecture over $\mathbb{Z}/N\mathbb{Z}$ implied by restriction, and (iv) reduces the moment-curve restriction estimate to a solution-counting conjecture $N(\vec y;N)\le C_\varepsilon N^\varepsilon \prod_{j<k}\gcd(y_j-y_k,N)$ (Conjecture 7.6), proven for $n=2,3$ via Hensel's lemma.

## Why it matters here
General background; no direct arena tie — restriction/Kakeya theory and Gauss-sum / $p$-adic stationary-phase machinery may inform autocorrelation (P14) and uncertainty-type problems, but the specific bounds here are model-setting, not arena-applicable.

## Open questions / connections
- Conjecture 7.6 (solution counts for the Vinogradov-type system $\sum x_j^k\equiv\sum y_j^k$) open for $n\ge 4$; would yield moment-curve restriction in the range $r\ge n(n+2)/2$.
- Full Kakeya maximal conjecture (14) over $\mathbb{Z}/N\mathbb{Z}$ open; finite-field Kakeya (Dvir) does not transfer because scale structure differs.
- Connects to Denef–Sperber / Igusa exponential-sum methods (cites [12], [28]) for systems of polynomial congruences.

## Key terms
Fourier restriction, Kakeya conjecture, Stein–Tomas theorem, paraboloid, $p$-adic analysis, Gauss sums, wave packet decomposition, Knapp example, Hensel's lemma, Vinogradov mean value, moment curve, projective space over $\mathbb{Z}/N\mathbb{Z}$, Mockenhaupt–Tao, Christ multilinear inequality
