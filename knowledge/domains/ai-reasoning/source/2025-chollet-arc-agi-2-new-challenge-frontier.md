---
type: source
kind: paper
title: ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems
authors: François Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, H. Pinkard
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.11831
source_local: ../raw/2025-chollet-arc-agi-2-new-challenge-frontier.pdf
topic: general-knowledge
cites:
---

# ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems

**Authors:** François Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, H. Pinkard  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.11831

## One-line
Introduces ARC-AGI-2, an upgraded grid-based reasoning benchmark designed to resist brute-force program search and measure compositional generalization in frontier AI systems.

## Key claim
ARC-AGI-2 is human-solvable (100% of tasks solved by ≥2 non-expert humans; 66% aggregate human attempt success; median 2.2–2.7 min/task) yet frontier models score ≤3.0% on the Semi-Private Eval — a much wider signal bandwidth than ARC-AGI-1 (where o3 reached 76–88%).

## Method
Benchmark construction, not an algorithm: tasks are input-output grid pairs (≤30×30, 10 colors) inferring an unstated rule from 2–5 demonstrations. Curation used large-scale first-party human testing (407 participants, 13,405 attempts) for empirical difficulty calibration, with subsets (Public/Semi-Private/Private Eval) matched within ≤1pp mean human accuracy. Tasks deliberately target multi-rule composition, multi-step sequential dependence, contextual rule application, and in-context symbol definition to defeat exhaustive program search.

## Result
Top models on the Semi-Private set (May 2025): o3-mini High 3.0%, o3 Medium 3.0%, ARChitects 2.5%, o4-mini 2.4%, Icecuber 1.6%, o1-pro Low 0.9%, Claude 3.7 (8K) 0.9% — all below the 5% "meaningful signal" threshold. ARC Prize 2025 offers $700K grand prize for ≥85% on the Private Eval set within a 12-hr / 4×L4 GPU / no-internet Kaggle sandbox.

## Why it matters here
General background; no direct arena tie — ARC-AGI is grid-puzzle inductive reasoning, not numerical optimization. Tangentially informs the agent's design principles: compositional generalization, brute-force resistance, and first-party human calibration are themes relevant to how the Einstein Arena self-improvement loop should evaluate its own progress (signal bandwidth, anti-memorization, cross-cycle compounding).

## Open questions / connections
- Can test-time adaptation (TTA) techniques that broke ARC-AGI-1 (o3, ARChitects) scale to ARC-AGI-2's compositional tasks, or does composition require a different architecture?
- Extends Chollet's "On the Measure of Intelligence" (2019) operationalization of fluid intelligence via core priors.
- Open: what does the cost/accuracy Pareto frontier look like once models cross the 5% meaningful-signal threshold?

## Key terms
ARC-AGI, abstraction and reasoning corpus, fluid intelligence, compositional generalization, program synthesis, test-time adaptation, Chollet, core knowledge priors, in-context symbol definition, brute-force resistance, benchmark calibration, frontier AI reasoning
