<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Language Models are Few-Shot Learners
authors: [Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei]
year: 2020
doi: 10.48550/arxiv.2005.14165
source_url: https://doi.org/10.48550/arxiv.2005.14165
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Language Models are Few-Shot Learners

## TL;DR
Scaling an autoregressive transformer to 175B parameters (GPT-3) produces strong task-agnostic few-shot performance via in-context learning — solving NLP tasks from natural-language instructions plus a handful of demonstrations, with no gradient updates or fine-tuning, sometimes rivaling fine-tuned SOTA.

## Key findings
- **GPT-3 = 175B params, 96 layers, d_model 12288, 96 heads, context window 2048 tokens**, trained on ~300B tokens (Table 2.1). It is 10× larger than any prior non-sparse LM. Architecture mirrors GPT-2 plus alternating dense/locally-banded sparse attention.
- **In-context learning** is the central mechanism: the model is conditioned purely on text — a task description and/or K demonstrations (typically 10–100) — then completes new instances. Three regimes studied: zero-shot, one-shot, few-shot. No weight updates in any.
- **Few-shot competes with fine-tuned SOTA on several tasks.** TriviaQA (closed-book): 64.3% (0-shot) → 68.0% (1-shot) → 71.2% (few-shot), the last beating prior fine-tuned closed-book SOTA. CoQA: 81.5/84.0/85.0 F1. LAMBADA: 76.2% zero-shot, 86.4% few-shot (+18% over prior SOTA). SuperGLUE few-shot avg 71.8, beating fine-tuned BERT-Large on 4/8 tasks.
- **Scale drives in-context learning.** The gap between zero-/one-/few-shot widens with model size — larger models are more proficient meta-learners (Figs 1.2, 1.3). Validation loss follows a smooth power law extended two more orders of magnitude (Fig 3.1, building on Kaplan et al. scaling laws).
- **On-the-fly reasoning emerges at the largest scale.** Arithmetic (Table 3.9): 100% on 2-digit addition, 98.9% 2-digit subtraction, 80.4% 3-digit addition few-shot — with a sharp jump from 13B to 175B. Word unscrambling, SAT analogies (65.2% few-shot vs 57% human average), and using novel words after one definition.
- **Synthetic news indistinguishable from human-written:** human detection accuracy fell to ~52% (chance) for 175B-generated ~200-word articles, vs ~86% for a deliberately-bad control model (Table 3.11); held even for ~500-word articles.
- **Weaknesses:** NLI (ANLI, RTE) and sentence-comparison tasks (WiC at 49.4% ≈ chance), some reading comprehension (RACE, QuAC). Authors attribute partly to the unidirectional autoregressive objective.
- **Contamination study:** systematic 13-gram-overlap analysis (a filtering bug left residual overlap); most benchmarks shifted negligibly on cleaned subsets, with PIQA and Winograd flagged (asterisked).

## Methods (brief)
Eight models from 125M to 175B params trained on a filtered+deduplicated Common Crawl (410B tokens, 60% of mix) blended with WebText2, Books1/2, and Wikipedia; higher-quality sets oversampled. Adam, cosine LR decay, weight decay 0.1, gradient clipping, model parallelism across V100s. Evaluation by per-token likelihood for multiple-choice and beam search (width 4) for free-form, with no fine-tuning.

## Limitations
Largest results often rest on dev-set scores (model too large for some test servers). Residual train/test contamination could inflate a minority of benchmarks. The work cannot cleanly separate genuine de-novo task learning from recognition of pre-training patterns; the model also has poor pre-training sample efficiency, no grounding, and known gender/race/religion biases.

## Citations of interest
- Kaplan et al. 2020 (Scaling Laws for Neural LMs) — the power-law basis for choosing model/data/compute scale.
- Radford et al. 2019 (GPT-2 / "LMs are Unsupervised Multitask Learners") — direct predecessor; architecture and in-context-learning precedent.
- Vaswani et al. 2017 (Attention is All You Need) — transformer architecture.
- Raffel et al. 2019 (T5) — fine-tuned closed-book QA and text-to-text baselines compared against.
- Child et al. 2019 (Sparse Transformer) — the alternating dense/sparse attention pattern.
- Roberts et al. 2020 (closed-book QA) — the closed-book evaluation setting GPT-3 extends.
