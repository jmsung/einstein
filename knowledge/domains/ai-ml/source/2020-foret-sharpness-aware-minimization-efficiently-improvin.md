---
type: source
kind: paper
title: Sharpness-Aware Minimization for Efficiently Improving Generalization
authors: Pierre Foret, Ariel Kleiner, H. Mobahi, Behnam Neyshabur
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.01412
source_local: ../raw/2020-foret-sharpness-aware-minimization-efficiently-improvin.pdf
topic: general-knowledge
cites:
---

# Sharpness-Aware Minimization for Efficiently Improving Generalization

**Authors:** Pierre Foret, Ariel Kleiner, H. Mobahi, Behnam Neyshabur  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.01412

## One-line
Introduces SAM, an optimizer that minimizes loss + local sharpness simultaneously by solving a min-max where the inner max is a small adversarial weight perturbation, biasing SGD toward flat minima that generalize better.

## Key claim
Replacing SGD/Adam with SAM uniformly improves test accuracy on CIFAR-10/100, ImageNet, SVHN, Fashion-MNIST, and fine-tuning benchmarks (e.g., ResNet-152 ImageNet top-1: $20.3\% \to 18.4\%$; PyramidNet+ShakeDrop CIFAR-100: $10.6\% \to 10.3\%$; ImageNet via EffNet-L2: $11.39\%$), and provides label-noise robustness on par with specialized methods. Backed by a PAC-Bayes bound $L_D(w) \le \max_{\|\epsilon\|_2 \le \rho} L_S(w+\epsilon) + h(\|w\|_2^2/\rho^2)$.

## Method
Reformulate training as $\min_w \max_{\|\epsilon\|_p \le \rho} L_S(w+\epsilon) + \lambda\|w\|_2^2$. Inner max is approximated by a first-order Taylor expansion, giving a closed-form dual-norm perturbation $\hat\epsilon(w) = \rho\,\mathrm{sign}(\nabla L)\,|\nabla L|^{q-1}/\|\nabla L\|_q^{q/p}$ (rescaled gradient when $p=2$); then take a standard SGD step on $\nabla L_S(w+\hat\epsilon(w))$, dropping second-order Hessian terms (each step = 2 backward passes).

## Result
PAC-Bayes generalization bound (Thm 2) ties test loss to neighborhood-max training loss plus a complexity term in $\log(1+\|w\|_2^2/\rho^2)$. Empirically yields SOTA on multiple vision tasks; introduces **$m$-sharpness** — per-micro-batch max over disjoint $m$-subsets — which correlates better with the generalization gap as $m$ decreases, and smaller $m$ also trains better (favorable for data-parallel scaling).

## Why it matters here
General background; no direct arena tie. Potentially relevant only as a loss-landscape lens — "wide vs sharp minima" is a metaphor occasionally invoked for non-convex math optimization (basin hopping, parallel tempering), but SAM itself targets stochastic neural net training, not the deterministic float64 optimizers used on Einstein Arena problems.

## Open questions / connections
- Why does including the second-order (Hessian-vector) terms in the SAM gradient *hurt* performance in practice?
- Can adversarial-perturbation regularization be transposed from weight space to *parameter* space of math optimizers (e.g., perturb a sphere-packing configuration before computing minimum pairwise distance) to escape sharp/spurious local optima?
- Relation to Entropy-SGD (Chaudhari 2016), SWA (Izmailov 2018), flat-minima hypothesis (Hochreiter-Schmidhuber 1997), all-layer margin (Wei-Ma 2020).
- $m$-sharpness as a generalization predictor with $m < n$ — a new theoretical handle distinct from full-train-set sharpness.

## Key terms
sharpness-aware minimization, SAM, flat minima, sharp minima, loss landscape geometry, PAC-Bayes generalization bound, adversarial weight perturbation, m-sharpness, min-max optimization, Hessian spectrum, dual norm perturbation, generalization gap, Foret, Neyshabur, Mobahi
