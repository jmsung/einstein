<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems"
authors: [Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Yuanchen Bei, Zihao Li, Jiaru Zou, Lingming Zhang, Yinglong Xia, Tong Zhang, Hanghang Tong, Jingrui He]
year: 2026
doi: null
source_url: https://arxiv.org/abs/2605.18747
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems

## TL;DR
A survey (literature through 2026) reframing **code** from a generated artifact into the *operational substrate* of agentic AI — the executable, inspectable, and stateful medium through which agents reason, act, model their environment, and coordinate. It organizes the field into three layers (harness interface → harness mechanisms → scaling to multi-agent) and ends with an open-problems agenda for "harness engineering."

## Key findings
- **Three-element decomposition of agentic systems**: (1) *model-internal capabilities* (reasoning, planning, evaluation), (2) *system-provided harness infrastructure* (tools, APIs, sandboxes, memory, validators, permission tiers, telemetry), and (3) the underexplored *agent-initiated code artifacts* (regression tests, temporary tools, DSL programs, reusable skills, intermediate program states) that agents create/execute/persist/share in the task loop. The survey's novel focus is (3).
- **Why code, specifically**: code is *executable* (outputs become verifiable operations), *inspectable* (intermediate computation exposed as structured traces), and *stateful* (the evolving program persists task progress across steps). These three properties are what make code function as a harness interface, not just a notation.
- **Layer 1 — Harness Interface (§2)**: code-for-reasoning (PoT, PAL, Chain-of-Code; formal/symbolic via Lean/Isabelle/Coq and theorem-provers; iterative generate–execute–verify–refine loops with RL on execution feedback, e.g. CodeRL, RLEF); code-for-acting (SayCan grounded skills, Code-as-Policies, Voyager lifelong skill libraries, GUI/robot policies); code-for-environment (structured world reps, execution-trace world models like CWM/WorldCoder, code-grounded eval envs SWE-bench/InterCode/AgentBench, and *verifiable environment construction* SWE-smith/EnvScaler).
- **Layer 2 — Harness Mechanisms (§3)**: planning (linear decomposition → structure-grounded → search-based → orchestration; note PLAN.md/AGENTS.md as filesystem-backed control objects), memory (working/semantic/experiential/long-term/multi-agent + context compaction & state offloading), tool use (function / environment-interaction / verification-driven / workflow-orchestration), and the **Plan-Execute-Verify (PEV) control loop** with sandboxed execution, multi-tier permissions (read-only / sandbox-edit / full-access + HITL gates), and deterministic sensors (linters, tests, type checkers, fuzzers).
- **Agentic Harness Engineering (§3.5)**: treats the harness itself as the object of optimization via *deep telemetry* → an *Evolution Agent* (observe → diagnose → propose → evaluate → promote) → *governed harness mutation* (every change carries a "change contract"; risky edits require HITL). Cites AutoHarness, Meta-Harness, GEPA, EvoMAC.
- **Layer 3 — Scaling (§4)**: role specialization (planner/coder/reviewer/tester/executor), interaction modes (collaborative synthesis, critique-and-repair [dominant], adversarial validation/fuzzing, reasoning debate), workflow topologies (chain/cyclic/hierarchical/star vs. adaptive: dynamic pool scaling, feedback-driven DAG restructuring, runtime self-reorganization). Position: a **shared code-centric harness substrate** with transactional state; SyncMind is highlighted as the only system formally defining ground-truth state Sₖ vs. agent belief Bₖ.

## Methods (brief)
Survey/taxonomy paper (no experiments). Synthesizes ~470 cited works into three connected layers plus five application domains, with comparison tables (reasoning/action/environment systems, planning modules, memory, tool-use, PEV control, MAS designs). Accompanied by a curated GitHub paper list.

## Limitations
A survey: no empirical contribution, no head-to-head evaluation. The authors repeatedly flag that reported "gains" (from planning, memory, etc.) are entangled with harness quality, oracle adequacy, and benchmark contamination — i.e. many cited claims are not isolated to the mechanism studied. Coverage is concentrated on software-engineering/coding agents; biology/embodied/personalization domains are surveyed more thinly.

## Citations of interest
- SWE-bench (Jimenez et al. 2023) — repository-level executable evaluation; recurring benchmark anchor.
- Voyager (Wang et al. 2023) — lifelong executable skill library in Minecraft; the canonical code-as-memory exemplar.
- ReAct (Yao et al. 2023) — interleaved thought/action/observation; lightweight precursor of linear-decomposition planning.
- ChatDev / MetaGPT / AgentCoder — foundational role-specialized multi-agent coding systems (waterfall/cyclic topologies, critique-and-repair).
- Virtual Lab (Swanson et al. 2025, *Nature*) — LLM PI + scientist agents composing ESM/AlphaFold-Multimer/Rosetta to design validated nanobodies.
- Biomni (Huang et al. 2025) — general biomedical AI agent mining bioRxiv to build a 25-subfield tool registry; molecular-cloning protocols rated comparable to a senior postdoc.
- Meta-Harness (Lee et al. 2026) & AutoHarness (Lou et al. 2026) — formalize/automate harness design as an optimization/synthesis problem.
