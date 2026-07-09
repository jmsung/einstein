---
type: source
kind: paper
title: Self-Refine: Iterative Refinement with Self-Feedback
authors: Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, S. Welleck, Bodhisattwa Prasad Majumder, Shashank Gupta, A. Yazdanbakhsh, Peter Clark
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2303.17651
source_local: ../raw/2023-madaan-self-refine-iterative-refinement-self-feedback.pdf
topic: general-knowledge
cites:
---

# Self-Refine: Iterative Refinement with Self-Feedback

**Authors:** Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, S. Welleck, Bodhisattwa Prasad Majumder, Shashank Gupta, A. Yazdanbakhsh, Peter Clark  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.17651

## One-line
An LLM iteratively improves its own output by generating, critiquing, and refining — all with the same model, no extra training.

## Key claim
A single frozen LLM (GPT-3.5 / ChatGPT / GPT-4) prompted in a FEEDBACK→REFINE loop beats one-shot generation by ~20% absolute on average across 7 diverse tasks, with gains up to +49.2% (Dialogue, GPT-4) and +8.7% on Code Optimization (GPT-4: 27.3→36.0%).

## Method
Three few-shot prompts ($p_{gen}, p_{fb}, p_{refine}$) drive one LLM $M$: generate $y_0 = M(p_{gen}\|x)$, then iterate $fb_t = M(p_{fb}\|x\|y_t)$ and $y_{t+1} = M(p_{refine}\|x\|y_0\|fb_0\|...\|y_t\|fb_t)$, retaining the full feedback history. Stops at a max iteration $t$ (≤4 here) or a self-emitted stop indicator (e.g., a scalar score in $fb_t$). Feedback must be **actionable + specific** — generic feedback ablates the gain, no feedback ablates more.

## Result
Across 7 tasks (Dialogue, Code Optimization, Code Readability, Math Reasoning, Sentiment Reversal, Acronym Gen, Constrained Gen with 20–30 concepts): +5 to +49 points absolute over one-pass. Diminishing returns past iteration ~3. Math gains are marginal (+0.2%) because the model often fails to detect its own reasoning errors (94% of ChatGPT math feedback says "everything looks good"). Ablations show 1-vs-$k$ sampling does NOT match SELF-REFINE — refinement beats just drawing $k=4$ samples. Fails on weaker base models (Vicuna-13B can't follow the refine format).

## Why it matters here
Directly informs the autonomous-loop agent design: the **feedback→refine** core is the same pattern as the project's self-improvement loop and council-dispatch protocol, and the empirical lesson — *feedback quality is the binding constraint* — argues for making council questions explicit and actionable rather than vague. The Math Reasoning failure (LLM can't self-detect subtle errors) is direct evidence for why **triple-verify is mandatory**: self-feedback alone does not reliably catch numerical/logic errors.

## Open questions / connections
- Self-feedback fails when the model can't detect its own error class (math, near-SOTA float-precision optima); pairs with external verifiers — how to design the equivalent of the arena verifier as the "fourth check" inside an autonomous loop?
- Diminishing returns by ~3 iterations: what's the analog cap for autonomous math-solving cycles before re-dispatching council vs. continuing to refine?
- Feedback quality dominates over refiner quality (61% of failures = bad feedback, 6% = bad refinement) — directly supports the project's *ask-the-question-first* rule.
- Extends prior refinement work (Welleck 2022, Bai 2022 RLHF/constitutional, Scheurer 2022 summarization) by removing the external feedback source.

## Key terms
self-refine, iterative refinement, self-feedback, LLM, few-shot prompting, GPT-4, ChatGPT, Codex, actionable feedback, chain-of-thought, refiner, self-improvement loop, test-time compute, in-context learning
