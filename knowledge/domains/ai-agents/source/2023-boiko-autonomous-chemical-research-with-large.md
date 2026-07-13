<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Autonomous chemical research with large language models
authors: [Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes]
year: 2023
doi: 10.1038/s41586-023-06792-0
source_url: https://doi.org/10.1038/s41586-023-06792-0
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Autonomous chemical research with large language models

## TL;DR
Coscientist is a GPT-4-driven multi-LLM agent that autonomously designs, plans, and executes chemistry experiments by combining web search, documentation retrieval, sandboxed code execution, and robotic-lab APIs — demonstrated across six tasks including the successful physical execution and optimization of Pd-catalysed Suzuki–Miyaura and Sonogashira cross-couplings.

## Key findings
- **Architecture (Fig. 1).** A central GPT-4 "Planner" acts over four commands — `GOOGLE`, `PYTHON`, `DOCUMENTATION`, `EXPERIMENT` — each backed by a module (Web searcher LLM, isolated Docker code executor, vector-search docs retriever, automation API). Command outputs are fed back as user messages; the Planner can self-correct code on errors.
- **Synthesis planning (Fig. 2).** On a 7-compound benchmark scored 1–5, the GPT-4 Web Searcher hit maximum scores for acetaminophen, aspirin, nitroaniline, and phenolphthalein, and was the only system reaching the ≥3 acceptable threshold for ibuprofen. All non-browsing models (GPT-3.5, GPT-4, Claude 1.3, Falcon-40B) failed ibuprofen; grounding via search reduced hallucinated routes (e.g. avoiding non-selective direct nitration of aniline).
- **Documentation retrieval (Fig. 3).** OT-2 API and Emerald Cloud Lab (ECL) Symbolic Lab Language docs were embedded with OpenAI `ada`; distance-based vector search supplied the Planner with API usage it lacked from pretraining. Generated ECL `ExperimentHPLC` SLL code ran successfully in a real cloud lab (caffeine standard); prompt-to-samples surfaced relevant stock solutions from a 1,110-sample catalogue.
- **Hardware control (Fig. 4).** From natural-language prompts ("colour every other row"), Coscientist wrote correct OT-2 protocols and, integrating a UV-Vis plate reader, solved a color-identification task across a 96-well plate — though it needed a guiding prompt to reason about absorbance wavelengths.
- **Integrated cross-coupling (Fig. 5).** Given source/target plates with reagents, two catalysts, two bases, and solvent, Coscientist searched the web for conditions, selected chemically correct coupling partners (never picking phenylboronic acid for Sonogashira), computed volumes, wrote OT-2 code, recovered from a wrong heater–shaker method name via the docs searcher, and ran reactions. GC–MS confirmed biphenyl (Suzuki, 9.53 min) and the tolane product (Sonogashira, 12.92 min). Notably used the heater–shaker module released *after* GPT-4's training cutoff.
- **Optimization as reasoning (Fig. 6).** Treated condition optimization as a 20-iteration yield-maximization game (5.2%/6.9% of two full reaction spaces — Perera Suzuki flow dataset; Doyle Buchwald–Hartwig). Scored by normalized advantage (1 = max yield, 0 = random). GPT-4 increased normalized advantage over iterations and exceeded standard Bayesian optimization (whose normalized advantage stayed near zero); prior info improved initial guesses but converged to the same NMA. GPT-3.5 mostly failed the required JSON schema. GPT-4 reasoned about reactivity even from raw SMILES strings (Fig. 6g).

## Methods (brief)
Multi-LLM agent built on GPT-4 chat completions with modular engineered system prompts defining a 4-command action space; ada-embedding vector search over API docs; sandboxed Docker Python execution (RDKit, NumPy). Physical validation via Opentrons OT-2 liquid handler + heater–shaker + UV-Vis, and ECL cloud lab; products confirmed by GC–MS. Optimization benchmarked against Bayesian optimization on two fully-mapped literature reaction datasets.

## Limitations
Proof of concept; "semi-autonomous" (plates moved manually, no human decision-making). Optimization tasks are lookup-table games over pre-mapped datasets, so possible training-data contamination is unverifiable; synthesis scoring (1–5) is acknowledged as subjective. Data/code/prompts withheld pending US AI regulation; only a simplified reproduction is released. Authors flag dual-use safety concerns.

## Citations of interest
- ChemCrow (Bran et al., 2023) — parallel work augmenting LLMs with chemistry tools.
- ReAct (Yao et al., ICLR) — synergizing reasoning and acting in LLMs, a core prompting strategy.
- GPT-4 Technical Report (OpenAI, 2023) — the underlying model.
- Perera et al., Science 2018 — automated nanomole-scale flow reaction-screening dataset used for optimization.
- Ahneman/Doyle et al., Science 2018 — ML prediction of C–N cross-coupling, the Buchwald–Hartwig benchmark dataset.
- Burger et al., Nature 2020 — mobile robotic chemist, prior autonomous-lab work.
