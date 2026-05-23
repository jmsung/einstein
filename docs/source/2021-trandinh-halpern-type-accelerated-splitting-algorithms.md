---
type: source
kind: paper
title: Halpern-Type Accelerated and Splitting Algorithms For Monotone Inclusions
authors: Quoc Tran-Dinh, Yang Luo
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.08150
source_local: ../raw/2021-trandinh-halpern-type-accelerated-splitting-algorithms.pdf
topic: general-knowledge
cites:
---

# Halpern-Type Accelerated and Splitting Algorithms For Monotone Inclusions

**Authors:** Quoc Tran-Dinh, Yang Luo  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.08150

## One-line
Develops new accelerated first-order algorithms — based on Halpern fixed-point iteration rather than Nesterov momentum — that achieve $O(1/k)$ rates on operator residual norms for monotone equations, monotone inclusions, and Douglas–Rachford splitting.

## Key claim
For a maximally monotone $L$-Lipschitz operator $G$, a Halpern-anchored variant of Popov's past-extragradient method achieves $\|G(x_k)\| = O(1/k)$ using only **one** evaluation of $G$ per iteration (vs two for extra-anchored gradient). Splitting variants attain $O(1/k)$ rate on the forward-backward residual $\|G_\gamma(x_k)\|$ for $0 \in A(x) + B(x)$, and a new accelerated Douglas–Rachford scheme attains $O(1/k)$ on $\|G_\gamma(x_k)\|$ under only maximal monotonicity of $A,B$ (no Lipschitz/cocoercivity).

## Method
Halpern-type anchored iteration $x_{k+1} = \beta_k x_0 + (1-\beta_k) T(x_k)$ with $\beta_k = 1/(k+2)$, analyzed via Lyapunov function $V_k = a_k\|G(x_k)\|^2 + b_k\langle G(x_k), x_k - x_0\rangle + c_k L^2 \|x_k - y_{k-1}\|^2$. Three algorithms: (1) anchored Popov past-extragradient for $G(x)=0$; (2) two splitting variants (extra-gradient and Popov-flavored) combining anchoring with forward–backward; (3) accelerated Douglas–Rachford with varying/constant stepsize. Specialized to convex–concave minimax problems and a new accelerated ADMM.

## Result
$O(1/k)$ rate on the squared operator-residual / forward-backward residual norm — optimal up to a constant for monotone Lipschitz equations. The single-evaluation Popov variant matches the two-evaluation extra-anchored rate of [Yoon–Ryu 2021]. Accelerated DR works under bare maximal monotonicity (no cocoercivity, no Lipschitz), distinguishing it from prior accelerated DR work [Patrinos et al. 2014, Maingé 2021] which required stronger assumptions or analyzed a different (intermediate) sequence.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — Halpern anchoring is a different acceleration recipe than Nesterov momentum, and could potentially apply to optimizer kernels used in saddle-point / minimax formulations of arena problems (e.g., LP-dual / Cohn–Elkies-style relaxations solved via primal-dual hybrid gradient). Not directly cited by any of the 23 problems' current strategies.

## Open questions / connections
- Whether Halpern anchoring transfers cleanly to stochastic / inexact-resolvent settings (authors flag this as future work).
- Extension to co-monotone (weakly monotone) operators — partially handled by [Lee–Kim 2021] for nonconvex-nonconcave minimax; gap for splitting case.
- Whether the constant-factor gap between one-eval Popov and two-eval extragradient can be closed in practice or is fundamental.
- Connection to optimistic gradient / forward-reflected methods used in online learning [Malitsky 2015] — Popov's scheme is equivalent absent the anchor.

## Key terms
Halpern fixed-point iteration, Popov past-extragradient, Douglas–Rachford splitting, monotone inclusion, maximally monotone operator, forward-backward residual, accelerated first-order method, Lyapunov function analysis, convex-concave minimax, accelerated ADMM, anchored extragradient, optimistic gradient
