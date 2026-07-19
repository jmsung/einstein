---
type: source
kind: paper
title: "COCO: a platform for comparing continuous optimizers in a black-box setting"
authors: N. Hansen, A. Auger, Olaf Mersmann, T. Tušar, D. Brockhoff
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.08785
source_local: ../raw/2016-hansen-coco-platform-comparing-continuous.pdf
topic: general-knowledge
cites:
---

# COCO: a platform for comparing continuous optimizers in a black-box setting

**Authors:** N. Hansen, A. Auger, Olaf Mersmann, T. Tušar, D. Brockhoff  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.08785

## One-line
COCO is an open-source benchmarking platform that automates how continuous black-box optimizers are compared, using runtime-to-target as the central performance measure across pseudo-randomized problem instances.

## Key claim
Solver comparison should be **budget-free** and **runtime-based**: measure number of $f$-evaluations to reach prescribed target precisions $t = f_{\mathrm{opt}} + \varepsilon$ (typically ~100 targets between $10^2$ and $10^{-8}$), aggregated as empirical CDFs / ERTs across function $\times$ dimension $\times$ instance, rather than reporting final $f$-values at a fixed budget.

## Method
Benchmark suite design: each function $f_{ij} = f_{[n,i,j]}: \mathbb{R}^n \to \mathbb{R}^m$ is parametrized by dimension $n$ and instance $j$ (pseudo-randomized translations/rotations), making deterministic and stochastic solvers directly comparable via instance-as-repetition. Performance is reported via **Expected Running Time** (ERT, with simulated restarts to handle unsuccessful runs) and **runtime ECDFs / data profiles** over $(f, n, j, t)$ tuples. Functions are chosen to be comprehensible, scalable in $n$, hard to exploit (non-separable, off-grid optima), and to model real difficulties (ill-conditioning, multimodality, ruggedness).

## Result
Provides the `bbob`, `bbob-noisy`, `bbob-biobj`, `bbob-largescale`, `bbob-mixint` suites (24 noiseless functions standard) with C/C++/Java/Matlab/Python interfaces, automated post-processing, and >300 archived datasets from >200 solvers (BFGS-P-StPt, NEWUOA, MCS, NIPOP-aCMA, NELDER-DOERR, RANDOMSEARCH, lmm-CMA-ES, ...). For multiobjective: quality indicator is normalized hypervolume $I_{HV}(S, (1,1))$ with the nadir as reference, switching to $-\min_{s,z} \mathrm{dist}(f^N(s), z)$ when the nadir is not yet dominated.

## Why it matters here
General background; no direct arena tie — but the methodology directly informs how this project should evaluate its own optimizer cycles: report runtime-to-target rather than final-score-at-budget, use multiple pseudo-random instances per problem to separate luck from skill, and never aggregate across dimension. The triple-verify rule and cycle-log discipline align with COCO's "budget-free, anytime, instance-randomized" philosophy.

## Open questions / connections
- Could the 24 `bbob` functions (ill-conditioned ellipsoid, attractive sector, Rastrigin variants) serve as a **calibration testbed** for the local CMA-ES / basin-hopping / parallel-tempering choices in `compute-router.md` before deploying them on the 23 arena problems?
- The "instance as randomization" pattern — would it help to define per-problem `instances` for our arena solvers (e.g., random rotations of P11 / P15 to detect overfitting to the specific arena verifier configuration)?
- ERT + simulated-restart machinery is a more principled alternative to "best of N seeds" that the cycle log currently uses — worth distilling into a technique page.

## Key terms
COCO, BBOB, black-box optimization, benchmarking, ERT (expected running time), runtime ECDF, data profiles, target precision, instance randomization, hypervolume indicator, derivative-free optimization, CMA-ES, NEWUOA, BFGS, MCS, budget-free experimental design, Hansen, Auger
