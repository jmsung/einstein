---
type: source
kind: paper
title: Multi-Object Manipulation via Object-Centric Neural Scattering Functions
authors: Stephen Tian, Yancheng Cai, Hong-Xing Yu, Sergey Zakharov, Katherine Liu, Adrien Gaidon, Yunzhu Li, Jiajun Wu
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2306.08748
source_local: ../raw/2023-tian-multi-object-manipulation-object-centric-neural.pdf
topic: general-knowledge
cites:
---

# Multi-Object Manipulation via Object-Centric Neural Scattering Functions

**Authors:** Stephen Tian, Yancheng Cai, Hong-Xing Yu, Sergey Zakharov, Katherine Liu, Adrien Gaidon, Yunzhu Li, Jiajun Wu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.08748

## One-line
A robotic manipulation pipeline that represents scenes as composable per-object relightable neural scattering fields, inverts them via CMA to recover 6D poses and light direction, and feeds those poses to a graph-neural-network dynamics model for visual model-predictive control under harsh lighting.

## Key claim
Combining object-centric neural scattering functions (OSFs) with a GNN dynamics model yields better long-horizon prediction and MPC pose-error performance than pixel-space FitVid and compositional-NeRF baselines, including on out-of-distribution scenes with 2 or 4 objects when trained only on 3-object scenes.

## Method
KiloOSF — an object-centric, relightable variant of NeRF using thousands of tiny MLPs — models per-object cumulative radiance transfer $f_\theta:(x,\omega_{\text{light}},\omega_{\text{out}})\to(\rho,\sigma)$, enabling compositional volumetric rendering with shadow mapping. Inverse parameter estimation uses CMA-ES (Hansen 2003) to minimize multi-view MSE between rendered and observed images, recovering object 6D poses ($\mathbb{R}^{n\times 7}$) and light position $L_p\in\mathbb{R}^3$. Dynamics are predicted by a GNN with dynamically constructed collision-proximity edges; planning uses MPPI rollouts scored by KiloOSF-rendered image MSE against the goal image.

## Result
Across 20 randomized tabletop pushing tasks with hemisphere-sampled unknown lighting and YCB objects, the method achieves lower final 6D pose error than FitVid+MPC and Driess et al.'s compositional NeRF baseline, with the gap holding in 2- and 4-object unseen settings. Real-world demos recover plausible spotlight position, distance, and "look-at," with PoseCNN-initialized poses refined by IoU-based mask matching.

## Why it matters here
General background; no direct arena tie — this is a robotics/3D-vision paper on visual MPC and inverse rendering, not relevant to sphere packing, autocorrelation, kissing numbers, or any Einstein Arena math problem. The only tangential touchpoint is its heavy use of CMA-ES, which the arena agent also relies on for many of the 23 problems.

## Open questions / connections
- CMA-ES used as a black-box optimizer over a non-convex appearance loss — same workhorse as einstein's optimizer stack; their multi-stage warmup (fix light, optimize objects, then jointly) is a CMA scheduling trick worth noting.
- Per-object OSF training is the bottleneck; meta-learned / amortized neural fields would extend the method.
- Limited to rigid objects and a simple distant-light model; deformables and area/environment lighting are open.

## Key terms
neural scattering function, OSF, KiloOSF, NeRF, compositional rendering, CMA-ES, covariance matrix adaptation, inverse rendering, 6D pose estimation, graph neural network dynamics, model-predictive control, MPPI, visual foresight, robotic manipulation
