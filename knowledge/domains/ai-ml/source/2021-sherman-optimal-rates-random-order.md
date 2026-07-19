---
type: source
kind: paper
title: Optimal Rates for Random Order Online Optimization
authors: Uri Sherman, Tomer Koren, Y. Mansour
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.15207
source_local: ../raw/2021-sherman-optimal-rates-random-order.pdf
topic: general-knowledge
cites:
---

# Optimal Rates for Random Order Online Optimization

**Authors:** Uri Sherman, Tomer Koren, Y. Mansour  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.15207

## One-line
Achieves optimal $O((G^2/\lambda)\log T)$ regret for online convex optimization in the random-order model when only the *average* loss is strongly convex, via algorithmic stability arguments for sampling without replacement.

## Key claim
For $G$-Lipschitz, $\beta$-smooth losses whose average $F = \tfrac{1}{T}\sum f_t$ is $\lambda$-strongly convex (but individual $f_t$ need not be convex), Algorithm 1 attains $\mathbb{E}[R_T] = O((G^2/\lambda)\log T)$ — matching the i.i.d. lower bound and removing the dimension factor $d$ and two factors of $1/\lambda$ from Garber et al. (2020)'s $O((dG^2/\lambda^3)\log T)$ bound.

## Method
Reframes random-order regret as average generalization error w.r.t. a without-replacement training sample, then proves *average-replace-one-out-of-sample (avg-oos) stability* of SGD by exploiting strong convexity of the population loss (rather than per-loss convexity). The key Lemma 3 shows the gradient step is contractive *in expectation*: $\mathbb{E}\|G(x;\psi,\eta) - G(y;\psi,\eta)\| \le (1-\eta\mu/2)\|x-y\|$ for $\eta \le \mu/\beta^2$. Algorithm 1 supplements this with a reservoir-style online sampling mechanism that converts random-order draws into i.i.d. uniform samples, keeping gradient estimates unbiased throughout all $T$ rounds; Algorithm 2 trades $\kappa = \beta/\lambda$ in regret for $O(d)$ memory.

## Result
**Theorem 1** (Algorithm 1, memory $O(Td)$): $\mathbb{E}[R_T] \le (2G^2/\lambda)(1+\log T) + (40G^2 + \beta^2 D^2 + 2\beta GD)/\lambda$. **Theorem 2** (Algorithm 2, memory $O(d)$): $\mathbb{E}[R_T] = O((\beta G^2/\lambda^2)\log T + \beta^3 D^2/\lambda^2 + \beta DG/\lambda)$. **Corollary 2** (convex but not strongly convex average): via $L_2$-regularization with $\alpha = 1/\sqrt{T}$, Algorithm 1 gives $O(\sqrt{T})$ regret; with $\alpha = 1/T^{1/3}$, Algorithm 2 gives $O(T^{2/3})$.

## Why it matters here
General background; no direct arena tie. The arena problems are static math-optimization targets (sphere packing, autocorrelation, kissing numbers), not online/sequential games — random-order regret theory does not bear on any of the 23 problems. Marginal relevance: the stability-of-SGD-with-strongly-convex-population framing could inform thinking about variance-reduced multistart on cumulative-but-not-individual objectives, but this is a stretch.

## Open questions / connections
- Extends Hardt-Recht-Singer (2016) uniform-stability analysis of SGD to the average-stability regime where only the population loss is strongly convex.
- Tightens Nagaraj-Jain-Netrapalli (2019) exchangeable-pairs analysis of SGD-without-replacement by removing the individual-convexity assumption.
- Leaves open whether the extra $\kappa$ factor in the low-memory Algorithm 2 is necessary, or whether $O(d)$-memory + optimal regret is achievable.

## Key terms
random-order online optimization, online convex optimization, SGD without replacement, algorithmic stability, average-replace-one stability, cumulative strong convexity, generalization bounds, sampling without replacement, regret bounds, contractive gradient step, reservoir sampling, condition number
