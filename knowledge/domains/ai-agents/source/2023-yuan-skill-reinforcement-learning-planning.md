<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks
authors: [Haoqi Yuan, Chi Zhang, Hongchen Wang, Feiyang Xie, Penglin Cai, Hao Dong, Zongqing Lu]
year: 2023
source_url: https://arxiv.org/abs/2303.16563
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
hierarchical reinforcement learning, Minecraft, MineDojo, MineCLIP, skill graph, LLM planning, Plan4MC, Finding-skill, Go-Explore, PPO, self-imitation learning, depth-first search planning, intrinsic reward, open-world agents
