---
type: source
kind: paper
title: An ODE method to prove the geometric convergence of adaptive stochastic algorithms
authors: Youhei Akimoto, A. Auger, N. Hansen
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.06703
source_local: ../raw/2018-akimoto-ode-method-prove-geometric.pdf
topic: general-knowledge
cites:
---

# An ODE method to prove the geometric convergence of adaptive stochastic algorithms

**Authors:** Youhei Akimoto, A. Auger, N. Hansen  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.06703

## One-line
Extends the ODE method of stochastic approximation to prove *geometric* (linear) convergence of constant-step-size, comparison-based adaptive search algorithms like CMA-ES.

## Key claim
For an algorithm $\theta_{n+1} = \theta_n + \alpha F_n$ with mean ODE $\dot\theta = F(\theta)$, geometric convergence $\mathbb{E}[\Psi(\theta_n)] \leq C \cdot r^n \Psi(\theta_0)$ (with $r<1$) holds whenever two conditions are met: (A1) a Lyapunov-like function $\Psi$ contracts geometrically along the ODE flow, i.e. $\Psi(\varphi(t;\theta)) \leq \Delta_{A1}(t)\Psi(\theta)$ with $\Delta_{A1}(t)\downarrow 0$; (A2) the stochastic-vs-ODE deviation is bounded *proportionally to* $\Psi(\theta_0)$ (not by a constant, as in standard SA theory). Applied to a step-size-adaptive ES on the sphere function, this yields explicit linear convergence of $\|m_n - x^*\|$ and $\sigma_n$ to zero.

## Method
ODE method + Lyapunov stability, with two practical verification theorems: Theorem 8 reduces (A1) to an upper-Dini-directional-derivative condition $D^+\Psi(\theta)[F(\theta)] \leq -c\,\Psi(\theta)$ (à la exponential stability in Lyapunov theory); Theorem 9 reduces (A2) to a constant-times-$\Psi$ bound on $\mathbb{E}[\|F_n\|^2]$ via a discrete Grönwall argument. A side contribution (Appendix B) is an *improved Chebyshev sum inequality* giving strictly positive lower bounds on covariances of non-negatively correlated random variables, used to lower-bound the drift of the rank-weighted update.

## Result
Geometric convergence in expectation is proved for the constant-$\alpha$ step-size-adaptive ES (Eq. 3 — a simplified CMA-ES) on the spherical objective $f(x) = \nu(\|x\|)$ with $\nu$ decreasing. The contraction factor on $\Psi(\theta_n) = \log(\|m_n\|/\sigma_n) + $ scale terms is proportional to $\exp(-\alpha)$ for small $\alpha$, and the framework also yields *first-hitting-time* bounds (not just asymptotic rates). Key per-step drift: $\langle \nabla V(\theta), F(\theta)\rangle \leq -c \cdot V(\theta)$ with explicit constants from rank-weights $w_k$, dimension $d$, and noncentrality $\xi(\theta) = \|m\|/\sigma$.

## Why it matters here
General background; no direct arena tie. Relevant only as theoretical grounding for *why* CMA-ES converges linearly — useful when picking CMA-ES variants for continuous problems (P1 sphere packing, P11 Hardin-Sloane configurations, any black-box continuous optimization in the arena's 23 problems) and for understanding when constant vs. decreasing step-size is the right call (connects to `findings/gpu-modal-compute.md` and the compute-router).

## Open questions / connections
- Does the framework extend to the *full* CMA-ES (covariance adaptation $C_n$), or only to scalar-$\sigma$ step-size ES?
- The proof is on the spherical/convex-quadratic landscape — when does it fail on multimodal landscapes that the arena actually presents?
- The improved Chebyshev inequality (Theorem 21, Appendix B) is a standalone tool — could it sharpen drift bounds for rank-weighted algorithms elsewhere?
- Extends [Borkar-Meyn 2000] (decreasing step-size ODE method) to the constant-step-size geometric-rate regime.

## Key terms
ODE method, stochastic approximation, geometric convergence, linear convergence, Lyapunov function, CMA-ES, evolution strategy, comparison-based optimization, rank-based update, step-size adaptation, IGO, natural gradient, Chebyshev sum inequality, Dini derivative, first hitting time, constant step-size, Akimoto, Auger, Hansen
