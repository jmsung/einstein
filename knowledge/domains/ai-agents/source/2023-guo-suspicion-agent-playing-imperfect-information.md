<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4"
authors: [Jiaxian Guo, Bo Yang, Paul Yoo, Bill Yuchen Lin, Yusuke Iwasawa, Yutaka Matsuo]
year: 2023
source_url: https://arxiv.org/abs/2309.17277
drive_file_id: 1CFt0H5EnSsZrG6G22rwRx0pCWLwoB2g5
text_source: paperclip
ingested_by: agent
---

# Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4

**Authors:** Jiaxian Guo, Bo Yang, Paul Yoo, Bill Yuchen Lin, Yusuke Iwasawa, Yutaka Matsuo  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.17277

## One-line
A prompt-engineered GPT-4 agent that plays imperfect-information card games (Leduc Hold'em, Coup, Limit Texas Hold'em) by explicitly simulating the opponent's beliefs via first- and second-order theory of mind.

## Key claim
With no specialized training, GPT-4 driven by a modular pipeline (observation interpreter → reflexion / pattern analysis → ToM-aware planner → evaluator) outperforms learning-based baselines DMC, DQN, and NFSP in Leduc Hold'em head-to-head chip counts, but still loses to the Nash-equilibrium algorithm CFR+ (−22 chips over 100 games with hindsight opponent observations).

## Method
Decomposes gameplay into LLM-prompted sub-modules: a structured rule/observation interpreter converts low-level state into readable text; a Reflexion module mines game history for behavior patterns; a planning module emits candidate actions; an evaluator estimates per-plan win/expected-chip rates. The ToM layer prompts GPT-4 to model the opponent's hand-conditional action distribution (first-order) and the opponent's model of the agent (second-order), enabling bluffing and counter-bluffing without iterative ToM recursion — a single prompt elicits both levels.

## Result
On Leduc Hold'em over 100 games: Suspicion-Agent (2nd-order ToM, GPT-4) scores +24/+45/+142 chips vs DMC/DQN/NFSP but −22 vs CFR+. Ablation: removing hindsight opponent-observation in history degrades from −22 to −42 vs CFR+. Open-source LLMs (Mistral-7B, Gemma-7B, Llama3-8B, Phi3-medium) underperform GPT-4 substantially, losing to all baselines except DMC/DQN. Qualitative samples in Coup and Limit Texas Hold'em show the agent bluffing (taxing as fake Duke) and strategically folding.

## Key terms
theory of mind, GPT-4 agent, imperfect information games, Leduc Hold'em, Texas Hold'em, Coup, CFR+, NFSP, DMC, Reflexion, prompt engineering, bluffing, opponent modeling, counterfactual regret minimization, Nash equilibrium
