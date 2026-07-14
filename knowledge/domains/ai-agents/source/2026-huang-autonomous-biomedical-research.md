<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-foundation-models, bio-multiomics, bio-drug-discovery, bio-protein-design]
title: "Autonomous biomedical research with an artificial intelligence agent"
authors: [Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Ryan Li, Yusuf Roohani, Lin Qiu, Shiyi Cao, Gavin Li, Junze Zhang, Di Yin, Rick Wierenga, Deniz Kavi, Sherry Liu, Tianwei She, Shruti Marwaha, Jennefer N. Carter, Xin Zhou, Matthew T. Wheeler, Jonathan A. Bernstein, Mengdi Wang, Peng He, Jingtian Zhou, Michael P. Snyder, Le Cong, Aviv Regev, Jure Leskovec]
year: 2026
doi: 10.1126/science.adz4351
source_url: https://doi.org/10.1126/science.adz4351
drive_file_id: 1Yh6D9Pram1SEZQnC1IWDmx56QQ3Xu4SM
text_source: pdf
ingested_by: claude-opus-4-8
---

# Autonomous biomedical research with an artificial intelligence agent

**Authors:** Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, et al.; Le Cong, Aviv Regev, Jure Leskovec (corresponding: Huang, Leskovec)
**Year:** 2026
**Venue:** Science (10.1126/science.adz4351; first release 9 July 2026)

## Abstract

Biomni is a general-purpose biomedical AI agent that autonomously executes diverse research
tasks. An action-discovery agent mines tools, databases, and protocols from thousands of
publications across 25 domains to build a unified agentic environment. The architecture
couples LLM reasoning with retrieval-augmented planning and code-based execution, composing
workflows dynamically without predefined templates. It generalizes across heterogeneous tasks
— causal gene prioritization, drug repurposing, rare-disease diagnosis, microbiome analysis,
molecular cloning — with no task-specific tuning, and case studies show it interpreting
multi-modal data, optimizing protein stability, orchestrating wet-lab instruments, and
generating experimentally testable protocols.

## Key contributions

- **Biomni-E1 environment:** an action-discovery LLM read the 100 most-recent papers × 25
  bioRxiv categories (2,500 papers) and extracted a unified action space — **150 verified
  specialized tools, 105 software packages, 59 databases** (Python/R/CLI; DBs exposed as one
  NL→query function per DB).
- **Biomni-A1 agent architecture** (general-purpose, no hardcoded per-task workflows): three
  innovations — (1) LLM-based **resource selection/retrieval** of a tailored tool/DB subset;
  (2) **code as a universal action interface** (loops, parallelism, conditionals, heterogeneous
  resource interleaving); (3) **adaptive planning** that iteratively refines an initial plan.
- **Biomni-R0:** an RL-trained open-source model that optimizes end-to-end task success by
  direct interaction with Biomni-E1 using expert-annotated rewards.

## Methods

Given a query, the agent retrieves relevant tools/DBs/software, generates a step-by-step plan
grounded in domain knowledge, and expresses each step as executable code, refining the plan
during execution. Databases split into API-accessible relational stores (PDB, OpenTarget,
ClinVar — unified per-DB NL query function) and locally preprocessed flat-file "data lake"
stores. RL (Biomni-R0) hill-climbs specialized tasks where zero-shot underuses the environment.

## Key results

- **Biomni-Eval1** (443 queries, 10 tasks): **57% avg**, vs base Claude Sonnet 4.5 30%, TxAgent
  25%, Claude Code 43%, ReAct+E1 44%.
- **HLE-Bio:** the A1 scaffold adds **6–12 pts** over LLM-only across multiple frontier
  backbones (gains attributed to scaffold+E1, not one model).
- **Expert parity, far faster:** single-cell RNA-seq annotation 45.8% (experts 40.5–50.9%;
  230→75 min); rare-disease dx 60% (experts 60–70%; 110→3 min); GWAS causal-gene 80% (90→4
  min/locus).
- **RL (Biomni-R0):** 8B 0.32→0.59 (beats Claude 4 Sonnet 0.56), 32B 0.35→0.67 (+10 pts from
  scaling).
- **Case studies:** (1) wearable chronobiology — 1,027-participant Fitbit COVID cohort (1.4B
  HR + 37M step records), reproduced 6 biomarkers + risk score (r=−0.34, r=+0.54 recovered);
  (2) skeletal multi-omics GRN — 336,162-cell snRNA/snATAC, recapitulated RUNX2/HHIP regulation
  and nominated AUTS2/ZFHX3/PBX1 regulators; (3) wet-lab-validated cloning — B2M sgRNA into
  lentiCRISPR v2, Golden Gate protocol executed, sequencing showed perfect alignment; (4)
  protein thermostability — AlphaFold2+ThermoMPNN pipeline, mutations Q83I/C66F/C110F, −4.108
  kcal/mol at 98% identity; (5) PyLabRobot orchestration of Hamilton STAR liquid handlers.

## Limitations / open questions

- Performance is **uneven** across tasks; not expert-level across the board; still weak on
  nuanced clinical judgment, experimental reasoning, and deep biological synthesis.
- **Recency bias:** action discovery used only the most-recent papers, risking omission of
  foundational-but-faded methods.
- Complex multi-step workflows (e.g. scRNA–scATAC multi-omics) need **structured prompts** with
  explicit intermediate steps — limits generalizability of high-level prompting.
- **Biosecurity:** agentic literature synthesis + protocol generation could lower misuse
  barriers; authors mitigate via academic-only tools, open-source transparency, policy engagement.
- Future: self-improvement via RL, multi-modal inputs, autonomous tool/DB discovery.
