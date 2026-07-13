<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors: [Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao]
year: 2022
source_url: https://arxiv.org/abs/2210.03629
drive_file_id: 1mXPCiS3FiIK72gXp5zTsdlMk0cUOlfep
text_source: pdf
ingested_by: agent
---

# ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2210.03629

## One-line
Interleaving verbal reasoning traces with task-specific actions in LLM prompts lets each improve the other, outperforming reasoning-only or acting-only prompting on QA, fact verification, and interactive decision-making tasks.

## Key claim
Augmenting an agent's action space with a "language" action (a thought $\hat{a}_t \in \mathcal{L}$ that updates context but doesn't touch the environment) lets reasoning and acting synergize: reasoning traces help induce, track, and revise action plans and handle exceptions, while actions let the model retrieve grounding information from external sources (e.g. Wikipedia), reducing hallucination relative to chain-of-thought (CoT) alone.

## Method
Few-shot in-context prompting of a frozen PaLM-540B with human-written trajectories that interleave Thought/Act/Observation steps ($c_{t+1} = (c_t, \hat{a}_t)$). For knowledge-intensive tasks (HotpotQA, FEVER), the action space is a 3-action Wikipedia API: `search[entity]` (returns first 5 sentences of the page or top-5 similar entities), `lookup[string]` (Ctrl+F-style next-sentence match), and `finish[answer]`. For decision-making tasks (ALFWorld, WebShop), thoughts are used sparsely (only where useful) rather than at every step, since actions dominate the trajectory. Baselines ablate ReAct trajectories into Standard (no thoughts/actions/observations shown), CoT (thoughts only, no environment interaction), CoT-Self-Consistency (21 sampled CoT trajectories, majority vote), and Act-only (actions without thoughts). A combined strategy lets the model back off from ReAct to CoT-SC (if ReAct returns no answer within 7 steps for HotpotQA / 5 for FEVER) or from CoT-SC to ReAct (if the majority answer occurs in fewer than n/2 of n samples). Also tests fine-tuning PaLM-8B/62B on 3,000 bootstrapped ReAct-generated trajectories with correct answers.

## Result
On HotpotQA (EM) / FEVER (Acc) with PaLM-540B: Standard 28.7/57.1, CoT 29.4/56.3, CoT-SC 33.4/60.4, Act 25.7/58.9, ReAct 27.4/60.9, CoT-SC→ReAct 34.2/64.6, ReAct→CoT-SC 35.1/62.0 (best overall combo), vs. supervised SoTA 67.5/89.5. On ALFWorld and WebShop, ReAct outperforms imitation/RL baselines trained on $10^3$–$10^5$ task instances by an absolute success-rate improvement of 34% and 10% respectively, using only 1–2 in-context examples. Manual error analysis of 50 correct + 50 incorrect HotpotQA trajectories per method shows CoT has much higher hallucination-driven false positives than ReAct (14% vs. 6%) and hallucination is 56% of CoT's failure mode vs. 0% for ReAct; ReAct's main failure mode is reasoning error (47%) and uninformative search results (23%). Fine-tuning: with only 3,000 examples, PaLM-8B ReAct becomes the best of the four fine-tuned methods, surpassing all PaLM-62B prompting methods.

## Key terms
ReAct, chain-of-thought (CoT), reasoning traces, thought-action-observation, interleaved reasoning and acting, few-shot in-context prompting, Wikipedia API tool use, hallucination, HotpotQA, FEVER, ALFWorld, WebShop, self-consistency (CoT-SC), PaLM-540B
