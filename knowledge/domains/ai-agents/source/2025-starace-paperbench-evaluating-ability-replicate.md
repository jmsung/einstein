<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: PaperBench: Evaluating AI's Ability to Replicate AI Research
authors: [Giulio Starace, Oliver Jaffe, Dane Sherburn, J. Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, E. Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan]
year: 2025
source_url: https://arxiv.org/abs/2504.01848
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# PaperBench: Evaluating AI's Ability to Replicate AI Research

**Authors:** Giulio Starace, Oliver Jaffe, Dane Sherburn, J. Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, E. Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.01848

## One-line
A benchmark measuring whether AI agents can replicate 20 ICML 2024 Spotlight/Oral papers from scratch — coding, executing, and matching reported empirical results — graded against author-co-developed hierarchical rubrics by an LLM judge.

## Key claim
Frontier agents show non-trivial but limited paper-replication ability: Claude 3.5 Sonnet (New) with simple scaffolding scores $21.0\%$ average Replication Score; on a 3-paper subset, ML PhDs (best-of-3, 48h) reach $41.4\%$ vs $26.6\%$ for o1, so models do not yet beat the human baseline. The o3-mini-high LLM judge attains $F_1 = 0.83$ on JudgeEval.

## Method
Each of 20 papers ships with a tree-structured rubric (8,316 leaf nodes total) co-authored with original authors; leaves are typed Code Development / Execution / Result Match and weighted, with the root score being a weighted-average rollup. Agents run in an Ubuntu+A10-GPU container with internet (author repos blacklisted), produce a `reproduce.sh`, and are graded by SimpleJudge (LLM ranks top-10 relevant files, then binary-grades each leaf with paper + addendum in context). A lightweight variant, PaperBench Code-Dev, drops the reproduction step and grades only code nodes.

## Result
Average Replication Scores (BasicAgent, 3 seeds): Claude 3.5 Sonnet $21.0 \pm 0.8\%$, o1-high $13.2 \pm 0.3\%$, R1 $6.0\%$, GPT-4o $4.1\%$, Gemini 2.0 Flash $3.2\%$, o3-mini-high $2.6\%$. IterativeAgent scaffolding (no early-stop, piecemeal prompts) lifts o1 to $24.4\%$ (12h) and $26.0\%$ (36h) and o3-mini to $8.5\%$, but *hurts* Claude ($16.1\%$). On Code-Dev, o1 reaches $43.4\%$. Models score well on Code Development leaves but collapse on Execution / Result Match — they write code but fail to integrate, run, and debug it across long horizons.

## Key terms
PaperBench, paper replication, LLM judge, JudgeEval, hierarchical rubric, agent scaffolding, BasicAgent, IterativeAgent, long-horizon agents, Claude 3.5 Sonnet, o1, o3-mini, ML R&D evaluation, autonomous agents
