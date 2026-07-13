<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning"
authors: [Wanjia Zhao, Mert Yuksekgonul, Shirley Wu, James Zou]
year: 2025
doi: 10.48550/arXiv.2502.04780
source_url: https://doi.org/10.48550/arXiv.2502.04780
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning

## TL;DR
SiriuS optimizes multi-agent LLM systems by building an "experience library" of reasoning trajectories that lead to correct outcomes, then fine-tuning each role-specialized agent on those trajectories — sidestepping the multi-agent credit-assignment problem and boosting accuracy by 2.86–21.88% on reasoning, biomedical QA, and negotiation tasks.

## Key findings
- **Core mechanism — bootstrapped trajectory library.** When a multi-agent team solves a task correctly (reward `R(s,a) > ε`), the *entire* interaction trajectory is retained as training data for each agent, on the premise that successful joint trajectories contain useful collaboration patterns even without pinpointing which step mattered. This avoids per-step supervision and the RL-style credit-assignment problem (parallels Foerster et al. 2018), extending STaR (Zelikman et al. 2022) from single-agent to multi-agent.
- **Trajectory augmentation for failures.** Failed trajectories are recovered: an external/critic agent generates feedback grounded in the ground-truth answer, the target agent regenerates a corrected solution, and the result is **rephrased to look as if solved directly** (no traces of correction) before re-entering the library. This enlarges otherwise-small good-trajectory sets.
- **Performance (Table 3, Problem-Solving).** On GPT-4o-mini: College Physics 39.25→46.73%, College Chemistry 41.54→60.00%, PubMedQA 67.40→73.40%. On GPT-3.5-turbo: Chemistry 38.46→56.92%, PubMedQA 56.40→74.20%. SiriuS consistently beat Single-Agent, STaR, CoMM (prompted multi-agent), and TextGrad.
- **TextGrad failure mode.** On long-context PubMedQA, TextGrad's optimizer could not parse instructions (GPT-3.5-turbo) or produce required-format answers (GPT-4o-mini), showing prompt-optimization fragility on weaker models / long contexts.
- **Actor-Critic setting (Table 5).** Adds a Judgment Agent (classifies correct/incorrect) plus a Critic (feedback without seeing the answer). SiriuS lifted GPT-3.5-turbo TP accuracy 11.80(Self-Correct)/18.40(Prompt)→35.00% and overall accuracy to 50.60%; GPT-4o-mini reached 59.80% TP / 66.80% overall. The Judgment Agent is the load-bearing component — replacing it with a base version sharply drops TP accuracy. Naive Self-Correct hurts because it modifies nearly all responses, corrupting initially-correct ones (cf. Kumar et al. 2024).
- **Competitive/negotiation settings (NegotiationArena).** Across Resource Exchange, Multi-Turn Ultimatum, and Seller-Buyer, SiriuS raised win rate and payoff as the advantaged player and reduced losses as the disadvantaged player. As Ultimatum Player 1 it secured larger splits; as Seller it improved from losing to consistently closing at 50 (a tie). Gains generalized to held-out initial-resource configs (e.g. 25/5 → 35/15; Resource=100 → 1000).
- **Ablations (Table 4).** (1) Mixing a SiriuS agent with a base agent degrades performance → joint multi-agent optimization matters. (2) Fine-tuning one shared LLM for all roles underperforms role-specific models → roles need specialized adaptation. (3) Removing augmentation lowers accuracy. (4) An extra fine-tuning iteration gave marginal further gains.

## Methods (brief)
Multi-agent system formalized as a directed communication graph `⟨S,A,T,R,N,G⟩` with topologically ordered, role-specialized LLM agents (e.g., Physicist → Mathematician → Summarizer; Context Analyst → Problem Solver). Per iteration: sample joint actions, threshold by reward to build per-agent good-trajectory sets, augment failures via feedback+regeneration+rephrasing, then standard SFT on each agent via OpenAI's fine-tuning API (GPT-3.5-turbo-0125, GPT-4o-mini, temperature 0). Datasets: College Physics/Chemistry (from MMLU/GPQA/TheoremQA, 2:1 train/test) and PubMedQA (500/500).

## Limitations
Evaluated only on GPT-3.5-turbo and GPT-4o-mini (no frontier/open models) and modest test splits (≤500). Requires ground-truth answers for the failure-augmentation step, limiting applicability where labels are unavailable. The rephrasing step deliberately hides correction provenance, and additional fine-tuning iterations yield diminishing returns.

## Citations of interest
- Zelikman et al. 2022 (STaR) — bootstrapping reasoning via self-generated rationales; SiriuS's single-agent ancestor.
- Yuksekgonul et al. 2024 (TextGrad) — natural-language "gradient" prompt optimization baseline.
- Chen et al. 2024a (CoMM) — training-free collaborative multi-agent prompting baseline.
- Bianchi et al. 2024 (NegotiationArena) — platform for the competitive negotiation tasks.
- Jin et al. 2019 (PubMedQA) — biomedical yes/no QA benchmark used throughout.
- Foerster et al. 2018 — counterfactual multi-agent policy gradients; framing for the credit-assignment problem.
- Kumar et al. 2024 — out-of-the-box LLM self-correction is unreliable without specialized training.
