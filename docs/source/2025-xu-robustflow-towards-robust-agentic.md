---
type: source
kind: paper
title: RobustFlow: Towards Robust Agentic Workflow Generation
authors: Shengxiang Xu, Jiayi Zhang, Shimin Di, Yuyu Luo, Liang Yao, Hanmo Liu, Jia Zhu, Fan Liu, Min-Ling Zhang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2509.21834
source_local: ../raw/2025-xu-robustflow-towards-robust-agentic.pdf
topic: general-knowledge
cites:
---

# RobustFlow: Towards Robust Agentic Workflow Generation

**Authors:** Shengxiang Xu, Jiayi Zhang, Shimin Di, Yuyu Luo, Liang Yao, Hanmo Liu, Jia Zhu, Fan Liu, Min-Ling Zhang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2509.21834

## One-line
Trains LLM workflow generators to produce the *same* DAG-shaped agentic workflow for semantically equivalent but differently phrased user instructions, via a two-stage SFT + self-consistency DPO pipeline.

## Key claim
Existing automated workflow generators (ADAS, AFlow, MaAS, FlowReasoner, ScoreFlow, Flow) collapse to 40-70% structural stability under paraphrase/requirement-augmentation/noise perturbations of identical-meaning queries — even at temperature 0. RobustFlow lifts node-chain and graph-structure robustness scores to ~70-90% (avg 0.82-0.89 across Code/Math/QA × 5 perturbation types).

## Method
Two-stage training. (1) **Instruction-augmented SFT**: from FLORA-Bench $(q_n, w_n^g)$ pairs, generate paraphrased $q_n^{(i)} = q_n + \delta^{(i)}$ keeping $w_n^g$ fixed, train standard cross-entropy on the augmented set. (2) **Self-consistency preference optimization (ScPO)**: for each semantic cluster $C(q)$, sample $r$ candidates per paraphrase, canonicalize each to its normalized DAG $\Gamma(w)$, score each unique workflow by $R_q(w) = s_q(w) + \lambda_q \cdot v_q(w)/|Y_q|$ (execution score + self-consistency vote share), then take $(w_q^+, w_q^-) = (\arg\max R_q, \arg\min R_q)$ as DPO preference pairs. Evaluation: structure-aware metrics — node-chain $F_{node}$ via LIS on aligned topological order under Sentence-BERT bipartite matching, and graph-structure $F_{graph}$ via reachability-pair F1 on aligned DAGs.

## Result
Built a benchmark of 1,255 base tasks × 6 synonymous variants → 31,889 workflows across MBPP, HumanEval, GSM8K, MATH, HotpotQA, DROP under 5 perturbation classes (requirement-aug, paraphrase, light/moderate/heavy TextAttack noise). RobustFlow's avg robustness 0.82-0.89 vs ScoreFlow 0.60-0.73, AFlow 0.42-0.49, Flow 0.63-0.70. Gains hold across all 5 perturbation classes and all 6 tasks.

## Why it matters here
General background; no direct arena tie. The math-solving protocol's council-dispatch and self-improvement loop are themselves agentic workflows — robustness-under-paraphrase is the failure mode that produces drift when the same problem statement gets re-framed across sessions. The ScPO recipe (canonicalize → vote-weight → DPO) is a plausible training-time fix for council-output consistency, and the node-chain + reachability F1 metrics are reusable for measuring whether the protocol produces stable trajectories on identical Einstein problems.

## Open questions / connections
- Does ScPO scale to *task-level* (long-horizon) workflows where a single canonical DAG may not exist, or only to query-level synthesis?
- Robustness here is measured against synonymous queries, not against *adversarial restatements that change difficulty cues* — would the same training regime hold under shifted persona/context priors (the analog of council-dispatch reframing)?
- Extends ScoreFlow (DPO on execution score alone) by adding the self-consistency vote term; ablation of $\lambda_q$ would clarify how much of the gain is voting vs. instruction-augmented SFT.

## Key terms
agentic workflow generation, robustness, semantic invariance, DPO, preference optimization, self-consistency, DAG canonicalization, longest increasing subsequence, reachability F1, Sentence-BERT alignment, paraphrase perturbation, TextAttack, ScoreFlow, AFlow, FLORA-Bench
