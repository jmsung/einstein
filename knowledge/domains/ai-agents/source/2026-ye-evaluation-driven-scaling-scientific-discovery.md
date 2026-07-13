<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning, sci-math]
title: Evaluation-driven Scaling for Scientific Discovery
authors: [Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Caiyin Yang, Chang Su, R. Thapa, Rui Yang, Ruihua Liu, Zeyu Li, Chongming Gao, D. Ding, Guangrong He, Miao Zhang, Lin Sun, Wenyang Wang, Yuchen Zhong, Zhuohao Shen, Di He, Jianzhu Ma, Stefano Ermon, Tongyang Li, Xiaowen Chu, James Zou, Yuzhi Xu]
year: 2026
source_url: https://arxiv.org/abs/2604.19341
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Evaluation-driven Scaling for Scientific Discovery

**Authors:** Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Caiyin Yang, Chang Su, R. Thapa, Rui Yang, Ruihua Liu, Zeyu Li, Chongming Gao, D. Ding, Guangrong He, Miao Zhang, Lin Sun, Wenyang Wang, Yuchen Zhong, Zhuohao Shen, Di He, Jianzhu Ma, Stefano Ermon, Tongyang Li, Xiaowen Chu, James Zou, Yuzhi Xu  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.19341

## One-line
A framework, SimpleTES, that scales LLM-driven scientific discovery by allocating evaluator-query budget across three axes — parallel trajectories, refinement depth, and local sampling — yielding new SOTAs on 21 problems including Erdős minimum overlap and autocorrelation inequalities.

## Key claim
Treating evaluation-driven loop scaling as a first-class axis (budget $N = C \times L \times K$) lets open-source `gpt-oss` models beat frontier models and bespoke pipelines, e.g. new SOTA on Erdős minimum overlap ($0.380856$, improving the prior AI record $0.380871$), AC2 (+$6.79\%$), AC3 (+$0.30\%$), sum-difference ($1.144887$, +$2.05\%$ over AlphaEvolve V2), and circle packing $n=26,32$.

## Method
SimpleTES runs $C$ independent trajectories in parallel; each trajectory iteratively performs $L$ feedback-driven refinement steps, with $K$ candidates drawn per step and the highest-scoring one committed to history. A context map $\Phi$ selects which historical nodes feed the next proposal — enabling recombination across the trajectory rather than purely sequential refinement. Optionally, successful trajectories are used as post-training supervision (label by best-in-trajectory outcome rather than per-step score), producing models that generalize to unseen problems. Domain-specific pipelines are emergent (e.g. FFT-conv + L-BFGS-B for AC2; DCT parameterization for AC3; coarse-to-fine for Erdős).

## Result
- **Erdős minimum overlap:** $0.380856$ (prev AI $0.380871$; $0.186‰$ over best human).
- **AC2 (autocorrelation):** $+6.79\%$ over best human bound, via FFT-based convolution + L-BFGS-B refinement.
- **AC3:** $+0.30\%$ over best human, via DCT parameterization.
- **Sum-difference problem:** $1.144887$, beating best human by $8.03\%$ and AlphaEvolve V2 by $2.05\%$, via "long AP backbone + sparse fringe corrections."
- **Circle packing in unit square:** SOTA at $n=26$ ($2.635983$) and $n=32$ ($2.939572$) via adaptive coarse-to-fine + LP routines.
- **Hadamard max determinant (order 29):** matches human lower-bound record $320 \cdot 7^{12} \cdot 2^{28}$, beating ThetaEvolve by $62.3\%$.
- Also: LASSO $2\times$ speedup, qubit routing $-24.5\%$ CNOTs, scaling-law $R^2$ $0.572 \to 0.674$.

## Key terms
SimpleTES, evaluation-driven scaling, test-time scaling, Erdős minimum overlap, autocorrelation inequality, AC2, AC3, FFT convolution, L-BFGS-B, discrete cosine transform parameterization, circle packing unit square, Hadamard maximum determinant, sum-difference problem, coarse-to-fine optimization, trajectory-level post-training, reward hacking, refinement depth, parallel trajectories, gpt-oss
