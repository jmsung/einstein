---
type: source
kind: paper
title: Dynamic Regret of Convex and Smooth Functions
authors: Peng Zhao, Yu-Jie Zhang, Lijun Zhang, Zhi-Hua Zhou
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.03479
source_local: ../raw/2020-zhao-dynamic-regret-convex-smooth.pdf
topic: general-knowledge
cites:
---

# Dynamic Regret of Convex and Smooth Functions

**Authors:** Peng Zhao, Yu-Jie Zhang, Lijun Zhang, Zhi-Hua Zhou  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.03479

## One-line
Designs online algorithms (Sword family) whose dynamic regret against any comparator sequence depends on smoothness-driven problem-dependent quantities rather than $T$, so easy/benign sequences pay much less than the minimax worst case.

## Key claim
Under convexity + $L$-smoothness, the universal dynamic regret can be improved from the minimax $O(\sqrt{T(1+P_T)})$ to $O(\sqrt{(1+P_T+\min\{V_T,F_T\})(1+P_T)})$, where $P_T=\sum_t\|u_{t-1}-u_t\|_2$, $V_T=\sum_t \sup_x\|\nabla f_{t-1}(x)-\nabla f_t(x)\|_2^2$, and $F_T=\sum_t f_t(u_t)$ — all $O(T)$ worst-case but often sublinear on benign streams.

## Method
Meta-expert framework: experts run online extra-gradient descent (OEGD) or OGD over a geometric grid of step sizes $\eta_i$ discretizing the unknown optimal $\eta^*$; a meta-algorithm (OptimisticHedge variant "VariationHedge") combines them with weights $p_{t+1,i}\propto\exp(-\varepsilon(\sum_s\langle\nabla f_s(x_s),x_{s,i}\rangle+\langle\nabla f_t(\bar x_{t+1}),x_{t+1,i}\rangle))$. The crucial trick is choosing the optimism $m_{t,i}=\langle\nabla f_{t-1}(\bar x_t),x_{t,i}\rangle$ with $\bar x_t=\sum_i p_{t-1,i}x_{t,i}$, so the negative term $-\|p_t-p_{t-1}\|_1^2/(4\varepsilon)$ in OptimisticHedge's regret cancels the $\|x_t-\bar x_t\|_2^2$ residue, leaving only $V_T$. Swordbest runs a second parallel Hedge over two optimism choices to obtain $\min\{V_T,F_T\}$ automatically.

## Result
Theorem 3 (Swordvar): $\sum_t f_t(x_t)-\sum_t f_t(u_t)\le O(\sqrt{(1+P_T+V_T)(1+P_T)})$. Theorem 5 (Swordsmall): $O(\sqrt{(1+P_T+F_T)(1+P_T)})$. Theorem 7 (Swordbest): best-of-both with $\min\{V_T,F_T\}$. All three specialize to Chiang et al.'s $O(\sqrt{V_T})$ and Srebro et al.'s $O(\sqrt{F_T^*})$ static-regret bounds when $P_T=0$, and match the $\Omega(\sqrt{T(1+P_T)})$ lower bound in the worst case. Step-size pool size $N_1=\lceil\tfrac12\log_2(GT/(8D^2L^2))\rceil+1$.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are offline mathematical optimizations (sphere packing, autocorrelation, kissing numbers) rather than online sequential games against an adversary — path-length / gradient-variation bounds don't apply. The only weak crossover is the self-bounding property $\|\nabla f(x)\|^2\le 4Lf(x)$ for non-negative smooth $f$ (Srebro et al. 2010, Lemma 4 here), which is a general tool for any smooth-and-nonneg loss landscape.

## Open questions / connections
- Extends Zhang et al. (2018a) minimax universal dynamic regret by adding smoothness adaptivity; extends Chiang et al. (2012) gradient-variation static regret to dynamic comparators.
- Whether $O(\min\{P_T^*,S_T^*,V_T^f\})$-style worst-case bounds (Zhao & Zhang 2020) can be lifted to universal dynamic regret under only convex+smooth (no strong convexity) remains open.
- Doubling trick handles unknown $V_T$ but not unknown $P_T$, since the comparator sequence is adversarial — a persistent obstacle for fully parameter-free dynamic regret.

## Key terms
online convex optimization, dynamic regret, universal dynamic regret, path-length, gradient variation, small-loss bound, smoothness, self-bounding property, OptimisticHedge, online extra-gradient descent, meta-expert framework, Zinkevich
