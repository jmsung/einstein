---
type: source
kind: paper
title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
authors: Hugo Touvron, Louis Martin, Kevin R. Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Niko-lay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, D. Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, A. Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel M. Kloumann, A. Korenev, Punit Singh Koura, M. Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, X. Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, J. Reizenstein, Rashi Rungta, Kalyan Saladi, A. Schelten, Ruan Silva, Eric Michael Smith, R. Subramanian, Xia Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zhengxu Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, M. Kambadur, Sharan Narang, Aur'elien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2307.09288
source_local: ../raw/2023-touvron-llama-open-foundation-fine-tuned.pdf
topic: general-knowledge
cites:
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models

**Authors:** Hugo Touvron, Louis Martin, Kevin R. Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Niko-lay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, D. Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, A. Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel M. Kloumann, A. Korenev, Punit Singh Koura, M. Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, X. Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, J. Reizenstein, Rashi Rungta, Kalyan Saladi, A. Schelten, Ruan Silva, Eric Michael Smith, R. Subramanian, Xia Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zhengxu Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, M. Kambadur, Sharan Narang, Aur'elien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2307.09288

## One-line
Releases Llama 2, a family of 7B–70B open-weight pretrained and RLHF-fine-tuned dialogue LLMs, with a detailed recipe for supervised fine-tuning, iterative reward modeling, and safety alignment.

## Key claim
Llama 2-Chat models match or exceed open-source chat baselines and approach closed-source assistants (ChatGPT, PaLM) on helpfulness/safety human evals; Llama 2 70B reaches MMLU 68.9, GSM8K 56.8, HumanEval 29.9, BBH 51.2 after pretraining on 2T tokens.

## Method
Standard auto-regressive transformer (RMSNorm pre-norm, SwiGLU, RoPE) with grouped-query attention (GQA) and 4k context, pretrained on 2T tokens with AdamW ($\beta_1=0.9,\beta_2=0.95$), cosine LR schedule. Alignment uses SFT on ~27.5k high-quality human dialogues, then iterative RLHF combining rejection sampling and PPO against two reward models (helpfulness, safety) trained on >1M human binary preference comparisons. Introduces "Ghost Attention" (GAtt) to maintain system-prompt adherence across multi-turn dialogue.

## Result
Llama 2 70B closes most of the gap to GPT-3.5 on MMLU/GSM8K but lags on code (HumanEval 29.9 vs 48.1). Toxicity on ToxiGen drops to ~0% across Llama 2-Chat sizes; TruthfulQA truth+info rises from ~50% (pretrained) to 64–67% (chat). Pretraining cost: 3.3M A100-80GB GPU-hours, 539 tCO2eq (fully offset). Contamination analysis flags only HellaSwag and MMLU-Humanities as measurably boosted.

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructure context for the agent itself (transformer architecture, RLHF, GQA, RoPE) — does not inform any math optimization problem (sphere packing, autocorrelation, kissing numbers, etc.).

## Open questions / connections
- Code-benchmark gap to GPT-4 suggests math/code-specific RLHF or specialized data mixes remain underexplored.
- Quality-over-quantity SFT finding (~27k examples sufficient) echoes Zhou et al. 2023 (LIMA) — open question on minimum sufficient alignment dataset size.
- GAtt is a heuristic for multi-turn system-prompt persistence; a principled attention-level fix is left open.

## Key terms
Llama 2, RLHF, PPO, rejection sampling, supervised fine-tuning, reward modeling, grouped-query attention, RoPE, SwiGLU, RMSNorm, Ghost Attention, transformer pretraining, alignment, helpfulness-safety tradeoff, TruthfulQA, ToxiGen, MMLU, HumanEval, GSM8K, dataset contamination
