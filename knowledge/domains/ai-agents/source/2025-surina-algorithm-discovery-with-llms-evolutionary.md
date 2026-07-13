<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning"
authors: [Anja Surina, Amin Mansouri, Lars Quaedvlieg, Amal Seddas, Maryna Viazovska, Emmanuel Abbe, Caglar Gulcehre]
year: 2025
doi: 10.48550/arXiv.2504.05108
source_url: https://doi.org/10.48550/arXiv.2504.05108
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning

## TL;DR
EvoTune augments FunSearch-style LLM evolutionary program search by closing the loop with RL (DPO) fine-tuning on the LLM generator, so the search operator itself improves over time — consistently outperforming a non-training FunSearch baseline on combinatorial-optimization and symbolic-regression tasks across three small (1B–3.8B) LLMs.

## Key findings
- **Core idea.** Existing LLM evolutionary search (FunSearch; Romera-Paredes 2024) treats the LLM as a *static* generator. EvoTune alternates two phases: (a) evolutionary search that bootstraps new Python programs from the best-so-far, and (b) RL fine-tuning that updates the LLM policy on the programs discovered, embodying Sutton's "Bitter Lesson" that search and learning are synergistic.
- **Algorithm.** An island-based program database stores all valid programs + scores. Prompts concatenate m=2 program-score pairs in Chain-of-Thought style, asking the model to identify what makes high-scorers differ. K=8 outputs/prompt; RL update every f_RL=400 search iters (every ~3,200 outputs); runs to T=2800 (~22.4k samples). Each run reinitializes from the base model π_θ0.
- **RL = off-policy DPO, not PPO.** Formulated as preference optimization (cheaper, no separate reward/value model). Higher- vs lower-scoring outputs from the same prompt are paired; failed/invalid programs paired against valid ones; triplets filtered by a dynamic threshold (30th percentile of recent rewards).
- **Forward-KL DPO preserves diversity.** A key design choice: forward-KL (mass-covering) regularization with high β=0.4 avoids the mode collapse of reverse-KL. Ablation on bin packing (Llama 1B): forward KL beats reverse KL on both top-50 reward and number of unique solutions (Fig 3b). Output diversity is treated as critical to evolutionary search success.
- **Consistent gains.** Across bin packing (BP), TSP, and flatpack (FP) × {Llama3.2-1B, Phi-3.5-Mini-3.8B, Granite-3.1-2B} × 3 sampling budgets (9.6k/16k/22.4k) on validation, validation-perturbed, and test sets, EvoTune lowers the mean top-50 optimality gap vs FunSearch in nearly all cells (Table 1). It also finds more unique-scoring solutions (Fig 2) and a higher *average* reward across all valid programs. Gap widens with larger sampling budget.
- **Real-world generality.** On Google Hash Code Datacenter Optimization, EvoTune scored **418, beating the top human team's 407** (FunSearch 414). On LLM-SR symbolic regression, EvoTune (Phi-3.5-Mini 3.8B) beat FunSearch and matched/surpassed larger LLM-SR baselines (Mixtral 8x7B, GPT-3.5-turbo) — e.g. Stress-Strain OOD NMSE 0.0035 vs LLM-SR's 0.0516/0.0946 (Table 2).
- **vs non-LLM baselines.** On 29 TSPLib instances, the evolved heuristic (trained with tiny GLS budget t_max=20) deployed at t_max=1000 achieved best average optimality gap (0.32) vs LEHD/NeuralGLS/KGLS (Table 4). Beats human-designed best-fit/greedy initializers for BP and FP (Table 5).

## Methods (brief)
LLM-driven evolutionary program synthesis over executable Python heuristics, evaluated on held-out validation instances (optimality gap as reward). RL phase uses DPO with LoRA (rank 64, α=32) via TRL+Accelerate; AdamW, cosine LR schedule with t-decayed init. Tasks: online bin packing (priority fn), TSP (penalty heuristic inside Guided Local Search), flatpack (placement scorer), plus Hash Code and LLM-SR benchmarks. Results averaged over 10 seeds. ReSTEM (iterative SFT on high-scorers) tried as alternative RL-Update but underperformed DPO and was harder to tune.

## Limitations
Small models only (1B–3.8B params) and modest sampling budgets (≤22.4k outputs) — scaling behavior unknown. RL phase adds compute cost; the training-vs-inference trade-off at scale is unexamined. Top-1/top-50 gains required careful tuning (average-reward gains were robust); gains on the Hash Code Self-Driving task did not beat top humans.

## Citations of interest
- Romera-Paredes et al. 2024 (*Nature*) — FunSearch; the static-generator baseline EvoTune extends.
- Rafailov et al. 2024 — Direct Preference Optimization (DPO); the RL-Update objective used.
- Wang et al. 2023 — generalizing DPO to diverse divergence constraints (forward-KL variant).
- Sutton 2019 — "The Bitter Lesson"; motivates search+learning synergy.
- Singh et al. 2023 / Gulcehre et al. 2023 — ReSTEM / ReST self-training, the alternative RL method and reinit strategy.
- Shojaee et al. 2024 — LLM-SR symbolic-regression benchmark suite.
- Veličković et al. 2024 — Hash Code competitive-programming heuristic-evolution setup.
