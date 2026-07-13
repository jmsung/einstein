<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval]
title: "ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers"
authors: [Hannah Lin, Martin Maas, Maximilian Roquemore, Arman Hasanzadeh, Fred Lewis, Yusuf Simonson, Tzu-Wei Yang, Amir Yazdanbakhsh, Deniz Altinbüken, Florin Papa, Maggie Nolan Edmonds, Aditya Patil, Don Schwarz, Satish Chandra, Chris Kennelly, Milad Hashemi, Parthasarathy Ranganathan]
year: 2025
source_url: https://arxiv.org/abs/2503.15669
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers

**Authors:** Hannah Lin, Martin Maas, Maximilian Roquemore, Arman Hasanzadeh, Fred Lewis, Yusuf Simonson, Tzu-Wei Yang, Amir Yazdanbakhsh, Deniz Altinbüken, Florin Papa, Maggie Nolan Edmonds, Aditya Patil, Don Schwarz, Satish Chandra, Chris Kennelly, Milad Hashemi, Parthasarathy Ranganathan  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.15669

## One-line
A production system at Google that mines historical commits to build a dictionary of performance anti-patterns, then uses vector-similarity search + a fine-tuned LLM to auto-refactor code across billions of lines, with human code review as the gate.

## Key claim
Over the past year ECO has submitted >6.4k commits / >25k changed lines into Google's production fleet with a >99.5% production success rate, yielding >2M normalized-core savings (~500k normalized cores/quarter).

## Method
Three-stage pipeline: (1) mine ~55k performance-improving historical commits via keyword + curated-source filtering to build an anti-pattern database (categories: Alloc/Args/Copy/Map/Move/Sort/Vector); (2) localize new opportunities via deep-code-embedding nearest-neighbor search over a Clang-parsed function IR annotated with Google-Wide-Profiling CPU/cycle counts, pruning shared/low-cost subtrees ($C_{\min}=0.1\%$, $C_{\max}=25\%$); (3) apply edits with a fine-tuned Gemini Pro 1.0, sampled across zero-shot / few-shot / CoT / ReAct prompts, then validated (compile + tests + LLM self-debug), human-reviewed, and post-submit-monitored via the fleet profiler.

## Result
Deep-code-embedding retrieval on code diffs achieves MAP@5 = 0.5362 vs 0.0728 for bag-of-words, a >7× retrieval improvement. On 48 held-out production commits, zero-shot ($CodeBLEU=0.967$, quality 0.531) and ReAct (0.969, 0.510) beat CoT (0.954, 0.344); CoT produces larger but less-accurate edits. Production submission rates differ by anti-pattern (Copy ~40% submitted, Map ~5%, Vector ~41%), and Vector edits show highest savings-per-line.

## Key terms
LLM code optimization, performance anti-patterns, vector similarity search, ScaNN, deep code embeddings, retrieval-augmented refactoring, Gemini fine-tuning, ReAct prompting, chain-of-thought, CodeBLEU, Google-Wide Profiling, warehouse-scale computing
