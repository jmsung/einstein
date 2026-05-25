---
type: source
kind: paper
title: On Convergence Lemma and Convergence Stability for Piecewise Analytic Functions
authors: Xiaotie Deng, Hanyu Li, Ningyuan Li
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2204.01643v3
source_local: ../raw/2022-deng-convergence-lemma-convergence-stability.pdf
topic: general-knowledge
cites:
---

# On Convergence Lemma and Convergence Stability for Piecewise Analytic Functions

**Authors:** Xiaotie Deng, Hanyu Li, Ningyuan Li  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2204.01643v3

## One-line
Proves that for functions built from finite compositions of analytic mappings and the $\max$ operator, $\delta$-stationary points near an isolated local minimum shrink to that minimum as $\delta \to 0$, and uses this to characterize "convergence stability" of stationary points in nonsmooth nonconvex optimization.

## Key claim
**Convergence lemma (Thm 1.1):** if $f$ is a finite composition of analytic maps and $\max$, and $x^*$ is an isolated local minimum, then $\exists r_1>0$ s.t. $\forall \varepsilon>0,\exists \delta_0>0$: every $\delta$-stationary point in $B(x^*,r_1)\cap\Omega$ lies in $B(x^*,\varepsilon)$ whenever $\delta<\delta_0$. Analyticity is *necessary* — replacing analytic with $C^\infty$ breaks the lemma (explicit counterexamples using $x^2\sin(1/x)$ and $e^{-1/|x|}\sin(1/x)$). **Thm 1.3:** $x^*$ is convergence-stable iff it is an isolated local minimum.

## Method
Rewrite $\max$ via $\max\{a,b\}=(|a-b|+a+b)/2$, reducing $f$ to compositions of analytic maps and $|\cdot|$. Partition $\Omega$ by sign patterns $\sigma(x)=(\mathrm{sign}\,z_1,\dots,\mathrm{sign}\,z_{m-1})$ into semi-analytic cells $Q_s$ where $f$ agrees with an analytic $f_s$. Apply Łojasiewicz's stratification theorems for semi-analytic sets (extending Whitney's complex-analytic stratification) plus Whitney's condition (a) on tangent-space convergence between strata; argue by contradiction that a sequence of $\delta_k$-stationary points with $\delta_k\to 0$ must converge into a well-conditioned stratum and hence to $x^*$.

## Result
The stationary set $S=\{x:G_f(x)\geq 0\}$ (where $G_f(x)=\inf_{x'\neq x}\,Df(x,x')/\|x'-x\|$) is sub-analytic and decomposes into finitely many connected sub-analytic submanifolds $A_i$, on whose closures $f$ is constant (Thm 1.2). Consequently stationary points take only finitely many function values, and non-isolated local minima propagate along entire strata. Corollary 6.1 gives a quantitative recipe: with $\lambda_0=\tfrac{1}{2}\min_{\|x-x^*\|\in[0.8r,0.9r]}(f(x)-f(x^*))$ and $r_1$ the largest radius where $f\leq f(x^*)+\lambda_0$, $x^*$ is $(r_1,\lambda_0)$-convergence-stable.

## Why it matters here
General background; no direct arena tie. The paper's relevance to einstein is methodological — it formalizes when local optimizers can be *trusted* to stay near a minimum under numerical noise, which underwrites triple-verify intuitions: an isolated local minimum on a piecewise-analytic landscape is convergence-stable, but a degenerate / non-isolated one is not (relevant to P11 contact-graph rigidity, P14 tolerance band, P17 strict-tol trap where landscape flatness produces drift).

## Open questions / connections
- Quantitative rate: how does the radius $r_1(\varepsilon)$ in Thm 1.1 scale with $\varepsilon$ for piecewise-analytic $f$? Authors only get continuity, not the linear gradient↔loss bound available in strongly convex $C^1$.
- Probabilistic version: extend convergence stability to Gaussian-perturbation models (smoothed analysis [Spielman–Teng]) rather than worst-case $\delta$.
- Connection to Łojasiewicz inequality for subanalytic functions (Bolte–Daniilidis–Lewis 2007) — same toolkit underlies KL-property convergence proofs for gradient dynamics.

## Key terms
convergence lemma, convergence stability, piecewise analytic functions, semi-analytic sets, sub-analytic sets, Łojasiewicz stratification, Whitney condition (a), Clarke subdifferential, Dini directional derivative, $\delta$-stationary point, nonsmooth nonconvex optimization, isolated local minimum
