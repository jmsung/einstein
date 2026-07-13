<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SkillClaw: Let Skills Evolve Collectively with Agentic Evolver"
authors: [Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu]
year: 2026
doi: 10.48550/arXiv.2604.08377
source_url: https://doi.org/10.48550/arXiv.2604.08377
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

## TL;DR
SkillClaw is a framework that lets LLM-agent "skills" (reusable procedural instructions) evolve automatically by aggregating interaction trajectories across many users, having an agentic evolver refine/create skills from that pooled evidence, validating updates overnight in real environments, and synchronizing only accepted improvements back to all agents — yielding cumulative, cross-user capability gains without any user effort.

## Key findings
- **Problem framing.** In current Claw-style agent deployments (OpenClaw and variants CoPaw, IronClaw, PicoClaw, ZeroClaw, NanoClaw, NemoClaw), skills are manually installed and remain static; solutions found in one session don't persist, so users repeatedly rediscover the same failure/recovery patterns. SkillClaw treats cross-user, over-time interactions as the primary evolution signal.
- **Closed-loop pipeline:** Multi-user Interaction → Session Collection → Skill Evolution → Validation → Deployment. Each session records the full causal chain (`prompt → action → feedback → … → agent response`) because most skill-level failures are *procedural* (wrong argument format, missing validation step, misordered tool call) and invisible in the final response.
- **Evidence aggregation.** Sessions are grouped by referenced skill `G(s)`, with skill-less sessions in `G(∅)`. Pooling multiple users invoking the *same* skill is treated as a natural ablation — the skill is the controlled factor — revealing where it works vs. breaks. The formal goal is `S' = Φ(S, T)`.
- **Agentic evolver** (an LLM agent with a structured harness, not a fixed pipeline) picks one of three actions per skill: **Refine** (correct/robustify based on failure patterns), **Create** (new skill for recurring sub-procedures, including from `G(∅)`), or **Skip** (insufficient evidence). It reasons over successful *and* failed sessions jointly — successes define invariants that must not be altered, failures define correction targets — making evolution cumulative rather than regressive.
- **Validation gate** runs at night in idle user environments under real toolchains. Candidate skill `s'` and current `s` are executed on day-collected tasks; the model compares task success and execution stability → Accept (merge + sync) or Reject (retained as candidate only). This induces **monotonic deployment** — the pool cannot degrade.
- **Main results** (WildClawBench, Qwen3-Max backbone, 8 concurrent users, 6 day–night rounds), absolute / relative gains vs. Day 1:
  - Social Interaction: 54.01% → 60.34% (+6.33 / +11.72%), single high-impact update on Day 2.
  - Search & Retrieval: 22.73% → 34.55% (+11.82 / +52.00%), staged (input reliability first, then constraint-aware planning).
  - Creative Synthesis: 11.57% → 21.80% (+10.23 / +88.41%), early jump from fixing execution-environment setup.
  - Safety & Alignment: 24.00% → 32.00% (+8.00 / +33.33%), reliability-driven (git auth fallback, clone protocols).
- **Controlled "Skill Evolve Lite"** on three custom queries: average +42.1% after one evolution round — save report 28.3% → 100.0%, basic extraction 21.7% → 69.6% (+47.8%), deadline parsing 41.1% → 48.0% (+6.9%). Procedural-knowledge gaps respond strongly; nuanced-reasoning tasks respond weakly.
- **Heterogeneous evolution paths** per category: workflow explicitness (Social), input-validation-then-strategy (Search), multimodal pipeline organization (Creative), recoverable execution (Safety). Case studies show concrete fixes: correcting a Slack mock API port (9100→9110), adding selective full-message retrieval, encoding correct output paths, stricter "first affiliation" definitions, treating missing dirs as non-blocking, and patching CUDA-hardcoded code for CPU.

## Methods (brief)
Simulated 6-round day/night deployment over WildClawBench (60 real-world tasks across 6 domains, 15–50 steps, full Linux containers, multimodal, hard-constraint scoring). All roles — agents, evolver, validator — powered by Qwen3-Max. Evolution prompts ("Summarize Session," "Evolve from Sessions," "Agentic Evolve") enforce conservative editing: preserve correct API contracts, distinguish skill vs. agent vs. environment failures, and maintain a version-based history ledger (`v<N>.md` + evidence).

## Limitations
Explicitly a small-scale test: only 8 users, 6 days, limited query volume / feedback depth / interaction diversity, and results reported for only 4 of 6 WildClawBench categories. Single backbone model (Qwen3-Max); no comparison against memory-based or alternative skill-evolution baselines. Validation adds substantial token cost (candidate skills re-executed in real environments). Gains on reasoning-heavy tasks (deadline parsing +6.9%) are marginal.

## Citations of interest
- Yao et al. 2022, *ReAct* — reasoning+acting paradigm underpinning the agents.
- Shinn et al. 2023, *Reflexion* — verbal self-correction; the memory-based prior SkillClaw contrasts with.
- Wang et al. 2023, *Voyager* — accumulating skill library for lifelong learning, the skill-centric lineage.
- Ding et al. 2026, *WildClawBench* — the 60-task real-world benchmark used for evaluation.
- Zhao et al. 2024, *ExpeL* — turning experience into reusable lessons (experiential learning baseline).
- Anthropic 2026, *What are Skills?* — the skill-as-explicit-unit framing SkillClaw evolves.
