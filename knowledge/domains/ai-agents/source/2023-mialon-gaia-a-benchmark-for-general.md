<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "GAIA: A Benchmark for General AI Assistants"
authors: [Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, Thomas Scialom]
year: 2023
doi: 10.48550/arXiv.2311.12983
source_url: https://doi.org/10.48550/arXiv.2311.12983
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# GAIA: A Benchmark for General AI Assistants

## TL;DR
GAIA is a benchmark of 466 real-world questions that are conceptually simple for humans (92% success) but hard for the strongest tool-augmented LLMs (GPT-4 with plugins ~15%), designed to test reasoning, multi-modality, web browsing, and tool use rather than expert knowledge. It inverts the prevailing trend of building benchmarks harder for humans, arguing that human-level robustness on such everyday tasks is the true next milestone toward AGI.

## Key findings
- **Human–AI gap is the headline result.** Human annotators score **92%** aggregated (94% L1, 92% L2, 87% L3); GPT-4 + plugins (human-selected, "oracle") scores **30.3% on L1, 9.7% on L2, 0% on L3**; plain GPT-4 scores **9.1% / 2.6% / 0%**. This contrasts sharply with LLMs surpassing humans on MMLU (GPT-4 86.4%), the bar exam, and USMLE.
- **466 questions** total, designed and annotated by humans (Surge AI). A **166-question dev set is released with annotations**; **300 are held out** (answers retained) to power a leaderboard.
- **Three difficulty levels by step/tool count** (Fig 1, Table 4): L1 (146 q) = ≤1 tool, ≤5 steps; L2 (245 q) = ~5–10 steps, multiple tools; L3 (75 q) = arbitrarily long action sequences, any tools. Level correlates with model performance, validating the difficulty proxy.
- **Capabilities required** (Fig 3): web browsing (355 questions), coding (154), multi-modality (138), diverse filetype reading (129), N/A/none (32). Questions may have attached files (xlsx, png, pdf, mp3, etc. — Fig 6).
- **Tool augmentation clearly helps**: the gap between plain GPT-4 and GPT-4+plugins demonstrates tool/web access unlocks accuracy and new use cases; plugins exhibit backtracking and query refinement (Figs 9–10).
- **AutoGPT-4 (autonomous tool selection) underperforms**: 14.4% L1 / 0.4% L2 — worse than plain GPT-4 on L2 — and is far slower (7.6–11.7 min vs ~0.2 min). Human + GPT-4-plugins gave the best score/time ratio.
- **Puzzles are a notable failure mode**: GPT-4 fails self-contained reasoning puzzles (Rubik's cube, Fig 11) even when classed as Level 1.
- **Validation cost**: each question independently re-answered by 2 new annotators; **68% valid as-is** (75% L1, 68% L2, 47% L3); ~2 hours of annotator time per question.

## Methods (brief)
Zero-shot prompting with a fixed prefix prompt enforcing a `FINAL ANSWER:` format; evaluation is automated **quasi-exact-match** against a single unambiguous factual answer (string, number, or comma-separated list), making scoring fast, factual, and robust to token-generation randomness. Questions are grounded in durable web sources of truth (Wikipedia, arXiv) or attached files; answers are by design absent from plain-text pretraining data to resist contamination (a "proof-of-work" analogy).

## Limitations
GAIA does not grade the reasoning trace (only the final answer), so it cannot attribute errors to sub-modules; it is English-only (excluding ~80% of the world's speakers and ~half the web); GPT-4+plugins scores are an unreproducible "oracle" (manual, ever-changing plugin selection); and questions may decay as web sources change or contamination occurs.

## Citations of interest
- Morris et al. 2023, *Levels of AGI* — framework under which a GAIA-solving system would be a "competent General AI" (one level above ChatGPT).
- Chollet 2019, *On the Measure of Intelligence* — argues for testing fundamental abilities/adaptation over specialized skills; GAIA's guiding philosophy.
- Hendrycks et al. 2021, *MMLU* — the saturated expert-knowledge benchmark GAIA contrasts itself against.
- Liu et al. 2023a, *AgentBench* — closed-environment agent benchmark; GAIA differs by using open real-world interaction without specified APIs.
- Mialon et al. 2023, *Augmented Language Models: a survey* — tool-augmentation background underpinning the evaluated systems.
- Zheng et al. 2023, *Judging LLM-as-a-judge (MT-Bench)* — motivates avoiding model-based evaluation in favor of exact-match scoring.
