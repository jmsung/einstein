<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning, sci-math]
title: Multi-objective Evolution of Heuristic Using Large Language Model
authors: [Shunyu Yao, Fei Liu, Xi Lin, Zhichao Lu, Zhenkun Wang, Qingfu Zhang]
year: 2024
source_url: https://arxiv.org/abs/2409.16867
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
LLM-driven evolutionary search, FunSearch, EoH, MEoH, multi-objective optimization, Pareto front, NSGA-II, MOEA/D, dominance-dissimilarity, Abstract Syntax Tree similarity, hypervolume, IGD, bin packing, traveling salesman, guided local search, code-search heuristics
