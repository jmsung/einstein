---
type: source
kind: paper
title: On primes in arithmetic progressions and bounded gaps between many primes
authors: Julia Stadlmann
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2309.00425
source_local: ../raw/2023-stadlmann-primes-arithmetic-progressions-bounded.pdf
topic: general-knowledge
cites:
---

# On primes in arithmetic progressions and bounded gaps between many primes

**Authors:** Julia Stadlmann  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.00425

## One-line
Improves the exponent of distribution for primes in arithmetic progressions to smooth moduli from $1/2 + 7/300$ to $1/2 + 1/40$, and uses it to tighten upper bounds on bounded gaps containing many primes.

## Key claim
**Theorem 1:** For any $\varepsilon > 0$ there exists $\delta > 0$ such that the Bombieri–Vinogradov-type inequality (1.1) holds for moduli $q \le x^{1/2 + 1/40 - \varepsilon}$ restricted to squarefree $x^\delta$-smooth $q$ (i.e., $q \mid P(x^\delta)$). **Theorem 2:** $H_m = \liminf_{n\to\infty}(p_{n+m} - p_n) \ll \exp(3.8075\, m)$, improving Baker–Irving's $\exp(3.815\, m)$.

## Method
A modified $q$-van der Corput process applied to the Type I exponential sums of Polymath [13]. The key trick: by Chinese-remaindering $e_{md}(By/(n+Cd))$ into $e_d(\cdot) \cdot e_m(\cdot)$ and substituting $y/n \equiv c \pmod{d}$, the $d$-factor decouples from $(n,y)$, allowing Cauchy–Schwarz with **both** $n$ and $y$ on the inside. This shrinks the diagonal contribution from $\Delta^{3/2} N^{1/2} Y$ to $\Delta N / Y$, permitting larger $\Delta$ ($\Delta < N/Y$ vs. previously $\Delta < N/Y^2$) and better off-diagonal bounds via Deligne. Combined with Harman's sieve to obtain the $H_m$ bound.

## Result
- Exponent of distribution $1/2 + 1/40 = 0.525$ for smooth squarefree moduli, vs. Polymath's $1/2 + 7/300 \approx 0.5233$.
- $H_m \ll \exp(3.8075\, m)$ (vs. Baker–Irving's $\exp(3.815\, m)$, Polymath's $\exp((4 - 28/157)m)$).
- Concrete small-$m$ improvements via shorter admissible $k$-tuples (computed by Sutherland): $H_2 \le 396{,}504$ (from $k = 35{,}265$), $H_3 \le 24{,}407{,}016$, $H_4 \le 1{,}391{,}051{,}532$, $H_5 \le 77{,}510{,}685{,}234$.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems is a prime-gap or Bombieri–Vinogradov problem. The transferable wisdom is methodological: **decoupling variables before Cauchy–Schwarz** (the CRT substitution that frees $d$ from $(n,y)$) is a generic exponential-sum technique that could inform autocorrelation / character-sum problems if any arise; the **diagonal-vs-off-diagonal balance** ($\Delta < N/Y^2$ vs. $N/Y$) is a recurring optimization pattern.

## Open questions / connections
- Pushes toward (but does not reach) Elliott–Halberstam ($\theta = 1$) or even $\theta = 1/2 + 1/20$; the limiting case is now $N_1, \dots, N_5 \approx x^{0.2}$.
- Extends Polymath [13] and Baker–Irving [2]; complements Maynard's well-factorable estimates [9,10,11] and Lichtman [7] / Pascadi [12] which use different coefficient restrictions.
- Open: can the same CRT-decoupling trick be combined with Maynard's triply-well-factorable framework to push past $5/8$ (Pascadi)?

## Key terms
Bombieri–Vinogradov, Elliott–Halberstam, exponent of distribution, smooth moduli, $q$-van der Corput, Type I estimates, Deligne bounds, exponential sums, bounded prime gaps, $H_m$, admissible $k$-tuple, Heath-Brown identity, Linnik dispersion method, Harman's sieve, Chinese Remainder Theorem, Cauchy–Schwarz, Polymath, Maynard, Zhang
