<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "ASI-Evolve: AI Accelerates AI"
authors: [Weixian Xu, Tiantian Mi, Yixiu Liu, Yang Nan, Zhimeng Zhou, Lin Zhang, Lyumanshan Ye, Yu Qiao, Pengfei Liu]
year: 2026
doi: 10.48550/arXiv.2603.29640
source_url: https://doi.org/10.48550/arXiv.2603.29640
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# ASI-Evolve: AI Accelerates AI

## TL;DR
ASI-Evolve is an agentic evolutionary framework that closes a learn–design–experiment–analyze loop to autonomously discover improvements across three pillars of AI development (architectures, data, learning algorithms), augmenting standard evolutionary agents with a literature-grounded *cognition base* and a *dedicated analyzer* that distills noisy experimental outcomes into reusable insights.

## Key findings
- **Framework novelty:** Unlike prior evolutionary search (AlphaEvolve, OpenEvolve, FunSearch, GEPA) that *evolves candidate solutions*, ASI-Evolve *evolves cognition itself* — accumulated experience + distilled insights are stored/retrieved to guide where to search next. Two distinguishing modules: a **Cognition Base** (human priors from literature, injected via embedding retrieval each round) and an **Analyzer** (turns verbose logs/metrics into compact decision-oriented reports written back to the database).
- **Pipeline:** 5 components — Researcher (LLM generates program + motivation), Engineer (runs experiment, returns scalar fitness + structured metrics, supports early-rejection timeouts and optional LLM-judge), Analyzer, Cognition store, and Database (UCB1 / random / greedy / MAP-Elites island sampling).
- **Architecture design (linear attention, DeltaNet baseline):** 1,350 candidates over 1,773 rounds → **105 architectures surpassing DeltaNet**. Best model **+0.97 points overall** (~3× the +0.34 gain of human-designed Mamba2). Top architectures reached 57.28% dev avg (vs DeltaNet 55.76%) and 45.40% generalization (vs 44.74%). Multi-stage scaling: ~20M → ~340M → ~1.3B params (100B tokens, 16 benchmarks incl. 6 OOD). Common winning theme: **adaptive, multi-scale routing** over fixed allocation.
- **Provenance analysis:** across 1,773 architectures, 51.7% from cognition base, 38.2% from accumulated experience, 10.1% novel; among the 105 SOTA, experience share rises to 44.8% and novelty drops to 6.6% — priors accelerate cold-start, experience compounds later.
- **Data curation (Nemotron-CC):** evolved cleaning strategies yield Nemotron-CC_ASI+ (504B tokens); 3B models on 500B tokens score **44.13 avg (+3.96 over raw)**, beating DCLM/FineWeb-Edu/Ultra-FineWeb. Large knowledge-intensive gains: **MMLU +18.64, CSQA +18.80, MedQA +13.48**.
- **RL algorithm design (GRPO baseline):** 300 rounds → 10 candidates beating GRPO; 3 significant after 14B-param verification. Gains: **+12.5 AMC32 (67.5→80.0), +11.67 AIME24 (20→31.67), +5.04 OlympiadBench (45.92→50.96)**. Discovered mechanisms include Pairwise Asymmetric Optimization (tanh-normalized pairwise advantages, asymmetric clipping, gradient dropout) and Budget-Constrained Dynamic Radius (percentile normalization with a global update-budget bound).
- **Circle packing (26 circles):** reaches SOTA 2.63597 in **17 rounds** (vs OpenEvolve 460, SkyDiscover 89), fastest among compared frameworks.

## Methods (brief)
Agentic evolutionary loop with LLM backbones (GPT-5-mini, Qwen3-32B). Each round samples database nodes, retrieves cognition items by embedding similarity, generates a program (full-file or diff mode), evaluates via task-specific scripts with timeouts/early-rejection, and distills outcomes via the Analyzer. Ablations (3 runs each) on circle packing isolate Analyzer and Cognition contributions; sampling-algorithm comparison (MAP-Elites vs UCB1 vs Random) shows UCB1 converges fastest *when* strong cognition priors are present (17 vs 79 steps for MAP-Elites).

## Limitations
Most validation rests on a single low-cost proxy (circle packing) with N=3 runs; the headline architecture/data/RL results lack repeated-seed statistics. The framework operates at mechanism-design level, so it cannot produce hardware-optimized CUDA kernels — LLM-judge efficiency penalties don't guarantee wall-clock competitiveness with hand-tuned implementations. The OpenEvolve/GEPA comparison uses a same-backbone simplification the authors acknowledge may bias against the baselines' best configurations.

## Citations of interest
- Novikov et al. 2025, *AlphaEvolve* — coding agent for algorithmic discovery; primary baseline and circle-packing benchmark source.
- Yang et al. 2025, *DeltaNet* — linear-attention baseline the architecture search improves on.
- Guo et al. 2025, *DeepSeek-R1 / GRPO* — RL algorithm baseline that evolved variants outperform.
- Bai et al. 2022, *DrugBAN* — bilinear attention DTI seed architecture for the biomedical transfer experiment.
- Lu et al. 2024, *The AI Scientist* — prior automated research pipeline, positioned as structured-task rather than open frontier discovery.
- Romera-Paredes et al. 2023, *FunSearch* — program-search precedent for discovering algorithms beating human designs.
