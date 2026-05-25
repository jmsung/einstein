---
type: source
kind: paper
title: "DrNAS: Dirichlet Neural Architecture Search"
authors: Xiangning Chen, Ruochen Wang, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.10355
source_local: ../raw/2020-chen-drnas-dirichlet-neural-architecture.pdf
topic: general-knowledge
cites:
---

# DrNAS: Dirichlet Neural Architecture Search

**Authors:** Xiangning Chen, Ruochen Wang, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.10355

## One-line
Reformulates differentiable neural architecture search (DARTS) as Dirichlet distribution learning over the operation-mixing simplex, with a progressive channel/operation pruning scheme to close the search-vs-evaluation gap.

## Key claim
Modeling architecture mixing weights $\theta \sim \mathrm{Dir}(\beta)$ with an anchor regularizer $\|\beta - \mathbf{1}\|_2 \le \delta$ implicitly bounds $\mathrm{tr}(\nabla^2_\mu \tilde{L}_{\text{val}})$ (Proposition 1), yielding 2.46% CIFAR-10 / 23.7% top-1 ImageNet error and SOTA on all three NAS-Bench-201 datasets.

## Method
Replace point-estimate softmax relaxation of operation weights with a learnable Dirichlet posterior; optimize $\beta$ via pathwise derivative estimators through the Beta CDF (Jankowiak 2018) inside DARTS's bi-level loop. Add $\ell_2$ anchor $\|\beta-\mathbf{1}\|_2$ to balance exploration/exploitation. Progressive learning: split search into stages, start with narrow super-network using partial-channel connection ($K=6$), then widen via Net2Net random mapping while pruning the operation candidate set.

## Result
CIFAR-10: 2.46% ± 0.03 test error, 4.1M params, 0.6 GPU-days. ImageNet (mobile): 23.7%/7.1% top-1/5, beating PC-DARTS (24.2%), GAEA+PC-DARTS (24.0%), ProxylessNAS (24.9%). NAS-Bench-201: 94.36/73.51/46.34 test accuracy on CIFAR-10/100/ImageNet-16-120 (CIFAR-100 hits the global optimum 73.51). Hessian dominant eigenvalue stays ~10× smaller than DARTS throughout search.

## Why it matters here
General background; no direct arena tie. The Dirichlet-over-simplex reparameterization and pathwise-derivative trick are conceptually transferable to any optimizer that needs gradient-based search over probability-simplex parameters (e.g., mixture weights in council-dispatch ensembles), but the paper's domain — CNN architecture search — is orthogonal to sphere packing, autocorrelation, kissing numbers, and the other Einstein Arena problem families.

## Open questions / connections
- Could pathwise Dirichlet sampling replace softmax parameterization in optimizer weighting (e.g., parallel-tempering temperature ladders, basin-hopping restart distributions)?
- The Laplace-approximation Hessian-trace bound (Proposition 1) is a generic regularization argument — does the same bound apply to any Dirichlet-reparameterized stochastic optimizer over a simplex?
- Connection to variational inference (Appendix A.5): KL-to-symmetric-Dirichlet prior ≈ $\ell_2$ anchor in practice — relevant if any arena problem ever needs Bayesian posterior over a discrete choice set.

## Key terms
Dirichlet distribution, neural architecture search, DARTS, pathwise derivative estimator, reparameterization, probability simplex, bi-level optimization, Laplace approximation, Hessian regularization, exploration-exploitation, variational inference, partial channel connection
