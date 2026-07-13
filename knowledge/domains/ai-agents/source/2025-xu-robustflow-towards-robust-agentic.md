<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: RobustFlow: Towards Robust Agentic Workflow Generation
authors: [Shengxiang Xu, Jiayi Zhang, Shimin Di, Yuyu Luo, Liang Yao, Hanmo Liu, Jia Zhu, Fan Liu, Min-Ling Zhang]
year: 2025
source_url: https://arxiv.org/abs/2509.21834
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
agentic workflow generation, robustness, semantic invariance, DPO, preference optimization, self-consistency, DAG canonicalization, longest increasing subsequence, reachability F1, Sentence-BERT alignment, paraphrase perturbation, TextAttack, ScoreFlow, AFlow, FLORA-Bench
