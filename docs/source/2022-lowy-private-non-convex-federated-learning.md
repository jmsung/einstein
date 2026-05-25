---
type: source
kind: paper
title: Private Non-Convex Federated Learning Without a Trusted Server
authors: Andrew Lowy, Ali Ghafelebashi, Meisam Razaviyayn
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.06735
source_local: ../raw/2022-lowy-private-non-convex-federated-learning.pdf
topic: general-knowledge
cites:
---

# Private Non-Convex Federated Learning Without a Trusted Server

**Authors:** Andrew Lowy, Ali Ghafelebashi, Meisam Razaviyayn  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.06735

## One-line
Differentially-private federated learning algorithms for non-convex losses (Proximal-PL and non-smooth) under inter-silo record-level DP (ISRL-DP) and shuffle DP (SDP), without trusting the server or other silos.

## Key claim
For heterogeneous FL with $\mu$-Proximal-PL, $L$-Lipschitz, $\beta$-smooth losses, Noisy Prox-SGD attains ISRL-DP excess risk $\tilde{O}\big(\tfrac{L^2}{\mu}(\tfrac{\kappa^2 d \ln(1/\delta)}{\epsilon^2 n^2 M} + \tfrac{\kappa}{Mn})\big)$ and SDP excess risk $\tilde{O}\big(\tfrac{L^2}{\mu}(\tfrac{\kappa^2 d \ln^2(d/\delta)}{\epsilon^2 n^2 N^2} + \tfrac{\kappa}{Mn})\big)$ with $\kappa=\beta/\mu$ — nearly matching the strongly-convex i.i.d. lower bounds up to $\tilde{O}(\kappa^2)$ factors, without convexity or i.i.d. data.

## Method
Noisy distributed Proximal SGD: each silo perturbs minibatch gradients with Gaussian (ISRL-DP) or binomial (SDP via secure shuffler) noise, server aggregates and applies a proximal operator step $w_{r+1}=\mathrm{prox}_{\eta f_1}(w_r-\eta\bar g_r)$. For ERM, a proximal variance-reduced SPIDER variant (FedProx-SPIDER) is introduced. Analysis novelty: treat each noisy proximal step as objective perturbation (Chaudhuri–Kifer), since under proximal+non-convexity, noise cannot be cleanly separated from non-private terms.

## Result
Theorem 2.1 (PPL SO) and Theorem 2.2 (PPL ERM) give the bounds above with matching lower bounds within $\tilde{O}(\kappa^2)$. Theorem 3.1 (non-convex non-smooth ERM, ISRL-DP) gives squared proximal-gradient norm $\tilde{O}\big((\tfrac{\sqrt{d}}{\epsilon n \sqrt{M}})^{4/3}\big)$, improving the prior smooth $\tilde{O}(\tfrac{\sqrt d}{\epsilon n\sqrt M})$ rate of Noble et al.; Theorem 3.3 gives the first non-trivial ISRL-DP non-convex lower bound $\Omega(d\ln(1/\delta)/(\epsilon^2 n^2 N))$. Experiments on MNIST, CIFAR-10, and WBCD show the SPIDER variant beats ISRL-DP MB-SGD / Local-SGD baselines at most $\epsilon\in\{0.75,\dots,18\}$.

## Why it matters here
General background; no direct arena tie. Differential-privacy federated optimization sits well outside the sphere-packing / autocorrelation / extremal-combinatorics scope of Einstein Arena. The only faint methodological echo is variance-reduced stochastic gradient (SPIDER) and proximal operators — generic optimization machinery not tied to any of the 23 problems.

## Open questions / connections
- Removing the a-priori Lipschitz bound assumption for heavy-tailed / unbounded data distributions.
- Closing the $\tilde{O}(\kappa^2)$ gap between PPL upper bounds and the strongly-convex lower bounds.
- Private hyperparameter tuning and pre-processing — currently done non-privately, inflating effective $\epsilon$.

## Key terms
differential privacy, federated learning, inter-silo record-level DP, shuffle DP, Proximal Polyak-Łojasiewicz inequality, SPIDER variance reduction, proximal operator, objective perturbation, non-convex optimization, Gaussian mechanism, stochastic gradient descent, heterogeneous silos
