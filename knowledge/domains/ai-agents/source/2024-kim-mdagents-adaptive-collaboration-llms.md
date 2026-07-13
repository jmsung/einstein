<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-clinical]
title: "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making"
authors: [Y. Kim, Chanwoo Park, H. Jeong, Yik Siu Chan, Xuhai Xu, Daniel McDuff, C. Breazeal, Hae Won Park]
year: 2024
source_url: https://arxiv.org/abs/2404.15155
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
multi-agent LLM, medical decision-making, complexity triage, multidisciplinary team, integrated care team, moderator agent, recruiter agent, chain-of-thought, self-consistency, role-playing, multi-agent debate, council dispatch
