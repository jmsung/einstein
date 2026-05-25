---
type: source
kind: paper
title: Identification of the Isotherm Function in Chromatography Using CMA-ES
authors: Mohamed Jebalia, Anne Auger, Marc Schoenauer, Francois James, Marie Postel
year: 2007
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0710.0322v1
source_local: ../raw/2007-jebalia-identification-isotherm-function-chromatography.pdf
topic: general-knowledge
cites:
---

# Identification of the Isotherm Function in Chromatography Using CMA-ES

**Authors:** Mohamed Jebalia, Anne Auger, Marc Schoenauer, Francois James, Marie Postel  ·  **Year:** 2007  ·  **Source:** http://arxiv.org/abs/0710.0322v1

## One-line
Applies CMA-ES (with restart + increasing population) to the inverse problem of identifying parametric isotherm functions in nonlinear chromatography from experimental chromatograms, beating a gradient-based method in both fitness and robustness.

## Key claim
On real ternary-mixture data (BA/PE/MBA), CMA-ES with restart reaches fitness $8.32 \times 10^{-3}$ on the full 6-parameter modified-Langmuir model, whereas the gradient method could not get below $\sim 10^{-2}$ on the same 6-parameter problem; on the reduced 3-parameter sub-problem CMA-ES matches the gradient method's $\approx 8.8 \times 10^{-3}$ but with deterministic convergence across all 12 independent runs.

## Method
CMA-ES restart variant [Auger–Hansen 2005]: rank-$\mu$ + rank-one covariance update with path-length step-size control, $\lambda = \lfloor 4 + 3 \log n \rfloor$ doubled at each of up to 5 restarts (criteria: TolFun, TolX, NoEffectAxis, CondCov $> 10^{14}$). Parameters are linearly rescaled to $[-1,1]^n$ using expert-supplied ranges; unfeasible offspring (negative parameters or CFL-violating, leading to numerical blowup of the Godunov scheme for $\partial_z c + \partial_t F(c) = 0$) are penalized with fitness $10^{20}$ / $> 10^6$ respectively. Fitness is the $L^2$ residual $J(H) = \int_0^T \|c_H(t,L) - c_\text{exp}(t)\|^2 dt$, summed across multiple experimental chromatograms.

## Result
On simulated data (Langmuir, Bi-Langmuir, Lattice models, $m \in \{1,2,3\}$ components, $n \in \{2,\dots,10\}$), CMA-ES reproducibly recovers ground-truth parameters to fitness $\sim 10^{-14}$, occasionally requiring 1–2 restarts to escape local optima. An ablation (Table I) shows tight expert ranges matter more than a good starting guess: with expert range, $100\%$ of 120 runs converge with zero restarts; with wide range + expert guess, $95\%$; with wide range + no guess, $84\%$. On real ternary data, all 12 CMA-ES runs converged to identical isotherm parameters vs. 10 distinct local optima for 10 gradient starts.

## Why it matters here
General background; no direct arena tie. Reinforces the wiki's existing CMA-ES technique pages with three concrete points: (i) **parameter scaling dominates initial guess** for multimodal landscapes — relevant to any arena problem where the agent picks bounds without strong priors; (ii) **restart-with-doubling-$\lambda$** is the canonical multimodal-escape recipe; (iii) CMA-ES is rank-invariant under monotone fitness transforms, so cost-function reshaping (e.g. clipping outliers) is free.

## Open questions / connections
- Multi-objective CMA-ES (Igel–Hansen–Roth 2007) for problems where two fitness signals disagree — could the same idea help any arena problem where local evaluator and exact reimplementation give slightly different objectives?
- The CFL-violation handling (large constant penalty + truncation) is crude; principled barrier/penalty design for "simulation blew up" failure modes is left open.
- Quadratic scaling of evaluation cost with grid resolution — same precision-vs-budget tension the arena agent faces with mpmath dps choice.

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, restart-CMA, IPOP-CMA, increasing population size, rank-one update, rank-mu update, path length control, step-size adaptation, inverse problem, parameter identification, Langmuir isotherm, Godunov scheme, hyperbolic conservation law, Auger, Hansen, multimodal optimization, parameter scaling
