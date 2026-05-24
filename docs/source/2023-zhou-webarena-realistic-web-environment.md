---
type: source
kind: paper
title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
authors: Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2307.13854
source_local: ../raw/2023-zhou-webarena-realistic-web-environment.pdf
topic: general-knowledge
cites:
---

# WebArena: A Realistic Web Environment for Building Autonomous Agents

**Authors:** Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2307.13854

## One-line
Introduces a self-hosted, reproducible web environment with 812 long-horizon natural-language tasks for benchmarking autonomous LLM agents on realistic browser workflows.

## Key claim
On WebArena, the best GPT-4 ReAct-style agent reaches only $14.41\%$ end-to-end task success vs $78.24\%$ for humans, exposing a large gap in agent capability on long-horizon, multi-page web tasks.

## Method
Builds four Dockerized open-source sites (E-commerce/Magento, Reddit/Postmill, GitLab, Adobe CMS) plus map (OpenStreetMap), Wikipedia, calculator, and scratchpad, populated with data scraped from real counterparts. Frames the environment as a deterministic MDP $\langle S,A,O,T\rangle$ with observation modes (DOM, screenshot, accessibility tree) and a compound keyboard/mouse action space. Evaluates functional correctness via programmatic locators + `exact_match` / `must_include` / `fuzzy_match` (GPT-4-judged) reward functions, not action-sequence surface match.

## Result
Across 812 tasks spanning information-seeking, site navigation, and content/config operations, GPT-4 + CoT + UA-hint gets $14.41\%$ SR; GPT-3.5-16k gets $6.28\%$; humans $78.24\%$. Error analysis identifies failure modes: lack of active exploration, no failure recovery, observation bias (latching onto first plausible info), and neglect of fine-grained observation details (e.g., re-typing already-entered queries). `fuzzy_match` via GPT-4 hits $100\%$ accuracy on date/duration equivalence.

## Why it matters here
General background; no direct arena tie. WebArena is an agent-evaluation benchmark for web navigation, not a math/optimization result — it does not inform sphere packing, autocorrelation, kissing number, or any of the 23 Einstein Arena problems. Possible meta-relevance: its functional-correctness-over-trace-match philosophy mirrors the repo's triple-verify stance (judge outcomes, not surface form).

## Open questions / connections
- How to instill active exploration and failure recovery in LLM agents — the named missing capabilities echo the self-improvement-loop's gap-detect step.
- Programmatic functional-correctness evaluation as a template for arena-style scoring where multiple valid execution paths exist.
- Extension to multi-modal observation (screenshot vs accessibility tree) — relevant only if future arena problems acquire a GUI surface.

## Key terms
WebArena, autonomous agents, LLM agent benchmark, GPT-4, ReAct, accessibility tree, DOM, functional correctness evaluation, fuzzy_match, web navigation, long-horizon tasks, reproducible environment
