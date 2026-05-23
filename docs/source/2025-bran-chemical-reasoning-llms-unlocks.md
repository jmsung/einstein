---
type: source
kind: paper
title: Chemical reasoning in LLMs unlocks strategy-aware synthesis planning and reaction mechanism elucidation
authors: Andrés M Bran, Théo A. Neukomm, Daniel P. Armstrong, Zlatko Jonvcev, P. Schwaller
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2503.08537
source_local: ../raw/2025-bran-chemical-reasoning-llms-unlocks.pdf
topic: general-knowledge
cites:
---

# Chemical reasoning in LLMs unlocks strategy-aware synthesis planning and reaction mechanism elucidation

**Authors:** Andrés M Bran, Théo A. Neukomm, Daniel P. Armstrong, Zlatko Jonvcev, P. Schwaller  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.08537

## One-line
LLMs are used as evaluators/judges (not generators) to guide tree-search algorithms over chemical-reasoning tasks — retrosynthetic route planning and reaction-mechanism elucidation — outperforming pure search baselines.

## Key claim
Positioning LLMs as scoring/ranking modules inside Monte Carlo Tree Search (rather than direct SMILES generators) yields state-of-the-art performance on natural-language strategy-aware retrosynthesis and on a 12-task mechanism-elucidation benchmark; Gemini-2.5-pro achieves correlation $\approx 0.56$ with expert-graded route alignment, ~50% over the next best model, while smaller models perform near random.

## Method
Hybrid system "Synthegy": a rule-based search algorithm (traditional retrosynthesis engines like AIZynth / Reaxys / Synthia, or an electron-pushing elementary-step enumerator for mechanisms) proposes candidate states; the LLM scores each candidate against a natural-language strategic prompt (e.g. "break pyrimidine early; get other rings from commercial materials"). Mechanism task: at each step the LLM ranks the ground-truth elementary electron-pushing move against 5 alternative distractor moves; metric = average score gap. Benchmark covers 4 targets × multiple strategy prompts + 12 reaction mechanisms.

## Result
Gemini-2.5-pro leads (corr 0.56), followed by o3 and open-weights DeepSeek-R1 (corr 0.36); Claude-3.5-Sonnet (corr 0.38) is cheaper/faster. Smaller models (gpt-4o-mini, distilled DeepSeek) are indistinguishable from random. A clear emergence threshold: capability essentially absent before mid-2024 (Claude-3.5-Sonnet release). Cost: full 60-route reranking batch ~$2–3, ~12 min wall-clock — practical for routine use.

## Why it matters here
General background; no direct arena tie. The methodological lesson — use LLMs as **evaluators/judges inside a search loop** rather than as solution generators, exploiting their strength in qualitative judgment while letting rule-based code handle precise structures — is directly transferable to the einstein-arena agent design (council dispatch, route/strategy scoring, self-improvement loop). Reinforces the emergence-threshold hypothesis: only frontier-scale models reliably do meaningful domain reasoning.

## Open questions / connections
- Can fine-tuned small open models close the gap with frontier LLMs on domain reasoning tasks (relevant to whether council-persona agents can be local)?
- The "LLM as scorer for MCTS branches" pattern — does it transfer to math-optimization search (e.g. ranking basin candidates, scoring approach plans)?
- Failure mode "grouping reactions instead of analyzing them individually" — analogue in long math derivations? Suggests prompting personas to evaluate one step at a time.

## Key terms
LLM-as-judge, Monte Carlo Tree Search, retrosynthesis, mechanism elucidation, electron-pushing, strategy-aware planning, Synthegy, emergence threshold, Gemini-2.5-pro, DeepSeek-R1, Claude-3.5-Sonnet, search-guided reasoning, model scaling, evaluator-not-generator
