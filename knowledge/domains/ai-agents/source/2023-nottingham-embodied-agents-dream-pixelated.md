<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling"
authors: [Kolby Nottingham, Prithviraj Ammanabrolu, Alane Suhr, Yejin Choi, Hannaneh Hajishirzi, Sameer Singh, Roy Fox]
year: 2023
source_url: https://arxiv.org/abs/2301.12050
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling

**Authors:** Kolby Nottingham, Prithviraj Ammanabrolu, Alane Suhr, Yejin Choi, Hannaneh Hajishirzi, Sameer Singh, Roy Fox  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2301.12050

## One-line
An RL agent (DECKARD) uses an LLM to hypothesize a DAG of subgoal dependencies, then grounds that hypothesis via environment interaction to accelerate exploration in Minecraft item-crafting.

## Key claim
LLM-hypothesized-then-verified Abstract World Models (AWMs) give ~12× sample-efficiency improvement over a no-LLM ablation on goal-driven crafting (e.g., stone pickaxe in 2.6M steps vs 32M), and remain robust under substantial errors in the LLM-predicted graph.

## Method
Two-phase loop: (Dream) few-shot prompt Codex to emit a Python dict of Minecraft recipes/tool/workbench requirements, parsed into a DAG $G=(X,E)$ over inventory-item subgoals; sample a branch on the verified frontier $F$ toward the target. (Wake) execute per-subgoal modular policies — VPT transformer finetuned with lightweight Houlsby adapters (~9.5M params/subgoal) via PPO with a KL-to-base regularizer and MineClip reward shaping — and add edges/nodes to $V$ as the agent verifies or corrects the hypothesized $E$.

## Result
On open-ended exploration, LLM guidance >2× speeds up discovery of stone-tier items; on "craft stone pickaxe," DECKARD matches or beats DreamerV3 (6M), VPT+RL (2.4B), and Align-RUDDER (2M) at 2.6M steps without expert demos or dense rewards. Codex AWM accuracy: 57% collectable/craftable label, 84% workbench, 66% ingredients, 55% exact recipe (all 391 items); 100/96/81/69% on the 37-item tool subtree. DECKARD outperforms its no-LLM ablation even under large synthetic edge insertion/deletion noise.

## Key terms
LLM-guided exploration, Abstract World Model, modular reinforcement learning, subgoal DAG, hypothesize-and-verify, Minecraft, DECKARD, Codex few-shot prompting, VPT transformer adapters, PPO, MineClip reward shaping, frontier sampling
