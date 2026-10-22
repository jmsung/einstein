---
type: source
kind: paper
title: "CiteME: Can Language Models Accurately Cite Scientific Claims?"
authors: O. Press, Andreas Hochlehnert, Ameya Prabhu, Vishaal Udandarao, Ofir Press, Matthias Bethge
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2407.12861
source_local: ../raw/2024-press-citeme-can-language-models.pdf
topic: general-knowledge
cites:
---

# CiteME: Can Language Models Accurately Cite Scientific Claims?

**Authors:** O. Press, Andreas Hochlehnert, Ameya Prabhu, Vishaal Udandarao, Ofir Press, Matthias Bethge  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.12861

## One-line
A human-curated benchmark of 130 unambiguous citation-attribution excerpts from recent ML papers, plus an LM agent (CiteAgent) that searches and reads papers to identify the cited work.

## Key claim
Frontier LMs achieve only $4.2$–$18.5\%$ accuracy on open-ended citation attribution vs $69.7\%$ for humans; equipping GPT-4o with search+read tools (CiteAgent) raises accuracy to $35.3\%$, and o1-preview reaches $61.3\%$ (though $\sim 38.7\%$ appears memorized).

## Method
Manually curated 130 single-citation excerpts from ML papers, filtered to remove instances GPT-4o could answer without tools. Built CiteAgent: a ReAct-style LM agent with three commands — `search(query, sort)` over Semantic Scholar (218M papers), `read(ID)` for full PDF text via PyPDF2, and `select(ID)` — capped at 15 actions per sample. Ablated across GPT-4o, Claude 3 Opus, LLaMA-3-70B, Claude 3.5 Sonnet, o1-mini, o1-preview, with/without demonstration trajectory, and across command subsets.

## Result
SPECTER and SPECTER2 retrieval baselines score $0\%$. Without tools, GPT-4o is $0\%$ by construction (filtered); Claude 3 Opus reaches $18.5\%$. With search+read+demo: GPT-4o $35.3\%$, Claude 3.5 Sonnet $40.3\%$, o1-preview $61.3\%$. Error analysis: $50\%$ misunderstand the excerpt, $32\%$ stop at a near-match paper, $18\%$ select the citing paper instead of the target. Performance drops on 2024 papers vs pre-2024 (e.g., GPT-4o $37.0\% \to 32.6\%$).

## Why it matters here
General background; no direct arena tie — the paper is about LM citation attribution, not math optimization. Tangentially relevant to the self-improvement loop's citation hygiene (every finding cites a `source/` entry) and to how the autonomous-loop agent might verify its own claims against ingested literature, but no concept/technique informs sphere packing, kissing numbers, autocorrelation, or any L0–L2 problem.

## Open questions / connections
- Can a smaller, focused retrieval index (the einstein wiki itself) make agent-style citation lookup more reliable than open-web Semantic Scholar?
- The o1-preview memorization confound ($38.7\%$ without tools) mirrors a concern for wiki-first-lookup: how much "knowledge" is memorized vs genuinely retrieved?
- Concurrent retrieval benchmarks: Ajith et al. (2024) on discoveries in ML papers; Bamboogle, GPQA as small-N benchmark precedents.

## Key terms
citation attribution, retrieval-augmented LM, CiteAgent, Semantic Scholar, SPECTER, SPECTER2, ReAct agent, benchmark curation, GPT-4o, Claude 3 Opus, hallucination, claim verification, paper discovery, LM-as-research-assistant
