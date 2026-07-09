---
type: source
kind: paper
title: Adversarial Bandits with Knapsacks
authors: Nicole Immorlica, Karthik Abinav Sankararaman, R. Schapire, Aleksandrs Slivkins
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.11881
source_local: ../raw/2018-immorlica-adversarial-bandits-knapsacks.pdf
topic: general-knowledge
cites:
---

# Adversarial Bandits with Knapsacks

**Authors:** Nicole Immorlica, Karthik Abinav Sankararaman, R. Schapire, Aleksandrs Slivkins  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.11881

## One-line
Extends the Bandits-with-Knapsacks (BwK) model to adversarial outcomes, proves regret minimization is impossible, and gives an $O(\log T)$-competitive algorithm (tight) via a repeated Lagrangian zero-sum game.

## Key claim
For Adversarial BwK with $K$ arms, $d$ resources, horizon $T$, and budget $B$, no algorithm can beat competitive ratio $\Omega(\log T)$ against the best fixed distribution $\text{OPT}_{\text{FD}}$; the proposed algorithm achieves $\mathbb{E}[\text{REW}] \geq \tfrac{1}{O(\log T)}(\text{OPT}_{\text{FD}} - \text{reg})$, matching this lower bound up to constants.

## Method
Reframe the LP relaxation of Stochastic BwK as a repeated zero-sum game whose payoff is the Lagrangian $L(X,\lambda) = r(X) + \sum_i \lambda_i(1 - \tfrac{T}{B} c_i(X))$, with a primal player (Hedge/EXP3 over arms) and a dual player (Hedge over resources) — `LagrangeBwK`. For the adversarial version, run `LagrangeBwK` as a black-box subroutine with geometrically increasing guesses $g$ of $\text{OPT}_{\text{FD}}$ inside a multi-phase meta-algorithm; competitive-ratio analysis uses a "stopped LP" benchmark $\text{OPT}_{\text{LP}}(\tau)$.

## Result
Lower bound: $\text{OPT}_{\text{FD}}/\mathbb{E}[\text{REW}] \geq \Omega(\log T)$ even with $K=2$, $d=1$. Upper bound: matching $O(\log T)$ competitive ratio, with high-probability variant. Against $\text{OPT}_{\text{DP}}$ (best dynamic policy) the ratio is $\geq T/B$ (impossible); against $\text{OPT}_{\text{FA}}$ (best fixed arm) it is $\Omega(K)$ and matched by random-arm-forever. Absent budgets, recovers the optimal $\tilde{O}(\sqrt{KT})$ adversarial bandit regret.

## Why it matters here
General background; no direct arena tie. The Lagrangian-as-repeated-zero-sum-game framing could inform meta-strategy questions (e.g., budget allocation across the 23 problems under a global compute budget), but none of the Einstein Arena problems are bandits/knapsack-shaped, so this is methodological reading rather than a technique to deploy.

## Open questions / connections
- Constant competitive ratio in the regime $B = \Omega(T)$ — resolved later by Castiglioni et al. (2022) using fixed-parameter LagrangeBwK.
- Sublinear dependence on $d$ — resolved by Kesselheim & Singla (2020) to $O(\log d \cdot \log T)$, with matching lower bound.
- "Best of both worlds" algorithm achieving $O(\log T)$ adversarial competitive ratio and $o(T)$ stochastic regret simultaneously — partially answered by Castiglioni et al. (2022).
- Weaker benchmark than fixed-distribution against which competitive ratio of 1 is achievable.

## Key terms
adversarial bandits, bandits with knapsacks, BwK, competitive ratio, Lagrangian game, repeated zero-sum game, primal-dual, EXP3, Hedge, regret minimization, online packing, dynamic pricing, AdWords, Nash equilibrium
