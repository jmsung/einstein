<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
authors: [Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao]
year: 2023
doi: 10.48550/arXiv.2303.11366
source_url: https://doi.org/10.48550/arXiv.2303.11366
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Reflexion: Language Agents with Verbal Reinforcement Learning

## TL;DR
Reflexion improves LLM agents not by updating weights but by having the agent verbally reflect on task-failure feedback and store those reflections in an episodic memory buffer that conditions subsequent trials — yielding large gains across decision-making, reasoning, and coding (e.g. 91% pass@1 on HumanEval vs GPT-4's 80%).

## Key findings
- **Core mechanism**: convert sparse binary/scalar environment feedback into *verbal* self-reflection (a textual "semantic gradient"), append it to a long-term memory buffer, and feed it back as context on the next attempt. No fine-tuning required.
- **Three-model modular architecture**: an **Actor** (Mₐ, generates text/actions — instantiated as Chain-of-Thought or ReAct), an **Evaluator** (Mₑ, scores trajectories — exact-match, heuristics, or LLM-as-judge), and a **Self-Reflection** model (M_sr, produces the verbal feedback). Short-term memory = current trajectory; long-term memory = accumulated reflections, bounded to Ω ≈ 1–3 experiences to fit context limits.
- **Decision-making (AlfWorld, 134 tasks)**: ReAct + Reflexion completes **130/134** tasks, an absolute **+22%** over ReAct alone, learning over 12 trials; baseline ReAct plateaus between trials 6–7 at a ~22% hallucination rate. A simple heuristic (same action/response >3 cycles, or >30 actions) triggers reflection to catch hallucination and inefficient planning.
- **Reasoning (HotPotQA, 100 questions)**: **+20%** over baselines. An ablation isolating self-reflection from plain episodic memory shows self-reflection adds an **8% absolute** boost over episodic-memory-only — refinement guided by reflection beats refinement alone. CoT(GT)+Reflexion corrects ~14% of questions the ground-truth-context baseline still got wrong.
- **Programming (HumanEval, MBPP, LeetcodeHardGym)**: sets SOTA on most benchmarks — HumanEval Python **91.0** pass@1 (vs 80.1 GPT-4), HumanEval Rust 68.0, MBPP Rust 75.4, Leetcode Hard Python 15.0 (vs 7.5 GPT-4). Uses self-generated unit tests (AST-filtered, ≤6 tests) for grounded self-evaluation, preserving pass@1 eligibility.
- **MBPP Python is the one regression** (77.1 vs 80.1): traced to a **16.3% false-positive rate** of internal test execution (tests pass but solution wrong) vs only 1.4% on HumanEval. False positives are the dominant failure mode because they cause premature submission; false negatives are recoverable.
- **Ablation (50 hardest HumanEval Rust)**: full Reflexion 0.68 vs base 0.60; omitting test generation *drops below baseline* to 0.52 (agent can't tell if code is correct, makes harmful edits); omitting the self-reflection NL step yields no gain over baseline — confirming both components are load-bearing and "blind trial-and-error debugging" without reflection fails on hard tasks.
- **Emergence**: self-correction is an emergent property of stronger models — weak StarChat-beta shows no Reflexion gain (0.26→0.26), while GPT-4 gains consistently across tasks.

## Methods (brief)
Empirical evaluation across three task families using GPT-3.5/GPT-4 actors, with task-appropriate evaluators (exact-match grading for QA, heuristics or LLM classification for AlfWorld, self-generated unit-test suites for code). Introduces LeetcodeHardGym (40 hard Leetcode problems across 19 languages, all post-dating GPT-4's pretraining cutoff) and uses MultiPL-E to translate benchmarks to Rust, demonstrating language-agnosticism.

## Limitations
As a natural-language policy optimizer it can get stuck in non-optimal local minima — it fails on WebShop (terminated after 4 trials, no improvement) where tasks demand creative exploration. Memory is a fixed sliding window (Ω=1–3); test-driven self-evaluation breaks for non-deterministic, impure, hardware-dependent, or concurrent functions. Gains depend entirely on the base LLM's self-evaluation capability.

## Citations of interest
- **ReAct (Yao et al. 2023, [30])** — the reasoning+acting actor that Reflexion builds on for decision-making and QA.
- **Chain-of-Thought (Wei et al. 2022, [26])** — the step-by-step reasoning actor and test-generation prompting strategy.
- **Self-Refine (Madaan et al. 2023, [15])** — closest prior work on iterative self-feedback; limited to single-generation reasoning.
- **CodeT (Chen et al. 2022, [5])** — self-generated unit tests to score code, prior SOTA Reflexion surpasses.
- **AlfWorld (Shridhar et al. 2021, [24])** and **HotPotQA (Yang et al. 2018, [28])** — the decision-making and multi-hop reasoning benchmarks.
- **HumanEval (Chen et al. 2021, [6])** — the code-generation benchmark where Reflexion reaches 91% pass@1.
