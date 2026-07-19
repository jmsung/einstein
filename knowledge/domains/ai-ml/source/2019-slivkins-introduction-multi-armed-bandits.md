---
type: source
kind: paper
title: Introduction to Multi-Armed Bandits
authors: Aleksandrs Slivkins
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.07272
source_local: ../raw/2019-slivkins-introduction-multi-armed-bandits.pdf
topic: general-knowledge
cites:
---

# Introduction to Multi-Armed Bandits

**Authors:** Aleksandrs Slivkins  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.07272

## One-line
A textbook-style survey of multi-armed bandit theory — sequential decision-making under uncertainty with the exploration–exploitation tradeoff — covering stochastic, adversarial, contextual, structured, and economic variants.

## Key claim
The bandit framework admits sharp regret bounds across regimes: $\tilde{O}(\sqrt{KT})$ minimax regret and $O(\sum_a \log T / \Delta(a))$ instance-dependent regret for stochastic $K$-armed bandits (UCB / Lai–Robbins), $O(\sqrt{T K \log K})$ for adversarial bandits (Exp3/Exp4), $\tilde{O}(T^{(d+1)/(d+2)})$ for Lipschitz bandits in metric dimension $d$ (zooming algorithm), with matching lower bounds via KL-divergence arguments.

## Method
Core toolkit: concentration inequalities (Hoeffding, Azuma) for confidence bounds (UCB); exponential-weights / multiplicative-update / Hedge for adversarial settings; importance-weighted unbiased estimators for bandit→full-feedback reduction (Exp3, Exp4); KL-divergence change-of-measure for lower bounds; adaptive discretization (zooming) for Lipschitz/continuum arms; Lagrangian / primal-dual for budget constraints (BwK); Thompson sampling as Bayesian posterior matching; follow-the-perturbed-leader for combinatorial actions.

## Result
Establishes the canonical regret landscape: stochastic $\Theta(\sqrt{KT})$ minimax with logarithmic instance-dependent floor; adversarial $\Theta(\sqrt{KT})$; Lipschitz bandits in $d$-dim metric with zooming dimension $z$ achieve $\tilde{O}(T^{(z+1)/(z+2)})$, optimal; Exp4 with $N$ experts gets $O(\sqrt{T K \log N})$; bandits-with-knapsacks attains $O(\text{OPT}\sqrt{1/B})$ competitive ratio; minimax theorem recoverable from no-regret dynamics in zero-sum games. Each chapter pairs algorithm with matching lower bound.

## Why it matters here
General background; no direct arena tie. The exploration–exploitation framework could inform meta-strategy for the autonomous loop itself (which problem/persona/technique to invest compute in next), and zooming / adaptive discretization is a candidate primitive for parameterized search over basins — but the paper's content is orthogonal to sphere packing, autocorrelation, kissing numbers, and the other Einstein Arena math problems.

## Open questions / connections
- Could UCB-style allocation rule the loop's compute router — treat "techniques in `skill-library.md`" as arms with regret $= $ wasted GPU-hours, exploit by success rate?
- Adaptive discretization (zooming algorithm, Kleinberg–Slivkins–Upfal) is a possible primitive for basin-hopping with non-uniform local volume — relevant to P11/P15/P16 multistart search.
- BwK (bandits-with-knapsacks) framework maps cleanly to the Modal $/hr budget constraint per problem.
- No connection to LP duality / Cohn–Elkies / equioscillation / modular forms / Sidon sets — this paper does not inform the math content of any arena problem directly.

## Key terms
multi-armed bandits, exploration-exploitation, UCB, regret, Thompson sampling, Exp3, Exp4, Hedge algorithm, adversarial bandits, contextual bandits, Lipschitz bandits, zooming algorithm, bandits with knapsacks, KL-divergence lower bound, Lai-Robbins, follow-the-perturbed-leader, no-regret dynamics, minimax theorem, Slivkins
