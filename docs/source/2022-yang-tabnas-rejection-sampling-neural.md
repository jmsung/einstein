---
type: source
kind: paper
title: "TabNAS: Rejection Sampling for Neural Architecture Search on Tabular Datasets"
authors: Chengrun Yang, Gabriel Bender, Hanxiao Liu, Pieter-Jan Kindermans, Madeleine Udell, Yifeng Lu, Quoc V. Le, Da Huang
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2204.07615
source_local: ../raw/2022-yang-tabnas-rejection-sampling-neural.pdf
topic: general-knowledge
cites:
---

# TabNAS: Rejection Sampling for Neural Architecture Search on Tabular Datasets

**Authors:** Chengrun Yang, Gabriel Bender, Hanxiao Liu, Pieter-Jan Kindermans, Madeleine Udell, Yifeng Lu, Quoc V. Le, Da Huang  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2204.07615

## One-line
Replaces resource-penalty rewards in RL-based neural architecture search with a rejection-sampling reward that silently discards infeasible architectures, plus a Monte-Carlo correction to keep the policy gradient unbiased.

## Key claim
On factorized search spaces, penalty-shaped rewards $Q(y) + \beta|T(y)/T_0 - 1|$ get trapped in local optima because layer choices are independent and bottleneck structures look bad marginally; conditioning the REINFORCE update on the feasible set $V$ via $J(y) = \mathrm{stop\_grad}(Q(y) - \bar Q) \cdot \log[P(y)/P(V)]$ recovers the global optimum, with $\widehat P(V)$ estimated by MC sampling proven unbiased and consistent.

## Method
REINFORCE over a factorized layer-size distribution with weight-sharing SuperNet and layer warmup (first 25% epochs). The RL gradient is taken only on feasible samples and uses the conditional log-probability $\log P(y \mid y \in V) = \log P(y) - \log P(V)$; $P(V)$ is approximated by importance-sampling estimator $\widehat P(V) = \frac{1}{N}\sum_k \frac{p^{(k)}}{q^{(k)}} \mathbf{1}(z^{(k)} \in V)$ with proposal $q = \mathrm{stop\_grad}(p)$, which is differentiable through $p^{(k)}$ but not $q^{(k)}$.

## Result
TabNAS recovers the Pareto-optimal architecture on a toy 2-layer space where Abs-Reward fails (converges either to a feasible-but-suboptimal or constraint-violating architecture). On Criteo (3-layer, $\le 41{,}153$ params), Volkert, Aloi, Connect-4, Higgs, and the NATS-Bench size space on CIFAR-100 ($\le 75$M FLOPs), the rejection-based reward consistently meets the constraint and matches or beats reference architectures, while MnasNet/TuNAS-style rewards either overshoot the budget or settle on inferior bottleneck-free architectures. Hyperparameter $N$ is monotonically "larger is better" and easier to tune than $\beta$.

## Why it matters here
General background; no direct arena tie. The conceptual transfer is the **conditional-distribution trick**: when a factorized proposal collides with a hard constraint that couples coordinates, replacing penalty-shaped objectives with rejection + an unbiased $P(\text{feasible})$ correction beats reward shaping. This is structurally analogous to constrained sampling/optimization over packings, kissing configurations, or contact-graph parametrizations where per-coordinate marginals mislead.

## Open questions / connections
- Variance reduction for $\widehat P(V)$ when $P(V)$ is tiny — TabNAS warms up so $P(V)$ rises; constrained-config problems with vanishing feasibility need importance proposals on $V$.
- Whether the rejection trick extends to continuous parametrizations with measure-zero feasible sets (active-constraint manifolds in sphere packing / Hardin-Sloane configurations).
- Relationship to constrained policy optimization (CPO, Lagrangian RL) — TabNAS is the all-or-nothing limit of a soft penalty.

## Key terms
neural architecture search, REINFORCE, rejection sampling, Monte Carlo estimator, importance sampling, policy gradient, factorized controller, weight sharing, SuperNet, bottleneck architecture, conditional probability gradient, resource-constrained optimization
