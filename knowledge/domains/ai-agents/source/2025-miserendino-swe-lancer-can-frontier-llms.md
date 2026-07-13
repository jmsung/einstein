<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?
authors: [Samuel Miserendino, Michele Wang, Tejal Patwardhan, Johannes Heidecke]
year: 2025
source_url: https://arxiv.org/abs/2502.12115
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?

**Authors:** Samuel Miserendino, Michele Wang, Tejal Patwardhan, Johannes Heidecke  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.12115

## One-line
A benchmark of 1,488 real Upwork freelance software-engineering tasks worth $1M total, graded by end-to-end Playwright tests and proposal-selection ground truth, measuring whether frontier LLMs can earn real money on full-stack engineering work.

## Key claim
Frontier LLMs remain unable to solve the majority of real freelance SWE tasks: best model (Claude 3.5 Sonnet) achieves pass@1 of 26.2% on IC SWE and 44.9% on SWE Manager tasks in the Diamond split, earning $208,050 of $500,800 possible (and >$400K of $1M on the full set).

## Method
Tasks are sourced from the Expensify open-source repository and graded two ways: (i) Individual Contributor (IC) tasks evaluated by triple-verified end-to-end Playwright browser tests rather than unit tests, with an optional "user tool" that simulates user interactions and returns screenshots/traces; (ii) SWE Manager tasks where the model picks the best of 4–5 real freelancer proposals, scored against the engineering manager's historical choice (99% human-agreement validated). Agents run in a Docker container with no internet, pass@1, plus ablations on test-time compute (o1 reasoning effort low/med/high), pass@k ($k\in[1,7]$), and user-tool removal.

## Result
On Diamond IC SWE: GPT-4o 8.0%, o1-high 16.5%, Sonnet 3.5 26.2%; on Diamond SWE Manager: GPT-4o 37.0%, o1-high 41.5%, Sonnet 3.5 44.9%. Higher reasoning effort on o1 raises pass@1 from 9.3% → 16.5% (earnings $16K → $29K) and disproportionately helps expensive tasks; pass@6 with GPT-4o matches pass@1 with o1 (~16.5%). Models localize bugs quickly via keyword search but fail to root-cause across files; using o1+freelancer-fallback would cut total freelance cost by 13.3% (pass@1) or 33.5% (pass@5). Open-source models (Deepseek-R1, Llama 3.3 70B) score ~4–6% on IC SWE under the same scaffold, dominated by instruction-following and user-tool failures.

## Key terms
SWE-Lancer, SWE-Bench, freelance software engineering benchmark, Upwork Expensify, end-to-end Playwright tests, pass@k, test-time compute, reasoning effort, agent scaffold, user tool, Claude 3.5 Sonnet, o1, GPT-4o, manager proposal selection, grader hacking
