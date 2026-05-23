---
type: source
kind: paper
title: Hyperagents
authors: Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.19461
source_local: ../raw/2026-zhang-hyperagents.pdf
topic: general-knowledge
cites: 
---

# Hyperagents

**Authors:** Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.19461

## One-line
Introduces *hyperagents* — self-referential agents that fuse a task agent and a meta agent into one editable program, so the self-improvement mechanism is itself modifiable across any computable task.

## Key claim
By making the meta-level modification procedure editable (metacognitive self-modification), the Darwin Gödel Machine extension DGM-H removes the coding-domain alignment assumption of DGM and achieves open-ended self-improvement that transfers across domains (coding, paper review, robotics reward design, Olympiad math grading) and across runs.

## Method
Build a single Python program (Turing-complete editable substrate) containing both a task agent and a meta agent; embed it in DGM's open-ended archive-based evolutionary loop where parents are sampled probabilistically by score $\times 1/(\text{compiled children}+1)$. Each iteration: select parent hyperagent → it self-modifies (any code, including its own meta-mechanism) → evaluate child empirically → add to archive. Initial hyperagent is a frozen FM with `bash` + file-edit tools and a minimal "modify any part of the codebase" prompt.

## Result
DGM-H matches DGM on Polyglot coding and substantially outperforms ablations (no-self-improve = ADAS; no-open-ended) and DGM/DGM-custom on paper review, robotics reward design, and IMO-level math grading. Emergent meta-improvements include persistent JSON memory, performance trackers, compute-aware iteration budgeting, bias detection (fixed a 99% accept-rate collapse: 49% → 63% accuracy), and rediscovery of UCB / softmax / stagnation-adaptive parent selection. Meta-skills learned in paper-review+robotics transfer to math grading; "BetterGrader" beats ProofAutoGrader by +4.06% accuracy by recovering Almost/Partial labels (recall +18.52% / +10.50%).

## Why it matters here
General background; no direct arena tie — but the DGM-H archive-with-metacognitive-modification pattern is directly applicable to the einstein autonomous-loop agent: it argues for an editable meta-mechanism and persistent cross-cycle memory (cf. cycle-log, skill-library) as the substrate for compounding wisdom, rather than a fixed handcrafted self-improvement instruction.

## Open questions / connections
- Parent selection ablation (Appendix E.5) shows learned UCB-style mechanisms still trail a handcrafted `score-child-prop` — when does meta-learning beat hand engineering on selection?
- How to design evaluation signals that resist Goodhart-style gaming as self-modification compounds? Especially relevant for arena scores with verifier drift.
- Extends DGM (Zhang 2025), ADAS (Hu 2025), Gödel Machine (Schmidhuber 2003); connects to AI-Scientist, evolutionary code search, and self-referential meta-learning (Kirsch–Schmidhuber 2022).
- Open: bounds on self-acceleration rate; conditions under which meta-improvement transfer is monotone vs. catastrophic.

## Key terms
hyperagent, Darwin Gödel Machine, DGM, metacognitive self-modification, self-referential meta-learning, open-ended exploration, archive-based evolution, stepping stones, UCB parent selection, persistent memory, evaluation gaming, Goodhart's law, foundation model agent, recursive self-improvement, ADAS
