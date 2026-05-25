---
type: source
kind: paper
title: Code as Agent Harness
authors: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2605.18747
source_local: ../raw/2026-ning-code-as-agent-harness.pdf
topic: agentic-harness
cites: 
---

# Code as Agent Harness

**Authors:** Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2605.18747

## One-line
A survey reframing code as the operational substrate ("harness") of LLM agents — the executable, inspectable, stateful medium through which agents reason, act, model environments, and verify progress.

## Key claim
Reliable long-horizon agent autonomy depends less on raw model reasoning and more on the surrounding *harness* — and code is the right medium for that harness because it is simultaneously executable (outputs become verifiable operations), inspectable (intermediate traces are structured), and stateful (program state persists across steps). The authors organize the field into three layers: harness interface (code for reasoning / acting / environment modeling), harness mechanisms (planning, memory, tool use, control, optimization), and scaling to multi-agent orchestration over shared code artifacts.

## Method
Literature survey (no theorem). Taxonomy is constructed by distinguishing three coupled elements of agent systems — model-internal capabilities, system-provided harness infrastructure, and *agent-initiated code artifacts* (regression tests, temporary tools, DSL programs, executable workflows, reusable skills, intermediate program states) — and organizing ~480 references around how those artifacts mediate reasoning, action, and environment state. Five application domains (coding assistants, GUI/OS, embodied, scientific discovery, personalization) are used as cross-cuts.

## Result
No numerical bound. Establishes a vocabulary and roadmap: harness interface (§2) → harness mechanisms (§3) → multi-agent scaling (§4) → open problems (§5). Open problems explicitly named: evaluation beyond final task success, semantic verification under incomplete feedback, regression-free self-evolving harnesses, transactional shared program state with semantic conflict resolution, human-in-the-loop safety as harness state, multimodal code-harness systems, and a "science of harness engineering."

## Why it matters here
Direct tie to this repo's autonomous-loop branch: this paper *names* what the einstein agent's `.claude/rules/`, cycle-log, wiki-first protocol, council dispatch, and `mb/` tracking actually are — an agent harness, with code (rules, scripts, distillations, cycle logs) as its substrate. Useful as a vocabulary anchor for the self-improvement-loop and cycle-discipline rules; the "evolution agent" and "governed harness mutation" sections (§3.5) map onto how this repo lets the agent author wiki pages under attribution. No math content for the 23 arena problems themselves.

## Open questions / connections
- Harness-level evaluation: how to measure self-improvement beyond per-cycle task success — relevant to `docs/agent/cycle-log.md` and `metrics.md`.
- Regression-free harness evolution: when the agent edits its own rules / skills, how to prevent silent capability loss — relevant to any future `/agent-reflect` that mutates `.claude/rules/`.
- Semantic verification under incomplete oracles: matches the project's triple-verify axiom (arena verifier is opaque/expensive) and P9/P14/P17 verifier-drift findings.
- Shared program state across multi-agent runs: relevant if council dispatch ever moves from "each persona writes a question" to "personas share a workspace."

## Key terms
agent harness, code as substrate, agent-initiated code artifacts, harness interface, harness mechanisms, multi-agent orchestration, executable reasoning, program-aided reasoning, tool use, memory engineering, sandboxed execution, self-evolving harness, verification under incomplete feedback, cycle discipline, Claude Code, Codex
