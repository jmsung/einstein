---
type: source
kind: paper
title: "AutoSurvey: Large Language Models Can Automatically Write Surveys"
authors: Yidong Wang, Qi Guo, Wenjin Yao, Hongbo Zhang, Xin Zhang, Zhen Wu, Meishan Zhang, Xinyu Dai, Min Zhang, Qingsong Wen, Wei Ye, Shikun Zhang, Yue Zhang
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.10252
source_local: ../raw/2024-wang-autosurvey-large-language-models.pdf
topic: general-knowledge
cites:
---

# AutoSurvey: Large Language Models Can Automatically Write Surveys

**Authors:** Yidong Wang, Qi Guo, Wenjin Yao, Hongbo Zhang, Xin Zhang, Zhen Wu, Meishan Zhang, Xinyu Dai, Min Zhang, Qingsong Wen, Wei Ye, Shikun Zhang, Yue Zhang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.10252

## One-line
A four-phase LLM pipeline (retrieve → outline → parallel subsection drafting → refine/evaluate) that auto-generates 8k–64k-token academic surveys with RAG-grounded citations and multi-LLM-as-judge scoring.

## Key claim
At 64k-token survey length, AutoSurvey achieves 82.25% citation recall / 77.41% precision (vs. naive RAG 68.79% / 61.97%; humans 86.33% / 77.78%) and content-quality scores of 4.73 coverage / 4.33 structure / 4.86 relevance (humans: 5.00 / 4.66 / 5.00), at ~3 minutes and $1.2 per survey.

## Method
Stage 1: embedding-retrieve $\sim$1200 papers for topic $T$ from a 530k-paper arXiv corpus, chunk by context window, generate per-chunk outlines, merge into a final 8-section outline. Stage 2: in parallel, for each subsection $O_i$, retrieve $\sim$60 papers via sub-outline query and draft $S_i = \text{Draft}(O_i, P_{sec})$ with inline `[paper_title]` citations later embedding-mapped to arXiv IDs. Stage 3: per-section refinement $R_i = \text{Refine}(S_i)$ using local context ± neighboring sections, then merge. Stage 4: Multi-LLM-as-Judge (GPT-4 + Claude-3-Haiku + Gemini-1.5-Pro) scores $N=2$ candidates on citation recall/precision (NLI-based) and 5-point rubrics for coverage/structure/relevance; best is selected.

## Result
Beyond the headline 64k numbers above, AutoSurvey holds steady across lengths (8k avg 4.61, 16k 4.60, 32k 4.58, 64k 4.62) while naive RAG degrades (4.33 → 4.19). Ablation: removing retrieval collapses citation recall to 60.11% / precision 51.65%; removing reflection has marginal effect. Meta-evaluation: Spearman $\rho = 0.5429$ between the mixture-of-judges ranking and human-expert rankings over 20 surveys (>0.5 = strong positive correlation). Error analysis of 100 unsupported claims: 51% overgeneralization, 39% misalignment, 10% misinterpretation.

## Why it matters here
General background; no direct arena tie. Tangentially relevant as a reference architecture for the einstein self-improvement loop — the retrieve→outline→parallel-draft→refine→multi-judge pattern parallels council-dispatch + wiki-first-lookup + cycle-discipline, and the multi-LLM-as-judge with $\rho \approx 0.54$ vs human is a calibration data point for any automated wiki-quality scorer.

## Open questions / connections
- Can the Multi-LLM-as-Judge rubric (coverage/structure/relevance + NLI-based citation recall/precision) be adapted to score wiki findings/concepts for the cycle-log's "self-improvement" honesty checks?
- The 51% overgeneralization rate suggests RAG citations alone don't constrain LLM parametric drift — what's the analog risk when an agent writes `docs/wiki/findings/` from retrieved sources?
- Extends STORM (Shao et al. 2024) and PaperRobot (Wang et al. 2019) from <4k to 64k-token generation via parallel subsection drafting; the chunked-outline-merge trick is the key scaling move.

## Key terms
AutoSurvey, retrieval-augmented generation, RAG, multi-LLM-as-judge, LLM-as-judge, citation recall, citation precision, NLI entailment, parallel subsection drafting, outline merging, Spearman rank correlation, survey automation, hallucination, overgeneralization, Claude-Haiku, GPT-4, Gemini-1.5-Pro, STORM, nomic-embed-text
