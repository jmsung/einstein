---
type: source
kind: paper
title: "AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization"
authors: M. Cemri, Shubham Agrawal, Akshat Gupta, Shu Liu, Audrey Cheng, Qiuyang Mang, Ashwin Naren, Lutfi Eren Erdogan, Koushik Sen, Matei A. Zaharia, Alexandros G. Dimakis, Ion Stoica
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2602.20133
source_local: ../raw/2026-cemri-adaevolve-adaptive-llm-driven.pdf
topic: general-knowledge
cites:
---

# AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization

**Authors:** M. Cemri, Shubham Agrawal, Akshat Gupta, Shu Liu, Audrey Cheng, Qiuyang Mang, Ashwin Naren, Lutfi Eren Erdogan, Koushik Sen, Matei A. Zaharia, Alexandros G. Dimakis, Ion Stoica  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2602.20133

## One-line
A hierarchical adaptive controller for LLM-guided evolutionary program search that uses an Adam-like "accumulated improvement signal" to dynamically modulate exploration intensity, route compute across islands, and inject meta-level solution tactics when stagnated.

## Key claim
On Circle Packing $N=26$, AdaEvolve reaches sum-of-radii $2.636$, surpassing the prior Human SOTA ($2.634$) and AlphaEvolve ($2.635$); on Circle Packing rectangle $N=21$ it reaches $2.36583237$ vs AlphaEvolve's $2.36583213$; it improves over open-source baselines (OpenEvolve, GEPA, ShinkaEvolve) across 185 problems including 6 math optimization, 7 ADRS systems, 172 Frontier-CS, with identical hyperparameters.

## Method
Treats LLM-driven evolution as zeroth-order adaptive optimization with three coupled levels driven by a single signal $G_t^{(k)} = \rho G_{t-1}^{(k)} + (1-\rho)(\delta_t^{(k)})^2$ (EMA of squared normalized improvements, Adam/RMSProp analogue). **L1 Local:** within-island exploration probability $I_t^{(k)} = I_{\min} + (I_{\max}-I_{\min})/(1+G_t^{(k)}+\epsilon)$, with $I_{\min}=0.1$, $I_{\max}=0.7$. **L2 Global:** UCB bandit over islands with rewards normalized by *global* best $f^*_{\text{global}}$ (not local best) to kill "poor-island bias," plus decayed reward/visit counts and dynamic island spawning when $G_t^{(k)} \le \tau_S = 0.02$ for all $k$. **L3 Meta:** when $G_t^{(k)} \le \tau_M = 0.12$ globally, a separate LLM analyzes the evaluator + best program + failed tactics and injects high-level "breakthrough idea" tactics (e.g., switch to SLSQP, Savitzky–Golay, Voronoi init) into mutation prompts.

## Result
Circle Packing (Square, $N=26$): $2.636$ best with both GPT-5 and Gemini-3-Pro (matches/exceeds AlphaEvolve $2.635$, Human $2.634$). Circle Packing (Rect, $N=21$): $2.366$. Heilbronn triangle/convex ($N=11$, $N=13$): $0.036$ / $0.029$ (matches or beats AlphaEvolve $0.0365$ / $0.0309$). MinMax Distance $N=3$: $0.2404$ (beats AlphaEvolve $0.2398$). ADRS: human-competitive or superior on 6/7. Ablations on Circle Packing: removing Meta-Guidance drops to $2.521$ (largest single contributor); removing local adaptation to $2.591$; fixed 2/5 islands underperform dynamic spawning. Stagnation case studies show Meta-Guidance injecting SLSQP refinement at iter 15 breaks a $2.541$ plateau, then exploitation drives convergence to $2.636$ at iter 65.

## Why it matters here
Direct relevance: **Circle Packing $N=26$ is structurally identical to Einstein Arena packing-family problems**, and AdaEvolve's $2.636$ is a *new SOTA reference value* for that geometry — worth verifying against this repo's own packing benchmarks. More structurally, this paper formalizes the *exact* loop einstein already runs (council dispatch → exploration → stagnation → meta-guidance → look-back); the EMA-of-squared-improvement signal is a directly portable "am I stagnating?" metric for our autonomous loop, and the global-vs-local reward normalization is a concrete fix for the bias toward problems with poor baseline scores.

## Open questions / connections
- The $G_t^{(k)} = \rho G_{t-1}^{(k)} + (1-\rho)\delta_t^2$ signal is a candidate replacement for our current ad-hoc "stagnated" heuristics in the autonomous-loop cycle_runner — does an Adam-style EMA outperform fixed-window checks on our problems?
- "Poor-island bias" via local normalization is the same trap as comparing problem-relative deltas across our 23 problems with very different score scales — global normalization by $f^*_{\text{global}}$ is the analogue to per-problem SOTA-relative scoring.
- Meta-Guidance generation = automated council dispatch with explicit "name concrete libraries/functions" prompt structure (Stage 1–6 in §A.2); compare to our persona-based question generation.
- Their Circle Packing $N=26$ trajectory ($0.96 \to 2.439$ at iter 1 from a random dense layout, then SLSQP breakthrough) is a recipe to triple-verify against our P1/packing pipeline.
- ARC-AGI-2 result ($49\%$ GPT-5, $50\%$ Gemini-3-Pro) suggests the adaptive controller generalizes beyond optimization to discrete reasoning — relevant to combinatorial/Sidon-set problems.

## Key terms
LLM-guided evolutionary search, zeroth-order optimization, adaptive optimizer, exponential moving average, Adam analogue, multi-armed bandit, UCB, island model, parent selection, exploration-exploitation, meta-prompting, circle packing N=26, Heilbronn triangle, SLSQP, Savitzky-Golay, AlphaEvolve, OpenEvolve, ShinkaEvolve, GEPA, stagnation detection, global normalization, dynamic island spawning, solution tactics, program synthesis, inference-time search
