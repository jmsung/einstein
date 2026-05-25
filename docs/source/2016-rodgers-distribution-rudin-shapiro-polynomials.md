---
type: source
kind: paper
title: On the distribution of Rudin–Shapiro polynomials and lacunary walks on SU(2)
authors: Brad Rodgers
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1606.01637
source_local: ../raw/2016-rodgers-distribution-rudin-shapiro-polynomials.pdf
topic: general-knowledge
cites:
---

# On the distribution of Rudin–Shapiro polynomials and lacunary walks on SU(2)

**Authors:** Brad Rodgers  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1606.01637

## One-line
Proves Saffari's and Montgomery's conjectures that normalized Rudin–Shapiro polynomial values $P_k(\omega)/\sqrt{2^{k+1}}$ become uniformly distributed in the unit disc as $k\to\infty$.

## Key claim
For $\omega$ uniform on the unit circle, $P_k(\omega)/\sqrt{2^{k+1}}$ converges in distribution to the uniform measure on $\mathbb{D}=\{|z|\le 1\}$ (Montgomery's conjecture), and in particular $|P_k(\omega)|^2/2^{k+1}$ becomes uniform on $[0,1]$ (Saffari's conjecture). Equivalently, the lacunary matrix product $g(\omega^{2^k})\cdots g(\omega)$ equidistributes to Haar measure on $SU(2)$, with $G(\omega^{2^k})\cdots G(\omega)$ equidistributing to Haar measure on $U(2)$.

## Method
Recast the inductive Rudin–Shapiro recursion as a matrix product $g(\omega^{2^k})\cdots g(\omega)\in SU(2)$ via a normalized $2\times 2$ unitary factor. Apply the Peter–Weyl/moment criterion: show $\mathbb{E}\,\pi(g(\omega^{2^k}))\cdots \pi(g(\omega))\to 0$ for every nontrivial irrep $\pi=t^\ell$ of $SU(2)$, by introducing a "halving" operator $S_\ell$ on Laurent-polynomial vectors and bounding its spectral radius $\rho(S_\ell)<1$ through a careful skew-diagonal elimination argument using properties of the unitary matrix $\tau^\ell$.

## Result
Theorems 1.1 (Saffari) and 1.2 (Montgomery) are established unconditionally; Theorem 1.3 gives Haar equidistribution on $SU(2)$, Lemma 1.4 establishes asymptotic independence of $\omega^{2^{k+1}-1}$ from $g(\omega^{2^k})\cdots g(\omega)$, and Theorem 1.5 lifts to Haar on $U(2)$. A consequence: Rudin–Shapiro polynomials provably do *not* satisfy a uniform lower bound $|P(z)|\gg\sqrt{N}$ on $|z|=1$ — they vanish on a non-negligible portion of the circle in the limit.

## Why it matters here
General background; no direct arena tie. Touches autocorrelation/flat-polynomial themes (Littlewood/$\pm 1$ coefficient polynomials, ultraflat construction) which are tangentially related to autocorrelation-inequality problems, but the techniques (SU(2) representation theory, lacunary CLT) are not currently invoked by the wiki's optimizer toolkit.

## Open questions / connections
- Do $\pm 1$ polynomials of arbitrarily high degree with $\sqrt{N}\ll|P(z)|\ll\sqrt{N}$ exist? (Open Littlewood flat-polynomial problem; numerical evidence in Odlyzko [21].)
- General conditions on $f:\mathbb{R}/\mathbb{Z}\to H$ ensuring $f(2^k t)\cdots f(t)$ equidistributes on compact $H$ — counterexample given for $H=\mathbb{Z}/2\mathbb{Z}$, so non-degeneracy + aperiodicity is not sufficient.
- Connection to noncommutative ergodic theorems (Karlsson–Ledrappier) and to Salem–Zygmund's classical CLT for lacunary trigonometric series.

## Key terms
Rudin–Shapiro polynomials, Saffari conjecture, Montgomery conjecture, lacunary series, Salem–Zygmund central limit theorem, SU(2) representation theory, Peter–Weyl theorem, Haar measure equidistribution, flat polynomials, Littlewood problem, ±1 coefficient polynomials, unimodular polynomials, autocorrelation, random matrix product
