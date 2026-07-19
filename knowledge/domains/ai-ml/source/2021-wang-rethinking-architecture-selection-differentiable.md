---
type: source
kind: paper
title: Rethinking Architecture Selection in Differentiable NAS
authors: Ruochen Wang, Minhao Cheng, Xiangning Chen, Xiaocheng Tang, Cho-Jui Hsieh
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.04392
source_local: ../raw/2021-wang-rethinking-architecture-selection-differentiable.pdf
topic: general-knowledge
cites:
---

# Rethinking Architecture Selection in Differentiable NAS

**Authors:** Ruochen Wang, Minhao Cheng, Xiangning Chen, Xiaocheng Tang, Cho-Jui Hsieh  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.04392

## One-line
Shows that DARTS' architecture parameters $\alpha$ don't reflect operation strength, and replaces magnitude-based selection with a perturbation-based criterion that measures each operation's contribution to supernet accuracy.

## Key claim
The magnitude of $\alpha$ in DARTS is a biased indicator of operation strength — provably so for skip vs. conv under an "unrolled estimation" model — and replacing magnitude-based selection with perturbation-based selection improves DARTS test error on CIFAR-10 from 3.00% to 2.61% (best 2.48%) and lifts NAS-Bench-201 cifar10 error from 45.7% to 11.89%, while also fixing DARTS' failure modes on the S1–S4 robustness spaces of Zela et al. (2020).

## Method
Given a pretrained DARTS supernet, iterate edges in random order; for each candidate operation $o$ on an edge, mask it out and measure the drop in validation accuracy ($\text{ACC}_{\setminus o}$); the operation whose removal hurts most is selected and discretized; the remaining supernet is fine-tuned ~5 epochs between edges to recover. A theoretical proposition derives, via Lagrange multipliers minimizing $\mathrm{Var}(m_e(x_e) - m^*)$ subject to $\theta_{\text{skip}} + \theta_{\text{conv}} = 1$, that optimal $\alpha^*_{\text{conv}} \propto \mathrm{Var}(x_e - m^*)$ and $\alpha^*_{\text{skip}} \propto \mathrm{Var}(o_e(x_e) - m^*)$, explaining why skip dominates as the supernet improves.

## Result
DARTS+PT: 2.61±0.08% (CIFAR-10), SDARTS-RS+PT: 2.54±0.10%, SGAS+PT: 2.56±0.10%; ImageNet top-1 26.7% → 25.5%. On Zela's S1–S4, DARTS+PT reduces error dramatically (e.g., S2 CIFAR-10: 4.85% → 2.79%; S4: 7.20% → 2.64%). Surprisingly, fixing $\alpha = 0$ (uniform) during supernet training and then applying PT performs on par with or better than DARTS+PT (NAS-Bench-201 cifar10: 6.20%), suggesting $\alpha$ may be unnecessary altogether.

## Why it matters here
General background; no direct arena tie — this is a deep-learning NAS paper, not optimization for Einstein Arena math problems. The most transferable idea is the **leave-one-out perturbation criterion** (rank components by accuracy/score drop when removed), which is a generic sensitivity-analysis pattern applicable to active-constraint or active-point diagnostics in optimization (e.g., the equioscillation active-triple style of finding).

## Open questions / connections
- Can one design supernet training that exploits the freedom of not needing $\alpha$ (i.e., uniform-weight training + PT selection)?
- Generalize the unrolled-estimation analysis ($\alpha^* \propto \mathrm{Var}(\cdot - m^*)$) beyond two-op cells.
- Extends Zela et al. (2020) by reattributing DARTS failure modes from supernet optimization to architecture selection.

## Key terms
DARTS, differentiable NAS, architecture parameters, perturbation-based selection, supernet, skip connection domination, unrolled estimation, ResNet, NAS-Bench-201, SDARTS, SGAS, leave-one-out sensitivity
