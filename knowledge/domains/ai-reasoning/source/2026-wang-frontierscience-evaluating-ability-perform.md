---
type: source
kind: paper
title: "FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks"
authors: Miles Wang, Robi Lin, Kat Hu, Joy Jiao, Neil Chowdhury, Ethan Y. Chang, Tejal Patwardhan
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2601.21165
source_local: ../raw/2026-wang-frontierscience-evaluating-ability-perform.pdf
topic: general-knowledge
cites:
---

# FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks

**Authors:** Miles Wang, Robi Lin, Kat Hu, Joy Jiao, Neil Chowdhury, Ethan Y. Chang, Tejal Patwardhan  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2601.21165

## One-line
Introduces FrontierScience, a benchmark of expert-written olympiad and PhD-research-level physics/chemistry/biology questions to measure frontier LLM scientific reasoning.

## Key claim
Frontier models have nearly saturated short-answer olympiad-style science (GPT-5.2: 77% on Olympiad track) but remain far from saturation on open-ended PhD research subtasks (GPT-5.2 / GPT-5: 25% on Research track at the 7/10-rubric-point success threshold).

## Method
Two-track benchmark construction. Olympiad track: 100 gold (of 500+) original short-answer problems by 42 IPhO/IChO/IBO-class medalists, graded by GPT-5-judge equivalency check. Research track: 60 gold (of 200+) open-ended subproblems by 45 PhD scientists, each scored by a 10-point pass/fail rubric whose items decompose intermediate reasoning steps, judged by GPT-5 at high reasoning effort. Iterative peer-review pipeline (≥1 reviewer Olympiad, ≥2 Research) with adversarial filtering against internal OpenAI models.

## Result
On the 160-question gold set, GPT-5.2 leads both tracks (77% Olympiad, 25% Research); Gemini 3 Pro reaches 76% Olympiad; GPT-5 ties GPT-5.2 at 25% Research and surprisingly beats GPT-5.1. Scaling reasoning effort lifts GPT-5.2 from 67.5%→77.1% (Olympiad) and 18%→25% (Research), while o3 marginally degrades at high effort on Research. Chemistry > physics ≈ biology across tracks; dominant failure modes are reasoning/logic errors, niche-concept misunderstanding, calculation mistakes, and factual inaccuracy.

## Why it matters here
General background; no direct arena tie — this is an AI-evaluation methodology paper, not a math result. Tangentially informs how to judge agent self-improvement: rubric-decomposed grading (intermediate-step checks) is the same honesty principle as the einstein cycle-log + triple-verify discipline.

## Open questions / connections
- How to baseline human expert performance on hyper-specialized PhD subproblems (authors leave this as future work).
- Rubric-judge reliability vs human grading on open-ended scientific reasoning — a noise ceiling the authors flag explicitly.
- Extends OlympiadBench, GPQA, PHYBench, CritPt, LAB-Bench, PaperBench by combining original adversarial construction + granular rubric grading; complementary to checkpoint-style verification (CritPt).
- No multimodal / wet-lab / ideation coverage — open frontier for benchmarks of "proposing novel research directions."

## Key terms
benchmark, scientific reasoning, olympiad, PhD research evaluation, rubric grading, GPT-5.2, Gemini 3 Pro, model-judge, IPhO, IChO, IBO, contamination, reasoning effort scaling, GPQA, OlympiadBench, CritPt
