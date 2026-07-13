<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "AlphaEvolve: A coding agent for scientific and algorithmic discovery"
authors: [Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog]
year: 2025
doi: null
source_url: null
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AlphaEvolve: A coding agent for scientific and algorithmic discovery

## TL;DR
AlphaEvolve is an evolutionary coding agent that orchestrates an ensemble of frontier LLMs (Gemini 2.0 Flash + Pro) to iteratively mutate code, grounded by automated evaluators, discovering provably-correct algorithms that beat SOTA on math/CS open problems and deliver real production gains across Google's compute stack — most notably a rank-48 algorithm for 4×4 complex matrix multiplication, the first improvement on Strassen (1969) in 56 years.

## Key findings
- **Core architecture.** An asynchronous evolutionary loop: a *prompt sampler* builds rich context from a *program database* (MAP-Elites + island model), an *LLM ensemble* proposes code diffs (SEARCH/REPLACE blocks), proposals are applied and scored by an *evaluators pool*, and survivors re-enter the database. Humans define "what" (initial program, evaluation metric, optional context); AlphaEvolve figures out "how."
- **Evolves whole files in any language**, up to hundreds of lines spanning multiple components — a major scale jump over its predecessor FunSearch (single Python function, ≤10–20 lines, millions of samples, small code-only LLMs). AlphaEvolve needs only thousands of samples, supports multi-objective optimization, and benefits from SOTA LLMs (Table 1).
- **Matrix multiplication (§3.1).** Improved SOTA for 14 of 54 tensor-decomposition targets (matched 38, fell behind on 2). For ⟨4,4,4⟩, found a **rank-48** decomposition over complex values vs Strassen's recursive rank-49 — first sub-49 algorithm over a characteristic-0 field in 56 years. General-purpose, yet surpasses the specialized AlphaTensor (Fawzi et al. 2022, which got rank-47 only over GF(2)). Evolved the *search algorithm* (optimizer, init, loss with discretization/hallucination terms, hyperparameter sweep), requiring ~15 mutations.
- **Open mathematics (§3.2).** Applied to 50+ problems across analysis, combinatorics, number theory, geometry. Matched best-known constructions in ~75%, surpassed SOTA in ~20%. Highlights: **kissing number in 11 dimensions** improved from 592 → **593** spheres; **Erdős's minimum overlap problem** upper bound 0.380927 → 0.380924; first autocorrelation inequality C₁ ≤ 1.5098 → 1.5053. Key trick: evolve *heuristic search programs* (given a fixed time budget, e.g. 1000s) rather than constructions directly, yielding multi-stage adaptive search strategies. Problems suggested by Terence Tao and Javier Gomez Serrano.
- **Google infrastructure (§3.3).** (1) Borg data-center scheduling heuristic deployed fleet-wide, continuously recovering **0.7%** of stranded compute; chosen over deep RL for interpretability/debuggability. (2) Gemini training kernel tiling: **23% average kernel speedup**, ~1% reduction in overall Gemini training time, cutting kernel-optimization time from months to days. (3) TPU Verilog arithmetic circuit: a verified bit-removal simplification — Gemini's first direct contribution to TPU circuits. (4) FlashAttention XLA IR optimization: **32% kernel speedup** plus **15%** on pre/post-processing.
- **Ablations (§4)** on matrix-mult and kissing-number tasks confirm each component matters: evolution (vs repeated sampling), prompt context, meta-prompt evolution, full-file evolution, and using powerful (not just small) LLMs each contribute significant gains (Figure 8).

## Methods (brief)
LLM-guided evolutionary computation over code, grounded by user-supplied programmatic `evaluate` functions returning scalar metrics (maximized). Features evaluation cascades (cheap-to-expensive test stages), optional LLM-generated feedback scores, parallelized evaluation (up to ~100 compute-hours/solution), meta-prompt co-evolution, and code annotated with `# EVOLVE-BLOCK-START/END` markers. Implemented as an asyncio throughput-optimized pipeline.

## Limitations
The hard constraint is that AlphaEvolve only handles problems with an *automated evaluator* — ruling out wet-lab natural-science tasks requiring manual experimentation. Empirically it ran out of GPU memory beyond ⟨5,5,5⟩ matrix sizes, and self-improvement feedback loops are slow (months). Results are a white paper (no peer review); full math details deferred to a forthcoming paper.

## Citations of interest
- Romera-Paredes et al. 2023 (FunSearch, Nature) — the direct predecessor AlphaEvolve generalizes.
- Fawzi et al. 2022 (AlphaTensor, Nature) — specialized RL approach to matrix-mult tensor decomposition that AlphaEvolve surpasses while being general.
- Strassen 1969 — the 56-year-old rank-49 baseline for 4×4 multiplication.
- Mouret & Clune 2015 (MAP-Elites) — database algorithm for exploration/exploitation balance.
- Gottweis et al. 2025 (AI Co-Scientist) — concurrent natural-language scientific-discovery agent; complementary paradigm.
- Mankowitz et al. 2023 (faster sorting via deep RL, Nature) — related provably-correct algorithm discovery.
