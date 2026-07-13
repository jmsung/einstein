<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-multiomics, bio-clinical]
title: Toward a Team of AI-made Scientists for Scientific Discovery from Gene Expression Data
authors: [Haoyang Liu, Yijiang Li, Jinglin Jian, Yuxuan Cheng, Jianrong Lu, Shuyin Guo, Jin Zhu, Mianchen Zhang, Mian Zhang, Haohan Wang]
year: 2024
source_url: https://arxiv.org/abs/2402.12391
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Toward a Team of AI-made Scientists for Scientific Discovery from Gene Expression Data

**Authors:** Haoyang Liu, Yijiang Li, Jinglin Jian, Yuxuan Cheng, Jianrong Lu, Shuyin Guo, Jin Zhu, Mianchen Zhang, Mian Zhang, Haohan Wang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2402.12391

## One-line
Proposes TAIS, a multi-agent LLM system (Project Manager, Data Engineer, Domain Expert, Statistician, Code Reviewer) that automates the gene-expression analysis pipeline to identify disease-predictive genes.

## Key claim
On the curated GenQEX benchmark (457 trait-condition pairs), TAIS achieves end-to-end SR $69.08\%$, F1 $30.27\%$, Jaccard $21.13\%$; with gold-standard preprocessing, the Statistician reaches F1 $89.30\%$ after 2 code-review rounds, identifying preprocessing as the dominant bottleneck.

## Method
Two-stage role-driven pipeline: data preparation (Data Engineer + Domain Expert + Code Reviewer) then regression (Statistician + Code Reviewer), coordinated by a Project Manager. Two interaction patterns — *write-run-audit* (bounded code-review loop) and *consultative coding* (biomedical decisions). Statistical backbone: Lasso for high-dim variable selection, eigenvalue-gap heuristic on covariance to detect confounders, LMM correction, and two-step regression with cross-cohort common-gene regressors to impute missing condition variables.

## Result
End-to-end F1 splits sharply by task type: single-step $45.05\%$ vs two-step $19.21\%$. Regression-only F1 climbs $55.95\% \to 80.12\% \to 89.30\%$ over $0/1/2$ review rounds; preprocessing-only F1 climbs $14.41\% \to 27.50\% \to 33.01\%$. Case study (Pancreatic Cancer × Vitamin D) finds 20+ genes with $80\%$ CV accuracy; 4 of top-5 (SLC11A1, SOCS1, LILRB3, SPA17) have literature support.

## Key terms
multi-agent LLM, role decomposition, code review loop, Lasso regression, confounding correction, linear mixed model, two-step regression, gene expression, GenQEX benchmark, TAIS, agent orchestration, MetaGPT
