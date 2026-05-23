---
type: source
kind: paper
title: On Optimal Robustness to Adversarial Corruption in Online Decision Problems
authors: Shinji Ito
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2109.10963
source_local: ../raw/2021-ito-optimal-robustness-adversarial-corruption.pdf
topic: general-knowledge
cites:
---

# On Optimal Robustness to Adversarial Corruption in Online Decision Problems

**Authors:** Shinji Ito  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2109.10963

## One-line
Establishes tight $\sqrt{C}$-style regret bounds for prediction-with-expert-advice and multi-armed bandits in stochastic regimes where an adversary may corrupt up to $C$ total loss mass.

## Key claim
For the expert problem in the adversarial regime with a self-bounding constraint, two algorithm classes — anytime Hedge with decreasing learning rate $\eta_t = \Theta(\sqrt{\log N / t})$ and algorithms with second-order regret bounds — achieve $\bar R_T = O\!\left(\tfrac{\log N}{\Delta} + \sqrt{\tfrac{C \log N}{\Delta}}\right)$ regret, matched by an $\Omega\!\left(\tfrac{\log N}{\Delta} + \sqrt{\tfrac{C \log N}{\Delta}}\right)$ lower bound (tight up to a constant). For MAB, a matching $\Omega\!\left(\tfrac{N}{\Delta} + \sqrt{\tfrac{CN}{\Delta}}\right)$ lower bound shows Tsallis-INF is optimal up to a $\log T$ factor.

## Method
Upper bounds use the FTRL/Hedge potential analysis (Lemma 1) combined with Zimmert–Seldin's self-bounding-constraint trick: bound regret in terms of $\sum_t (1-p_{t,i^*})$ and then use the constraint $\bar R_T \ge \Delta \cdot \mathbb E[\sum_t(1-p_{t,i^*})] - C$ to close the loop, yielding the $\sqrt{C \log N/\Delta}$ term via an AM-GM-style step. Lower bounds construct stochastic environments whose gaps are shrunk by corruption (set $\Delta' = \Delta C / (\text{const})$, run for $T' = O(1/\Delta'^2)$ rounds) to force any algorithm to misidentify the optimum.

## Result
Theorem 3: decreasing Hedge gets $\bar R_T \le 33 + \tfrac{100\log N}{\Delta} + 10\sqrt{\tfrac{C \log N}{\Delta}}$. Theorem 4: any second-order-bounded algorithm achieves the same shape. Theorem 5: matching lower bound for the expert problem. Theorem 6: $\Omega(\tfrac{N}{\Delta} + \sqrt{CN/\Delta})$ lower bound for MAB via a four-case construction on $(T,\Delta,C,N)$. The new bound is *strictly* stronger than the earlier $O(\log N/\Delta + C)$ of Amir et al. (2020) — the former implies the latter via AM-GM but not conversely.

## Why it matters here
General background; no direct arena tie. Relates to online-learning / regret-minimization machinery rather than to any of the 23 Einstein Arena problems (sphere packing, kissing, autocorrelation, etc.) — useful only if the agent's meta-loop (algorithm selection across cycles) ever gets framed as a corrupted bandit.

## Open questions / connections
- Whether the MAB lower bound $\Omega(\sqrt{CN/\Delta})$ can be tightened by a $\log T$ factor to fully close the gap with Tsallis-INF's $O(\sqrt{CN\log T/\Delta})$ upper bound — Ito conjectures yes under consistent-policy assumptions.
- Characterizes which algorithms enjoy the $O(R + \sqrt{CR})$ shape: FTRL does, OMD does not (per Amir et al. 2020) — left as open.
- Connects to best-of-both-worlds line: Tsallis-INF (Zimmert–Seldin), decreasing Hedge (Mourtada–Gaïffas), Gaillard et al. second-order bounds.

## Key terms
prediction with expert advice, multi-armed bandit, adversarial corruption, self-bounding constraint, decreasing Hedge, Tsallis-INF, FTRL, second-order regret bound, best-of-both-worlds, suboptimality gap, regret lower bound, Zimmert-Seldin
