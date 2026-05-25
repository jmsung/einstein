---
type: source
kind: paper
title: "Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics"
authors: Haodong Feng, Lugang Ye, Dixia Fan
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2512.04716
source_local: ../raw/2025-feng-towards-fluid-scientist-llm-powered.pdf
topic: general-knowledge
cites:
---

# Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics

**Authors:** Haodong Feng, Lugang Ye, Dixia Fan  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.04716

## One-line
An end-to-end multi-agent LLM system that autonomously runs physical fluid-mechanics experiments (hypothesis → robotic execution → data analysis → manuscript) on a computer-controlled water tunnel studying vortex- and wake-induced vibration of tandem cylinders.

## Key claim
With human-in-the-loop, the LLM-driven framework reproduced classical VIV/WIV benchmarks (frequency lock-in within 4%; 27× amplitude enhancement at critical spacing $L/D=4$) and discovered a previously unreported universal anti-resonance frequency $f_\text{opt}=1.37 f_n$ yielding up to $-77.5\%$ amplitude suppression; a 3-unit tanh neural-network fit ($R^2=0.796$) outperformed a physics-decomposed analytical formula ($R^2\approx 0.43$) by 31% in fitting accuracy (83% in explained variance).

## Method
An automated circulating water tunnel with programmatic control of velocity, cylinder position, forcing frequency/amplitude is driven by six specialized LLM agents (hypothesis, experiment, hardware, analysis, evaluation, manuscript) using Claude Sonnet 4.5 and Qwen-Plus. Two modes: human-in-the-loop (expert selects hypotheses and validates) and fully autonomous virtual-real interaction. Formula discovery proceeded by trying mechanistic Gaussian-envelope decompositions, then polynomial/rational forms, finally settling on a 3-hidden-unit $\tanh$ network optimized via L-BFGS-B over 148 configurations.

## Result
122 active-WIV experiments across 4 adaptive rounds reduced a >3000-config search space to a quantitative model with three governing equations: anti-resonance $f_\text{opt}=1.37 f_n$ (spacing-invariant), subharmonic transition boundary $U_{r,\text{crit}}=13.0-0.12 A_f$, and spacing scaling $\text{Enh}(L/D)=\text{Enh}(4)\cdot\sqrt{4/(L/D)}$. Discovered a "fate-bifurcation" at $L/D=5$ with critical $\text{Re}\approx 9500$ where amplitude collapses 21%. Neural-net surrogate: $R^2=0.796$, MAE $=0.106$, RMSE $=0.138$.

## Why it matters here
General background; no direct arena tie — this is fluid-mechanics LLM-agent infrastructure, not a math-optimization paper. The methodological lesson relevant to the Einstein Arena loop is the adaptive-resolution hypothesis-driven campaign (3000 → 122 trials via coarse-to-fine refinement) and the empirical finding that NN surrogates beat mechanistic decompositions on strongly nonlinear response surfaces — a cautionary data point for any "fit a physical formula" step in problems like P14/P17 where evaluator surfaces are nonlinearly coupled.

## Open questions / connections
- Does the adaptive 4-stage coarse-to-fine campaign template generalize as a meta-protocol for arena problems (cf. council-dispatch + gap-detect)?
- When should the agent abandon mechanistic parameterization and switch to a tanh-network surrogate? The paper's pivot trigger ($R^2$ stuck at 0.43 after augmentation) is a candidate heuristic.
- Extends Khalak & Williamson (1999), Assi et al. (2010, 2013); leaves open high-Re ($>10^5$), 3D effects, and phase control.

## Key terms
vortex-induced vibration, wake-induced vibration, fluid-structure interaction, tandem cylinders, anti-resonance, lock-in frequency, LLM multi-agent system, autonomous experimentation, neural network surrogate, hyperbolic tangent activation, L-BFGS-B, hypothesis-driven search, Reynolds number transition, subharmonic resonance, Khalak-Williamson, Assi
