<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
authors: [Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom]
year: 2023
source_url: https://arxiv.org/abs/2302.04761
drive_file_id: 1LkU_ejlTWb85jyLn-c05zlYJIUm1u9ZM
text_source: pdf
ingested_by: agent
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.04761

## One-line
A language model finetunes itself, in a self-supervised way, to decide which external APIs to call, when, and with what arguments, using only a handful of demonstrations per tool.

## Method
Given a plain-text corpus $\mathcal{C}$ and a small set of tools (question answering, calculator, Wikipedia search, machine translation, calendar), the model $M$ (GPT-J, 6.7B) is prompted with a few human-written examples per API to sample candidate API calls at high-probability positions in each text. Each candidate call is executed to get a result $r_i$, then filtered by comparing the weighted cross-entropy loss $L_i$ of predicting subsequent tokens with the call+result given as prefix ($L_i^+$) versus without any call or with an empty result ($L_i^-$); a call is kept only if $L_i^- - L_i^+ \geq \tau_f$, i.e. it demonstrably reduces the model's own loss on the following tokens. Surviving calls are interleaved into the original text (position $i$: $x_{1:i-1}, e(c_i,r_i), x_{i:n}$), and $M$ is finetuned on this augmented dataset $\mathcal{C}^*$ (which still contains the unmodified originals too) with a standard LM objective — so the model learns purely from its own filtered self-generated feedback, no human tool-use labels. At inference, decoding proceeds normally until $M$ emits "→" (expects an API result), at which point the real API is called and its output is spliced in before continuing generation.

## Result
On LAMA (SQuAD/Google-RE/T-REx), Toolformer improves over the best same-size baseline by 11.7/5.2/18.6 points and beats OPT-66B and GPT-3-175B despite being GPT-J-6.7B-based, using the QA tool in 98.1% of examples. On math benchmarks (ASDiv/SVAMP/MAWPS) it scores 40.4/29.4/44.0 vs 7.5/5.2/9.9 for vanilla GPT-J and still clearly beats OPT-66B and GPT-3-175B, calling the calculator on 97.9% of examples. Even with API calls disabled at inference, the finetuned model outperforms baselines, suggesting finetuning on tool-augmented data also improves the model's intrinsic capabilities (e.g. 22.1/6.3/34.9 on LAMA subsets vs 19.2/5.6/9.3 for GPT-J+CC). Filtering thresholds $\tau_f \in \{0.5, 1.0, 2.0\}$ yield markedly different dataset sizes (e.g. calculator: 3,680 → 994 → 138 examples), showing the self-supervised filter is highly selective.

## Key terms
Toolformer, tool use, self-supervised finetuning, API calls, GPT-J, in-context learning, question answering tool, calculator tool, Wikipedia search, machine translation, calendar tool, zero-shot, LAMA benchmark, weighted cross-entropy filtering
