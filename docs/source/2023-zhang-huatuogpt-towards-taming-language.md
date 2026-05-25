---
type: source
kind: paper
title: HuatuoGPT, towards Taming Language Model to Be a Doctor
authors: Hongbo Zhang, Junying Chen, Feng Jiang, Fei Yu, Zhihong Chen, Jianquan Li, Guimin Chen, Xiangbo Wu, Zhiyi Zhang, Qingying Xiao, Xiang Wan, Benyou Wang, Haizhou Li
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2305.15075
source_local: ../raw/2023-zhang-huatuogpt-towards-taming-language.pdf
topic: general-knowledge
cites:
---

# HuatuoGPT, towards Taming Language Model to Be a Doctor

**Authors:** Hongbo Zhang, Junying Chen, Feng Jiang, Fei Yu, Zhihong Chen, Jianquan Li, Guimin Chen, Xiangbo Wu, Zhiyi Zhang, Qingying Xiao, Xiang Wan, Benyou Wang, Haizhou Li  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.15075

## One-line
A Chinese medical chatbot fine-tuned on a mix of ChatGPT-distilled and real doctor–patient data, then aligned via RLAIF to behave more like a doctor (asking clarifying questions, issuing diagnoses) than ChatGPT does.

## Key claim
Combining distilled ChatGPT data with real-world doctor data in SFT and then applying RL from AI feedback (RLAIF) produces a 7B medical model (HuatuoGPT, based on Bloomz-7b1-mt) that beats GPT-3.5-turbo in GPT-4-judged medical consultation on >60% of cases and outperforms prior open-source Chinese medical LLMs (BenTsao, DoctorGLM) in both single-turn (52% win vs ChatGPT, 10.5% vs GPT-4) and multi-turn (86% vs DoctorGLM, 58% vs ChatGPT) human evaluation.

## Method
Two-stage training on Bloomz-7b1-mt: (1) SFT on a hybrid corpus of 61.4k ChatGPT-distilled instructions, 69.8k real doctor instructions, 68.9k two-ChatGPT-roleplay conversations, and 26.0k real doctor-patient multi-turn dialogues; (2) RLAIF where a reward model trained on LLM-scored response pairs (rated on informativeness, coherence, factuality vs real doctor diagnosis) drives PPO with KL penalty $r = r_{RM} - \lambda_{KL} D_{KL}(\pi \| \pi_0)$, $\lambda_{KL}=0.05$, only last two layers updated, 16k steps.

## Result
On automatic GPT-4 evaluation over 100 KUAKE-QIC questions across 10 medical intents, HuatuoGPT outperforms GPT-3.5-turbo in 3 categories (Indicators Interpretation, Condition Diagnosis, Medical Expenses) and ties in 2; achieves SOTA on cMedQA2, webMedQA, and Huatuo-26M benchmarks among open-source medical LLMs. Ablations show real-data-only models ask clarifying questions but write briefly; distilled-only models write fluently but never diagnose; only the full SFT+RLAIF pipeline does both.

## Why it matters here
General background; no direct arena tie. The paper is about NLP fine-tuning of a medical chatbot, with no relevance to sphere packing, kissing numbers, autocorrelation, extremal graphs, or any Einstein Arena problem family. Method-level lesson (mixing distilled + ground-truth data, AI-judge reward modeling) is an LLM-training pattern, not math wisdom.

## Open questions / connections
- Verification of generated medical content (the paper flags this as a deployment blocker) — analogous to this project's triple-verify discipline, but for free-text rather than numerical scores.
- RLAIF as a label-free alignment shortcut [Bai et al. 2022 constitutional AI] — possibly relevant if the agent ever uses an LLM-judge to rank its own wiki drafts, but not the math itself.
- No mathematical content to extend; out of scope for the council / problem-solving loop.

## Key terms
HuatuoGPT, medical LLM, RLAIF, reinforcement learning from AI feedback, supervised fine-tuning, distilled data, ChatGPT distillation, reward model, KL penalty, Bloomz-7b1-mt, instruction tuning, medical consultation
