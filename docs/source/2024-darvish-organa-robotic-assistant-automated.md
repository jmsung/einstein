---
type: source
kind: paper
title: "ORGANA: A Robotic Assistant for Automated Chemistry Experimentation and Characterization"
authors: K. Darvish, Marta Skreta, Yuchi Zhao, Naruki Yoshikawa, Sagnik Som, Miroslav Bogdanovic, Yang Cao, Han Hao, Haoping Xu, Alán Aspuru-Guzik, Animesh Garg, F. Shkurti
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2401.06949
source_local: ../raw/2024-darvish-organa-robotic-assistant-automated.pdf
topic: general-knowledge
cites:
---

# ORGANA: A Robotic Assistant for Automated Chemistry Experimentation and Characterization

**Authors:** K. Darvish, Marta Skreta, Yuchi Zhao, Naruki Yoshikawa, Sagnik Som, Miroslav Bogdanovic, Yang Cao, Han Hao, Haoping Xu, Alán Aspuru-Guzik, Animesh Garg, F. Shkurti  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2401.06949

## One-line
An LLM-driven assistive robotic system that plans, schedules, and executes multi-step chemistry experiments (solubility, recrystallization, pH, electrochemistry) with chemist-in-the-loop interaction and auto-generated reports.

## Key claim
Organa automates the full electrochemistry pipeline for quinone (AQS) characterization — including mechanical electrode polishing — executing a 19-step plan in parallel; user study shows >50% reduction in frustration/physical demand and an average 80.3% time saving for users vs. manual execution.

## Method
Combines LLM-based natural-language reasoning (experiment goal → high-level plan) with an extension of PDDLStream task-and-motion planning that incorporates PDDL2.1-style durative actions (action-start/action-end with agent availability predicates and a time-varying total-cost) to solve TAMP and scheduling jointly, minimizing makespan. Perception uses a ZED Mini camera with neural-depth mode for transparent objects plus AprilTags. Electrochemistry parameter estimation uses MLE via `scipy.optimize.fmin` on a piecewise-linear Pourbaix model $\mu_{eV}(\text{pH})$ with parameters $\theta=(pK_{a1}, pK_{a2}, k, E_\infty, \sigma_{eV})$, plus importance-sampled marginal posteriors under a uniform prior.

## Result
On AQS quinone characterization across pH 4–9, Organa recovered Pourbaix slopes of $-61.3, -61.8, -61.0$ mV/pH (theory: $-59$ mV/pH for pH $< pK_{a1}$) and $pK_{a1}$ estimates of $8.12, 7.86, 8.10$ (literature: $7.68$) across three runs of 6 measurements each. Solubility accuracy was 7.2%/11.2%/12.3% for NaCl/sucrose/alum vs literature. Successfully demonstrated parallel execution of polishing + washing + CV + pH-measurement steps.

## Why it matters here
General background; no direct arena tie. The paper's relevance to Einstein Arena math optimization is essentially nil — it concerns wet-lab robotics, not combinatorial/continuous optimization theory. The only tangentially-transferable element is the durative-action PDDL2.1 + cost-minimization scheduling pattern, which is irrelevant to the agent's current sphere-packing/autocorrelation/extremal-graph problem families.

## Open questions / connections
- The PDDLStream-with-scheduling extension is presented informally; formal completeness/optimality guarantees for joint TAMP+scheduling remain open.
- Importance-sampling posterior estimation under uniform prior is brittle for tight $pK_{a2}$ when data lacks pH > 9 coverage — high variance noted by authors.
- Extends CLAIRify [7] (single-experiment XDL translation) to multi-experiment reasoning with troubleshooting loops; related to ChemCrow and Coscientist LLM-agent paradigms.

## Key terms
self-driving labs, PDDLStream, PDDL2.1 durative actions, task and motion planning, scheduling, LLM agents, electrochemistry automation, cyclic voltammetry, Pourbaix diagram, quinone AQS, maximum likelihood estimation, importance sampling
