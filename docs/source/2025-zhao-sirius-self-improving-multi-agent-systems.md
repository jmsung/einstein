---
type: source
kind: paper
title: SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning
authors: Wanjia Zhao, Mert Yuksekgonul, Shirley Wu, James Zou
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.04780
source_local: ../raw/2025-zhao-sirius-self-improving-multi-agent-systems.pdf
topic: general-knowledge
cites: 
---

# SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning

**Authors:** Wanjia Zhao, Mert Yuksekgonul, Shirley Wu, James Zou  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.04780

## One-line
A self-improvement framework that fine-tunes each agent in a multi-agent LLM system on its own successful reasoning trajectories, with feedback-driven augmentation of failed ones.

## Key claim
Bootstrapped supervised fine-tuning on retained successful multi-agent trajectories (plus rephrased corrections of failures) improves reasoning / biomedical QA accuracy by 2.86%–21.88% over single-agent, STaR, CoMM, and TextGrad baselines, and strengthens negotiation outcomes in competitive games.

## Method
Define the system as $\langle S, A, T, R, N, G\rangle$ with $N$ LLM agents on a directed interaction graph $G$. At each iteration: (1) sample joint trajectories $a_i^{(n)} \sim P_{\theta^{(n)}}(\cdot \mid x_i, a_i^{\mathrm{Pre}(A^{(n)})})$; (2) keep trajectories whose outcome reward $R_i(s,a) > \epsilon$ into a per-agent "experience library" $C_t^{(n)}$; (3) for failed trajectories, an external feedback agent (with ground truth) produces critique $f_i$, the agent regenerates $\hat a_i^{r}$, and the result is *rephrased* to look like a direct solution before being added; (4) standard SFT per agent on $C_t^{(n)}$. Three system topologies are tested: sequential expert pipelines (Physicist→Mathematician→Summarizer), Actor-Judgment-Critic, and two-player competitive games.

## Result
On College Physics, College Chemistry, and PubMedQA, SIRIUS beats the strongest baseline by 1–10 points (e.g. GPT-4o-mini PubMedQA 73.4 vs CoMM 70.6; College Chemistry 60.0 vs 49.2). In the Actor-Critic setting, TP-accuracy jumps from 18.4→35.0 (GPT-3.5) and 51.6→59.8 (GPT-4o-mini), with the Judgment Agent being the most load-bearing component (ablation: replacing it drops TP accuracy most). In competitive games (Resource Exchange, Ultimatum, Seller-Buyer), SIRIUS-trained players raise win rate and payoff vs base opponents and generalize to unseen resource scales (100→1000, 25/5→35/15).

## Why it matters here
General background; no direct arena tie. Relevant to the einstein agent's **council-dispatch + self-improvement-loop architecture** — SIRIUS is a concrete recipe for *learning from outcome-only reward* across a multi-agent pipeline, which is exactly the credit-assignment problem when personas (Gauss, Tao, Cohn, …) collaborate on a math problem and only the final triple-verified score is graded. The "rephrase regenerated answers so they look first-pass" trick is directly applicable to wiki-finding distillation from failed cycles.

## Open questions / connections
- Extends STaR (Zelikman 2022) from single-agent to multi-agent; complements TextGrad (Yuksekgonul 2024) which optimizes prompts rather than weights.
- Joint-fine-tune vs single-shared-LLM ablation shows specialization wins — supports per-persona fine-tuning rather than one model with role prompts.
- Augmentation requires ground-truth feedback agent — open how to apply when ground truth is unknown (the actual arena case where score is the only signal).
- Marginal gains from extra fine-tuning iterations — diminishing returns suggest the experience library saturates quickly.

## Key terms
multi-agent systems, bootstrapped reasoning, experience library, supervised fine-tuning, credit assignment, actor-critic, STaR, trajectory augmentation, self-improvement, LLM negotiation, judgment agent, rephrasing, PubMedQA, outcome reward
