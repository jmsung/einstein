<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: In-the-Flow Agentic System Optimization for Effective Planning and Tool Use
authors: [Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi, James Zou, Pan Lu]
year: 2025
doi: 10.48550/arXiv.2510.05592
source_url: https://doi.org/10.48550/arXiv.2510.05592
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# In-the-Flow Agentic System Optimization for Effective Planning and Tool Use

## TL;DR
AGENTFLOW is a trainable agentic framework that coordinates four modules (planner, executor, verifier, generator) through an evolving memory and optimizes its planner *on-policy inside the live multi-turn loop* via a new algorithm, Flow-GRPO; a 7B backbone tuned this way beats specialized tool-RL baselines and even ~200B GPT-4o across ten reasoning benchmarks.

## Key findings
- **Core architecture**: Four specialized modules — Action Planner (the only trainable module), Tool Executor, Execution Verifier, Solution Generator — interact over multiple turns via a shared *deterministic, structured evolving memory* M and a five-tool toolset (Base Generator, Python Coder, Google Search, Wikipedia Search, Web Search). Each turn cycles plan → execute → verify; memory updates deterministically until the verifier emits STOP or a turn budget is hit.
- **Flow-GRPO** (Flow-based Group Refined Policy Optimization): tackles long-horizon, sparse-reward credit assignment by broadcasting a *single verifiable trajectory-level outcome reward* (binary, LLM-as-judge via GPT-4o) to every turn. This converts multi-turn RL into a sequence of tractable single-turn updates; the paper proves (§B) that maximizing the global multi-turn objective is equivalent to maximizing the expected token-level local objective under the on-policy state distribution. Group-normalized advantages, PPO-style clipping, and a KL penalty (β=0.001) stabilize training.
- **Headline gains** (7B Qwen2.5-Instruct backbone, all modules+tools): average accuracy improvements over top baselines of **+14.9% search, +14.0% agentic, +14.5% math, +4.1% scientific**. Surpasses ~200B GPT-4o across all domains (e.g., agentic GAIA 33.1% vs 17.3%, +15.8%; math 51.5% vs 35.1%, +16.4%).
- **In-the-flow RL is essential, not optional**: ablation (Table 3) shows offline SFT distilling GPT-4o planner traces causes *catastrophic collapse* (−19.0% vs frozen baseline), because token-level imitation misaligns with trajectory-level success. Flow-GRPO instead yields **+17.2%** average over the frozen baseline. A frozen GPT-4o planner gives only +5.8% — a capable but static planner can't co-adapt to live dynamics.
- **Learned tool behavior**: post-training the planner selects task-appropriate tools — on 2Wiki it raises Google Search use +42.0%; on specialized MedQA it shifts away from Google Search (66.2→10.9%) toward Wikipedia Search (0→59.8%) and Web Search (0→19.5%). Tool-calling error rate drops up to **−28.4%** on GAIA. Qualitative cases (Fig 7, §F) show self-correction, escape from error loops, and spontaneous novel tool combinations.
- **Efficiency & scaling**: rewards rise while response length shortens/stabilizes; ToRL (monolithic tool-RL) stagnates and degrades by comparison. Gains hold scaling backbone 3B→7B; increasing max turns T from 3→10 monotonically improves accuracy (avg turns consumed rises accordingly) without degenerate looping.

## Methods (brief)
On-policy RL fine-tuning of only the planner module with Flow-GRPO (lr 1e-6, temp 0.5, batch 32, 8 rollouts/sample, max 3 turns during training, 2048-token planner output) on 8×A100. Training data mixes Search-R1 and DeepMath QA pairs; GPT-4o is the LLM-as-judge reward and the eval correctness judge. Evaluated across ten benchmarks (Bamboogle, 2Wiki, HotpotQA, Musique, GAIA, AIME24, AMC23, GameOf24, GPQA, MedQA), three-trial averages.

## Limitations
Only the planner is trained (executor/verifier/generator frozen); reward is binary final-outcome via an LLM judge, which can mislabel. Training capped at 3 turns; test sets subsampled to 100 examples for several search benchmarks. The convergence analysis only establishes *near*-monotonic improvement in practice, not strict guarantees. Some "success" case studies reach the right multiple-choice answer despite a flawed intermediate computation (e.g., the relativistic GPQA example), so outcome-reward can reward right-answer-wrong-reasoning.

## Citations of interest
- Shao et al. 2024 (DeepSeekMath / GRPO) — the group-relative policy optimization base that Flow-GRPO extends to multi-turn.
- Jin et al. 2025 (Search-R1) — monolithic search tool-RL baseline and training-data source.
- Wu et al. 2024 (AutoGen) — training-free multi-agent baseline AGENTFLOW most directly contrasts against.
- Lu et al. 2025 (OctoTools) — extensible-tool agentic framework; tool-standardization methodology adopted for fair eval.
- Guo et al. 2025 (DeepSeek-R1) — outcome-based RL for reasoning that motivates the verifiable-reward paradigm.
- Mialon et al. 2023 (GAIA) — the agentic benchmark where gains over GPT-4o are largest.
