---
type: note
kind: paper-relevance
about: 2023-furuta-multimodal-web-navigation-instruction-finetuned
canonical: ../../domains/ai-agents/source/2023-furuta-multimodal-web-navigation-instruction-finetuned.md
---

# Relevance note — Multimodal Web Navigation with Instruction-Finetuned Foundation Models

Canonical distillation: [`2023-furuta-multimodal-web-navigation-instruction-finetuned.md`](../../domains/ai-agents/source/2023-furuta-multimodal-web-navigation-instruction-finetuned.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The paper is on web-agent training (multimodal SL, instruction-following LLM, ViT temporal/local tokens) — orthogonal to Einstein Arena's math optimization problems (sphere packing, kissing numbers, autocorrelation, etc.). Useful only as ambient context for agent-architecture design choices in the autonomous loop, not as a math source.

## Open questions / connections
- Multi-step memory-heavy tasks (guess-number, count-shape) remain weak — suggests long-horizon reasoning gap in instruction-finetuned encoder-decoders.
- Ablation showing ViT pre-training choice (ImageNet vs JFT-3B vs CLIP vs MAE vs DINO) is marginal while temporal+local token design dominates — perception-token engineering > pretrained-vision-data scale at this regime.
- Extends Gur et al. 2022 (WebN-T5, HTML-only) by adding vision; positions offline SL as competitive with online RL given a large enough demonstration corpus.
