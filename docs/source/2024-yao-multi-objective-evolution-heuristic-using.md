---
type: source
kind: paper
title: Multi-objective Evolution of Heuristic Using Large Language Model
authors: Shunyu Yao, Fei Liu, Xi Lin, Zhichao Lu, Zhenkun Wang, Qingfu Zhang
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2409.16867
source_local: ../raw/2024-yao-multi-objective-evolution-heuristic-using.pdf
topic: general-knowledge
cites:
---

# Multi-objective Evolution of Heuristic Using Large Language Model

**Authors:** Shunyu Yao, Fei Liu, Xi Lin, Zhichao Lu, Zhenkun Wang, Qingfu Zhang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2409.16867

## One-line
An LLM-driven evolutionary framework (MEoH) that searches a Pareto set of heuristics trading off solution quality vs runtime in a single run, rather than chasing a single best heuristic.

## Key claim
On online Bin Packing (Weibull, capacities 100/500, up to 100k items) and TSP (random + TSPLIB up to 1,002 nodes), MEoH yields a non-dominated front of heuristics that match or beat single-objective FunSearch/EoH on the optimality gap while running **up to 10× faster**; e.g. BPP100k C100: 0.080% gap in 59s vs EoH's 0.391% gap in 503s.

## Method
LLM (GPT-3.5-turbo) acts as a zero-shot variation operator inside a $(\mu+\lambda)$ MOEA over Python heuristic code + natural-language descriptions. Novel **dominance–dissimilarity score**: pairwise dissimilarity matrix $S_{ij} = -\mathrm{SimAST}(i,j)$ from Abstract-Syntax-Tree subtree overlap is element-wise masked by a Pareto-dominance indicator $D_{ij} = \mathbf{1}[x_i \prec x_j]$, then column-summed and softmaxed to drive parent selection and population truncation. Five EoH-style prompt operators (E1/E2 exploration, M1/M2/M3 modification) generate offspring; AST dissimilarity prevents the population from collapsing onto one code template, which conventional NSGA-II/MOEA/D fail to do in this discrete code space.

## Result
HV ↑ and IGD ↓ vs EoH and vs vanilla NSGA-II/MOEA/D on both tasks. MEoH(Best) on TSPLIB ≤200 nodes: 0.018% gap @ 2.35s (vs FunSearch 0.050%/3.4s, EoH 0.093%/25.9s). Demonstrated extension to 3 objectives (gap, runtime, Halstead readability). No theoretical guarantees; purely empirical, two combinatorial benchmarks, 3 seeds.

## Why it matters here
General background — no direct arena tie. Potentially relevant as scaffolding for the autonomous-loop self-improvement layer: the dominance-dissimilarity / AST-diversity trick is a concrete antidote to LLM-driven evolutionary search collapsing onto one code template, which is the same failure mode the einstein agent risks when re-running optimizers across cycles. Does **not** advance any of the 23 arena math problems directly.

## Open questions / connections
- Extends FunSearch (Romera-Paredes 2024) and EoH (Liu 2024) — both already on the einstein agent's radar as code-search baselines.
- Scaling beyond ~3 objectives is flagged as unsolved; relevant if the cycle-runner ever weights gap + runtime + code-complexity + readability jointly.
- AST-similarity as diversity proxy is cheap but syntactic; semantically equivalent code with different ASTs would be falsely "diverse" — open question whether behavioral/output dissimilarity is a better signal for math-optimizer heuristics.
- No connection to LP duality, Cohn–Elkies, equioscillation, or any concept currently in the einstein wiki.

## Key terms
LLM-driven evolutionary search, FunSearch, EoH, MEoH, multi-objective optimization, Pareto front, NSGA-II, MOEA/D, dominance-dissimilarity, Abstract Syntax Tree similarity, hypervolume, IGD, bin packing, traveling salesman, guided local search, code-search heuristics
