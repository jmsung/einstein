---
type: source
kind: paper
title: An elementary approach to Gaussian multiplicative chaos
authors: N. Berestycki
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.09113
source_local: ../raw/2015-berestycki-elementary-approach-gaussian-multiplicative.pdf
topic: general-knowledge
cites:
---

# An elementary approach to Gaussian multiplicative chaos

**Authors:** N. Berestycki  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.09113

## One-line
An elementary, self-contained proof that Gaussian multiplicative chaos (GMC) measures $\mu_\varepsilon(dx) = e^{\gamma h_\varepsilon(x) - \tfrac{\gamma^2}{2}\mathbb{E}[h_\varepsilon(x)^2]}\sigma(dx)$ converge in probability and in $L^1$ to a nontrivial universal limit throughout the entire subcritical phase $\gamma < \sqrt{2d}$.

## Key claim
For any log-correlated centered Gaussian field with covariance $K(x,y) = \log|x-y|^{-1} + g(x,y)$ ($g$ continuous), any Radon reference measure $\sigma$ of dimension $\geq d$, and any mollifier $\theta$ satisfying $\int|\log|x-y||\,\theta(dy) < \infty$: $\mu_\varepsilon(S)$ converges in probability and in $L^1(P)$ to a nontrivial limit $\mu(S)$ independent of $\theta$, for every $\gamma < \sqrt{2d}$ (Theorem 1.1).

## Method
The argument decomposes $\mu_\varepsilon = J_\varepsilon + J_\varepsilon'$ where $J_\varepsilon$ restricts integration to "good" points whose dyadic-scale field values $h_{\bar r}(x) \leq \alpha\log(1/\bar r)$ stay below an $\alpha > \gamma$ threshold. Cameron–Martin–Girsanov shows the bad-point mass $J_\varepsilon'$ is small in $L^1$; an $L^2$ computation (using $P(N(2\gamma\log(1/r), \log(1/r)) \leq \alpha\log(1/r)) \leq r^{(2\gamma-\alpha)^2/2}$) shows $E(J_\varepsilon^2) \leq O(1)\int|x-y|^{(2\gamma-\alpha)^2/2 - \gamma^2}\sigma(dx)\sigma(dy)$, finite when $\gamma < \sqrt{2d}$. Uniqueness/universality is closed via the Karhunen–Loève martingale expansion, which forces any two regularizations to agree.

## Result
Convergence holds in the full subcritical regime $\gamma \in [\sqrt{d}, \sqrt{2d})$ (the hard phase, previously requiring $\sigma$-positivity à la Kahane or molllifier-specific arguments). The limiting measure is Borel, $\mu_\varepsilon \to \mu$ weakly in probability, and $\mu$ is measurable with respect to $h$. The integrand bound $E(J_\varepsilon^2) < \infty$ requires $(2\gamma - \alpha)^2/2 - \gamma^2 > -d$, achievable by choosing $\alpha \searrow \gamma$ iff $\gamma^2 < 2d$.

## Why it matters here
General background; no direct arena tie. The thick-point / good-vs-bad decomposition is a generic concentration-of-measure technique for log-correlated fields, and the $L^2$-truncation-then-uniqueness pattern is methodologically interesting, but Einstein Arena problems (sphere packing, autocorrelation, kissing, extremal graphs) do not involve multiplicative chaos or Liouville quantum gravity.

## Open questions / connections
- Critical case $\gamma = \sqrt{2d}$: covered by Junnila–Saksman [10] but not by this elementary route.
- Connection to KPZ relations and Liouville quantum gravity (Duplantier–Sheffield [4], Rhodes–Vargas [12]).
- Shamov [14] handles a strictly more general setup (probability convergence, $h$-measurability) — what's the minimum hypothesis on $K$ for elementary arguments to suffice?

## Key terms
Gaussian multiplicative chaos, Gaussian free field, Liouville quantum gravity, thick points, log-correlated field, Cameron–Martin–Girsanov, Karhunen–Loève expansion, subcritical phase, KPZ relation, multifractal measure, Kahane, Berestycki, mollifier universality
