---
type: source
kind: paper
title: Tight Analysis of Difference-of-Convex Algorithm (DCA) Improves Convergence Rates for Proximal Gradient Descent
authors: Teodor Rotaru, Panagiotis Patrinos, Franccois Glineur
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2503.04486
source_local: ../raw/2025-rotaru-tight-analysis-difference-of-convex-algorithm.pdf
topic: general-knowledge
cites:
---

# Tight Analysis of Difference-of-Convex Algorithm (DCA) Improves Convergence Rates for Proximal Gradient Descent

**Authors:** Teodor Rotaru, Panagiotis Patrinos, Franccois Glineur  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.04486

## One-line
Gives tight per-iteration decrease bounds for the difference-of-convex algorithm (DCA) across six curvature regimes — including a weakly-convex $f_2$ — and uses the DCA↔PGD equivalence to sharpen proximal gradient descent rates.

## Key claim
For $F = f_1 - f_2$ with $f_1 \in \mathcal{F}_{\mu_1,L_1}$, $f_2 \in \mathcal{F}_{\mu_2,L_2}$ (at least one smooth, $\mu_1+\mu_2 > 0$ or $\mu_1=\mu_2=0$), one DCA step satisfies $F(x) - F(x^+) \ge \tfrac{\sigma_i}{2}\|g_1 - g_2\|^2 + \tfrac{\sigma_i^+}{2}\|g_1^+ - g_2^+\|^2$ with explicit $(\sigma_i, \sigma_i^+)$ in six regimes partitioned by the thresholds $B := \mu_1^{-1} + \mu_2^{-1} + L_2^{-1}$ and $E := \tfrac{L_2+\mu_2}{L_1 L_2}\cdot\tfrac{L_2-L_1}{-\mu_2} + \mu_1^{-1} - L_1^{-1}$; this yields $\mathcal{O}(1/N)$ sublinear convergence to critical points and rates conjectured tight in regimes $p_1, p_2, p_3$.

## Method
Performance Estimation Programming (PEP) framework of Drori–Teboulle / Taylor et al.: encode the worst-case one-step decrease as an SDP over interpolable curvature constraints, then construct an algebraic certificate by weighting two key cocoercivity-style inequalities (eqs. (9), (10)) with a scalar $\alpha$ tuned per regime. Tightness is supported by explicit piecewise-quadratic worst-case function constructions (Propositions 5–6) and PEP numerical verification.

## Result
Six closed-form denominators $p_i = \sigma_i + \sigma_i^+$ (Table 1) covering all sign combinations of $(\mu_1, \mu_2, L_1-L_2)$, with the $B=0$ curve separating tight regimes ($p_1, p_2, p_3$) from non-tight ($p_4, p_5, p_6$). Optimizing the DC splitting $F = (f_1 - \lambda\|\cdot\|^2/2) - (f_2 - \lambda\|\cdot\|^2/2)$ over $\lambda$ can produce up to 167% larger denominators than the default splitting (Table 3); in Example 1 (smooth nonconvex $F$, $L_F = -\mu_F = 1$), best-$\lambda$ DCA achieves $p^* = 1.724$, beating optimal-stepsize gradient descent ($p_{GD} = 1.5396$) by 12%. PGD equivalence $f_1 = h + \tfrac{1}{2\gamma}\|\cdot\|^2$, $f_2 = \tfrac{1}{2\gamma}\|\cdot\|^2 - \varphi$ shows stepsizes $\gamma > 1/L_\varphi$ correspond to weakly convex $f_2$ — explaining why long-step PGD can accelerate.

## Why it matters here
General background; no direct arena tie. Closest contact: optimizer-technique knowledge for problems where the agent uses proximal/composite first-order methods or DC reformulations (sparse logistic, compressed sensing, MSVM) — but the Einstein Arena problem set is dominated by sphere packing, autocorrelation, kissing, and combinatorial extremal problems where mpmath polish / L-BFGS / SLSQP / SDP dominate, not PGD/DCA.

## Open questions / connections
- Tightness of regimes $p_4, p_5, p_6$ over $N>1$ iterations is open (Conjecture 2 only covers $p_1, p_2, p_3$).
- Extends Abbaszadehpeivasti et al. (2023) two-regime convex-only DCA analysis to four new regimes including weakly convex $f_2$.
- Connection to Faust et al. (2023) Bregman proximal point view of DCA and to Yurtsever–Sra (2022) Frank–Wolfe-as-DCA reduction — suggests other first-order methods may inherit these tight rates.
- Open: how to choose $\lambda^*$ in closed form when only $(\mu_F, L_F)$ are known but not the split curvatures.

## Key terms
difference-of-convex algorithm, DCA, proximal gradient descent, PGD, performance estimation programming, PEP, weakly convex, hypoconvex, convex conjugate, Moreau envelope, curvature splitting, sublinear convergence, critical point, Bregman proximal point, Rotaru, Patrinos, Glineur, Abbaszadehpeivasti, Taylor
