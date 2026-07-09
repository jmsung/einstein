---
type: source
kind: paper
title: Multi-armed Bandit Problems with Strategic Arms
authors: M. Braverman, Jieming Mao, Jon Schneider, S. Weinberg
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1706.09060
source_local: ../raw/2017-braverman-multi-armed-bandit-problems-strategic.pdf
topic: general-knowledge
cites:
---

# Multi-armed Bandit Problems with Strategic Arms

**Authors:** M. Braverman, Jieming Mao, Jon Schneider, S. Weinberg  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.09060

## One-line
Studies a multi-armed bandit variant where each arm is a strategic agent that chooses how much of its private per-round reward $v_a$ to forward to the principal, and asks how the principal can incentivize arms to surrender most of their value.

## Key claim
Low-regret adversarial bandit algorithms (e.g. EXP3) are fundamentally incompatible with strategic-arm revenue extraction: any $\delta$-low-regret algorithm admits an $O(\sqrt{T\delta})$-Nash equilibrium for the arms yielding only $o(T)$ principal revenue; yet a different (non-low-regret) mechanism — a scoring-rule-plus-second-price construction — achieves dominant-strategy revenue $\mu' T - o(T)$, where $\mu'$ is the second-largest arm mean.

## Method
Negative side: explicit construction of collusive "market-sharing" arm strategies, with the key technical tool being a submartingale / Azuma's-inequality argument that bounds $|c_{i,t}/\mu_i - c_{j,t}/\mu_j| \le B = O(\sqrt{KT\delta})$ under collusion, forcing any low-regret principal to split pulls equally. Positive side: a two-phase mechanism — elicit each arm's mean $\mu_i$ via a logarithmic proper scoring rule (Brier/McCarthy), then a punishment-style second-price scheme that pulls the highest-reported-mean arm so long as it remits $\mu'$ each round, else blacklists it.

## Result
Theorem 3.1 (explicit obs.): any $\delta$-low-regret $M$ admits a $(\delta+1)$-Nash equilibrium with zero principal revenue. Theorem 3.4 (tacit obs., $K$ arms): under $|\mu_1 - \mu_2| \le \mu_1/K$, a $(\rho,\delta)$-low-regret $M$ admits an $O(\sqrt{KT\delta})$-Nash equilibrium with principal revenue $\le O(\sqrt{KT\delta})$. Theorem 1.3/Corollary 4.2: a truthful mechanism extracts $\mu' T - o(T)$ in dominant strategies; Lemma 4.3 shows this $\mu'$ rate is tight.

## Why it matters here
General background; no direct arena tie. This is mechanism design / strategic learning theory and does not bear on sphere packing, autocorrelation, kissing numbers, or any current Einstein Arena problem. It would only be relevant if the agent itself were modeled as a principal facing strategic verifiers/sub-agents, which is not the current setup.

## Open questions / connections
- Does there exist a single mechanism that is simultaneously low-regret in the adversarial setting AND extracts $\Omega(T)$ revenue in *some* Nash equilibrium (rather than just *no* equilibrium being bad)?
- Can the positive mechanism be extended to non-stationary arm distributions, where learning must continue throughout the $T$ rounds without re-opening collusion channels?
- Defining strategic equilibrium for adversarially-generated rewards (arms lack priors to reason about future utility) — perhaps via no-regret strategies over a restricted class.

## Key terms
multi-armed bandit, strategic arms, EXP3, low-regret algorithm, Nash equilibrium, dominant strategy, second-price auction, proper scoring rule, logarithmic scoring rule, principal-agent problem, tacit collusion, repeated auctions, Azuma's inequality, submartingale, mechanism design
