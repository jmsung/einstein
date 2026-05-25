---
type: source
kind: paper
title: The Elicitation Game: Evaluating Capability Elicitation Techniques
authors: Felix Hofstätter, Teun van der Weij, Jayden Teoh, Henning Bartsch, Francis Rhys Ward
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.02180
source_local: ../raw/2025-hofsttter-elicitation-game-evaluating-capability.pdf
topic: general-knowledge
cites:
---

# The Elicitation Game: Evaluating Capability Elicitation Techniques

**Authors:** Felix Hofstätter, Teun van der Weij, Jayden Teoh, Henning Bartsch, Francis Rhys Ward  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.02180

## One-line
Stress-tests capability-elicitation techniques against intentionally hidden-capability "model organisms," introducing a circuit-breaking-based organism more robust than password-locking.

## Key claim
Prompting (few-shot + response prefilling) can elicit hidden MCQA capabilities from both password-locked and circuit-broken models, but for code generation (APPS) only fine-tuning reliably elicits the hidden capability from circuit-broken organisms; combining techniques (N-shot + prefilling + steering) consistently outperforms single methods. Notably, anti-refusal training elicits hidden code-generation capability without any code-related training data.

## Method
Two model organisms are trained from Mistral-7B and Gemma-2-9B: (1) **password-locked**, fine-tuned so $\hat{s} \sim s(\cdot \mid c_{\text{pw}})$ and $\tilde{s} \sim s(\cdot \mid c)$ with $\tilde{s} \ll \hat{s}$; (2) a novel **circuit-broken** variant applied on top, using loss $L_{\text{CB}} = \text{ReLU}(\cos\_\text{sim}(\text{rep}_{p_{\theta_{\text{CB}}}}(c), \text{rep}_{p_\theta}(c)))$ on no-password inputs and $L_{\text{retain}} = \|\text{rep}_{p_{\theta_{\text{CB}}}}(c) - \text{rep}_{p_\theta}(c)\|_2$ on password inputs. Elicitation techniques evaluated: N-shot prompting (N=1,3,5,10), response prefilling, multi-turn jailbreak, concept/persona activation steering (contrastive vectors at mid-layers 8–15 / 12–19), SFT, and anti-refusal SFT.

## Result
Password-locked Mistral-base on WMDP: 13.5% (0-shot) → 58.1% (5-shot), vs 58.4% with password. Circuit-broken counterpart: 0.8% (0-shot) → 33.8% (10-shot) for N-shot alone, but 61.1% with prefilling. On APPS code generation, circuit-broken organism resists N-shot (≤4.5%) and prefilling (≤7%); only SFT (and anti-refusal SFT, which uses no code data) recovers capability. Steering is consistently weaker than prompting and highly hyperparameter-sensitive. Practical recommendation: use fine-tuning when feasible; otherwise combine prompting techniques.

## Why it matters here
General background; no direct arena tie. Relevant only as agent-safety context (model-organism methodology, hidden-capability elicitation) — orthogonal to math-optimization problems on the einstein arena.

## Open questions / connections
- Can circuit-breaking-style robustness training be adapted to *positively* elicit latent reasoning capabilities (inverse use of the loss)?
- Why does anti-refusal training transfer to code generation despite zero code data — what shared representation does it unblock?
- Extends Greenblatt et al. (2024) password-locking and Zou et al. (2024) circuit-breaking; leaves open whether circuit-broken models can be made robust to *combined* prompting + fine-tuning attacks.
- Steering vectors underperform prompting — open whether better steering-vector construction (Tan et al. 2024 reliability work) closes the gap.

## Key terms
capability elicitation, model organisms, password-locking, circuit-breaking, sandbagging, activation steering, contrastive steering vectors, anti-refusal training, few-shot prompting, response prefilling, WMDP, MMLU, APPS, supervised fine-tuning, AI safety evaluations
