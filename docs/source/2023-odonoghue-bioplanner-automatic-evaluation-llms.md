---
type: source
kind: paper
title: "BioPlanner: Automatic Evaluation of LLMs on Protocol Planning in Biology"
authors: Odhran O'Donoghue, Aleksandar Shtedritski, John Ginger, Ralph Abboud, Ali E. Ghareeb, J. Booth, S. Rodriques
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2310.10632
source_local: ../raw/2023-odonoghue-bioplanner-automatic-evaluation-llms.pdf
topic: general-knowledge
cites:
---

# BioPlanner: Automatic Evaluation of LLMs on Protocol Planning in Biology

**Authors:** Odhran O'Donoghue, Aleksandar Shtedritski, John Ginger, Ralph Abboud, Ali E. Ghareeb, J. Booth, S. Rodriques  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.10632

## One-line
Automatic evaluation framework for LLM-generated biology lab protocols by converting free-text protocols into pseudocode with a closed set of admissible pseudofunctions.

## Key claim
LLM-generated protocols can be evaluated automatically (rather than by costly manual review) by reformulating protocol writing as multiple-choice pseudofunction selection; GPT-4 beats GPT-3.5 on next-step prediction (70.6% vs 65.0% function accuracy unshuffled) and on Levenshtein-ordered protocol generation, and one GPT-4-generated E. coli cryopreservation protocol executed successfully in a wet lab.

## Method
A "teacher" GPT-4 translates a natural-language protocol into (i) an admissible set of Python-like pseudofunctions and (ii) ground-truth pseudocode, with an automatic feedback loop checking Python validity, function definitions, argument units. A "student" LLM is then given only the title, description, and admissible pseudofunctions and must reconstruct the pseudocode; evaluation uses function-call accuracy, precision/recall, normalized Levenshtein distance $L_{dn}=L_d/N$, BLEU, and SciBERTScore (cosine similarity of SciBERT embeddings of argument values).

## Result
Introduces BIOPROT: 100 manually-audited biology protocols (avg 12.5 steps, 641 tokens, 10.3 pseudofunctions each). 59/100 generated pseudocode files required no human edits. GPT-4 next-step accuracy 70.6% (unshuffled) / 57.0% (shuffled); GPT-3.5 65.0% / 36.1%. Protocol-generation $L_{dn}$: GPT-4 0.396 vs GPT-3.5 0.498. Function retrieval is poor (GPT-4 precision 32.5% nearest, 48.8% random). GPT-4 as self-evaluator only marginally above chance (~43%). Llama-2-7B substantially underperforms. End-to-end agent generated and executed an E. coli overnight-culture + glycerol cryopreservation protocol.

## Why it matters here
General background; no direct arena tie. The Einstein Arena agent solves math optimization problems (sphere packing, autocorrelation, kissing numbers), not biology protocols — this paper's domain is orthogonal. The only tangential relevance is methodological: the teacher/student split with auto-generated admissible action sets is a generic LLM-evaluation pattern that doesn't transfer to numerical optimizer evaluation, where triple-verify against arena verifier is the operative discipline.

## Open questions / connections
- Can the teacher/student admissible-action paradigm extend beyond biology to chemistry, materials, or mathematical proof planning?
- Does shuffling-induced performance drop reflect genuine planning weakness or just positional priming from sequential pseudofunction definition order?
- GPT-4 self-evaluation barely above chance — confirms prior findings (Bran et al. 2023; Wang et al. 2023b) that LLM-as-judge is unreliable for open-ended scientific output.

## Key terms
LLM evaluation, protocol planning, pseudocode, admissible action space, teacher-student, BIOPROT, GPT-4, SciBERTScore, Levenshtein distance, chain-of-thought, Toolformer, PDDL planning
