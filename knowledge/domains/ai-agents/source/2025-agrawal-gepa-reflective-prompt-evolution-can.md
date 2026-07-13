<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
authors: [Lakshya A. Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J. Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab]
year: 2025
doi: 10.48550/arXiv.2507.19457
source_url: https://doi.org/10.48550/arXiv.2507.19457
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

## TL;DR
GEPA is a prompt optimizer for compound AI systems that mutates prompts using natural-language reflection on execution traces and maintains a Pareto frontier of candidates; across six tasks it beats the RL method GRPO by ~6% on average (up to 20%) while using up to 35× fewer rollouts, and beats the leading prompt optimizer MIPROv2 by >10%.

## Key findings
- **Core thesis**: Serialized rollouts (reasoning chains, tool calls, compiler/eval errors) are rich natural-language learning signals. Reflecting on them in language extracts more per-rollout learning than the sparse scalar rewards used by policy-gradient RL (GRPO).
- **Sample efficiency vs RL**: On Qwen3-8B, GEPA beats GRPO (24,000 rollouts) on 5/6 tasks by margins of 19.0%, 2.73%, 13.66%, 5.19%, 0.7%, using up to **35× fewer rollouts**. GEPA matches GRPO's best validation after only 243–1179 rollouts (up to 78× more sample-efficient). Restricted to *train-set* rollouts, GEPA needs only 79–737 rollouts to reach optimum (the bulk of its budget is spent on validation for candidate selection, not learning signal).
- **vs MIPROv2 (prior SOTA)**: GEPA wins on all benchmarks/models — aggregate gains of +13.33% (GEPA+Merge) and +12.19% (GEPA) over baseline vs MIPROv2's +5.64% (GPT-4.1 Mini). Margins up to 11.1% (GPT-4.1 Mini) and 10.3% (Qwen3-8B). Example: +12% accuracy on AIME-2025.
- **Instruction-only > joint instruction+few-shot**: Reflectively evolved *instructions* beat MIPROv2's joint instruction+demonstration optimization, reversing prior findings that exemplars dominate. Attributed to improved instruction-following/self-reflection in modern LLMs.
- **Pareto selection is load-bearing**: Replacing greedy SelectBestCandidate (TextGrad-style) or BeamSearch (APO-style) with Pareto-based sampling gives +12.44% vs +6.05% and +5.11% respectively (Table 3). Greedy selection stalls in local optima after one improvement; Pareto "illumination" (Mouret & Clune 2015) samples among candidates that win on ≥1 task instance, weighted by lead count.
- **Cross-model transfer**: Prompts optimized on weaker Qwen3-8B transfer to GPT-4.1 Mini for +9.00% aggregate (up to +27.67% on HotpotQA), beating baselines optimized directly on GPT-4.1 Mini.
- **Cheaper prompts**: GEPA prompts are up to 9.2× shorter than MIPROv2's (mostly instructions, not few-shot demos), reducing inference cost; higher-performing optimizers trend toward shorter prompts.
- **Merge (system-aware crossover)**: GEPA+Merge combines complementary lineages that optimized disjoint modules; helps GPT-4.1 Mini (+2% aggregate) but degraded Qwen3-8B (hyperparameter-sensitive).
- **Extended uses**: As inference-time search, GEPA lifts GPT-4o NPU-kernel vector utilization from 4.25% → 30.52% mean (no RAG), and pushes CUDA KernelBench fast₁ from ~0% to >20%. As adversarial search, a learned distractor prompt dropped GPT-5 Mini AIME-2025 pass@1 from 76% → 10%.

## Methods (brief)
GEPA (Genetic-Pareto) runs a genetic loop: select a Pareto-frontier candidate, sample a minibatch, trace execution, call a feedback function µf returning score + natural-language feedback (e.g. compiler errors, failed rubrics), reflectively rewrite one module's prompt via a reflection LM, accept if minibatch score improves, then evaluate on the full Pareto-selection validation set. Evaluated on HotpotQA, IFBench, HoVer, PUPA, AIME-2025, LiveBench-Math using Qwen3-8B and GPT-4.1 Mini, against GRPO (LoRA + full finetune), MIPROv2, Trace/OptoPrime, and TextGrad under matched rollout budgets (within ~10%).

## Limitations
Six benchmarks, two models; AIME is the one task where GEPA does not clearly beat GRPO (GRPO 38.0 vs GEPA 32.0 on Qwen3-8B). Merge's budget-allocation/timing hyperparameters were not tuned per-model (hurt Qwen3-8B). Inference-time-search and adversarial results are explicitly "preliminary." Most of GEPA's rollout budget is validation overhead, so reported efficiency depends on validation-set sizing.

## Citations of interest
- Shao et al. 2024 (DeepSeekMath/GRPO) — the RL baseline GEPA is compared against.
- Opsahl-Ong et al. 2024 (MIPROv2) — prior SOTA prompt optimizer, joint instruction+demo via Bayesian optimization.
- Khattab et al. 2024 (DSPy) — compound-AI-system framework and formalization GEPA builds on.
- Yuksekgonul et al. 2025 (TextGrad) — textual-gradient backprop optimizer; basis for the SelectBestCandidate ablation.
- Mouret & Clune 2015 (MAP-Elites / illumination) — inspiration for Pareto-based candidate diversity.
- Yao et al. 2023 (ReAct) — canonical compound/agentic scaffolding the problem formulation subsumes.
- Pyatkin et al. 2025 (IFBench) and Li et al. 2025 (PUPA/PAPILLON) — key benchmarks with per-module feedback functions.
