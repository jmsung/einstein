---
type: source
kind: paper
title: On exponential convergence of SGD in non-convex over-parametrized learning
authors: Raef Bassily, Mikhail Belkin, Siyuan Ma
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.02564
source_local: ../raw/2018-bassily-exponential-convergence-sgd-non-convex.pdf
topic: general-knowledge
cites:
---

# On exponential convergence of SGD in non-convex over-parametrized learning

**Authors:** Raef Bassily, Mikhail Belkin, Siyuan Ma  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.02564

## One-line
Proves that mini-batch SGD with a fixed step size achieves exponential (linear) convergence on smooth non-convex losses satisfying the Polyak-Łojasiewicz (PL) condition in the interpolation regime.

## Key claim
For $\beta$-smooth per-sample losses with $\lambda$-smooth, $\alpha$-PL empirical risk $L$ and interpolation ($\ell_i(w^*)=0$), mini-batch SGD with batch size $m$ and step size $\eta^*(m) = \frac{m}{\lambda(\beta + \lambda\alpha m(m-1))}$ satisfies $\mathbb{E}[L(w_t)] \le \left(1 - \frac{\alpha\,\eta^*(m)}{2}\right)^t L(w_0)$ — the first exponential SGD convergence result for a class of non-convex functions (including some multi-layer NNs).

## Method
Direct Polyak-style descent-lemma argument: from $\lambda$-smoothness expand $L(w_{t+1})$, take expectation over the mini-batch, bound the stochastic gradient variance using $\beta$-smoothness + non-negativity of $\ell_i$ (giving $\|\nabla\ell_i\|^2 \le 2\beta\ell_i$), then apply the PL inequality $\|\nabla L\|^2 \ge \alpha L$ to reduce to a contraction in $L(w_t)$. The optimal step size falls out of optimizing the resulting quadratic in $\eta$.

## Result
Theorem 1 gives the contraction rate above; the step size $\eta^*(m)$ scales with $m$ and with $1/\alpha$ (an open question whether the $\alpha$-dependence is necessary). Claim 1 + Corollary 1 show the smooth-PL class is closed under maps $\Phi$ with bounded Jacobian spectrum ($a \le \lambda_{\min}(J_\Phi^T J_\Phi) \le \lambda_{\max} \le b$), preserving exponential convergence with rate scaling by $a^2/b^2$. Theorem 2 sharpens the bound for losses of the form $\ell_i(w)=\tilde\ell_i(Aw)$ with strongly-convex $\tilde\ell_i$, giving rate $(1 - \alpha\sigma_{\min}^2\eta^*(m))^t$ without $\alpha$-dependence in $\eta$.

## Why it matters here
General background; no direct arena tie. The PL condition could be relevant if the agent ever frames an arena problem as ERM on a smooth surrogate where gradient-norm-vs-value bounds are checkable — but the Einstein Arena problems are geometric/combinatorial extremal, not stochastic ERM, so this is mostly orthogonal.

## Open questions / connections
- Is the $1/\alpha$ factor in the step-size bound for PL (vs strongly convex) tight or an artifact of the proof?
- Extends Ma-Bassily-Belkin 2018 (ICML, interpolation + strongly convex) to non-convex PL; connects to Karimi-Nutini-Schmidt 2016 on PL ↔ RSI ↔ one-point convexity equivalences.
- Implies exponential SGD convergence for the over-parametrized NN class of Soltanolkotabi-Javanmard-Lee 2018 — first such result for multi-layer nets.

## Key terms
Polyak-Lojasiewicz condition, PL inequality, stochastic gradient descent, mini-batch SGD, exponential convergence, linear convergence, interpolation regime, over-parametrization, smooth non-convex optimization, empirical risk minimization, restricted secant inequality, Jacobian spectrum invariance, Bassily, Belkin, Polyak
