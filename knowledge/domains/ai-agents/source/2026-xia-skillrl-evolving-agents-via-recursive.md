<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning"
authors: [Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, Huaxiu Yao]
year: 2026
doi: 10.48550/arXiv.2602.08234
source_url: https://doi.org/10.48550/arXiv.2602.08234
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

## TL;DR
SkillRL distills raw agent trajectories into a compact, hierarchical "SkillBank" of reusable strategies and co-evolves that library with the agent's policy during RL, beating memory-based and vanilla-RL baselines by 15.3%+ on ALFWorld, WebShop, and seven search-QA benchmarks while using ~10% less context.

## Key findings
- **Core thesis: abstraction beats memorization.** Prior memory-based agents store raw trajectories, which are token-heavy and noisy. SkillRL instead distills trajectories into named, reusable skills, achieving **10–20× token compression** vs raw trajectories while improving (not degrading) reasoning utility.
- **Three components:** (1) *experience-based skill distillation* — a teacher model (OpenAI o3) processes both successful trajectories (extract winning strategic patterns) and failed ones (synthesize concise failure lessons / counterfactuals); (2) *hierarchical SkillBank* — splits into **general skills** (universal strategies, e.g. systematic exploration, precondition checks) and **task-specific skills** retrieved by semantic similarity (TopK, K=6, threshold δ=0.4); (3) *recursive skill evolution* — after each validation epoch, failed trajectories in low-performing categories (Acc < δ) drive teacher-generated new/refined skills, so library and policy co-evolve.
- **Training pipeline:** base model Qwen2.5-7B-Instruct → cold-start SFT on teacher-generated skill-augmented traces (teaches the model *how* to retrieve/apply skills) → GRPO RL (lr 1e-6, group size 8, batch 16) with KL anchored to the SFT reference policy.
- **Headline results:** **89.9%** success on ALFWorld and **72.7%** on WebShop, state-of-the-art. **+12.3 points absolute over vanilla GRPO** on ALFWorld (77.6→89.9), attributable to skill augmentation alone since GRPO is the shared optimizer. Largest per-task gains on the hardest multi-step tasks: PickTwo +22.8, Cool +23.0, Heat +15.
- **Beats much larger closed models:** the 7B SkillRL exceeds GPT-4o by 41.9 points and Gemini-2.5-Pro by 29.6 points on ALFWorld — "skill learning can compensate for model scale."
- **Beats memory-augmented RL:** outperforms MemRL (21.4%, frozen policy), EvolveR (43.8%), and Mem0+GRPO (54.7%) by ~35 points on ALFWorld — validating that co-evolving skill abstraction > trajectory compression or prompt-based memory.
- **Search-QA:** average **47.1%** across 7 datasets, vs Search-R1 38.5% and EvolveR 43.1%; strong OOD generalization (trained only on NQ + HotpotQA), e.g. +19.4 over EvolveR on Bamboogle.
- **Ablations (Table 3):** removing hierarchy −13.1 (ALFWorld); replacing SkillBank with raw trajectories −25 (largest drop, supports the abstraction thesis); removing cold-start SFT −20; removing dynamic evolution −5.5.
- **Dynamics:** SkillBank grows from 55 skills (12 general + 43 task-specific) to 100 by step 150, growth dominated by task-specific skills. Evolution accelerates convergence (>80% within 60 steps vs ~90 for the no-evolution variant) and raises the ceiling. Prompt length stays <1,300 tokens vs ~1,450 for raw-memory (≈10.3% reduction).

## Methods (brief)
LLM-agent RL with GRPO (clipped PPO-style objective, intra-group normalized advantages, KL to reference). Teacher model o3 distills trajectories into structured JSON skills (name / principle / when-to-apply) and generates SFT data. Evaluated on ALFWorld (embodied text), WebShop (e-commerce), and single/multi-hop search-QA. 8×H100, ~30 h/experiment.

## Limitations
Single 7B base model (Qwen2.5) and a single strong teacher (o3); gains may not transfer to other backbones. Evaluated only on three benchmark families (no real-world deployment); relies on binary task-success rewards, leaving sparse/partial-credit settings untested. Skill quality is bounded by the teacher's distillation; no analysis of skill-library contradiction or staleness as it grows.

## Citations of interest
- Shao et al., 2024 (DeepSeekMath / GRPO) — the RL optimizer SkillRL builds on.
- Shinn et al., 2023 (Reflexion) — verbal self-reflection on failures; conceptual precursor to failure-lesson distillation.
- Yao et al., 2022b (ReAct) — interleaved reasoning/acting baseline.
- Zhao et al., 2024 (ExpeL) — experiential learning via external experience pools; key memory baseline.
- Anthropic, 2024 (Agent Skills) — design inspiration for compact, reusable skill abstraction.
- Wu et al., 2025 (EvolveR) — self-evolving experience-driven agent; closest memory-augmented-RL competitor.
- Shridhar et al. (ALFWorld) & Yao et al., 2022a (WebShop) — primary evaluation environments.
