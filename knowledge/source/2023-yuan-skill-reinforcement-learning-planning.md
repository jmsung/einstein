---
type: source
kind: paper
title: Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks
authors: Haoqi Yuan, Chi Zhang, Hongchen Wang, Feiyang Xie, Penglin Cai, Hao Dong, Zongqing Lu
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2303.16563
source_local: ../raw/2023-yuan-skill-reinforcement-learning-planning.pdf
topic: general-knowledge
cites:
---

# Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks

**Authors:** Haoqi Yuan, Chi Zhang, Hongchen Wang, Feiyang Xie, Penglin Cai, Hao Dong, Zongqing Lu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.16563

## One-line
Plan4MC builds a demonstration-free Minecraft agent by training fine-grained RL "basic skills" (Finding / Manipulation / Crafting) and composing them via depth-first search over an LLM-generated skill dependency graph.

## Key claim
A hierarchical agent that decomposes long-horizon tasks into RL-acquired atomic skills + LLM-extracted skill-graph planning solves 40 diverse Minecraft tasks (some requiring >10 sequential skills, up to 121 planning steps) and unlocks the iron pickaxe in only 7M environment steps — substantially more sample-efficient than prior demonstration-free RL (which needed >10M steps just for cobblestone).

## Method
Skills are split into three types: a target-free hierarchical Finding-skill (PPO high-level over grid-state-count rewards + DQN low-level goal-reach policy), Manipulation-skills (PPO + self-imitation with MineCLIP intrinsic reward, plus distance/attack/depth task-specific rewards), and Crafting-skills (single action). A ChatGPT prompt produces structured `{consume, require, equip, obtain}` records that form a directed acyclic skill graph; at runtime a DFS walks parents of the goal node, tracking inventory, and interleaves planning with execution after each skill call. No human demonstrations are used.

## Result
Plan4MC reaches average success rates of 0.42 (Cut-Trees), 0.29 (Mine-Stones), 0.27 (Mine-Ores), 0.32 (Interact-Mobs) across 40 tasks, vs ~0–0.17 for MineAgent (flat PPO+CLIP) and 0.03–0.26 for interactive-LLM planners. Ablations show the Finding-skill is the dominant contributor (removing it halves success on most sets), the LLM-graph DFS beats interactive-LLM planning by avoiding uncontrollable LLM mistakes (LLM is used only offline for graph construction, with 6/55 manual corrections), and a Go-Explore variant that replaces nearby-spawn training with Finding-skill bootstrapping generalizes comparably or better (0.54 / 0.35 / 0.20 / 0.38).

## Why it matters here
General background; no direct arena tie. The paper is about hierarchical RL + LLM planning for Minecraft, not math optimization — it shares no concepts with sphere packing, autocorrelation, kissing numbers, sieves, or extremal combinatorics. The only loose analogy is the *self-improvement-loop / council-dispatch / skill-library* architecture in this repo: Plan4MC's skill-graph + DFS planner is a structural cousin to the einstein agent's wiki-graph + gap-detector pipeline, but the techniques don't transfer to numerical optimization.

## Open questions / connections
- Can the "fine-grained basic skills + dependency graph" pattern be ported to a numerical-optimizer agent (techniques as nodes, preconditions as edges)? Speculative — needs a different cost model than item inventories.
- Plan4MC still needs human correction on ~11% of LLM-generated graph nodes — what does an automated verifier for graph correctness look like?
- Relates to Go-Explore (Ecoffet et al.) for exploration bootstrapping and to LLM-as-planner work (SayCan, Voyager, DEPS); does not relate to any cited paper in `knowledge/wiki/`.

## Key terms
hierarchical reinforcement learning, Minecraft, MineDojo, MineCLIP, skill graph, LLM planning, Plan4MC, Finding-skill, Go-Explore, PPO, self-imitation learning, depth-first search planning, intrinsic reward, open-world agents
