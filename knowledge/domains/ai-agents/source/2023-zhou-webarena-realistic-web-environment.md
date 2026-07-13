<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
authors: [Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig]
year: 2023
source_url: https://arxiv.org/abs/2307.13854
drive_file_id: 1SDq4zxssOTvqB5vJrBF6adGfnA33tVtv
text_source: paperclip
ingested_by: agent
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

## Key terms
WebArena, autonomous agents, LLM agent benchmark, GPT-4, ReAct, accessibility tree, DOM, functional correctness evaluation, fuzzy_match, web navigation, long-horizon tasks, reproducible environment
