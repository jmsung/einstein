---
type: source
kind: paper
title: The fundamental Laplacian eigenvalue of the regular polygon with Dirichlet boundary conditions
authors: R. Jones
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1712.06082
source_local: ../raw/2017-jones-fundamental-laplacian-eigenvalue-regular.pdf
topic: general-knowledge
cites:
---

# The fundamental Laplacian eigenvalue of the regular polygon with Dirichlet boundary conditions

**Authors:** R. Jones  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1712.06082

## One-line
Extends the $1/S$ asymptotic expansion of the lowest Dirichlet Laplacian eigenvalue of the $S$-sided regular polygon by two new (conjectural) terms and numerically diagnoses the series' divergence for small $S$.

## Key claim
For the $\pi$-area regular polygon, $\lambda(S) \sim j_{01}^2 \left(1 + \tfrac{4\zeta(3)}{S^3} + \tfrac{(12-2j_{01}^2)\zeta(5)}{S^5} + \tfrac{(8+4j_{01}^2)\zeta^2(3)}{S^6} + \tfrac{(36-12j_{01}^2-12j_{01}^4)\zeta(7)}{S^7} + \tfrac{(48+8j_{01}^2+2j_{01}^4)\zeta(3)\zeta(5)}{S^8} + \cdots\right)$, with $C_1=C_2=C_4=0$; the $C_7, C_8$ terms are new conjectures, and the series appears to converge only for $S \geq 10$ (critical $S_{\rm cr} \approx 8.89 \pm 0.12$).

## Method
Compute fundamental eigenvalues to ~50 digits for $S = 5,\ldots,150$ using high-precision numerics (PARI/GP, several months CPU). Fit the truncated 38-term series via linear regression at 200-digit precision over $S=13,\ldots,150$ to extract numerical coefficients $C_\mu$. Use the LLL integer-relation algorithm on $C_7, C_8$ to recover closed forms as integer combinations of $\{1, j_{01}^2, j_{01}^4\}$ times $\zeta(7)$ or $\zeta(3)\zeta(5)$, with relative residuals $\sim 10^{-30}$.

## Result
The GSB result through $C_6$ is independently confirmed to 27-36 digits. Two new conjectural terms $C_7, C_8$ are identified analytically; relative truncation error of $\lambda^{[8]}(S)$ scales as $\approx -18.38/S^{7.86}$, giving 15-digit accuracy at $S=128$. Coefficients alternate in sign for $\mu>7$ and grow as $\ln|C_\mu| \sim 2.185\mu - 27.81$, implying asymptotic-only convergence with critical $S_{\rm cr} = e^a \approx 8.5$–$9.3$.

## Why it matters here
General background; no direct arena tie — the regular-polygon Laplacian problem is not among the 23 Einstein Arena problems. The methodology (high-precision numerics + LLL integer-relation recovery of closed-form coefficients from a divergent asymptotic series) is reusable wisdom for problems where analytical structure must be extracted from numerical data.

## Open questions / connections
- Can $C_9$ and higher be recovered? Author failed at 27-digit precision; needs more digits or a richer ansatz (e.g., $\zeta(3)^3$ alongside $\zeta(9)$).
- Is Boady's conjecture (zeta arguments are odd integers $\geq 3$) correct, or does the sequence track odd primes $\{3,5,7,11,\ldots\}$?
- What is the closed-form $\lambda(S)$ for which this is merely the asymptotic expansion? Only $S=3,4$ have known closed forms ($4\pi/\sqrt{3}$, $2\pi$).
- Extension to higher eigenvalues in the same symmetry class (replace $j_{01}$ with other Bessel roots) — relevant to Casimir-energy applications (Oikonomou 2010).

## Key terms
Laplacian eigenvalue, Dirichlet boundary, regular polygon, asymptotic expansion, Riemann zeta function, Bessel function roots, LLL integer relation algorithm, high-precision numerics, calculus of moving surfaces, Grinfeld-Strang, divergent asymptotic series, conformal mapping
