---
type: source
kind: paper
title: Neural Ordinary Differential Equations
authors: T. Chen, Yulia Rubanova, J. Bettencourt, D. Duvenaud
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.07366
source_local: ../raw/2018-chen-neural-ordinary-differential-equations.pdf
topic: general-knowledge
cites:
---

# Neural Ordinary Differential Equations

**Authors:** T. Chen, Yulia Rubanova, J. Bettencourt, D. Duvenaud  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.07366

## One-line
Parameterize a neural network's hidden-state dynamics as an ODE $dh/dt = f(h,t,\theta)$ and train it end-to-end by backpropagating through a black-box ODE solver via the adjoint sensitivity method.

## Key claim
Reverse-mode gradients of any ODE solver output can be computed in $O(1)$ memory and time linear in problem size by solving an augmented adjoint ODE backwards in time; further, a continuous transformation replaces the $O(D^3)$ $\log\det |\partial f/\partial z|$ in normalizing flows with an $O(D)$ trace $\mathrm{tr}(\partial f/\partial z)$.

## Method
Treat the solver as a black box; define the adjoint $a(t)=\partial L/\partial z(t)$ obeying $da/dt = -a(t)^T \partial f/\partial z$, and integrate the concatenated state $[z, a, \partial L/\partial \theta]$ backwards using a second ODE solve, with vector-Jacobian products supplied by autodiff. For density modeling, replace finite-flow change-of-variables with the instantaneous change-of-variables $\partial \log p(z(t))/\partial t = -\mathrm{tr}(df/dz)$, derived via Jacobi's formula and Picard existence under Lipschitz $f$.

## Result
On MNIST, ODE-Net matches ResNet test error (0.42% vs 0.41%) with $O(1)$ memory vs $O(L)$ and comparable parameter count (0.22M vs 0.60M); backward NFE is ~half forward NFE. Continuous normalizing flows with $M$ hidden units are linear-cost in $M$ (vs $O(M^3)$ for standard NF) and empirically out-perform $K$-layer planar NFs at density matching and maximum-likelihood density estimation; latent-ODE time-series models extrapolate irregularly-sampled spirals where RNN baselines fail.

## Why it matters here
General background; no direct arena tie — the Einstein Arena problems are static optimization (sphere packing, autocorrelation, kissing numbers) rather than dynamics learning. The adjoint sensitivity method is, however, a textbook example of the dual-ODE / Pontryagin technique that could inform any gradient-flow or continuous-time relaxation of a discrete optimization (e.g., parameterizing a configuration trajectory).

## Open questions / connections
- Can the instantaneous change-of-variables trick be exploited for sampling on constraint manifolds relevant to packing problems?
- Adjoint method is Pontryagin (1962) — the same machinery underlies optimal-control-as-optimization formulations.
- Connection to ResNet-as-Euler-discretization (Lu et al. 2017; Haber & Ruthotto 2017): does adaptive-step solver give a better "depth router" than fixed L?
- Reconstructing trajectories backwards can drift numerically; checkpointing tradeoff is unresolved.

## Key terms
neural ODE, adjoint sensitivity method, Pontryagin, continuous normalizing flow, instantaneous change of variables, Jacobi formula, Picard existence, Lipschitz continuity, vector-Jacobian product, ResNet-as-Euler, latent ODE, variational autoencoder, Poisson process likelihood, Runge-Kutta, implicit Adams
