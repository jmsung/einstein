---
type: source
kind: paper
title: Two-derivative error inhibiting schemes with post-processing
authors: Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1912.04159v1
source_local: ../raw/2019-ditkowski-two-derivative-error-inhibiting-schemes.pdf
topic: general-knowledge
cites: 
---

# Two-derivative error inhibiting schemes with post-processing

**Authors:** Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1912.04159v1

## One-line
Extends the error-inhibiting general linear method (EIS) framework to two-derivative GLMs, so a scheme of truncation order $p$ delivers global order $p+1$, and order $p+2$ after a cheap linear post-processor.

## Key claim
For a zero-stable two-derivative GLM $V^{n+1} = DV^n + \Delta t A F(V^n) + \Delta t R F(V^{n+1}) + \Delta t^2 \hat A \dot F(V^n) + \Delta t^2 \hat R \dot F(V^{n+1})$ with rank-one consistent $D$ and order conditions $\tau_j=0$ for $j\le p$, the three EIS+ conditions $D\tau_{p+1}=0$, $D\tau_{p+2}=0$, $D(A+R)\tau_{p+1}=0$ force the global error to the form $E^n = \Delta t^{p+1}\tau_{p+1}^n + O(\Delta t^{p+2})$, whose leading term is removable by a Vandermonde-based post-processor — yielding explicit schemes to order 8, explicit SSP schemes to order 7, and A-stable implicit schemes to order 5.

## Method
Discrete Duhamel decomposition of the error recursion $E^{n+1} = (I-\Delta t R F_y^n)^{-1}[(D + \Delta t A F_y^n)E^n + \tau^{n+1}] + O(\Delta t^2)$ into four pieces (initial, last-step truncation, second-to-last propagated, bulk sum); the three null-space conditions on $D$ kill the bulk-sum and intermediate contributions, leaving an isolated leading term that an $ms\ge p+3$ flipped-Vandermonde filter $\Phi = T\,\mathrm{diag}(0,1,\dots,1)\,T^{-1}$ annihilates. Coefficients of D, A, R, $\hat A$, $\hat R$ are then found by Matlab optimization with stability (linear / SSP / A-stable) as objective and order + EIS+ conditions as constraints.

## Result
Explicit eEIS+ methods up to order 8 (e.g. eEIS+(4,8)$_2$ with 4 stages), explicit SSP eSSP-EIS+ methods up to order 7 with SSP coefficient $C\approx 1.08$ for (3,6), and A-stable diagonal-$R,\hat R$ implicit iEIS+ methods to order 5 — all with explicit $\tau_{p+1}$ vectors for post-processing. Van der Pol convergence test confirms predicted slopes (4.7→5.8 for (2,6), 7.0→7.7 for (4,8), 3.0→4.0 for iEIS+(2,4), 3.9→5.0 for iEIS+(3,5)); linear advection step-function test shows SSP coefficients beat their guarantees and post-processing leaves total variation essentially unchanged ($\approx 10^{-15}$).

## Why it matters here
General background; no direct arena tie — Einstein Arena problems are static optimization (packing / extremal / autocorrelation), not time-evolution ODEs, so two-derivative GLM machinery is out of scope. The only weak adjacency is the *Vandermonde post-processor trick* (recover one extra order of accuracy from a structured residual) as a generic mathematical pattern, but the wiki has no current consumer for it.

## Open questions / connections
- Extends Ditkowski–Gottlieb–Grant 2019 (arxiv 1910.02937) from one-derivative to two-derivative GLMs; same proof scaffold, only $\tau$ definition changes — suggests trivial extension to $k$-derivative GLMs.
- Authors flag nonexistence questions: no eSSP-EIS(2,5)$_2$ or eSSP-EIS(3,7)$_2$ found despite searching — proof of nonexistence open.
- Connection to Kulikov / Weiner quasi-consistency theory (Skeel 1978) — same superconvergence phenomenon, different sufficient-condition framework.

## Key terms
general linear method, two-derivative Runge-Kutta, error inhibiting scheme, EIS+, post-processing, superconvergence, strong stability preserving, SSP coefficient, A-stable, truncation error, Vandermonde filter, quasi-consistency, Lax-Richtmyer equivalence, Ditkowski, Gottlieb, Grant
