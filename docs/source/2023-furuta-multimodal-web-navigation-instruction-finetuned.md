---
type: source
kind: paper
title: Multimodal Web Navigation with Instruction-Finetuned Foundation Models
authors: Hiroki Furuta, Ofir Nachum, Kuang-Huei Lee, Yutaka Matsuo, S. Gu, Izzeddin Gur
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2305.11854
source_local: ../raw/2023-furuta-multimodal-web-navigation-instruction-finetuned.pdf
topic: general-knowledge
cites:
---

# Multimodal Web Navigation with Instruction-Finetuned Foundation Models

**Authors:** Hiroki Furuta, Ofir Nachum, Kuang-Huei Lee, Yutaka Matsuo, S. Gu, Izzeddin Gur  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.11854

## One-line
Introduces WebGUM, a multimodal (HTML + screenshot) instruction-finetuned encoder-decoder agent for autonomous web navigation, trained offline on a large demonstration corpus.

## Key claim
WebGUM (Flan-T5-XL + ViT-B16, 3B params) achieves 94.2% average success on MiniWoB++, exceeding the prior best offline method (WebN-T5, 48.4%) by +45.8 points, surpassing online RL-finetuned CC-Net (93.5%), humans (93.5%), and GPT-4-based RCI (94.0%); on WebShop it reaches 45.0% success with 3B params, beating PaLM-540B ReAct (40.0%).

## Method
Jointly finetune an instruction-finetuned T5 (Flan-T5) encoder-decoder with a pre-trained ViT vision encoder. ViT tokenizes a 2-step history of $16\times16$ patch screenshots into $14\times14\times2 = 392$ temporal+local visual tokens; the T5 encoder consumes these alongside HTML, instruction, and action history; the decoder emits free-form text actions of the form `function(selector, text)`. Trained on a 347K-episode multimodal corpus self-collected via prior LLM agents (38× larger than the human dataset of Liu et al. 2018).

## Result
On MiniWoB++ (56 tasks, 100 eval episodes each): Base-size WebGUM with only 2.8K demos already reaches 61.1%, beating WebN-T5; scaled to XL + 401K demos it hits 94.2%. Adding image modality lifts HTML-only 88.7% → 94.2%, with the largest gains on book-flight (+50%), shape recognition (+22%), and social-media (+21%). Instruction-finetuning (Flan-T5 vs T5) adds ~25 points; compositional task generalization (6 stitched tasks) reaches 78.5% vs Synapse 73.8%.

## Why it matters here
General background; no direct arena tie. The paper is on web-agent training (multimodal SL, instruction-following LLM, ViT temporal/local tokens) — orthogonal to Einstein Arena's math optimization problems (sphere packing, kissing numbers, autocorrelation, etc.). Useful only as ambient context for agent-architecture design choices in the autonomous loop, not as a math source.

## Open questions / connections
- Multi-step memory-heavy tasks (guess-number, count-shape) remain weak — suggests long-horizon reasoning gap in instruction-finetuned encoder-decoders.
- Ablation showing ViT pre-training choice (ImageNet vs JFT-3B vs CLIP vs MAE vs DINO) is marginal while temporal+local token design dominates — perception-token engineering > pretrained-vision-data scale at this regime.
- Extends Gur et al. 2022 (WebN-T5, HTML-only) by adding vision; positions offline SL as competitive with online RL given a large enough demonstration corpus.

## Key terms
WebGUM, MiniWoB++, WebShop, Mind2Web, Flan-T5, instruction finetuning, vision transformer, ViT, multimodal agent, offline imitation learning, web navigation, HTML grounding, temporal-local visual tokens, encoder-decoder, foundation model agent
