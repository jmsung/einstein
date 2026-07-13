<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-verification
domains: [ai-verification, ai-reasoning]
title: "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark"
authors: [Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, Wenhu Chen]
year: 2024
source_url: https://arxiv.org/abs/2406.01574
drive_file_id: 1aEWPtGKsZFbOtCiLEIPKYFwUF2xUj1Nr
text_source: pdf
ingested_by: agent
---
# MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark

**Authors:** Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, Wenhu Chen  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.01574

## One-line
MMLU-Pro extends MMLU with 10-way multiple choice (vs. 4), more reasoning-heavy college-level questions, and expert-reviewed noise removal, producing a benchmark that is both harder and more stable under prompt variation.

## Key claim
MMLU has saturated (frontier models cluster at 86-87%) and is overly sensitive to prompt phrasing and easy to game via 4-option guessing; MMLU-Pro fixes this by tripling distractors to 10 options, filtering out questions that 5+ of 8 weaker models already answer correctly, and adding harder STEM/reasoning questions, yielding a benchmark where the best model (GPT-4o) only reaches 72.6% and prompt-sensitivity drops from 4-5% to 2%.

## Method
Pipeline: Original MMLU -> Initial Filtering -> Question Collection and Integration -> Option Augmentation -> Expert Review -> MMLU-Pro (Figure 2). Initial filtering evaluates all MMLU questions with 8 models (Llama-2-7B/13B-Chat, Llama-2-7B, Mistral-7B, Gemma-7B, Yi-6B/6B-Chat) and drops 5,886 questions answered correctly by more than 4 of them (deemed "too easy"), while merging the original 57 subjects into 14 broader disciplines (math, physics, chemistry, law, engineering, psychology, business, biology, philosophy, health, economics, other, CS, history). New questions are pulled from the STEM Website, TheoremQA, and SciBench; GPT-4-Turbo extracts short answers from STEM Website/TheoremQA solutions and generates 3 additional distractors. Option Augmentation then uses GPT-4-Turbo to expand every question from 4 to 10 answer choices (6 new plausible distractors) to cut chance-guessing probability. Expert Review has two phases: Phase 1 verifies correctness/appropriateness and removes non-text-answerable or multimodal questions; Phase 2 uses Gemini-1.5-Pro to flag potential false-negative distractors, which human experts then adjudicate. Evaluation uses 5-shot Chain-of-Thought prompting (0-shot for Gemini-1.5-Pro/Flash) with regex-based answer extraction (`answer is \(?([A-J])\)?`, with a fallback regex, and random-choice fallback if both fail).

## Result
Final dataset: 12,032 questions across 14 disciplines (avg. 9.47 options/question; 83% have the full 10 options, 17% fewer). Expert review found and removed issues per source: Incorrect Answers (MMLU 350, STEM Website 483, SciBench 11), False Negative Options (MMLU 1,953, STEM Website 293, SciBench 15), Bad Questions (MMLU 385, STEM Website 862, SciBench 15). Top model GPT-4o scores 72.6% overall (vs. 87.4% on MMLU) — a 14.8-point drop; GPT-4-Turbo scores 63.7%. Accuracy drop across models ranges 16-33% relative to MMLU. Prompt-variation sensitivity (24 prompt styles) falls from 4-5% (MMLU) to 2% (MMLU-Pro). CoT improves GPT-4o by 19 points on MMLU-Pro, whereas CoT hurts performance on original MMLU — indicating MMLU-Pro requires genuine multi-step reasoning. Discriminative power improves: the GPT-4o vs. GPT-4-Turbo gap widens from 1% (MMLU) to 9% (MMLU-Pro). Best open-source model is Llama-3-70B-Instruct (56.2%), trailing closed-source leaders. Error analysis on 120 GPT-4o mistakes: 39% reasoning-process flaws, 35% lack of domain expertise, 12% computational errors.

## Key terms
MMLU-Pro, multi-task language understanding, ten-option multiple choice, chain-of-thought prompting, benchmark saturation, distractor augmentation, prompt robustness, expert review pipeline, false negative options, discriminative benchmark, STEM reasoning, GPT-4o evaluation
