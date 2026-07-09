---
type: source
kind: paper
title: "cmaes : A Simple yet Practical Python Library for CMA-ES"
authors: Masahiro Nomura, Masashi Shibata
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2402.01373
source_local: ../raw/2024-nomura-cmaes-simple-yet-practical.pdf
topic: general-knowledge
cites:
---

# cmaes : A Simple yet Practical Python Library for CMA-ES

**Authors:** Masahiro Nomura, Masashi Shibata  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2402.01373

## One-line
A pure-Python, NumPy-only CMA-ES library that bundles recent practical extensions (learning-rate adaptation, warm-starting, mixed-variable, multi-objective) behind a simple ask-and-tell API.

## Key claim
A minimal-dependency CMA-ES implementation can simultaneously be educationally readable AND ship state-of-the-art extensions — LRA-CMA, WS-CMA, CatCMAwM, COMO-CatCMAwM — none of which exist in rival ES libraries (pycma, evojax, evosax, pymoo, Nevergrad). It is integrated into Optuna and Katib and has >450 GitHub stars.

## Method
Standard $(\mu/\mu_w,\lambda)$-CMA-ES: sample $x_i = m^{(g)} + \sigma^{(g)} \sqrt{C^{(g)}} z_i$ with $z_i \sim \mathcal{N}(0,I)$, rank solutions, update evolution paths $p_\sigma, p_c$, then update $m, \sigma, C$ via rank-one + rank-$\mu$ updates (Hansen 2016 variant). Extensions: (i) LRA-CMA adapts the learning rate $\eta$ on distribution parameters to hold the signal-to-noise ratio constant (handles multimodal + noisy); (ii) WS-CMA fits a GMM to source-task solutions then minimizes KL to seed the target-task initial $(m,\sigma,C)$; (iii) CatCMAwM extends CMA-ESwM's margin-based integer handling to joint continuous/integer/categorical via lower- AND upper-bounded marginal probabilities; (iv) COMO-CatCMAwM uses the Sofomore framework — multiple CatCMAwM kernels optimizing UHVI (uncrowded hypervolume improvement) subproblems.

## Result
On the 40-D Rastrigin function with the default $\lambda = 4 + \lfloor 3\log d \rfloor = 15$, vanilla CMA-ES gets trapped in local optima while LRA-CMA reaches the global optimum with no hyperparameter tuning. CatCMAwM beats SOTA Bayesian-optimization baselines on mixed-variable benchmarks. COMO-CatCMAwM is competitive with or better than NSGA-II and MOTPE on bi-objective mixed-variable hypervolume. The library also slashes pickle serialization size vs pycma (Fig. 3) — important for resumable hyperparameter studies.

## Why it matters here
Directly relevant to the **compute-router / optimizer-selection** layer: arena problems P3, P11 (kissing-number-like), P15/P16 (equioscillation), and any rugged/ill-conditioned basin search are textbook CMA-ES territory, and LRA-CMA's no-tuning guarantee on multimodal landscapes is exactly the property needed for autonomous-loop runs. CatCMAwM/COMO add a mixed-variable path the wiki currently lacks — useful when a problem couples a continuous configuration with discrete combinatorial choices (e.g., a Sidon-set anchor pattern + continuous offsets).

## Open questions / connections
- Does LRA-CMA's $\eta$-adaptation interact safely with mpmath/float64 polish phases, or does it stall once the SNR collapses near a SOTA basin?
- Can WS-CMA transfer solutions across arena dimensions (e.g., from $n=49$ to $n=50$) by treating the smaller-$n$ optimum as a source-task GMM?
- COMO-CatCMAwM is currently bi-objective only — the Sofomore $k$-kernel design generalizes, but extension to >2 objectives is left open.
- Connects to the existing `techniques/compute-router.md` row "CMA-ES large population" (float32 MPS vs float64 Modal): cmaes is pure NumPy, so it routes local-CPU, not GPU.

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, learning rate adaptation, LRA-CMA, warm starting, WS-CMA, CatCMAwM, mixed-variable optimization, multi-objective optimization, Sofomore, uncrowded hypervolume improvement, ask-and-tell, Hansen, black-box optimization, natural gradient, IPOP-CMA-ES, BIPOP-CMA-ES, Optuna
