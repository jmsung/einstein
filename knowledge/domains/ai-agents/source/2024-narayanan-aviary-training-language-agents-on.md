<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Aviary: training language agents on challenging scientific tasks"
authors: [Siddharth Narayanan, James D. Braza, Ryan-Rhys Griffiths, Manu Ponnapati, Albert Bou, Jon Laurent, Ori Kabeli, Geemi Wellawatte, Sam Cox, Samuel G. Rodriques, Andrew D. White]
year: 2024
doi: null
source_url: https://arxiv.org/abs/2412.21154
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Aviary: training language agents on challenging scientific tasks

## TL;DR
Aviary is an open-source gymnasium that formalizes language agents as policies solving language-grounded POMDPs ("language decision processes"); trained on it with expert iteration plus inference-time majority voting, an 8B open-source model (Llama-3.1-8B-Instruct) matches or beats frontier LLM agents and human experts on scientific tasks at up to **100× lower inference cost**.

## Key findings
- **Language decision process (LDP) formalism.** Agents are framed as policies πθ solving POMDPs whose action/observation spaces are natural-language strings. θ subsumes any optimizable component (LLM weights, temperature, internal reasoning, memory retrieval). Agents are implemented as **stochastic computation graphs** (deterministic + stochastic nodes); RAG, rejection sampling, and ReAct are each expressed as simple SCGs.
- **Five environments**, three scientific: (1) **molecular cloning** (SeqQA / CloningScenarios — DNA construct manipulation with ~20 tools: PCR, Gibson/Golden Gate assembly, codon optimization, restriction digest), (2) **PaperQA2 Local** (LitQA2 literature QA, refactored to local tantivy search), (3) **protein stability** (propose 3–7 stabilizing mutations, scored by Rosetta cart_ddg). Plus GSM8K and HotpotQA recast as environments.
- **Training recipe.** Behavior cloning (BC) to seed the trajectory buffer, then **expert iteration (EI)** — rejection-sampling fine-tuning on self-generated high-reward trajectories (Algorithm 1). SeqQA: untrained Llama-3.1-8B solves only **1%**; BC gives a large jump, EI adds **+14% absolute** over 8 epochs (2841 seed trajectories). LitQA2: untrained agent ~30%, EI reaches **72%** on test, using difficulty-weighted task sampling (weight ∝ 1−pass_rate).
- **Inference-time scaling.** Majority voting (consensus@k) adds **~20 percentage points** on both SeqQA and LitQA2. On SeqQA the Llama-3.1-8B EI agent exceeds the Claude 3.5 Sonnet agent at all sample counts, reaching **0.89** at ~945 rollouts (vs. 0.87 prior best from the joint US/UK AISI report). On LitQA2 the Sonnet agent plateaus at **~0.89–0.90**; the small EI agent matches human/prior-best at a single sample.
- **Cost.** SeqQA: $0.07/trajectory (Sonnet) vs **$0.00066** (Llama-3.1-8B EI); human PhD contractors cost **$4–$12 per question**. Same SeqQA accuracy reached at ~100× lower cost; LitQA2 majority voting with the small model beats single-rollout Sonnet at 3× less cost.
- Self-trained agents converge on **shorter, less diverse** trajectories than the demonstration set (Fig. 5) — online learning discovers distinct, more efficient solution paths.

## Methods (brief)
Base model Llama-3.1-8B-Instruct (gpt-4o for GSM8K/HotpotQA) trained on Nvidia A100s with asynchronous multi-worker trajectory collection + SFT (cross-entropy). Agents capped at 10 steps (18 for PaperQA). Evaluation on held-out splits constructed to be absent from pretraining corpora; error bars by bootstrap resampling. Two open-source libraries released: `aviary` (environments) and `ldp` (agent/training framework).

## Limitations
Benchmarks are multiple-choice with easy automated scoring; real discovery is not tested. Human comparisons are imperfect (humans lacked the same tools). Majority-voting trends measured on <200 unique questions, so plateaus may be artifacts of small sets. Train/test overfitting gap observed on SeqQA. Cost estimate for the trained model assumes vanilla-8B serving prices.

## Citations of interest
- Laurent et al. 2024 (LAB-Bench / SeqQA) — source of the molecular-cloning benchmark and human baselines.
- Skarlinski et al. 2024 — PaperQA2 superhuman literature synthesis; LitQA2 prior best (0.67).
- Yao et al. 2023 (ReAct) — reasoning+acting agent architecture expressed as an SCG.
- Schulman et al. 2015 — stochastic computation graphs, the backbone formalism.
- Anthony et al. 2017 / Anthony 2021 — expert iteration ("thinking fast and slow").
- Brown et al. 2024 (Large Language Monkeys) — inference-compute scaling via repeated sampling.
- Tsuboyama et al. 2023 — megascale protein folding-stability dataset used for the protein task.
