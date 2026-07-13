<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "General agents need world models"
authors: [Jonathan Richens, David Abel, Alexis Bellot, Tom Everitt]
year: 2025
source_url: https://arxiv.org/abs/2506.01622
drive_file_id: 17SzQJpJPKrleufm3hPKtsMrDySSsicE6
text_source: pdf
ingested_by: agent
---

# General agents need world models

**Authors:** Jonathan Richens, David Abel, Alexis Bellot, Tom Everitt  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.01622

## One-line
Proves that any agent satisfying a regret bound on a sufficiently diverse set of multi-step goal-directed tasks must have implicitly learned an accurate predictive model of its environment, and shows how to extract that model from the agent's policy alone.

## Key claim
Any goal-conditioned policy with a bounded failure rate $\delta$ across composite goals of maximum depth $n>1$ (Def. 5, "bounded goal-conditioned agent") fully determines an approximate world model $\hat{P}_{ss'}(a)$ of the environment's transition function, with error $|\hat{P}_{ss'}(a) - P_{ss'}(a)| \le \sqrt{2P_{ss'}(a)(1-P_{ss'}(a))/((n-1)(1-\delta))}$ (Theorem 1) — i.e., there is no model-free shortcut to general, long-horizon competence; increasing an agent's performance ($\delta \to 0$) or the depth $n$ of goals it can achieve forces the implicit world model to become more accurate.

## Method
Formalizes the environment as a controlled Markov process (cMP) and goals as LTL expressions (Eventually/Next/Now operators) over goal-states, composed sequentially/in parallel into "composite goals" of a given depth $n$ (number of sub-goals). Defines an optimal goal-conditioned agent (Def. 4) and a relaxed "bounded" agent (Def. 5) parameterized by failure rate $\delta$ and max goal depth $n$. Proves Theorem 1 by reduction: constructs an algorithm (Algorithm 1, detailed in Appendix C) that queries the agent's policy on composite goals built from either/or sub-goal pairs ($\psi = \psi_a \vee \psi_b$); because the agent satisfies the regret bound, its action choice reveals which sub-goal has higher success probability, and this information is used to estimate transition probabilities $\hat{P}_{ss'}(a)$ with provable error bounds. The recovery algorithm is unsupervised (only needs the policy $\pi$) and universal (works for any agent satisfying Def. 5 in any environment satisfying Assumption 1: finite, irreducible, stationary cMP with $\ge 2$ actions). A separate result (Theorem 2) shows myopic agents (goals with depth $n=1$) are the exception: their policies impart only trivial ($\epsilon=1$) bounds on the transition function, so learning a world model is not necessary for purely immediate-outcome agents.

## Result
For $\delta \ll 1, n \gg 1$ the error scales as $\mathcal{O}(\delta/\sqrt{n}) + \mathcal{O}(1/n)$. Experiments train agents on a randomly generated 20-state, 5-action sparse cMP via trajectories of increasing length $N_\text{samples}$, then recover the world model with a simplified algorithm (Algorithm 2). Agents empirically violate the worst-case regret bound (worst-case regret $\delta=1$ for every goal depth tested), yet Algorithm 2 still recovers the transition function with low mean error that decays as $\sim \mathcal{O}(n^{-1/2})$ as the agent is trained on longer trajectories — matching the theoretical scaling — showing the result is robust even when agents strongly violate the competence assumptions. $N_\text{max}(\langle\delta\rangle=0.04)$ (max goal depth at $\le 0.04$ average regret) fits as $\sqrt{0.16(N-4.79)}$ against $N_\text{samples}$, and mean error $\langle\epsilon\rangle$ vs. average regret $\langle\delta\rangle$ at depth $n=50$ fits $0.01(0.32e^{16.93\delta}+1.12)$.

## Key terms
world models, goal-conditioned agents, controlled Markov process, Linear Temporal Logic (LTL), composite goals, regret bound, bounded agent, model-free RL, inverse reinforcement learning, model identifiability, emergent capabilities, mechanistic interpretability, Google DeepMind, Richens
