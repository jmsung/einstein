---
type: source
kind: paper
title: The Intrinsic Robustness of Stochastic Bandits to Strategic Manipulation
authors: Zhe Feng, D. Parkes, Haifeng Xu
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.01528
source_local: ../raw/2019-feng-intrinsic-robustness-stochastic-bandits.pdf
topic: general-knowledge
cites:
---

# The Intrinsic Robustness of Stochastic Bandits to Strategic Manipulation

**Authors:** Zhe Feng, D. Parkes, Haifeng Xu  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.01528

## One-line
Proves that classic stochastic bandit algorithms (UCB, ε-Greedy, Thompson Sampling) remain low-regret when arms strategically inflate their own reward feedback under a cross-period budget.

## Key claim
For any adaptive arm manipulation strategy with total budget $B = \sum_{i\neq i^*} B_i$ and $K$ arms over horizon $T$, all three algorithms attain regret $O\!\left(\sum_{i\neq i^*} \max\{B_i,\, \sigma^2 \ln T/\Delta_i\}\right) = O(\max\{B, K\ln T\})$, and this is tight — matched by an $\Omega(\max\{B, K\ln T\})$ lower bound (for UCB even at Nash equilibrium).

## Method
Standard $(\alpha,\psi)$-UCB analysis is extended by tracking a *modified* UCB term $\widetilde{\mathrm{UCB}}_i(t) = \mathrm{UCB}_i(t) + \beta_{t-1}^{(i)}/n_i(t-1)$ that absorbs cumulative manipulation $\beta_t^{(i)}$, then choosing threshold $C_i(T)=\max\{3B_i/\Delta_i,\, 81\sigma^2\ln T/\Delta_i^2\}$ to decompose $\mathbb{E}[n_i(T)]$ and bound the tail via Chernoff-Hoeffding. Lower bound uses a *coupling* argument showing the Lump-Sum-Investing (LSI) strategy — spend entire budget on first pull — is dominant under UCB and first-order stochastically dominates any other strategy in pulls received.

## Result
Theorem 3.1: $\mathbb{E}[R(T)] \le \sum_{i\neq i^*} \max\{3B_i,\, 81\sigma^2\ln T/\Delta_i\} + (1+3)\Delta_i$. Theorem 3.4: under LSI equilibrium, $\mathbb{E}[R(T)] \ge \Delta\sum_{i\neq i^*} B_i/(2\Delta_i) - O(\ln T/\Delta)$. Sublinear regret persists whenever $B = o(T)$; beats state-of-the-art robust-bandits bound (Gupta et al. 2019) by factor $K$ when the optimal arm cannot be contaminated.

## Why it matters here
General background; no direct arena tie — Einstein Arena problems are deterministic math optimization, not bandit/online-learning. Tangentially informs the agent's *own* meta-policy if it were ever to schedule across noisy/strategic compute resources or arm-like sub-optimizers, but this is a stretch.

## Open questions / connections
- Whether LSI is also a Nash equilibrium for ε-Greedy and Thompson Sampling (left open).
- Can the modern robust-bandit algorithms (Lykouris et al. 2018, Gupta et al. 2019) match the $O(\max\{B,K\ln T\})$ bound when the optimal arm is protected?
- Extension to non-stationary bandits (Besbes et al. 2019, Cheung et al. 2019) under strategic arms.

## Key terms
stochastic multi-armed bandits, UCB, epsilon-greedy, Thompson sampling, strategic manipulation, regret upper bound, regret lower bound, Lump Sum Investing, dominant strategy, subgame perfect Nash equilibrium, sub-Gaussian rewards, adversarial corruption
