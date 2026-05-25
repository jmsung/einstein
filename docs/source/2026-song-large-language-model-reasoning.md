---
type: source
kind: paper
title: Large Language Model Reasoning Failures
authors: Peiyang Song, Pengrui Han, Noah D. Goodman
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2602.06176
source_local: ../raw/2026-song-large-language-model-reasoning.pdf
topic: general-knowledge
cites: 
---

# Large Language Model Reasoning Failures

**Authors:** Peiyang Song, Pengrui Han, Noah D. Goodman  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2602.06176

## One-line
First comprehensive survey of reasoning failures in LLMs, organized by a two-axis taxonomy (reasoning type × failure type).

## Key claim
LLM reasoning failures can be systematically organized along two complementary axes — reasoning type (embodied vs. non-embodied; informal vs. formal) and failure type (fundamental architectural failures, application-specific limitations, robustness vulnerabilities) — and most documented failures (reversal curse, compositional reasoning gaps, counting, ToM brittleness, anchoring/framing biases, MAS coordination breakdowns) trace to a small set of shared root causes: next-token-prediction objective, Transformer causal masking, RLHF amplification of human biases, and absence of embodied grounding.

## Method
Literature survey + taxonomy construction. Authors aggregate hundreds of prior case studies into a unified 2-axis framework, attach root-cause hypotheses (architecture / training data / alignment process / lack of embodiment) and mitigation families (data-centric, in-processing/adversarial training, post-processing/prompting, retrieval augmentation, context engineering) to each failure mode, and release a companion GitHub index (Awesome-LLM-Reasoning-Failures).

## Result
Catalog of failure modes with representative diagnostic examples: working-memory N-back collapse for n>2; A-not-B inhibitory failures; Wisconsin Card Sorting 25.1% accuracy after rule switch; reversal curse on GPT-style models (absent in BERT); two-hop reasoning degrading to uniform ~1/3 over candidates; composition failure where atomic problems solved individually fail when chained; basic counting errors ("how many a's"); MWP instability under irrelevant context insertion or numeric resampling; ToM accuracy collapse at 3rd-order belief nesting; framing/anchoring/order biases; MAS long-horizon planning, inter-agent misalignment, and termination failures.

## Why it matters here
General background; no direct arena tie. Relevant indirectly to the einstein agent's own design: the failure taxonomy names the exact pitfalls the council-dispatch + wiki-first + triple-verify protocol is meant to counter (anchoring on prior strategy, compositional reasoning across problems, MAS coordination among personas, distraction by irrelevant context), so it is a useful diagnostic lens for cycle-log post-mortems rather than a math-content source.

## Open questions / connections
- Compositional reasoning failure (atomic-solve, composed-fail) is directly relevant to multi-stage optimizer pipelines — does the agent's protocol stage chaining (specialize → execute → look back) inherit the same brittleness?
- Anchoring bias and proactive interference predict that an agent loaded with prior strategy.md will under-explore alternative parameterizations — the cycle-discipline rule's mandatory qmd query is essentially a debias intervention; survey supports this design but offers no quantitative efficacy data.
- MAS termination/verification failures (Pan et al. 2025 examples) parallel the wiki self-improvement loop's "step 5 deliverable" gap — same failure pattern of declaring done without verification.

## Key terms
LLM reasoning failures, reversal curse, compositional reasoning, theory of mind, anchoring bias, framing effect, multi-agent systems, chain-of-thought, RLHF bias amplification, working memory, cognitive flexibility, embodied reasoning, MWP robustness, next-token prediction limitations
