<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation"
authors: [Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak, James Zou]
year: 2024
doi: 10.1101/2024.11.11.623004
source_url: https://www.biorxiv.org/content/10.1101/2024.11.11.623004v1
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation

## TL;DR
The Virtual Lab is an AI-human research framework where an LLM principal-investigator agent leads a team of specialized LLM agents (and a critic) through structured "meetings" to do open-ended interdisciplinary science; applied to nanobody design, it built an ESM→AlphaFold-Multimer→Rosetta pipeline that produced 92 mutant nanobodies, two of which gained experimentally-validated binding to recent SARS-CoV-2 variants (JN.1, KP.3) while retaining ancestral binding.

## Key findings
- **Architecture.** A human supplies high-level agendas; an LLM PI agent (GPT-4o here) auto-creates scientist agents — each defined by *title, expertise, goal, role* — and runs two meeting types: **team meetings** (all agents discuss broad direction over N≈3 rounds, PI synthesizes each round and summarizes) and **individual meetings** (one agent does a specific task, optionally critiqued by a **Scientific Critic** agent). For this project the PI created an Immunologist, a Machine Learning Specialist, and a Computational Biologist.
- **Parallel meetings + merge.** Each meeting is run 5× in parallel at high "creative" temperature (0.8), then a single merge meeting at low "consistent" temperature (0.2) fuses the best elements — a more flexible analogue to majority voting.
- **Design decisions made by agents.** Agents chose to (1) design *nanobodies* over antibodies, (2) *modify existing* nanobodies rather than de novo, and (3) start from four anti-Wuhan-RBD nanobodies: **Ty1, H11-D4, Nb21, VHH-72**. Tools selected: **ESM** (ESM-1b, log-likelihood ratio for point mutations), **AlphaFold-Multimer** (interface pLDDT, ipLDDT), and **Rosetta** (dG-separated binding energy, REF15 scoring).
- **Pipeline.** Per nanobody: ESM ranks all point mutations → top 20 → AlphaFold-Multimer + Rosetta → combined **weighted score** (WS = ESM LLR + AF ipLDDT − Rosetta dG, PI correctly used a negative Rosetta weight) → top 5 advance; 4 rounds of iterative mutation, then top 23 selected per nanobody via an ESM-LLR computed against wild-type (LLR_WT). **92 total designs** (23 × 4).
- **Computational metrics.** All 92 had positive ESM LLR; 78/92 (85%) improved AF ipLDDT vs wild-type, 32 (35%) reached ipLDDT ≥ 80; 60 (65%) improved Rosetta dG, 23 (25%) reached dG ≤ −50.
- **Experimental validation.** Expressed in *E. coli*; ~94% expressed/soluble (only 6.5% poor), 38% high/very-high expression. By indirect ELISA against an RBD panel (Wuhan, BA.2, JN.1, KP.2.3, KP.3): H11-D4/Nb21 series retained Wuhan binding in 96% (44/46); Ty1 mutants tolerated mutation poorly (10/23 retained Wuhan). **Two standout designs**: Nb21 I77V-L59E-Q87A-R37Q gained JN.1 binding (and some KP.3 binding, intensity ~3.5 vs ~0.1 wild-type), and Ty1 V32F-G59D-N54S-F32S gained JN.1 binding while improving Wuhan binding. Authors attribute gained variant binding to AlphaFold/Rosetta (antigen-aware) and propose introduced negative charges (L59E, R37Q, G59D) form favorable electrostatics with positively-charged variant RBD mutations (e.g. E484K).
- **Human effort.** Agents wrote 122,462 words (98.7%); the human wrote only 1,596 (1.3%). Each meeting took ~5–10 min.

## Methods (brief)
Multi-agent LLM orchestration (GPT-4o) via structured team/individual meetings with parallel-meeting merging. Computational design used ESM-1b, AlphaFold-Multimer (LocalColabFold 1.5.5), and Rosetta (REF15). Validation: nanobodies expressed in *E. coli* periplasm; RBDs (JN.1/KP.3/KP.2.3/BA.2/Wuhan) expressed in Expi293; binding by multiplexed indirect ELISA on a printed RBD antigen array.

## Limitations
n=92 designs from 4 templates with only one to four mutations; only two showed novel-variant binding, and that binding was moderate (EC50 ~10⁻⁵ vs ~10⁻⁶ for Wuhan). LLM knowledge-cutoff caused use of older tools (AlphaFold-Multimer not AF3) and buggy code requiring human-flagged corrections; agents avoided hard decisions without explicit "choose only one" prompting. AlphaFold/Rosetta scoring is itself imperfect, so correct usage does not guarantee accurate binding prediction.

## Citations of interest
- Hie et al. 2024 (Nat. Biotechnol.) — efficient antibody evolution from protein language models; the closest prior method (Virtual Lab differs in LLR numerator and uses only ESM-1b).
- Evans et al. 2021 — AlphaFold-Multimer, used for complex structure prediction.
- Lin et al. 2023 (Science) — ESM evolutionary-scale protein language model.
- Yin & Pierce 2024 — AlphaFold antibody-antigen modeling evaluation; basis for ipLDDT thresholds.
- Boiko et al. 2023 (Coscientist) and Lu et al. 2024 (AI Scientist) — prior LLM-for-science frameworks the Virtual Lab contrasts against.
- Wu et al. 2023 (AutoGen) — multi-agent LLM conversation framework.
