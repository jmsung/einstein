<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
authors: [Yoonho Lee, Roshen Nair, Qizheng Zhang, Omar Khattab, Kangwook Lee, Chelsea Finn]
year: 2026
doi: 10.48550/arXiv.2603.28052
source_url: https://doi.org/10.48550/arXiv.2603.28052
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Meta-Harness: End-to-End Optimization of Model Harnesses

## TL;DR
Meta-Harness is an outer-loop system that searches over the *harness code* (the prompt/retrieval/memory/orchestration logic wrapping a frozen LLM) using a coding-agent proposer that retrieves the full source, scores, and execution traces of all prior candidates via a filesystem — and it beats hand-engineered harnesses and prior text optimizers on text classification, math reasoning, and agentic coding.

## Key findings
- **The core thesis:** the harness — code deciding what to store, retrieve, and present to the model — can cause a 6× performance gap on the same benchmark on a fixed model [ref 47]. Meta-Harness automates harness engineering rather than leaving it manual.
- **Key design choice — full history via filesystem.** Each evaluated harness contributes a directory with its source code, scores, and execution traces. The proposer (Claude Code with Opus-4.6) queries this via `grep`/`cat` rather than ingesting a single prompt. A single evaluation can produce up to **10,000,000 tokens** of diagnostic info — ~3 orders of magnitude beyond prior text optimizers (Table 1: 0.002–0.026 Mtok/iter vs. 10.0 for Meta-Harness). In the hardest setting the proposer reads a **median of 82 files/iteration** (range 69–99; ~41% prior source code, ~40% execution traces), referencing 20+ prior candidates per step.
- **Online text classification:** beats Agentic Context Engineering (ACE) by **7.7 points** (48.6% vs 40.9% avg over USPTO-50k/Symptom2Disease/LawBench) and MCE by 8.6, while using **4× fewer context tokens** (11.4K vs 50.8K for ACE). Matches best prior text optimizers' final accuracy in ~0.1× the evaluations (after just 4 vs ~40); final accuracy exceeds them by >10 points (Fig 1, Fig 4).
- **Interface ablation (Table 3):** scores-only → 34.6 median / 41.3 best; scores+summary → 34.9 / 38.7; **full traces → 50.0 / 56.7**. Raw execution traces are the load-bearing ingredient; LLM summaries do not recover the signal and may hurt.
- **OOD generalization (Table 5):** selected harness wins on 6/9 unseen classification datasets, 73.1% avg vs ACE 70.2%. (Naively adding few-shot examples beyond 32 *hurt* on 7/9 tasks.)
- **Retrieval-augmented math (Table 6):** a single discovered BM25 retrieval harness improves 200 IMO-level problems by **+4.7 points avg** over no-retriever, transferring across **5 held-out models** (GPT-5.4-nano/mini, Gemini-3.1-Flash-Lite, Gemini-3-Flash, GPT-OSS-20B); beats BM25 baseline by 1.3 and avoids dense-retrieval/random-few-shot regressions.
- **TerminalBench-2 (Table 7):** on Haiku 4.5, **37.6%** — #1 among all Haiku agents (vs Goose 35.5, Terminus-KIRA 33.7). On Opus 4.6, 76.4% — #2, surpassing hand-engineered Terminus-KIRA (74.7%).
- **Qualitative causal reasoning (Appendix A.2):** across iterations the proposer diagnosed a *confound* (regressions came from a shared cleanup-prompt rewrite, not the structural bugfixes), isolated it, then pivoted to a purely *additive* "environment bootstrap" (inject a sandbox snapshot before the agent loop) — the winning TerminalBench-2 change (~80 LOC on Terminus-KIRA, gaining on 7/89 tasks).

## Methods (brief)
An evolutionary outer loop (Algorithm 1): seed a population from baseline harnesses, then for N iterations the coding-agent proposer queries the filesystem of all prior candidates, proposes k new single-file Python harnesses, validates the interface, evaluates on a held-out-from-test *search set*, and logs everything back. Maintains a Pareto frontier (accuracy vs context cost) with no parent-selection rule. Base model M is always frozen; the proposer is guided by a minimal domain-specific skill. Typical run: ~60 harnesses over 20 iterations. Decontamination for the math corpus used exact-prefix + fuzzy Jaccard (0.8) against eval/search sets.

## Limitations
TerminalBench-2 search and final eval ran on the *same* 89 tasks (a "discovery" setting, mitigated by manual/regex overfitting audits), so that result is not held-out generalization. Demonstrated with a single proposer (Claude Code/Opus-4.6); robustness across proposer agents is untested. ForgeCode's higher Opus-4.6 score (81.8%) was not reproducible from public code. Search-set sizes are small (50–100 examples; 88 math problems), and the method's cost (10M tokens/eval) is high.

## Citations of interest
- Zhang et al. (ACE) [59] — agentic context engineering via reflective memory curation; the main hand-designed baseline.
- Ye et al. (MCE) [52] — meta context engineering via agentic skill evolution; second classification baseline.
- Agrawal et al. (GEPA) [1] — reflective prompt evolution; closest text optimizer in feedback richness (per-candidate rollout traces).
- Novikov et al. (AlphaEvolve) [35] / Sharma (OpenEvolve) [43] — LLM-mutation evolutionary code search with scalar/program-DB feedback.
- Yuksekgonul et al. (TTT-Discover) [54/55] — learning to discover at test time; PUCT reuse rule, compared head-to-head.
- KRAFTON AI & Ludo (Terminus-KIRA) [25] — minimal-harness TerminalBench baseline the winning coding harness builds on.
- Sutton, *The Bitter Lesson* [45] — framing for general agents outperforming hand-engineered solutions once search is enabled.
