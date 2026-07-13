<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: HyperAgents
authors: [Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina]
year: 2026
doi: 10.48550/arXiv.2603.19461
source_url: https://doi.org/10.48550/arXiv.2603.19461
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# HyperAgents

## TL;DR
HyperAgents are self-referential agents that fuse a task agent and a *modifiable* meta agent into a single editable program, so the self-improvement mechanism itself can be rewritten ("metacognitive self-modification"). Instantiated as DGM-Hyperagents (DGM-H), they generalize recursive self-improvement beyond coding to any computable task and learn transferable meta-level machinery (memory, performance tracking) that carries across domains.

## Key findings
- **Core idea**: prior self-improving systems (notably the Darwin Gödel Machine, DGM) rely on a *fixed, handcrafted* instruction-generation step. This works in coding only because evaluation and self-modification are both coding tasks (an alignment assumption that fails elsewhere). HyperAgents remove this by making the entire meta-level procedure editable.
- **DGM-H** keeps DGM's open-ended, archive-based evolutionary search (parent selection ∝ performance, inversely ∝ number of compiled children; λ=10, top-m=3 midpoint) but lets agents modify how they self-modify.
- **Coding (Polyglot, 80 iters)**: training subset 0.140 → 0.340 (CI 0.300–0.380); full benchmark 0.084 → 0.267 (CI 0.231–0.280) — comparable to original DGM (0.140→0.380; 0.142→0.307) *despite not being handcrafted for coding*.
- **Paper review (100 iters)**: test score 0.0 → 0.710 (CI 0.590–0.750), beating AI-Scientist-v2 static baseline (0.630). Original DGM = 0.0; manually-customized DGM-custom = 0.590.
- **Robotics reward design (Genesis Go2 quadruped)**: 0.060 → 0.372 (CI 0.355–0.436), surpassing the default reward (0.348). On the held-out torso-height test task, DGM-H reliably discovers jumping behaviors where DGM-custom gets stuck in the "stand tall" local optimum.
- **Ablations**: removing self-improvement (≈ADAS) or open-ended exploration yields little/no gain (p<0.05 vs DGM-H in both domains) — both components are necessary.
- **Transferable meta-learning (imp@k metric)**: hyperagents optimized on paper-review + robotics, then transferred to unseen **Olympiad math grading**, achieve imp@50 = 0.630 (CI 0.540–0.630) under a *fixed* meta agent, vs 0.0 for transferred DGM-custom agents and 0.0 for the initial agent. Meta-level skill is general, not domain-specific.
- **Compounding across runs**: continuing DGM-H from transfer hyperagents on math grading reaches 0.640 vs 0.610 from scratch; starting from ProofAutoGrader + transfer meta agent improves it 0.561 → 0.601 accuracy on full IMO-GradingBench (MAE 0.178 → 0.175).
- **Emergent meta-machinery (qualitative)**: the system autonomously invents a `PerformanceTracker`, persistent JSON `MemoryTool` storing synthesized insights/causal hypotheses, compute-aware planning (behavior conditioned on iterations remaining), automated bias detection (caught a 99%-accept / 49%-accuracy collapse, corrected to 63%), and — given freedom — rediscovers UCB and temperature-softmax parent selection.

## Methods (brief)
DGM-H extends the DGM archive-evolution loop with an editable meta agent built around a frozen FM (Claude 4.5 Sonnet for self-modification; o3-mini/GPT-4o/o4-mini for task eval) with bash + file-editor tools. Across 4 domains, agents pass a staged evaluation (small subset → full set) and are scored on held-out test tasks; 5 runs each, medians with 95% bootstrap CIs (1,000 resamples) and Wilcoxon signed-rank tests. A 100-iteration run costs ≈88.6M tokens.

## Limitations
Fixed task distribution and a fixed outer loop (parent selection and evaluation remain non-modifiable in the main experiments; only preliminary results in Appendix E.5 modify selection, and it does not beat the handcrafted mechanism). Several headline transfer/compounding gains are not statistically significant (p>0.05), resting on higher medians/CIs. Results depend on benchmark fidelity — the system faithfully amplifies dataset biases and is prone to evaluation gaming (Goodhart). N=5 runs per condition.

## Citations of interest
- Zhang et al., 2025b — Darwin Gödel Machine: the open-ended self-improving coding system DGM-H directly extends.
- Hu et al., 2025 (ADAS) — Automated Design of Agentic Systems; the "w/o self-improve" baseline.
- Schmidhuber, 2003 — Gödel Machine; provably-optimal self-modification, theoretical antecedent.
- Kirsch & Schmidhuber, 2022 — self-referential meta-learning, the conceptual basis for editable meta-levels.
- Luong et al., 2025 — IMO-GradingBench / ProofAutoGrader, the math-grading domain and static baseline.
- Yamada et al., 2025 — AI-Scientist-v2; paper-review static baseline.
- Clune, 2019 — AI-GAs: open-ended AI-generating algorithms, the guiding paradigm.
