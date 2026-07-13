<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-drug-discovery]
title: "Robin: A multi-agent system for automating scientific discovery"
authors: [Ali E. Ghareeb, Benjamin Chang, L. Mitchener, Angela Yiu, Caralyn J. Szostkiewicz, Jon M. Laurent, Muhammed Razzak, Andrew D. White, Michaela M. Hinks, S. Rodriques]
year: 2025
source_url: https://arxiv.org/abs/2505.13400
drive_file_id: 1NRO-VBBTe8TayZlJE4qOOhIEAZWqg6ZC
text_source: paperclip
ingested_by: agent
---

# Robin: A multi-agent system for automating scientific discovery

**Authors:** Ali E. Ghareeb, Benjamin Chang, L. Mitchener, Angela Yiu, Caralyn J. Szostkiewicz, Jon M. Laurent, Muhammed Razzak, Andrew D. White, Michaela M. Hinks, S. Rodriques  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.13400

## One-line
Robin is a multi-agent LLM system that automates the full scientific-discovery loop — literature-based hypothesis generation, experimental design, and data analysis — demonstrated by discovering ripasudil as a novel dry-AMD drug-repurposing candidate.

## Key claim
A coordinated trio of LLM agents (Crow + Falcon for literature, Finch for data analysis) can autonomously propose, refine, and validate therapeutic hypotheses in an iterative lab-in-the-loop cycle; applied to dAMD it nominated ROCK inhibition of RPE phagocytosis and identified ripasudil, which produced a 7.5-fold phagocytosis increase vs DMSO (1.75× by human re-analysis) and revealed ABCA1 upregulation (3-fold, adj. $p = 2.13\times10^{-83}$) as a novel mechanistic target.

## Method
Pipeline of OpenAI o4-mini (hypothesis synthesis) + Claude 3.7 Sonnet (pairwise LLM-judge tournament) + PaperQA2-based retrieval agents (Crow shallow, Falcon deep) + Finch (Aviary-framework Jupyter agent) for raw flow-cytometry/RNA-seq analysis. Diversity is exploited by launching ~10 independent Finch trajectories per dataset and synthesizing a consensus meta-analysis. Workflow: disease → 10 mechanism hypotheses → ranked assay → 30 drug candidates → ranked tournament → wet-lab test → Finch analysis → next-round hypotheses.

## Result
On dAMD, Robin reviewed ~151 + ~400 papers, selected an RPE phagocytosis assay, top-ranked Y-27632 (ROCKi) which was experimentally confirmed, then in round 2 nominated ripasudil with the largest measured effect among 11 tested compounds. RNA-seq follow-up (also Robin-proposed) found ROCKi-induced upregulation of actin-organization, small-GTPase, and autophagy GO terms, plus a strong ABCA1 upregulation linking the mechanism to known dAMD lipid-handling pathology. LLM-judge selected on average 7.25/10 of human experts' top hypotheses and showed higher inter-trial consistency than human reviewers.

## Key terms
multi-agent LLM, scientific discovery automation, hypothesis generation, drug repurposing, PaperQA2, Crow, Falcon, Finch, Aviary framework, LLM-judge tournament, consensus meta-analysis, lab-in-the-loop, ROCK inhibitor, ripasudil, ABCA1, dry age-related macular degeneration
