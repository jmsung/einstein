---
type: source
kind: paper
title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
authors: Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, J. Aung, Dane Sherburn, E. Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mkadry
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.07095
source_local: ../raw/2024-chan-mle-bench-evaluating-machine-learning.pdf
topic: general-knowledge
cites:
---

# MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

**Authors:** Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, J. Aung, Dane Sherburn, E. Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mkadry  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.07095

## One-line
Introduces a 75-competition Kaggle-based benchmark that measures whether AI agents can autonomously perform real-world ML engineering, with human-leaderboard-anchored medal scoring.

## Key claim
The best agent evaluated — OpenAI's o1-preview with the AIDE scaffold — earns at least a Kaggle bronze medal in $16.9\%$ of competitions at pass@1, rising to $34.1\%$ at pass@8; GPT-4o (AIDE) scores $8.7\%$ in 24h and $11.8\%$ in 100h.

## Method
Curate 75 Kaggle competitions (22 Low / 38 Medium / 15 High complexity) from 5673 candidates, reconstructing train/test splits so that local grading is comparable to the original Private leaderboard; assign bronze/silver/gold by Kaggle's team-count-dependent thresholds. Agents run in a Docker sandbox (36 vCPU, 440 GB RAM, 1× A10 GPU, 24 h) under three scaffolds — AIDE (Kaggle-specific tree search over solutions), MLAgentBench (MLAB), and OpenHands — with a local validation server, GPT-4o-based rule-breaking detector, and the Dolos plagiarism checker (>60% similarity threshold). Contamination is probed via token-level familiarity (mean per-token probability under the base model) and via manually obfuscated competition descriptions.

## Result
AIDE dominates general-purpose scaffolds (GPT-4o: $8.7\%$ vs MLAB $0.8\%$, OpenHands $4.4\%$). Doubling GPUs barely moves the score (8.7 → 10.2%), and a CPU-only run still hits $9.1\%$ — agents fail to adapt strategy to hardware. Familiarity vs performance shows Pearson $r=-0.24$ ($p=0.04$, i.e. slightly *negative*), and obfuscated descriptions score $8.4\%$ vs $8.5\%$ original — no detectable contamination uplift. Failure modes: agents rarely use the validation server, MLAB/OpenHands often terminate early, all agents ignore disk/RAM/time budgets, and medal rates collapse on post-2022 competitions.

## Why it matters here
General background; no direct arena tie — MLE-bench is an ML-engineering agent benchmark, not a math-optimization one. Closest relevance is methodological: it is a sibling to the autonomous-loop infrastructure being built in `cb-feat-autonomous-loop/` and offers a concrete template for scaffold comparison (AIDE tree search vs ReAct-style MLAB vs OpenHands), pass@k scaling curves, contamination probes (token familiarity, description obfuscation), and the *cherry-picking-forbidden* discipline already encoded in this repo's `cycle-discipline.md`.

## Open questions / connections
- Does an AIDE-style tree search over candidate optimizer configurations transfer from Kaggle ML pipelines to Einstein Arena math-optimization runs (basin hops, Remez exchanges, LP relaxations)?
- Why does extra compute (2× GPU, 100 h) yield only marginal gains — is the ceiling scaffold quality (failure to iterate / debug) rather than raw compute, mirroring the project's "hammer the optimizer harder ≠ progress" anti-pattern?
- The Dolos + log-inspection rule-breaking detector is a direct analogue to a needed audit tool for the autonomous-loop council dispatch: how to verify that persona subagents actually consult the wiki rather than re-derive from training?
- The token-familiarity test (Carlini-style) is a cheap contamination probe — could be applied to detect whether the LLM-distill step has memorized arxiv math sources verbatim.

## Key terms
MLE-bench, AIDE, MLAgentBench, OpenHands, Kaggle benchmark, ML engineering agents, pass@k, scaffold comparison, tree search over solutions, dataset contamination, token familiarity probe, Dolos plagiarism detection, o1-preview, autonomous agent evaluation, cycle discipline
