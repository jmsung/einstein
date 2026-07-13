<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
authors: [Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, J. Aung, Dane Sherburn, E. Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mkadry]
year: 2024
source_url: https://arxiv.org/abs/2410.07095
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
MLE-bench, AIDE, MLAgentBench, OpenHands, Kaggle benchmark, ML engineering agents, pass@k, scaffold comparison, tree search over solutions, dataset contamination, token familiarity probe, Dolos plagiarism detection, o1-preview, autonomous agent evaluation, cycle discipline
