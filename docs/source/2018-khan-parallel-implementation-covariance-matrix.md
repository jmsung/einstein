---
type: source
kind: paper
title: A parallel implementation of the covariance matrix adaptation evolution strategy
authors: Najeeb Khan
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1805.11201v1
source_local: ../raw/2018-khan-parallel-implementation-covariance-matrix.pdf
ingested_for_concept: cma-es-with-warmstart.md
cites: 
---

# A parallel implementation of the covariance matrix adaptation evolution strategy

**Authors:** Najeeb Khan  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1805.11201v1

## One-line
A student report implementing CMA-ES inside the pythOpt framework and parallelizing its objective-function evaluations across processes via Python's `pathos` library.

## Key claim
A fork-join parallelization of the $K$ per-generation $f$-evaluations in a single CMA-ES instance yields a measured speedup of roughly $2\times$ on 16 processes (execution time $\sim 19$ min vs $\sim 103$ min serial) on a synthetic expensive sphere objective ($n=100$, 512 evals), confirming that the approach helps only when $f$-evaluations dominate the per-generation CMA update cost.

## Method
Standard $(\mu/\mu_W,\lambda)$-CMA-ES per Hansen's tutorial: sample $x_k^{(g+1)} \sim m^{(g)} + \sigma^{(g)}\,\mathcal{N}(0,C^{(g)})$, weighted-recombine the top-$Z$, update mean (Eq. 2.2), rank-$Z$-update (Eq. 2.9) plus rank-1-update via cumulated evolution path $p_c$ (Eqs. 2.10-2.13), and step-size control through the conjugate path $p_\sigma = (1-c_\sigma)p_\sigma + \sqrt{c_\sigma(2-c_\sigma)\mu_{\rm eff}}\,C^{-1/2}(m^{(g+1)}-m^{(g)})/\sigma$ (Eq. 2.14-2.15). Parallelization is the per-iteration `pool.map(objFunc.evaluate, X)` of the $K$ sampled points; the covariance eigendecomposition $C = BD^2B^T$ remains serial. Future-work sketch: replace $O(n^3)$ eigh with parallel Cholesky factorization for the inverse square root.

## Result
On CEC-style benchmarks (sphere, Rosenbrock, Rastrigin, Ackley, Griewank, Schwefel, Schaffer F6, etc.) at 1024 $f$-evals, CMA-ES beats PSO/DWPSO/TVACPSO on most functions, ties on hyperellipsoid/deceptive, and loses on a few (e.g. dejongfive, parabola, alpine). Parallel speedup $S(n,P)$ and efficiency $E(n,P)=S/P$ measured for $P\in\{1,2,4,8,16\}$ on the 100-dim dummy sphere with per-eval cost $\sim 13$s: speedup saturates well below ideal (efficiency $\to 0.34$ at $P=16$), and the report explicitly attributes this to the cheap objective — efficiency expected to improve for genuinely expensive $f$.

## Why it matters here
Background reference for CMA-ES mechanics and a precise statement of which CMA steps are embarrassingly parallel ($f$-evals) vs sequential (eigendecomposition, mean/covariance update) — directly informs the compute-router decision for "CMA-ES large population" workloads on local MPS vs Modal. The pcmalib (Müller et al. 2009) and the Hakkarinen et al. 2012 fault-tolerant pCMA-ES are cited as the two prior parallel CMA-ES designs (multi-instance PSO-of-CMA-ES vs per-instance population parallelism), useful when choosing a parallelization strategy for arena problems whose evaluators dominate cost.

## Open questions / connections
- When does per-instance population parallelism (this paper, Hakkarinen et al.) beat multi-instance "PSO of CMA-ES" parallelism (Müller et al. pcmalib)? Crossover depends on $f$-eval cost vs CMA update cost vs basin diversity.
- Can Cholesky factorization of $C$ (PSD) replace eigendecomposition for the inverse square root, and does parallel Cholesky scale better than parallel eigh at the $n=50$-$100$ regime typical of arena problems?
- The paper does not study large-population float64 GPU CMA-ES (the regime where Modal A100/H100 wins per compute-router); it stays in CPU-process fork-join.

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, derivative-free optimization, evolutionary algorithm, rank-1 update, rank-$\mu$ update, evolution path cumulation, step-size control, parallel objective evaluation, Cholesky decomposition, pythOpt, Hansen, fork-join parallelism
