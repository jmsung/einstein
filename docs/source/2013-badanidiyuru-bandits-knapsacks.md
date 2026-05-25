---
type: source
kind: paper
title: Bandits with Knapsacks
authors: Ashwinkumar Badanidiyuru, Robert D. Kleinberg, Aleksandrs Slivkins
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1305.2545
source_local: ../raw/2013-badanidiyuru-bandits-knapsacks.pdf
topic: general-knowledge
cites:
---

# Bandits with Knapsacks

**Authors:** Ashwinkumar Badanidiyuru, Robert D. Kleinberg, Aleksandrs Slivkins  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1305.2545

## One-line
Introduces "bandits with knapsacks" (BwK), a multi-armed bandit model with $d$ resource budgets $B_i$ where the process halts once any budget is exhausted, and gives algorithms achieving information-theoretically optimal regret.

## Key claim
Two algorithms (BalancedExploration and PrimalDualBwK) achieve regret $\tilde{O}(\sqrt{mOPT} + OPT\sqrt{m/B})$ against the optimal dynamic policy, where $m$ is the number of arms and $B = \min_i B_i$; a matching lower bound $\Omega\!\left(\min(OPT, OPT\sqrt{m/B} + \sqrt{mOPT})\right)$ is proved via a KL-divergence argument.

## Method
LP relaxation: bound OPT by $OPT_{LP}$, the value of an LP over time-invariant arm-mixtures, and compete against that. BalancedExploration explores each arm maximally subject to confidence-set feasibility ("explore as much as possible, narrow CIs eliminate suboptimal mixtures"). PrimalDualBwK runs multiplicative-weights (Hedge) on the *dual* resource-cost vector and at each step plays the arm with the best UCB-reward / LCB-cost ratio.

## Result
Regret bound (1) is optimal up to polylog factors for every $(m,B,OPT)$. Concrete corollaries: dynamic pricing with limited supply achieves $\tilde{O}(B^{2/3})$ regret (tight; first sublinear-in-supply bound vs optimal *dynamic* policy); dynamic procurement $\tilde{O}(T/B^{1/4})$; dynamic ad allocation $\tilde{O}(\sqrt{B})$. Per-round runtime $O(md)$ for PrimalDualBwK. Preadjusted discretization extends to infinite action spaces (prices in an interval).

## Why it matters here
General background; no direct arena tie. The arena problems are offline geometric/extremal optimization, not online exploration-exploitation under budget — BwK's LP-duality + multiplicative-weights framing could weakly inform compute-budget allocation across persona/strategy "arms" in the autonomous loop, but it is not a math technique for any of the 23 problems.

## Open questions / connections
- Computing the optimal dynamic policy from known latent distributions is conjectured PSPACE-hard (cf. Papadimitriou–Tsitsiklis 1999 on optimal queuing control).
- Extensions: contextual BwK (Badanidiyuru–Langford–Slivkins 2014), concave-rewards/convex-knapsacks (Agrawal–Devanur 2014), linear contextual BwK (Agrawal–Devanur 2016).
- Discretization error for $\ge 2$ non-time resource constraints in infinite action spaces remains open in general.

## Key terms
multi-armed bandit, bandits with knapsacks, BwK, regret minimization, LP relaxation, multiplicative weights update, Hedge algorithm, primal-dual, UCB confidence bounds, KL-divergence lower bound, dynamic pricing, dynamic procurement, exploration-exploitation, online stochastic packing
