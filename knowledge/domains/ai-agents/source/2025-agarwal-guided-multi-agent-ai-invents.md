<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Guided multi-agent AI invents highly accurate, uncertainty-aware transcriptomic aging clocks
authors: [Vinayak Agarwal, Orion Li, Christopher A. Petty, Timothy Kassis, Paul W. K. Rothemund, David A. Sinclair, Ashwin Gopinath]
year: 2025
doi: null
source_url: https://doi.org/10.1101/2025.09.08.674588
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Guided multi-agent AI invents highly accurate, uncertainty-aware transcriptomic aging clocks

## TL;DR
A human-supervised, four-agent AI research system (K-Dense, built on Gemini 2.5 Pro) was directed at the open-ended goal "explore aging and transcriptomics" and, over weeks, produced a state-of-the-art transcriptomic aging clock (R² = 0.854, MAE = 4.26 yr) with calibrated per-prediction uncertainty — demonstrating guided multi-agent AI as a discovery accelerator for data-rich domains.

## Key findings
- **System (K-Dense).** Four coordinated agents — Literature Reviewer, Research Planner, Coder & Analyst (called DendroForge, itself 5 sub-agents), Writer & Summarizer — loop under PI supervision (max 50 cycles) with reflexion/self-correction loops to reduce hallucination. Built on Gemini 2.5 Pro (2M-token context); task-specific temperatures (1.0 hypothesis gen, 0.7 reasoning, 0.3 factual synthesis). Convergence gated on R² > 0.85, calibration error < 1%, or human approval. Orange arrows in Fig. 1b mark the human intervention points.
- **Data.** ARCHS4 reprocessed RNA-seq: 57,584 samples, 28 tissues, 1,039 studies, ages 1–114; top 5,000 variable genes; bimodal age distribution (peaks at 21 and 71 yr).
- **Multi-Model Architecture (MMA).** Four age-stratified XGBoost models (Young 1–30, Early-Middle 30–50, Late-Middle 50–70, Elderly 70+). Individual windows R² ≈ 0.68–0.74; ensemble R² = 0.957, MAE 3.7 yr — beating prior SOTA (Qi et al. DeepQA, MAE 4.82 yr) and far above single global XGBoost (R² = 0.619), LightGBM (0.604), LinearSVR (0.574), Ridge (0.539), ElasticNet (0.310) (Fig. 2). **Limitation:** MMA needs chronological age to select the model → not a true standalone clock; learned gating failed.
- **Sliding-window analysis.** 85 overlapping 30-yr windows (1-yr steps) revealed "wave-like" gene-importance bands — genes peak for ~20–30 yr then fade (Fig. 3a). Stage-specific top markers: MIR29B2CHG (young), RBP1/AMPD3 (early-middle), CHAMP1 (late-middle), SEPTIN3 (elderly); CDKN2A/p16 recurs across windows. Importance follows exponential decay (λ = 0.0419, R² = 0.940) → signal concentrated in few hub genes. Pathway enrichment shows a quantitative anabolic→catabolic reversal: proliferation 0.88 (youth) → 0.40 (elderly); stress/senescence inverse.
- **Tissue specificity.** Same temporal wave across tissues but largely non-overlapping gene sets (blood vs colon). Performance: lung R² = 0.969, blood 0.958, ileum 0.958; heart 0.910, adipose 0.887, retina 0.594 (outlier). "Universal timing, tissue-specific execution."
- **Unified ensemble clock with UQ.** Derivative-threshold filtering pools only "stable expert" windows (|derivative| < 0.5), eliminating the age-input requirement. Confidence weighting lifts R² 0.726→0.854 and MAE 6.17→4.26 yr; mean calibration error 0.7%. The clock "knows when it doesn't know" — low confidence concentrates at transitional/extreme ages where biological heterogeneity peaks.

## Methods (brief)
ARCHS4 RNA-seq filtered to 1,039 human studies (≥10M reads, RIN ≥6, healthy/aging-relevant). XGBoost models (max_depth 8, lr 0.05, n_est 300) with 5-fold stratified CV, 80/20 splits, leave-one-study-out validation against batch effects. Ensemble UQ via 3-point smoothing + 25-model-window derivative regression; confidence = 100×(0.4·expert_factor + 0.6·derivative_factor). Reliability diagrams for calibration. The entire analysis was generated/run by the agent system under iterative human prompting (Supplementary Notes 1–2).

## Limitations
Feature importance is correlative, not causal; ARCHS4 has unresolved pre-analytical batch effects and a bimodal age bias; per-tissue sliding windows were feasible only for blood and colon (sufficient coverage); MMA still needs age input; no independent-cohort or distribution-shift validation. Authors acknowledge residual error/hallucination "leakage" despite supervision.

## Citations of interest
- Jumper et al. 2021 (AlphaFold) — motivating exemplar of AI-driven discovery.
- Gottweis et al. 2025 (AI co-scientist), Lu et al. 2024 (AI Scientist), Bran et al. 2023 (ChemCrow) — prior single-task AI-research frameworks K-Dense extends.
- Shinn et al. 2023 (Reflexion) — verbal-RL self-correction underlying K-Dense's reflexion loops.
- Lachmann et al. 2018 (ARCHS4) — the reprocessed RNA-seq resource used for training.
- Qi et al. 2025 (DeepQA) — prior SOTA transcriptomic clock (MAE 4.82 yr) benchmark.
- Horvath 2013 / Levine 2018 (PhenoAge) / Lu 2019 (GrimAge) — methylation-clock lineage contrasted as "black-box" correlates.
