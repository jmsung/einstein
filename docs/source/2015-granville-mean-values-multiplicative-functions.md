---
type: source
kind: paper
title: Mean values of multiplicative functions over function fields
authors: A. Granville, Adam J. Harper, K. Soundararajan
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1504.05409
source_local: ../raw/2015-granville-mean-values-multiplicative-functions.pdf
topic: general-knowledge
cites:
---

# Mean values of multiplicative functions over function fields

**Authors:** A. Granville, Adam J. Harper, K. Soundararajan  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1504.05409

## One-line
Adapts the authors' new proof of Halász's theorem on mean values of multiplicative functions to the polynomial ring $\mathbb{F}_q[x]$, where technical clutter from the integer case disappears and the core analytic ideas become transparent.

## Key claim
For $f$ in the class $\mathcal{C}(\kappa)$ (multiplicative on monics with $|\Lambda_f(F)| \le \kappa\Lambda(F)$), the mean value $\sigma(n) = q^{-n}\sum_{M\in\mathcal{M}_n} f(M)$ satisfies a Halász-type bound $|\sigma(n)| \le \tfrac{\kappa^2}{n}\int_0^1 \max_{|z|=\sqrt{t}} |F^\perp(z/q)|\,\tfrac{1-t^{n-1}}{1-t}\,dt + \tfrac{\kappa}{n}$ (Theorem 1.1), with the clean corollary $|\sigma(n)| \ll_\kappa (\kappa+1+M)e^{-M}(2n)^{\kappa-1}$ where $e^{-M}(2n)^\kappa := \max_{|z|=1/q}|F^\perp(z)|$.

## Method
A ternary contour-integral identity (Lemma 3.1) expresses $n\sigma^\perp(n)$ as an integral of three generating-function factors over $|z|=1/(q\sqrt{t})$; Cauchy–Schwarz / Parseval bounds two factors, and max-modulus controls the third. The function-field setting eliminates Perron-truncation errors and lets the proof proceed via clean power-series manipulation rather than Dirichlet-series analysis. A separate "Lipschitz" argument (Prop. 4.1 + Lemmas 5.1–5.2) compares $\sigma_\theta(n+\ell)$ to $\sigma_\theta(n)$ via the rotated parameter $\theta$ maximizing $|F^\perp(e(-\theta)/q)|$, with a Fourier expansion of $|\cos(\pi t)|$ governing the optimal exponent.

## Result
Lipschitz estimate (Theorem 1.3, $\kappa=1$): $|\sigma_\theta(n+\ell) - \sigma_\theta(n)| \ll (\ell/n)^{1-2/\pi}\log(2n/\ell) + (\log n)^{O(1)}/n^{1-c_m}$, where $m$ is the smallest odd integer not dividing $\ell$ and $c_m := \tfrac{1}{m}\mathrm{cosec}(\pi/2m)$ — so $c_m \searrow 2/\pi$ through odd $m$. The second term is a genuinely new phenomenon absent from the integer case; explicit examples with $\chi(k) = \mathrm{sign}(\cos(2\pi k/m))$ show it is sharp up to log factors (e.g. $m=3$: $\sigma(3n) = -\sigma(3n+1) \sim n^{-1/3}/\Gamma(2/3)$, $\sigma(3n+2)=0$, giving exponent $1-c_3 = 1/3$).

## Why it matters here
General background; no direct arena tie. Function-field mean-value technology is a clean playground for analytic-number-theory ideas (Halász, Wirsing integral equations, Selberg–Delange) that could inform sieve-theoretic or autocorrelation problems if such ever surface, but none of the 23 Einstein Arena problems currently lean on $\mathbb{F}_q[x]$ machinery.

## Open questions / connections
- Function-field analog of Granville–Soundararajan's optimal constant $\delta_1 = -0.656\ldots$ for $\pm 1$ completely multiplicative functions (Remark 8) — parity obstruction $f(F)=(-1)^{\deg F}$ blocks a direct port.
- Function-field analog of Koukoulopoulos's converse theorem (Remark 7): replace "$\sigma(n)=0$ for $n>k$" by "$|\sigma(n)| \ll n^{-A}$" and derive a dichotomy on $\chi(\ell)$ decay.
- Extends Elliott (1989), Granville–Soundararajan 2001/2003 mean-value spectrum work, and Wirsing's integral-equation framework to $\mathbb{F}_q[x]$.
- Smooth-polynomial count $N(n,m)$ deviates from the Dickman approximation $\rho(n/m)q^n$ when $n\approx m^2$ — a phenomenon with no $y$-smooth-integer parallel in the usual range $u\approx\log y$.

## Key terms
Halász theorem, multiplicative functions, function fields, $\mathbb{F}_q[x]$, mean values, Lipschitz estimate, Dickman function, smooth polynomials, Selberg–Delange, Wirsing integral equation, Dirichlet convolution, generating functions, Granville, Soundararajan, Harper, Koukoulopoulos
