<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "BioPlanner: Automatic Evaluation of LLMs on Protocol Planning in Biology"
authors: [Odhran O'Donoghue, Aleksandar Shtedritski, John Ginger, Ralph Abboud, Ali Essa Ghareeb, Justin Booth, Samuel G Rodriques]
year: 2023
doi: 10.48550/arXiv.2310.10632
source_url: https://doi.org/10.48550/arXiv.2310.10632
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# BioPlanner: Automatic Evaluation of LLMs on Protocol Planning in Biology

## TL;DR
BioPlanner introduces an automatic framework for evaluating LLMs on biology-protocol planning by converting free-text protocols into pseudocode with a closed set of admissible "pseudofunctions," turning protocol writing into a robustly-scorable next-step/sequence-prediction task — and demonstrates the framework end-to-end by having a GPT-4 agent generate a novel protocol that was run successfully in a wet lab.

## Key findings
- **Core idea**: Evaluating natural-language protocols is hard (n-gram metrics like BLEU/BERTScore miss action order and substance relations; granularity varies). The fix is a **teacher/student pseudocode paradigm** (Fig. 1): a "teacher" GPT-4 converts a protocol into a protocol-specific set of pseudofunctions + ground-truth pseudocode; a "student" model must reconstruct the pseudocode given only the admissible functions and a description. This reduces protocol writing to multiple-choice-like function selection, scorable automatically.
- **BIOPROT dataset**: 100 biology protocols from Protocols.io, filtered automatically and manually for biology relevance, reproducibility, ≥3 steps. Stats — avg 12.5 steps, 641 tokens/protocol, 10.3 pseudofunctions/protocol, 17.2 lines of pseudocode (Tables 1–2).
- **Pseudocode generation quality**: Generated via one-shot prompt + automatic feedback loop (flags invalid Python, missing functions/arguments, missing units). On manual review by a lab scientist, **59/100 protocols required no edits**; 24% had 1–3 edited lines, 17% had >3; avg 11.8 line edits in edited files (Table 3). Most common errors were missing units (usually non-blocking).
- **Next-step prediction** (Table 4): GPT-4 function accuracy 70.6% vs GPT-3.5 65.0% (unshuffled). Shuffling input functions hurts both (GPT-4 → 57.0%, GPT-3.5 → 36.1%), since teacher-generated functions appear roughly in call order, leaking a signal. Argument metrics: ~97% precision / ~95% recall on names; SciBERTScore ~88%.
- **Full protocol generation** (Table 5): GPT-4's main edge is **ordering** — much better normalized Levenshtein distance (Ld_n ~0.40 vs GPT-3.5 ~0.50); precision/recall of function use are comparable. Shuffling consistently degrades performance.
- **Function retrieval** (Table 6): Both models are weak (GPT-4 random precision 48.8%, nearest-neighbor 32.5%); ambiguity (e.g. `Mix` vs `MixSubstance`) penalizes valid choices, so nearest-neighbor distractors are *harder* than random.
- **GPT-4 as evaluator** (Table 8): Only slightly above chance at preferring ground truth over generations (~40–44%), echoing prior findings that LLM judges favor longer/coherent over correct outputs.
- **Machine-generated descriptions** (Table 7) slightly *improve* over original human descriptions.
- **Llama-2-7B** (Tables 9–10) substantially underperforms; iterative feedback helped GPT models but distracted Llama, which often stated intent rather than writing code.
- **Human benchmark** (App. F): on function selection, human precision 87.5% beats GPT-4; on next-step prediction, human accuracy 54.8% ≈ GPT-4 shuffled.

## Methods (brief)
LLMs accessed via OpenAI API (GPT-3.5, GPT-4) plus Llama-2-7B; text-embedding-ada-002 for nearest-neighbor protocol retrieval; SciBERT sentence encoder for argument-value similarity (SciBERTScore). Metrics: function accuracy, precision/recall, normalized Levenshtein distance for ordering, BLEU + SciBERTScore for arguments; mean ± SD over 5 runs. Real-world validation used a Toolformer-style chain-of-thought GPT-4 agent with a protocol-search tool to assemble a novel protocol from retrieved pseudofunctions.

## Limitations
N=100 protocols, biology-only, single competent-scientist review; only one of two generated protocols (E. coli cryopreservation) was physically executed. Closed-source paid models (~$1000 API spend) limit reproducibility; the function-order signal from teacher generation inflates unshuffled scores. Retrieval metrics are confounded by synonym ambiguity, and the GPT-4-evaluator result can't distinguish "generations are correct" from "judge can't tell."

## Citations of interest
- Boiko et al. 2023 (arXiv:2304.05332) — emergent autonomous scientific research with LLMs; motivates lab automation.
- Bran et al. 2023, ChemCrow (arXiv:2304.05376) — LLM + chemistry tools for synthesis planning; source of the "manual evaluation only" gap and LLM-judge bias finding.
- Schick et al. 2023, Toolformer (arXiv:2302.04761) — tool-use paradigm underlying the real-world validation agent.
- Ahn et al. 2022, SayCan (arXiv:2204.01691) — restricted admissible action set for robotic planning; conceptual basis for pseudofunctions.
- Wei et al. 2022, Chain-of-Thought (arXiv:2201.11903) — reasoning decomposition used by the validation agent.
- Teytelman et al. 2016, Protocols.io (PLoS Biol 14(8):e1002538) — source database for BIOPROT.
- Beltagy et al. 2019, SciBERT — encoder for the SciBERTScore argument metric.
