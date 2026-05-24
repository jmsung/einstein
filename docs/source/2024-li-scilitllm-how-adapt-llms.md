---
type: source
kind: paper
title: "SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding"
authors: Sihang Li, Jian Huang, Jiaxi Zhuang, Yaorui Shi, Xiaochen Cai, Mingjun Xu, Xiang Wang, Linfeng Zhang, Guolin Ke, Hengxing Cai
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2408.15545
source_local: ../raw/2024-li-scilitllm-how-adapt-llms.pdf
topic: general-knowledge
cites:
---

# SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding

**Authors:** Sihang Li, Jian Huang, Jiaxi Zhuang, Yaorui Shi, Xiaochen Cai, Mingjun Xu, Xiang Wang, Linfeng Zhang, Guolin Ke, Hengxing Cai  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.15545

## One-line
A two-stage recipe — continual pre-training (CPT) on cleaned scientific PDFs plus supervised fine-tuning (SFT) on synthetic domain instructions — that adapts a general-purpose LLM (Qwen2.5) into a scientific-literature-understanding specialist (SciLitLLM-7B / 14B).

## Key claim
The CPT+SFT pipeline yields average gains of $+4.0\%$ on SciAssess and $+10.1\%$ on SciRIFF over leading sub-10B LLMs; SciLitLLM-7B surpasses Llama-3.1-70B and Qwen2.5-72B on SciRIFF, and SciLitLLM-14B leads among open-source LLMs on both benchmarks. Ablations show that filtering the lowest-25% of CPT text by an educational-value classifier is the optimal quality/quantity trade-off (vs 15% or 35% thresholds).

## Method
Hybrid pipeline: (1) **CPT** — parse 73k textbooks + 625k papers with PyPDF2, use Llama3-8B-Instruct (~2.52M tok/A100-hr) to correct PDF format/grammar errors, then fine-tune a 109M-param fineweb-edu BERT classifier on 50k Llama3-70B-scored samples to filter the bottom 25% by educational value, leaving 12.7B scientific tokens mixed with 11B Redpajama general tokens; (2) **SFT** — generate synthetic instructions for under-represented domains (materials, medicine, drug-discovery) by keyword-and-task-guided prompting (20 keywords sampled at temperature 3 from per-domain frequency tables, five task types: table/entity/molecule extraction, molecule translation, MCQ/TF), deduplicate with Levenshtein similarity $(1-\text{lev}(q_1,q_2))(1-\text{lev}(a_1,a_2))$ via disjoint-set merge, and filter by a 5-axis GPT-4o quality rubric (clarity, complexity, correctness, usefulness, adaptability; threshold mean $\geq 4$).

## Result
SciLitLLM-7B/14B trained on 23.7B CPT tokens (1 epoch, seq 2048, cosine LR $10^{-5}\to 0$, weight decay 0.1, grad clip 1.0; 3 days on 32 A100s for 7B, 7 days for 14B). New SciLitIns dataset: 93k instructions / 86M tokens across 3 domains and 5 task types. Contamination analysis (3×50-char substring match per GPT-4 protocol) shows 1.1–11% rates on SciAssess but negligible effect: clean-set vs full-set scores differ by $\leq 1.3$ pp. Human–quality-filter Spearman agreement (0.76 CPT, 0.88 SFT) matches or exceeds human–human (0.58, 0.89).

## Why it matters here
General background; no direct arena tie. The CPT+SFT recipe, PDF→clean-text pipeline, and educational-value quality filter are methodological references for any future "agent ingests its own corpus" work in einstein's `docs/raw/` → `docs/source/` flow, but the paper covers no math optimization, packing, or extremal-combinatorics content that bears on the 23 arena problems.

## Open questions / connections
- Could the fineweb-edu-style quality classifier be retrained on the einstein wiki's existing high-vs-low-quality `docs/source/` distillations to auto-score new ingests?
- The synthetic-instruction pipeline (keyword sampling + Levenshtein dedup + multi-axis LLM rubric) is a possible template for generating diverse `docs/wiki/questions/` seeds during council dispatch — but the paper offers no evidence this transfers to mathematical reasoning tasks.
- Extends Phi/Gunasekar "educational value" filtering and SciRIFF/SciGLM/ChemLLM instruction-tuning lines; leaves open whether CPT+SFT helps on reasoning-heavy (not retrieval-heavy) scientific tasks.

## Key terms
continual pre-training, supervised fine-tuning, CPT, SFT, instruction synthesis, PDF parsing, quality classifier, fineweb-edu, educational value filter, Levenshtein deduplication, scientific literature understanding, Qwen2.5, SciRIFF, SciAssess, SciLitIns, domain adaptation, knowledge injection
