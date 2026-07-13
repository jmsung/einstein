<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: TextGrad: Automatic \"Differentiation\" via Text
authors: [Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou]
year: 2024
source_url: https://arxiv.org/abs/2406.07496
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
TextGrad, textual gradients, automatic differentiation, backpropagation, LLM feedback, prompt optimization, instance optimization, test-time training, self-refinement, Reflexion, DSPy, compound AI systems, GPQA, LeetCode, DOCKSTRING, Vina score, QED druglikeness, IMRT treatment planning, momentum, constrained optimization, computation graph
