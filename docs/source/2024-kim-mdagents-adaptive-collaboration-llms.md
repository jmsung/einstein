---
type: source
kind: paper
title: "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making"
authors: Y. Kim, Chanwoo Park, H. Jeong, Yik Siu Chan, Xuhai Xu, Daniel McDuff, C. Breazeal, Hae Won Park
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2404.15155
source_local: ../raw/2024-kim-mdagents-adaptive-collaboration-llms.pdf
topic: general-knowledge
cites:
---

# MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making

**Authors:** Y. Kim, Chanwoo Park, H. Jeong, Yik Siu Chan, Xuhai Xu, Daniel McDuff, C. Breazeal, Hae Won Park  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.15155

## One-line
A multi-agent LLM framework that triages each medical query into low / moderate / high complexity and dispatches a single PCP, an MDT, or an ICT accordingly.

## Key claim
Adaptive complexity-based routing of LLM collaboration beats fixed solo and group baselines on 7 of 10 medical benchmarks, with up to +4.2% accuracy ($p<0.05$); moderator review + external knowledge in group mode adds +11.8% average accuracy.

## Method
A moderator LLM classifies query complexity (low/moderate/high) using clinical constructs (acuity, comorbidity, severity). A recruiter LLM then assembles either a single Primary Care Clinician agent (CoT/Self-Consistency prompting), a Multi-Disciplinary Team running an $R$-round, $T$-turn iterative consensus discussion, or an Integrated Care Team of multiple specialist teams whose reports are synthesized in a final review step.

## Result
MDAgents wins 7/10 benchmarks across medical-knowledge and multi-modal reasoning tasks. Pearson correlation between LLM and physician complexity ratings is low (gpt-4o-mini: $-0.09$; gpt-4: $0.07$; gemini-1.5-flash: $0.11$); physician inter-rater ICC2k $= 0.269$, ICC3k $= 0.280$ — even humans agree only moderately on complexity. Ablations show moderator review + external medical knowledge contribute the bulk of the gain (+11.8%).

## Why it matters here
General background; no direct arena tie. The framework's structure — complexity triage → recruit specialist council → multi-round consensus with moderator → final synthesis — is directly analogous to einstein's council-dispatch + math-solving-protocol rules, and could inform how the autonomous loop adaptively sizes its persona council per problem complexity.

## Open questions / connections
- Can a complexity classifier reliably triage Einstein Arena problems by category (sphere_packing vs combinatorics vs uncertainty) the way moderator triages MDM cases?
- Moderator + external-knowledge contributed +11.8% — is the analogous lever for math personas the wiki-first retrieval step, and is it the dominant gain there too?
- Static vs flexible conversation patterns (Table 1) — current council-dispatch is static (3-5 personas, one shot); does adding rounds + early-stopping like MDT help on hard arena problems?

## Key terms
multi-agent LLM, medical decision-making, complexity triage, multidisciplinary team, integrated care team, moderator agent, recruiter agent, chain-of-thought, self-consistency, role-playing, multi-agent debate, council dispatch
