---
type: source
kind: paper
title: SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
authors: Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.08377
source_local: ../raw/2026-ma-skillclaw-let-skills-evolve.pdf
topic: general-knowledge
cites: 
---

# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

**Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.08377

## One-line
A framework that lets LLM-agent skills (reusable procedural artifacts) evolve automatically by aggregating multi-user interaction trajectories, diagnosing recurring success/failure patterns with an "agentic evolver," and synchronizing refined skills back to all agents.

## Key claim
Treating cross-user trajectories as the primary signal for skill evolution — with a fixed harness + open-ended LLM reasoning over grouped session evidence — yields monotonic, validator-gated improvements on WildClawBench (Qwen3-Max backbone, 8 users, 6 day–night rounds), e.g. Social Interaction 54.01% → 60.34% (+11.7%), Search & Retrieval 22.73% → 34.55% (+52.0%), Creative Synthesis 11.57% → 21.80% (+88.4%), Safety & Alignment 24.00% → 32.00% (+33.3%).

## Method
Closed loop $\text{Interaction} \to \text{Evidence} \to \text{Evolution} \to \text{Validation} \to \text{Deployment}$. Sessions are stored as structured causal chains (prompt → action → feedback → … → response), grouped per skill $G(s) = \{\tau_i \mid s \in K_i\}$ plus a no-skill group $G(\emptyset)$. An agentic LLM evolver picks one of {refine, create, optimize_description, skip} per group, reasoning jointly over successes (invariants to preserve) and failures (targets to fix). Candidate skills are A/B-validated overnight in real environments; only accepted ones merge into the shared repo, ensuring monotonic deployment.

## Result
On WildClawBench (60 tasks, 6 capability domains, 15–50 step horizons, hard-constraint scoring), 6 rounds of day-night evolution improved all four reported categories under the validator gate, with most of the gain landing in the first 1–2 rounds (resolving a "primary bottleneck"), then stabilizing. The paper also specifies the underlying prompts: a session summarizer (8–15 sentence trajectory-aware summary), a per-skill evolver with conservative-editing constraints (preserve API contracts/endpoints; do not bloat skills with agent-runtime advice), and a history-aware variant requiring `v<N>.md` + `v<N>_evidence.md` audit trail before any edit.

## Why it matters here
Directly relevant to the einstein agent's self-improvement loop and `.claude/rules/` / `docs/wiki/` architecture: SkillClaw's "preserve invariants from successes, target failures, never silently drop correct environment info" maps onto the project's [failure-is-a-finding](.claude/rules/failure-is-a-finding.md), [wiki-attribution](.claude/rules/wiki-attribution.md), and [cycle-discipline](.claude/rules/cycle-discipline.md) rules. The mandatory history+evidence ledger and "skip > speculative edit" default are concrete patterns to import for any autonomous rule/skill evolver in this repo; the anti-pattern warning ("don't replace correct API info with 'go read source code'") is a direct guardrail for agentic wiki edits.

## Open questions / connections
- Single-user analogue: einstein has one developer but many problems/cycles — does grouping by *problem* (not user) and using cross-problem trajectories give the same "natural ablation" signal SkillClaw gets from cross-user variance?
- Validation gate transfer: SkillClaw's overnight A/B in real envs is the monotonicity guarantee; the einstein analogue would be re-running prior cycles' qmd queries / optimizer scripts against the proposed rule edit before merging.
- Extends Voyager (Wang 2023), Reflexion (Shinn 2023), SkillWeaver (Zheng 2025), ReasoningBank (Ouyang 2025), Evolver (Wu 2025); leaves open whether agentic evolution beats a frozen-rule baseline once skill counts grow large (no ablation reported on evolver vs hand-curated updates).

## Key terms
agentic evolver, skill library, multi-user trajectory aggregation, cross-user knowledge transfer, session causal chain, refine/create/skip action, conservative editing, history ledger, validator-gated deployment, monotonic skill pool, WildClawBench, Qwen3-Max, LLM agent self-improvement, OpenClaw
