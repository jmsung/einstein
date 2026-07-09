---
type: source
kind: paper
title: "Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4"
authors: Jiaxian Guo, Bo Yang, Paul Yoo, Bill Yuchen Lin, Yusuke Iwasawa, Yutaka Matsuo
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2309.17277
source_local: ../raw/2023-guo-suspicion-agent-playing-imperfect-information.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems (sphere packing, autocorrelation, kissing, sieve) are single-player optimization, not adversarial games — ToM-aware planning has no immediate use. The modular-prompt decomposition (interpreter + reflexion + planner + evaluator) is a weak analog to the council-dispatch / self-improvement loop, but the wiki already covers that better in the persona/council pages.

## Open questions / connections
- Whether the "second-order ToM via single prompt" finding generalizes to non-game reasoning (e.g., predicting which research direction another agent would pursue) — possibly relevant to multi-persona council dispatch.
- The Reflexion-style game-history → pattern analysis pipeline overlaps with `failure-is-a-finding` / cycle-log discipline, but for adversarial rather than self-improvement settings.
- Why CFR+ remains uncatchable: ToM cannot recover the Nash mixed strategy that game-theoretic regret minimization computes.

## Key terms
theory of mind, GPT-4 agent, imperfect information games, Leduc Hold'em, Texas Hold'em, Coup, CFR+, NFSP, DMC, Reflexion, prompt engineering, bluffing, opponent modeling, counterfactual regret minimization, Nash equilibrium
