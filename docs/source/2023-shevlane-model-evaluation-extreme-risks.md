---
type: source
kind: paper
title: Model evaluation for extreme risks
authors: Toby Shevlane, Sebastian Farquhar, Ben Garfinkel, Mary Phuong, Jess Whittlestone, Jade Leung, Daniel Kokotajlo, Nahema Marchal, Markus Anderljung, Noam Kolt, Lewis Ho, Divya Siddarth, S. Avin, W. Hawkins, Been Kim, Iason Gabriel, Vijay Bolina, Jack Clark, Y. Bengio, P. Christiano, Allan Dafoe
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.15324
source_local: ../raw/2023-shevlane-model-evaluation-extreme-risks.pdf
topic: general-knowledge
cites:
---

# Model evaluation for extreme risks

**Authors:** Toby Shevlane, Sebastian Farquhar, Ben Garfinkel, Mary Phuong, Jess Whittlestone, Jade Leung, Daniel Kokotajlo, Nahema Marchal, Markus Anderljung, Noam Kolt, Lewis Ho, Divya Siddarth, S. Avin, W. Hawkins, Been Kim, Iason Gabriel, Vijay Bolina, Jack Clark, Y. Bengio, P. Christiano, Allan Dafoe  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.15324

## One-line
A position paper arguing that frontier AI developers must build "dangerous capability evaluations" and "alignment evaluations" to detect extreme risks before training, deployment, and proliferation.

## Key claim
Model evaluation should be embedded as critical governance infrastructure for frontier AI: developers must evaluate models for (a) dangerous capabilities (cyber-offense, deception, persuasion, weapons acquisition, long-horizon planning, AI development, situational awareness, self-proliferation) and (b) misalignment propensity (power-seeking, shutdown-resistance, goal-misgeneralization, collusion), with results feeding training/deployment/security decisions.

## Method
Conceptual framework paper, not empirical. Proposes a taxonomy of dangerous capabilities (Table 1) and alignment-failure behaviors, a workflow embedding evaluations into training-risk-assessment, deployment-risk-assessment, transparency, and security pipelines, and a list of design criteria (comprehensiveness, fault-finding, robustness to deception, surfacing latent capabilities, mechanistic + behavioral) for an evaluation portfolio.

## Result
No numerical theorems; the deliverables are (i) the dangerous-capability taxonomy with 9 categories, (ii) a 4-pillar governance blueprint (responsible training, responsible deployment, transparency, appropriate security), (iii) a list of 6 limitations (factors beyond the model, unknown threat models, capability overhang, deceptive alignment, emergence, overtrust) and 4 hazards of doing evals (proliferation of capabilities, competitive pressure, superficial Goodharted safety, harms during evaluation).

## Why it matters here
General background; no direct arena tie. Relevant only as meta-context for the einstein agent's own self-evaluation discipline — the paper's "robust to deception," "surfacing latent capabilities," and "Goodharted superficial safety" warnings parallel this repo's triple-verify and cycle-discipline rules against optimizing toward the evaluator rather than ground truth.

## Open questions / connections
- What combinations of dangerous capabilities are jointly most dangerous (paper flags as open).
- How to build alignment evaluations that rule out deceptive alignment in situationally-aware models — paper has no proposed solution.
- How to do scaling-law forecasting of emergent capabilities when emergence is by definition discontinuous.
- Connects to: Ngo et al. (alignment problem from deep learning), Perez et al. (model-written evals), ARC Evals (self-proliferation evals on GPT-4/Claude).

## Key terms
dangerous capability evaluation, alignment evaluation, frontier model, deceptive alignment, situational awareness, capability overhang, self-proliferation, power-seeking, red teaming, model audit, emergent capabilities, AI governance
