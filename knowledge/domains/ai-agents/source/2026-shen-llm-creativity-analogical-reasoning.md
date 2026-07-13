<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Unlocking LLM Creativity in Science through Analogical Reasoning
authors: [Andrew Shen, Shaul Druckmann, James Zou]
year: 2026
doi: null
source_url: https://arxiv.org/abs/2605.11258
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Unlocking LLM Creativity in Science through Analogical Reasoning

## TL;DR
LLMs prompted for open-ended scientific solutions mode-collapse to a few canonical answers; a two-step "analogical reasoning" (AR) harness — extract a problem's relational structure, map it to a distant domain, then search that domain for solutions — boosts solution diversity by 90–173% and novelty from ~2% to >50%, and the transferred solutions deliver real gains on four biomedical benchmarks.

## Key findings
- **Mode collapse quantified.** Across 150 generations/problem aggregated over 3 LLMs, baseline "no-domain" and "cross-domain" prompts reach domain Vendi Scores of only 2.64 / 2.84 and solution Vendi Scores 5.81 / 8.34; only ~5% of domains (7–8 unique) and ~57–66% of solutions were unique. For "predict 3D structure from sequence," baselines collapse onto AlphaFold2 variants.
- **AR mitigates collapse.** AR improves domain Vendi Score by 100–115% and solution Vendi Score by 90–173% (to 15.90 aggregated), finding ~3.5× more unique domains and 1.3× more unique solutions than the best baseline. The analogy search space is larger than direct/cross-domain solution recall.
- **Novelty.** LLM-judged binary novelty rises no-domain < cross-domain < AR for all models (Claude 1.6%<21.6%<50.4%; GPT 9.0%<28.2%<58.8%; Gemini 8.9%<37.8%<68.9%). Human study: AR solutions judged more novel than the strongest baseline 78% of the time (κ=0.445), and "reasonable" 67% of the time (vs 86% for cross-domain — novelty trades against feasibility).
- **Analogy quality.** AR analogies score highest on Domain Distance (>3× the no-domain baseline, e.g. 6.99/6.83/7.53) and Novelty (4.82/5.27/5.58), exceeding even the human ground-truth analogies; Structural Depth is comparable across settings. Human–LLM agreement reached 88.6% (Domain Distance) and 75.7% (Novelty).
- **Four biomedical case studies** (solution implemented by Claude Code Opus 4.6, search via Perplexity Deep Research):
  1. **Perturbation effect prediction** (Srivatsan20/PerturBench): economics analogy → finite mixture models; MMD PCA distributional distance improved from LA baseline 1.65 → 0.13 (~13×) when hybridized (LA+FMM).
  2. **Cell-cell communication** (OpenProblems): telecom signal-to-noise analogy → SNR scoring; SOTA AUPRC 0.248 vs all 14 baselines.
  3. **Brain region interaction**: communication-networks analogy → PCMCI causal discovery; ρ=0.729 Spearman agreement with the published Ridge method, comparable downstream prediction (ρ=0.335 vs 0.317).
  4. **Oligonucleotide property prediction** (OligoGym): chess piece-square-tables analogy → position-encoded features; improved 5/6 (Random) and 6/6 (Nucleobase) datasets over linear baseline, new SOTA on 2 datasets with PST+k-mer.
- AR costs ~$0.02/problem.

## Methods (brief)
AR is grounded in Gentner's structure-mapping theory: analogies = object mappings + shared relations (attributes are not transferred). Two LLM calls per generation — an extraction agent (temp 1.0) pulls problem objects/relations and generates cross-domain analogies, a search agent uses each analogy to retrieve solutions. Evaluated on 50 problems sampled from a curated 266-paper "AR Dataset" of real cross-domain breakthroughs, across Claude Sonnet 4.5, GPT-5.2, Gemini 3 Flash. Diversity = Vendi Score over OpenAI embeddings; novelty via Semantic-Scholar retrieval + SPECTER re-rank + LLM judge (validated against human annotations).

## Limitations
N=50 evaluation problems (API-cost-limited), all biomedical; novelty/quality rely on LLM judges (validated but imperfect). AR raises novelty at the cost of feasibility (reasonable rate 67% vs 86% baseline) — not every analogy yields a viable solution, and real-world viability assessment remains the bottleneck. The pipeline isolates solution generation and is not yet integrated into an end-to-end execution-grounded loop.

## Citations of interest
- Gentner 1983 — structure-mapping theory of analogy (the framework AR operationalizes).
- Friedman & Dieng 2023 — Vendi Score, the diversity metric used throughout.
- Lu et al. 2024 (AI Scientist), Gottweis et al. 2025 (AI Co-scientist), Swanson et al. 2024 (Virtual Lab) — autonomous-science systems AR aims to augment.
- Ahlmann-Eltze et al. 2025 — deep perturbation models fail to beat linear baselines (motivates case study #1).
- Webb, Holyoak & Lu 2023 — emergent analogical reasoning in LLMs (latent capability AR exploits).
- Shahid et al. 2025 — literature-grounded novelty assessment (basis for the retrieval/re-rank novelty scorer).
