<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Harnessing Agentic Evolution
authors: [Jiayi Zhang, Yongfeng Gu]
year: 2026
source_url: https://arxiv.org/abs/2605.13821
drive_file_id: 1i3Sniw2RGBlqfKEDynDkP6kxswCGcR46
text_source: paperclip
ingested_by: agent
---

# Harnessing Agentic Evolution

**Authors:** Jiayi Zhang, Yongfeng Gu, et al.  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2605.13821

## One-line
Formulates LLM-driven iterative optimization ("agentic evolution") as an interactive environment in which a meta-agent edits the *mechanism* that drives future search rather than producing the next candidate itself.

## Key claim
A harnessed meta-editing framework (AEVO) that periodically rewrites the evolution procedure or the agent's operating context outperforms five evolution baselines on Terminal-Bench and ARC-AGI-2 (≈26% relative improvement over the strongest baseline) and reaches state-of-the-art on three open-ended optimization tasks under a fixed iteration budget — notably 1138 cycles on Anthropic's VLIW kernel task within 100 rounds, and matching best-known results on circle_packing_26 ($2.6359$) and autocorrelation_second ($0.9459$).

## Method
Treat the evolution loop as an environment with state $s_r=(r,C_r)$ where $C_r$ accumulates candidates, traces, failures, and costs; a meta-agent $M$ observes $o_r=\Phi(s_r)$ and outputs an edit action $a_r$ that updates the transition mechanism $\Pi_{r+1}=\text{Edit}(\Pi_r,a_r)$. The harness provides a protected evaluator, fixed workspace layout, and a two-phase loop alternating *meta-editing* (revise procedure code / skills / goals / notes / validators) with an *evolution segment* (run $\Pi_r$ for a budgeted number of inner rounds). The same loop is instantiated over (a) explicit procedure code (selection, optimization, feedback summary, update rules) and (b) a general-purpose coding agent's operating context (Claude Code / Codex with Claude-Opus-4.7 or GPT-5.4).

## Result
On Terminal-Bench, AEVO-Procedure reaches 53.8 (Avg@3) vs. 44.3 best baseline (ADAS/DGM/AFlow/SPO/GEPA); on ARC-AGI-2, 47.0 vs. 36.0. On open-ended tasks the agent-mode AEVO ties or beats Codex/Claude-Code/OpenEvolve/HyperAgents on all three objectives while keeping per-round cost low (\$0.32–1.40). The evolved VLIW-kernel harness builds layered durable state — task skill, hypothesis-carrying session goals, a persistent "family map" of architectures tried, replay utilities, and structured session notes — that ratchet a 1774-cycle baseline down to 1138 cycles via an explicit-family port (−597), depth-1 madd selectors (−10), depth-3 reduced-flow selectors (−19), and per-lane alu/xor rebalancing (−8).

## Key terms
agentic evolution, meta-editing, AEVO, harness, evolution-as-environment, procedure-based vs agent-based evolution, AlphaEvolve, OpenEvolve, HyperAgents, AFlow, GEPA, ARC-AGI-2, Terminal-Bench, circle packing 26, autocorrelation inequality, VLIW kernel optimization, persistent family map, mechanism-level intervention, Claude Code, Codex
