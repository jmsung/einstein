---
type: source
kind: paper
title: TextGrad: Automatic \"Differentiation\" via Text
authors: Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.07496
source_local: ../raw/2024-yuksekgonul-textgrad-automatic-differentiation-text.pdf
topic: general-knowledge
cites:
---

# TextGrad: Automatic \"Differentiation\" via Text

**Authors:** Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.07496

## One-line
A PyTorch-style framework that "backpropagates" natural-language critiques from LLMs through computation graphs to optimize variables (prompts, code, molecules, treatment plans) without numerical gradients.

## Key claim
Treating LLM-generated textual feedback as "gradients" and applying analogues of SGD/momentum/minibatching yields turn-key optimization of compound AI systems: GPQA Diamond 51%→55%, LeetCode-Hard 26%→36% (vs Reflexion 31%), GSM8k prompt-tuning ~77.8%→91.9%, and OAR dose reductions in prostate IMRT planning vs clinician baselines.

## Method
Each system is a DAG where every variable $v = f_v(\text{Preds}(v))$ and $f$ can be any blackbox (LLM call, simulator, docking engine, LP solver). A "gradient operator" $\nabla_{\text{LLM}}(x, y, \partial L/\partial y)$ prompts an LLM with the forward context plus downstream criticism to produce text feedback on $x$; aggregation over successors mirrors $\partial L/\partial v = \sum_{w} \nabla f(v,w,\partial L/\partial w)$. A "Textual Gradient Descent" (TGD) step prompts an LLM to revise $v$ given its current value plus accumulated feedback, with optional momentum (past iterates) and constrained-optimization analogues (natural-language constraints).

## Result
Across five domains with **no per-domain prompt tuning**: (1) LeetCode-Hard pass@1 0.36±0.018 vs Reflexion 0.31±0.012 (zero-shot vs 1-shot, gpt-4o); (2) GPQA Diamond 55% vs 51% baseline; MMLU subsets similar gains via test-time solution refinement; (3) prompt optimization on Object Counting/Word Sorting/GSM8k pushing gpt-3.5 near gpt-4; (4) molecule design from trivial fragments (benzene, pentane, acetamide) reaches Vina < −7 with QED > 0.8 across 58 DOCKSTRING targets, 95% novel vs ChEMBL by iter 6, implicitly avoiding mutagenic/toxic structures; (5) prostate IMRT plans with lower rectum/bladder mean dose than clinicians while matching PTV D95.

## Why it matters here
General background; no direct arena tie — the Einstein Arena workflow is numerical optimization with verified scoring (triple-verify), not blackbox text-feedback loops. However TextGrad is a plausible mental model for the agent's *own* self-improvement loop (council dispatch → gap → finding → concept): textual "gradients" on wiki pages and strategy.md, with cycle-log as the optimization trace. Relevant if any sub-step (prompt for council personas, refinement of strategy.md drafts) is ever framed as iterative LLM-feedback optimization.

## Open questions / connections
- Does TGD converge or oscillate on long horizons? The paper reports ≤10 iterations; no convergence analysis or step-size theory beyond the gradient-descent analogy.
- How does it compare against DSPy-style compiled prompts on the same prompt-optimization benchmarks under matched compute? GSM8k split is borrowed from DSPy but no head-to-head.
- Extends Pryzant et al. ("Automatic Prompt Optimization with 'Gradient Descent'", 2023) by generalizing beyond prompts to arbitrary variables and arbitrary forward functions.
- Open: can textual gradients be combined with numerical gradients in hybrid systems (e.g., LLM proposes a molecule, autodiff polishes geometry)?
- For agent self-improvement: could `docs/agent/cycle-log.md` rows be treated as ∂L/∂(strategy) signals to refine `mb/<problem>/strategy.md` via TGD?

## Key terms
TextGrad, textual gradients, automatic differentiation, backpropagation, LLM feedback, prompt optimization, instance optimization, test-time training, self-refinement, Reflexion, DSPy, compound AI systems, GPQA, LeetCode, DOCKSTRING, Vina score, QED druglikeness, IMRT treatment planning, momentum, constrained optimization, computation graph
