---
type: source
kind: paper
title: The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity
authors: P. Shojaee, Iman Mirzadeh, Keivan Alizadeh-Vahid, Maxwell Horton, Samy Bengio, Mehrdad Farajtabar
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2506.06941
source_local: ../raw/2025-shojaee-illusion-thinking-understanding-strengths.pdf
topic: general-knowledge
cites:
---

# The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity

**Authors:** P. Shojaee, Iman Mirzadeh, Keivan Alizadeh-Vahid, Maxwell Horton, Samy Bengio, Mehrdad Farajtabar  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.06941

## One-line
Empirical study showing that Large Reasoning Models (LRMs) collapse to near-zero accuracy beyond problem-specific complexity thresholds and counterintuitively *reduce* thinking effort near collapse, despite ample token budget.

## Key claim
Across four controllable puzzles (Tower of Hanoi, Checker Jumping, River Crossing, Blocks World), frontier LRMs (Claude-3.7-Sonnet-Thinking, DeepSeek-R1, o3-mini, QwQ-32B) exhibit three regimes vs. complexity: (1) non-thinking models win on simple problems, (2) thinking helps at medium complexity, (3) both collapse to ~0% at high complexity — and LRM thinking-token usage *decreases* past the collapse point even though models stay well below the 64k context limit.

## Method
Controlled puzzle environments with simulator-based verification of both final answers and intermediate move sequences in CoT traces. Complexity is varied by problem size $N$ (disks, checkers, blocks, actor/agent pairs); 25 samples/instance; matched thinking vs. non-thinking model pairs (Claude-3.7 w/wo thinking, DeepSeek-R1 vs V3, QwQ-32B vs Qwen2.5-32B) compared at equivalent inference token budgets via pass@k. Failure analysis localizes the first wrong move in the sequence; ablations test sampling (T=0 vs T=1) and explicit-algorithm provision.

## Result
Collapse thresholds are model- and puzzle-specific (e.g., QwQ-32B: Hanoi $N\!=\!7$, Checker $N\!=\!2$, Blocks $N\!=\!10$, River $N\!=\!3$). Compositional depth is *not* the sole predictor: models solve ~$10^2$-move Hanoi instances but fail at ~$10^1$-move River Crossing. Providing the explicit recursive algorithm does **not** shift the collapse point for either DeepSeek-R1 or V3. At low complexity LRMs "overthink" — finding the correct answer early then continuing to explore wrong alternatives; at high complexity they fixate on early wrong answers and waste the remaining budget.

## Why it matters here
General background; no direct arena tie. Relevant to the autonomous-loop agent's *meta-design* (council dispatch, self-improvement loop): warns that more thinking tokens ≠ better solutions past a complexity threshold, and that explicit algorithms in-context don't repair compositional planning failure — supporting this repo's stance of triple-verify + external simulators + wiki-compounded knowledge over pure CoT scaling.

## Open questions / connections
- Does the collapse threshold correlate with training-data exposure (River Crossing scarcity hypothesis) rather than computational complexity?
- Can structured tool use (code execution, external verifiers like our triple-verify) bypass the collapse, since algorithm-provision-in-prompt cannot?
- Extends overthinking literature [Chen et al., Sui et al.] and pass@k convergence [Yue et al.] by adding controlled-complexity puzzle axis absent from MATH-500/AIME.

## Key terms
Large Reasoning Models, LRM, Chain-of-Thought, overthinking, reasoning collapse, inference-time scaling, pass@k, Tower of Hanoi, Checker Jumping, River Crossing, Blocks World, compositional depth, DeepSeek-R1, Claude-3.7-Sonnet-Thinking, o3-mini, QwQ-32B, self-correction, algorithmic reasoning, data contamination
