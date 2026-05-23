---
type: source
kind: paper
title: Differentially Private Non-Convex Optimization under the KL Condition with Optimal Rates
authors: Michael Menart, Enayat Ullah, Raman Arora, Raef Bassily, Cristóbal Guzmán
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.13447v2
source_local: ../raw/2023-menart-differentially-private-non-convex-optimization.pdf
topic: general-knowledge
cites: 
---

# Differentially Private Non-Convex Optimization under the KL Condition with Optimal Rates

**Authors:** Michael Menart, Enayat Ullah, Raman Arora, Raef Bassily, Cristóbal Guzmán  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2311.13447v2

## One-line
Gives the first differentially private ERM algorithms for losses satisfying the Kurdyka-Łojasiewicz (KL) condition, achieving near-optimal excess-risk rates without requiring convexity.

## Key claim
Under $\rho$-zCDP, for $L_0$-Lipschitz, $L_1$-smooth $F$ satisfying the $(\gamma,\kappa)$-KL* condition with $\kappa\in[1,2]$, excess empirical risk $\tilde O\!\left((\sqrt d/(n\sqrt\rho))^\kappa\right)$ is achievable (and nearly tight); for unknown KL parameters an adaptive noisy-GD variant attains $\tilde O\!\left((\sqrt d/(n\sqrt\rho))^{2\kappa/(4-\kappa)}\right)$, which is near-optimal at $\kappa=2$.

## Method
A modified noisy **Spider** variance-reduced gradient method with *adaptive, variable-length rounds* and target-risk thresholds $\hat\Phi_k$ that trigger early stopping when the KL-induced gradient lower bound weakens; for $\kappa\ge 2$ (weakly convex), a private **approximate proximal-point** method. The unknown-KL case uses noisy GD whose per-step noise scales with the current (privately estimated) gradient norm, exploiting that large gradients let one add more noise "for free."

## Result
Achieves $\tilde O(d/(n^2\rho))$ for PL ($\kappa=2$), matching the strongly-convex lower bound of Bassily-Smith-Thakurta. Adaptive noisy-GD attains $\tilde O((\sqrt d/(n\sqrt\rho))^{2/3})$ in the slowest regime $\kappa=1$, and without any KL assumption finds a stationary point with gradient norm between $\tilde O(\sqrt d/(n\sqrt\rho))$ (good case) and $\tilde O((\sqrt d/(n\sqrt\rho))^{1/2})$ (worst case, matching best prior non-variance-reduced rates).

## Why it matters here
General background; no direct arena tie — this is differential-privacy optimization theory, not extremal combinatorics or sphere packing. The KL/PL gradient-domination *condition* and the trick of letting the noise budget track the gradient norm could conceivably inform private/regularized optimizer design, but no Einstein Arena problem currently invokes it.

## Open questions / connections
- Tight lower bound for $\kappa\in[1,1+\Omega(1)]$ and for $\kappa>2$ remains open.
- Extends [WYX17, LGR23] (PL-only) and [ALD21] (convex growth condition); KL is strictly weaker than both.
- Whether variance-reduced Spider-style methods can close the stationary-point gap of [ABG+23] without KL.

## Key terms
Kurdyka-Łojasiewicz condition, Polyak-Łojasiewicz, gradient domination, differential privacy, zCDP, empirical risk minimization, noisy gradient descent, Spider variance reduction, proximal point method, weak convexity, growth condition, non-convex optimization
