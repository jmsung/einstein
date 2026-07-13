<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?"
authors: [Xiang Deng, Jeff Da, Edwin Pan, Yan He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean M. Hendryx, Zifan Wang, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler]
year: 2025
source_url: https://arxiv.org/abs/2509.16941
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

**Authors:** Xiang Deng, Jeff Da, Edwin Pan, Yan He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean M. Hendryx, Zifan Wang, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2509.16941

## One-line
Introduces a contamination-resistant, enterprise-grade SWE-agent benchmark of 1,865 long-horizon multi-file software engineering problems where frontier LLM agents plateau below 45% Pass@1.

## Key claim
Frontier coding agents (Claude Sonnet 4.5, GPT-5 high, Claude Opus 4.1) score only 39.5–43.6% Pass@1 on the public set ($N=731$) and drop to 10.1–17.8% on the commercial set ($N=276$) — a sharp gap vs >70% on SWE-Bench Verified, exposing that current agents fail on multi-file, long-horizon enterprise tasks (mean reference patch: 107.4 LOC across 4.1 files).

## Method
Curates 1,865 issue-resolution tasks from 41 actively maintained repos (11 public GPL-licensed, 12 held-out, 18 commercial-startup), filtering trivial 1–10 line edits and capping 50–100 instances/repo. A three-stage human-in-the-loop pipeline augments each problem with (1) rewritten problem statement, (2) human-authored requirements grounded in unit tests, and (3) explicit interface signatures to suppress false negatives from API-name mismatches; environments are Dockerized per-language with fail2pass/pass2pass test verification. Models are evaluated under the SWE-Agent scaffold (50-turn cap) with GPT-5 LLM-as-judge classifying failure trajectories into 10 buckets.

## Result
Top model Claude Sonnet 4.5: 43.6% public / not reported commercial; Opus 4.1: 17.8% commercial vs 22.7% public (50-turn $2 cap). Ablation removing requirements+interface drops GPT-5 from 25.9% → 8.4% and Opus 4.1 from 22.7% → 8.2%, showing unit-test verifiers are dominated by false negatives without spec scaffolding. Failure-mode analysis: Opus 4.1 fails mostly via wrong-solution (35.9%) + syntax errors (24.2%); Sonnet 4 collapses on context overflow (35.6%) + endless file reading (17%); Qwen3-32B fails on tool-use (42%). Performance degrades sharply past 3 files modified.

## Key terms
SWE-Bench Pro, SWE-Agent, LLM coding agents, benchmark contamination, copyleft licensing, multi-file patches, fail2pass tests, pass2pass tests, Pass@1, LLM-as-a-judge, failure mode taxonomy, long-horizon software engineering
