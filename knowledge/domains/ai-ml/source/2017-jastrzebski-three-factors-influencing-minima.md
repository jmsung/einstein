---
type: source
kind: paper
title: Three Factors Influencing Minima in SGD
authors: Stanislaw Jastrzebski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, A. Storkey
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.04623
source_local: ../raw/2017-jastrzebski-three-factors-influencing-minima.pdf
topic: general-knowledge
cites:
---

# Three Factors Influencing Minima in SGD

**Authors:** Stanislaw Jastrzebski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, A. Storkey  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.04623

## One-line
Argues that the learning-rate-to-batch-size ratio $\eta/S$ — not $\eta$ or $S$ alone — is the key control knob in SGD, setting both the dynamics and the width of the minima found.

## Key claim
SGD is an Euler–Maruyama discretization of an SDE in which $\eta$ and $S$ appear only as the ratio $\eta/S$; at a quadratic minimum (with $C \approx H$) the stationary Ornstein–Uhlenbeck distribution gives $\mathbb{E}(L)/\mathrm{Tr}(H) \propto \eta/S$, so higher $\eta/S$ ⇒ wider minima ⇒ better generalization.

## Method
Models the SGD update as $\theta_{k+1} = \theta_k - \eta g(\theta_k) + \eta\,\xi/\sqrt{S}$ with $\xi$ zero-mean Gaussian of covariance $C(\theta)$ (via CLT over the minibatch), then identifies this as the EuM discretization of $d\theta = -g\,dt + \sqrt{\eta/S}\,R\,dW$. Near a minimum, quadratic approximation + assumption $C=H$ yields an OU process whose stationary covariance is $\mathrm{cov}(z) = (\eta/2S)I$. A complementary isotropic-covariance analysis derives a Gibbs–Boltzmann equilibrium with temperature $T=\eta\sigma^2/S$ and uses Laplace's approximation to compare basin probabilities $p_A/p_B$.

## Result
Theoretical: $\mathbb{E}(L) = (\eta/4S)\,\mathrm{Tr}(H)$, so for fixed loss, $\mathrm{Tr}(H) \propto S/\eta$. Empirically (VGG11, ResNet56 on CIFAR10; 4-layer MLP on Fashion-MNIST / MNIST): rescaling $\eta$ and $S$ by the same factor reproduces learning curves on an epoch axis (linear rescaling beats $\sqrt{S}$ rescaling); higher $\eta/S$ correlates with smaller max-eigenvalue and Frobenius norm of $H$ and higher validation accuracy; cyclic batch-size schedules substitute for cyclic learning-rate schedules; the scaling law breaks when $\eta$ grows too large (discretization error) or $S$ approaches $N$ (CLT failure).

## Why it matters here
General background; no direct arena tie. Relevant only as meta-methodology — if the agent ever trains a surrogate net or uses SGD-based optimization, $\eta/S$ should be treated as the single noise-temperature knob; the OU-stationary $\mathbb{E}(L) \propto \eta\,\mathrm{Tr}(H)/S$ identity is a clean instance of the temperature ↔ basin-width tradeoff that also appears in basin-hopping / parallel-tempering tuning (compute-router workloads).

## Open questions / connections
- Extends Mandt et al. (2017), Li et al. (2017), Junchi Li et al. (2017) on SGD-as-SDE; explicitly makes $S$ visible where Li et al. did not.
- Concurrent with Smith & Le (2017), Chaudhari & Soatto (2017) on noise-scale / non-equilibrium stationary distributions.
- Open: when does $C \approx H$ break (Appendix A gives a realizability condition); how does anisotropy of $C$ (Zhu et al. 2018, Sagun et al. 2017) modify the basin-selection law beyond the isotropic Gibbs case.
- Open: principled cyclic-noise schedules vs constant $\eta/S$ — why cycling produces wider endpoints at matched final noise level.

## Key terms
SGD, stochastic differential equation, Euler-Maruyama discretization, Ornstein-Uhlenbeck process, learning-rate-to-batch-size ratio, Hessian trace, flat minima, Gibbs-Boltzmann equilibrium, Laplace approximation, gradient covariance, generalization gap, cyclic learning rate
