---
type: source
kind: paper
title: Voyager: An Open-Ended Embodied Agent with Large Language Models
authors: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, A. Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi (Jim) Fan, Anima Anandkumar
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.16291
source_local: ../raw/2023-wang-voyager-open-ended-embodied-agent.pdf
topic: general-knowledge
cites:
---

# Voyager: An Open-Ended Embodied Agent with Large Language Models

**Authors:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, A. Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi (Jim) Fan, Anima Anandkumar  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.16291

## One-line
An LLM-driven Minecraft agent that self-generates a curriculum, writes/refines executable code skills, and accumulates them in a retrievable library to achieve open-ended lifelong learning without gradient updates.

## Key claim
GPT-4 acting through (i) an automatic curriculum, (ii) a growing skill library of code, and (iii) iterative prompting with environment feedback + execution errors + self-verification yields 3.3× more unique items, 2.3× longer map traversal, and up to 15.3× faster tech-tree unlocks vs ReAct / Reflexion / AutoGPT, and is the only baseline to reach diamond tools and to zero-shot transfer skills to a new world.

## Method
Three coupled modules around a blackbox GPT-4: an *automatic curriculum* prompted with agent state + completed/failed task history to propose the next "discover-diverse" task (in-context novelty search); a *skill library* storing each verified task-solving JavaScript (Mineflayer) function, keyed by an ada-002 embedding of a GPT-3.5-written description and retrieved top-5 by task-plan embedding; and an *iterative prompting loop* that runs the generated code, feeds back chat-log observations + interpreter errors + a separate GPT-4 self-verifier's critique, and refines up to 4 rounds before committing or requesting a new task.

## Result
On MineDojo with gpt-4-0314, VOYAGER collects 63 unique items in 160 iterations (vs ~19 for AutoGPT, far fewer for ReAct/Reflexion), unlocks wooden/stone/iron tools in 6/11/21 iterations averaged over 3 trials, and is the only method to reach diamond (1/3 trials, 102 iter). Ablations: removing self-verification drops items by 73%, random curriculum drops 93%, GPT-3.5 substitution gives 5.7× fewer items; skill-retrieval top-5 accuracy is 96.5%; results replicate on gpt-4-0613.

## Why it matters here
General background; no direct arena tie — but architecturally relevant to the einstein autonomous-loop agent: the curriculum→skill-library→self-verification triple maps onto the project's gap-detect → wiki-finding → triple-verify loop, and the embedding-indexed reusable-code library is a precedent for storing optimizer "techniques" as retrievable skills keyed by qmd-style descriptions.

## Open questions / connections
- How does code-as-skill (with embedding retrieval) compare to natural-language findings (the wiki's current unit) for cross-problem transfer?
- Self-verification by a second LLM critic vs the project's triple-verify (independent reimplementation + analytical cross-check) — when does LLM critique suffice and when does it hallucinate success (paper notes the spider-string failure)?
- Curriculum hallucinations ("copper sword") parallel the wiki's "agent proposes unreachable concept" risk — what gating prevents the skill library from compounding fake skills?

## Key terms
LLM agent, lifelong learning, automatic curriculum, skill library, code-as-action, in-context learning, self-verification, iterative prompting, GPT-4, Minecraft, MineDojo, embodied agent, novelty search, catastrophic forgetting
