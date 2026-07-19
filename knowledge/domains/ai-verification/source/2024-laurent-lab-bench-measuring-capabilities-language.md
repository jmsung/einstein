---
type: source
kind: paper
title: "LAB-Bench: Measuring Capabilities of Language Models for Biology Research"
authors: Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, M. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, S. Rodriques
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2407.10362
source_local: ../raw/2024-laurent-lab-bench-measuring-capabilities-language.pdf
topic: general-knowledge
cites:
---

# LAB-Bench: Measuring Capabilities of Language Models for Biology Research

**Authors:** Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, M. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, S. Rodriques  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.10362

## One-line
Introduces a 2,400-question multiple-choice benchmark (LAB-Bench) that evaluates LLMs on practical biology research tasks — literature retrieval, figure/table interpretation, database lookup, protocol troubleshooting, and DNA/protein sequence manipulation — against PhD-level human baselines.

## Key claim
Frontier LLMs (GPT-4o, Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, Llama-3-70B) still underperform expert humans across most LAB-Bench categories; Claude 3.5 Sonnet matches or narrowly exceeds humans on TableQA but all models trail badly on FigQA, SuppQA, DbQA lookups, long-sequence manipulation (PCR-primers-len, RE-seq-lenfrags), and the 41 "human-hard" Cloning Scenarios.

## Method
Two-track dataset construction: programmatic generation for sequence/database subtasks (SeqQA's 15 subtasks via BioPython Restriction, ORF/Kozak scripts; DbQA via MSigDB, DisGeNet, OMIM, miRDB, ClinVar, ProteinGym, P-HIPSter, Ensembl, GTRD), and expert-authored questions for literature/figure/table/protocol/cloning tasks. Evaluation uses zero-shot chain-of-thought prompting with an explicit "Insufficient information" option, parsing `[ANSWER]X[/ANSWER]` tags, and reports accuracy, precision (selective accuracy on attempted), and coverage. A noteworthy generation trick: ask frontier models to draft questions, harvest the nonsensical ones, and have humans revise them to identify the "null space" of model reasoning.

## Result
On the 2,457-question benchmark with ~69% human coverage, no model approaches human performance overall. TableQA is easiest for models; FigQA and SuppQA are hardest. SeqQA precision sits around 40–50% across models, with sharp drops on tasks requiring subsequence access (amplicon length given primers, fragment lengths from restriction digests). Models often achieve apparent success via distractor elimination — e.g., guessing "Ampicillin" in cloning scenarios — exposing that multiple-choice scores overstate reasoning ability. The authors flag this as a methodological warning: MCQ benchmarks need open-answer validation, and human baselines on hard tasks may need to be replaced by "proofs-of-possibility."

## Why it matters here
General background; no direct arena tie. LAB-Bench is a biology research benchmark — its math content (sequences, combinatorics of fragments) doesn't touch sphere packing, kissing numbers, autocorrelation, or any of the 18 active Einstein Arena problems. The only transferable lesson is methodological: the paper's caution that distractor quality determines whether a benchmark measures reasoning or test-taking, and that frontier models pass questions by heuristic elimination rather than computation — relevant to how this repo designs its own agent-evaluation harness (`docs/agent/cycle-log.md`, `skill-library.md`) but not to any math finding.

## Open questions / connections
- Does retrieval/tool augmentation close the gap on the lookup-heavy subtasks (LitQA2, SuppQA, DbQA)? The authors cite prior LitQA work showing RAG helps but don't measure it here.
- How much of SeqQA's primer/restriction performance is recoverable via deterministic tool use (BioPython, ApE) versus requiring genuine sequence reasoning?
- Methodological connection: the "ask the model to draft, then keep the questions it fails" technique parallels the failure-is-a-finding rule — failed model outputs as signal for where capability gaps live.

## Key terms
LAB-Bench, biology benchmark, large language models, multiple choice evaluation, retrieval-augmented generation, selective accuracy, coverage, zero-shot chain-of-thought, sequence manipulation, cloning scenarios, distractor design, FutureHouse, human baseline, benchmark contamination
