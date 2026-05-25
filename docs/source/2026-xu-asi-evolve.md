---
type: source
kind: paper
title: ASI-Evolve: AI Accelerates AI
authors: Weixian Xu, Tiantian Mi, et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.29640
source_local: ../raw/2026-xu-asi-evolve.pdf
topic: agentic-harness
cites: 
---

# ASI-Evolve: AI Accelerates AI

**Authors:** Weixian Xu, Tiantian Mi, et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.29640

## One-line
An agentic evolution framework that closes a learn–design–experiment–analyze loop to autonomously discover better neural architectures, pretraining-data pipelines, and RL algorithms, with side experiments on circle packing and drug-target prediction.

## Key claim
ASI-EVOLVE delivers concrete gains across three AI-development pillars (architecture: +0.97 over DeltaNet, ~3× the human Mamba2 gain; data curation: +3.96 avg, >+18 on MMLU; RL algorithm: +12.5 on AMC32, +11.67 on AIME24, +5.04 on OlympiadBench vs GRPO) and reaches SOTA on circle packing $n=26$ ($\sum r_i \approx 2.635$) in as few as 17 rounds.

## Method
Evolutionary LLM-agent loop with two distinguishing components: (1) a **Cognition Base** — an embedding-indexed store of ~150 textual priors mined from domain papers, retrieved per round via semantic search over sampled parent nodes' motivations/analyses; (2) an **Analyzer** that ingests full experimental logs and distills them into compact, decision-oriented reports persisted to the database. Sampling policies (UCB1, greedy, random, MAP-Elites islands) plug behind a unified interface; full-file or diff-edit code generation, static/debug/novelty filter agents, and multi-stage (20M → 340M → 1.3B) fitness evaluation manage cost.

## Result
On circle packing $n=26$ in the unit square, the system reaches the AlphaEvolve target $\sum r_i \approx 2.635$ in ~17 rounds, faster than OpenEvolve and GEPA under aligned configs. Architecture run: 1,350 candidates over 1,773 rounds, 105 beat DeltaNet; best model 57.28% avg vs 55.76% (dev) and 45.40% vs 44.74% (OOD). DTI transfer (DrugBAN seed): +6.94 AUROC on unseen drugs, +4.36 doubly-cold-start, via Sinkhorn (optimal-transport) attention + domain marginalization + top-k sparse gating.

## Why it matters here
Direct arena tie via the circle-packing benchmark — the cognition-base recipe (geometric priors: HCP density $\pi/(2\sqrt{3})$, corner radius bound $\tfrac{\sqrt{2}}{2}$, variable radii; SLSQP + multi-start + DE polish; $\epsilon=10^{-8}$ slack) is a templated playbook for einstein's packing problems (P1, P11) and a reference for how to structure the self-improvement loop's cognition/analyzer split. The "evolve cognition, not just solutions" framing maps onto einstein's wiki-first + analyzer-finding loop.

## Open questions / connections
- Does the cognition base saturate or keep helping past the cold-start regime? Ablation shows "No Cognition" eventually catches up — what's the asymptotic gap?
- Sampling-policy sensitivity (UCB1 vs MAP-Elites island) drives long-horizon trajectories — which fits einstein's per-problem geometry best?
- Extends AlphaEvolve / OpenEvolve / GEPA / ShinkaEvolve; leaves open whether multi-objective fitness (loss + benchmark + judge) generalizes to triple-verify-style ground-truth checks.
- Can the Analyzer's "distill logs into reusable insight" pattern replace or augment einstein's `failure-is-a-finding` dead-end notes?

## Key terms
agentic evolution, cognition base, analyzer, MAP-Elites, UCB1, circle packing, AlphaEvolve, OpenEvolve, GEPA, DeltaNet, linear attention, Sinkhorn attention, optimal transport, drug-target interaction, SLSQP multi-start, hexagonal close packing, self-improvement loop, neural architecture search
