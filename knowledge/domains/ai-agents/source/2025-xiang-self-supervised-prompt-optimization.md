<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Self-Supervised Prompt Optimization
authors: [Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu, Xinbing Liang, Fengwei Teng, Jinhao Tu, Fashen Ren, Xiangru Tang, Sirui Hong, Chenglin Wu, Yuyu Luo]
year: 2025
doi: 10.48550/arXiv.2502.06855
source_url: https://doi.org/10.48550/arXiv.2502.06855
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Self-Supervised Prompt Optimization

## TL;DR
SPO is a reference-free prompt-optimization framework that derives both evaluation and optimization signals purely from pairwise comparisons of an LLM's own outputs — no ground truth or human feedback — matching or beating state-of-the-art methods at 1.1–5.6% of their cost (~$0.15 per dataset, 3 samples).

## Key findings
- **Core idea (OvO vs OvG).** Existing prompt optimizers depend on external references — ground-truth answers (benchmark scoring) or human feedback — which are unavailable for open-ended tasks and costly to annotate. SPO replaces *Output-vs-Ground-truth* (OvG) with *Output-vs-Output* (OvO): an LLM evaluator picks the better of two outputs from two prompts, and an LLM optimizer rewrites the prompt toward the preferred output. Evaluation and optimization signals both come "from the data" like self-supervised learning.
- **Loop (Algorithm 1).** Optimize-Execute-Evaluate: ϕ_opt generates a new prompt from the current-best prompt + its outputs; ϕ_exe runs it on 3 sampled questions; ϕ_eval does pairwise comparison vs the current best; on a win, the new prompt/answer becomes best. Runs to a fixed iteration cap (default 10). Only **8 LLM calls per iteration**, **3 samples**, no answers needed.
- **Closed-task results (Table 1, GPT-4o-mini execution, 5 benchmarks).** SPO avg performance **66.9**, beating the best baseline by **1.9** and topping all conventional prompting; reaches best-in-class on GPQA (**43.6**) and BBH-Navigate (**97.2**). Comparable to ground-truth-dependent optimizers (APE, OPRO, PromptAgent, PromptBreeder, TextGrad) while costing far less.
- **Cost (Table 1).** Avg optimization cost **$0.15** per dataset vs $2.71–$13.14 for baselines — i.e. **1.1–5.6%** of their cost.
- **Open-ended tasks (MT-Bench writing/roleplay/humanities, Fig 5).** GPT-4o-judged win rates improve across all execution models (Claude-3.5-Sonnet, DeepSeek-V3, GPT-4o-mini); smaller models with SPO-optimized prompts frequently beat larger models in IO mode.
- **Transferability / weak models (Tables 2–3).** Robust across optimizer/evaluator/executor combinations; best result 97.8 (GPT-4o-mini in all three roles). Lifts a weak executor (Claude-3-Haiku) on BBH-Navigate from **62.2 → 89.7**.
- **Overfitting behavior.** Both sample count and iteration count show inverted-U curves; performance peaks then degrades (e.g. Claude-3.5-Sonnet peaks at iteration 7 = 95.8% then declines). Authors fix 3 samples / 10 iterations as the cost–performance sweet spot.
- **Emergent strategy.** In the BBH-Navigate trajectory (Appendix A.5.1), the prompt evolves from textual position-reasoning to spontaneously adopting coordinate-system reasoning — never explicitly instructed.

## Methods (brief)
Optimizer/evaluator/executor are separable LLMs (default: Claude-3.5-Sonnet optimizer, GPT-4o-mini evaluator+executor; temp 0.7 opt, 0.3 eval, 0 exec). Bias in pairwise judging is mitigated by 4 rounds of randomized (order-swapped) evaluation. Evaluated on 5 closed benchmarks (GPQA-Diamond, AGIEval-MATH L5, LIAR, WSC, BBH-Navigate) plus MT-Bench open-ended categories, averaged over 3 runs.

## Limitations
Quality is bounded by the evaluator LLM's task comprehension — biased/weak on specialized domains (the authors flag this for scientific use). Pairwise-judge biases are reduced, not eliminated. Optimizes for a single execution model (no cross-model transfer objective). Susceptible to overfitting the 3 sampled questions beyond ~10 iterations.

## Citations of interest
- Wei et al. 2022 — Chain-of-Thought prompting; SPO's default seed prompt and motivating evidence that outputs reflect prompt quality.
- Zheng et al. 2023 — LLM-as-a-judge / MT-Bench; the evaluation method and open-ended benchmark SPO builds on.
- Yüksekgönül et al. 2024 — TextGrad ("differentiation via text"); a textual-gradient OvG baseline SPO outperforms on cost.
- Yang et al. 2023 — OPRO (LLMs as optimizers); ground-truth-dependent baseline.
- Fernando et al. 2024 — PromptBreeder (self-referential prompt evolution); evolutionary baseline.
- Zhang et al. 2024a — AFlow (automating agentic workflow generation); same group, related automated-optimization line.
