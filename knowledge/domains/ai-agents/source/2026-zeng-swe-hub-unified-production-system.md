<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks
authors: [Yuchen Zeng, Shupeng Li, Daxiang Dong, R. Xu, Zimo Chen, Liwei Zheng, Yuxuan Li, Zhe Zhou, Hao-Dong Zhao, Lun Tian, Hengjia Xiao, Tianshun Zhu, Longkun Hao, Jianmin Wu]
year: 2026
source_url: https://arxiv.org/abs/2603.00575
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks

**Authors:** Yuchen Zeng, Shupeng Li, Daxiang Dong, R. Xu, Zimo Chen, Liwei Zheng, Yuxuan Li, Zhe Zhou, Hao-Dong Zhao, Lun Tian, Hengjia Xiao, Tianshun Zhu, Longkun Hao, Jianmin Wu  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.00575

## One-line
A production "data factory" that converts raw repositories into reproducible, executable software-engineering tasks spanning short-horizon repair to repository-scale construction.

## Key claim
Treating SWE data generation as a modular production stack — a shared execution substrate (pinned containers + standardized verifier entrypoints) plus three task product lines (SWE-Scale, Bug Agent, SWE-Architect) — yields continuously generated, execution-grounded tasks across the full SWE lifecycle, rather than one-off benchmark releases.

## Method
Env Agent + Test Agent automatically containerize heterogeneous repos and standardize test entrypoints/result schemas, producing a reusable execution substrate. SWE-Scale combines tree-sitter-based polyglot code analysis with procedural mutation operators (operator change/flip, operand swap, chain break, branch swap, block drop, method drop, etc.) and Kubernetes-scale stateless validation to mass-produce localized bug-fix instances. Bug Agent generates system-level cross-module regressions via a context–edit–verify loop seeded by call-graph hotspots and pass-to-fail signals, while Issue Agent produces symptom-centric, anti-leakage user reports; SWE-Architect uses coverage-graph scope mining + code hollowing + DOC/API reverse-engineering agents to produce build-a-repo tasks validated against hidden tests.

## Result
A unified task schema $T = (f, R, P_{bug}, P, O, V, M)$ where family $f \in$ {SWE-Scale, Bug Agent, SWE-Architect}, with execution-only success criterion $V(R') = \mathbb{I}[\text{RunTests}(R', E, T_{hidden}) = \text{PASS}]$. The system delivers an architectural integration result rather than a numerical bound: three task families share one verifier interface, enabling Kubernetes-parallel, stateless verification with deterministic replays and leakage-resistant issue prompts. A taxonomy of 13 procedural bug modifiers across operational/control-flow/structural/class-oriented categories is given.

## Key terms
SWE-Hub, data factory, execution substrate, Env Agent, SWE-Scale, Bug Agent, Issue Agent, SWE-Architect, pass-to-fail signal, code hollowing, tree-sitter, Kubernetes-native verification, symptom-cause separation, repository-scale construction
