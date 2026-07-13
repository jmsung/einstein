<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
authors: [Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar]
year: 2023
doi: 10.48550/arXiv.2305.16291
source_url: https://doi.org/10.48550/arXiv.2305.16291
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Voyager: An Open-Ended Embodied Agent with Large Language Models

## TL;DR
Voyager is the first LLM-powered (GPT-4) embodied lifelong-learning agent in Minecraft that autonomously explores, accumulates an ever-growing library of reusable code-skills, and self-verifies task completion — with no model fine-tuning and no human intervention — outperforming prior LLM-agent methods by large margins.

## Key findings
- **Three-component architecture** (no gradient updates; GPT-4 queried as a blackbox): (1) an **automatic curriculum** that proposes the next task to "discover as many diverse things as possible" (in-context novelty search), (2) a **skill library** of executable programs indexed by an embedding of each skill's description (vector DB; key = GPT-3.5 description embedding, value = code), and (3) an **iterative prompting mechanism** using **code as the action space**.
- **Iterative prompting** fuses three feedback types per round: environment feedback (e.g. "I cannot make an iron chestplate because I need 7 more iron ingots"), code-interpreter execution errors, and **self-verification** (a separate GPT-4 critic that checks success and emits a critique). It retries up to **4 rounds** before the curriculum reissues/defers the task; on success the program is committed to the library.
- **Exploration:** discovers **63 unique items** in 160 prompting iterations — **3.3×** more than baselines.
- **Tech-tree mastery (Table 1):** unlocks wooden tool **15.3×** faster, stone **8.5×**, iron **6.4×** faster than baselines; the **only** method to reach the **diamond** tier (1/3 trials). Baselines ReAct, Reflexion, AutoGPT fail to unlock any tier (0/3).
- **Map traversal: 2.3×** longer distances across more diverse terrain.
- **Zero-shot generalization** to a fresh world (Table 2): Voyager solves all four unseen tasks (Diamond Pickaxe, Golden Sword, Lava Bucket, Compass) in ~18–21 iterations; baselines solve none in 50. The skill library is **plug-and-play** — bolting it onto AutoGPT lifts AutoGPT from 0/3 to partial success.
- **Ablations (Fig. 9):** removing the automatic curriculum (→ random) drops discovered items **93%**; removing self-verification drops them **73%** (the single most important feedback type); GPT-4 vs GPT-3.5 for code generation yields **5.7×** more unique items. Skill library prevents the late-stage plateau / catastrophic forgetting.
- Skill retrieval is reliable: **top-5 accuracy 96.5%** (top-1 80.2%) over 309 samples (Table A.4). Robust to model version (gpt-4-0314 ≈ gpt-4-0613).

## Methods (brief)
Built on MineDojo with Mineflayer JavaScript control primitives (mineBlock, craftItem, smeltItem, killMob, etc.). Uses gpt-4-0314 (temp 0; 0.1 for the curriculum to encourage diversity), gpt-3.5-turbo for auxiliary NLP/self-ask context, and text-embedding-ada-002 for skill indexing. Chain-of-thought prompting precedes every code generation; a warm-up schedule progressively exposes more agent state. Three trials per method; max 160 prompting iterations (50 for generalization).

## Limitations
GPT-4 API cost is ~15× GPT-3.5, and the quality leap is required (GPT-3.5/open LLMs insufficient). The curriculum hallucinates impossible tasks ("copper sword"); code generation hallucinates invalid APIs/recipes (e.g. cobblestone as fuel); self-verification occasionally misjudges. No visual perception (text-only GPT-4 at the time); 3D building requires human-in-the-loop feedback. Evaluated only in Minecraft, n=3 trials, high variance (diamond reached 1/3).

## Citations of interest
- **ReAct** (Yao et al. 2022) — reasoning+acting traces; a Voyager baseline.
- **Reflexion** (Shinn et al. 2023) — verbal self-reflection memory; baseline, and the contrast point for self-verification.
- **AutoGPT** (2023) — ReAct-style autonomous goal decomposition; strongest baseline, boosted by Voyager's skill library.
- **MineDojo** (Fan et al. 2022) — the open-ended Minecraft benchmark/framework Voyager runs on.
- **Voyager VPT** (Baker et al. 2022) — video-pretrained low-level Minecraft controller; orthogonal gradient-based approach.
- **Code as Policies** (Liang et al. 2022) / **ProgPrompt** (Singh et al. 2022) — LLM-generated executable code as the action representation.
- **DreamCoder** (Ellis et al. 2020) — wake-sleep growth of a reusable, interpretable program library; conceptual ancestor of the skill library.
