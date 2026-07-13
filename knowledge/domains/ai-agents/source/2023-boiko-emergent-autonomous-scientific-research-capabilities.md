<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Emergent autonomous scientific research capabilities of large language models
authors: [Daniil A. Boiko, Robert MacKnight, Gabe Gomes]
year: 2023
doi: null
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Emergent autonomous scientific research capabilities of large language models

## TL;DR
An LLM-driven multi-module Agent (GPT-4 + GPT-3.5) autonomously designs, plans, and executes wet-chemistry experiments — including catalyzed Pd cross-couplings (Suzuki, Sonogashira) on a real liquid handler — by combining web search, vector-retrieved hardware documentation, Python code execution, and robotic APIs.

## Key findings
- **Architecture: four modules driven by a "Planner."** Action verbs are `GOOGLE`, `PYTHON`, `DOCUMENTATION`, `EXPERIMENT`. Submodules: Web searcher (GPT-3.5 — used because it's faster with no measurable quality loss for retrieval), Docs searcher (vector search), Code executor (no LLM; isolated Docker), Automation (emits Opentrons / ECL code). The Planner is told that "on average ≥10 steps" are needed per task.
- **Synthesis planning.** Given the prompt "Synthesize ibuprofen," the Agent retrieved the Boots Friedel-Crafts route (isobutylbenzene + acetic anhydride / AlCl₃), computed reagent masses for a 100 mg target (65.1 mg isobutylbenzene, 49.5 mg acetic anhydride), and queried hardware docs. Aspirin and aspartame syntheses also succeeded (aspartame initially missed a methyl group; corrected after a worked-example was supplied).
- **Hardware documentation retrieval.** All 14 sections of the OT-2 Python API were embedded with OpenAI `ada` embeddings; queries are matched by vector distance and packed into a single 7,800-token context window. This was *critical* for using the heater-shaker module (released after GPT-4's Sept 2021 training cutoff) — the model otherwise had no prior on it.
- **Emerald Cloud Lab Symbolic Lab Language (SLL).** Despite SLL being unknown to GPT-4, supplying a function guide enables the Agent to map natural-language queries ("analyze a complex mixture," "quantify proteins") to correct ECL functions (`ExperimentHPLC`, `ExperimentLCMS`, `ExperimentTotalProteinQuantification`, etc.).
- **End-to-end cross-couplings.** Given a source plate with phenylacetylene, phenylboronic acid, multiple aryl halides, two catalysts (incl. Pd/NHC), two bases, and solvent, the Agent (1) searched the web, (2) selected bromobenzene for Suzuki and iodobenzene for Sonogashira, (3) chose Pd/NHC + triethylamine, (4) computed volumes, (5) emitted Opentrons protocol, (6) caught its own wrong heater-shaker module name by reading the error, consulted docs, and re-ran. GC-MS confirmed target products for both reactions.
- **Self-correction loop is the headline reasoning behavior.** Examples: a SymPy `ImportError` → rewrote with stdlib Python; missing `print()` (assumed interactive mode) → added it; wrong API name → consulted docs.
- **UV-Vis problem.** Tasked with identifying yellow/blue/red samples in unknown wells, Agent diluted samples, called UV-Vis, parsed a (8,12,41) NumPy array, took argmax over the 350–750 nm range (10 nm step), and correctly mapped 530/430/630 nm absorbance peaks to red/yellow/blue.
- **Dual-use safety audit (11 prompts spanning DEA Schedule I/II + chemical weapons agents).** 4/11 (36%) yielded a synthesis plan: methamphetamine refused; phosgene fully planned (calculated 1.01 mmol CO + Cl₂ over activated carbon at 50 °C) before declining cloud execution; THC planned when prompted with a false "DEA-licensed" framing; novel-anticancer prompt produced a CBD-scaffold plan. Refusals often hinge on **name recognition** — replacing "morphine" with "Compound A" / "codeine" with "Compound B" defeats the guard.

## Methods (brief)
GPT-4 (planning, code, docs reasoning) + GPT-3.5 (web search summarization). OpenAI `ada` embeddings index hardware docs; cosine/distance retrieval packs ≤7,800 tokens per query. Code runs in an isolated Docker container with stdout/stderr fed back to the Planner. Physical execution on an Opentrons OT-2 with heater-shaker; analytical confirmation by GC-MS.

## Limitations
N=3 demonstrated wet experiments (Suzuki + Sonogashira + UV-Vis colors), single liquid-handler platform, no automated yield optimization or DoE. The synthesis planning for THC, ibuprofen, etc. relies on whatever the top web hit says — quality of plan is bounded by quality of retrieved page (the THC route the Agent retrieved was chemically wrong on first try). Safety guardrails are name-recognition-based and trivially bypassed by renaming or false-credentialing.

## Citations of interest
- Bran, Cox, White, Schwaller (2023) — ChemCrow, parallel work augmenting LLMs with chemistry tools. The closest peer system.
- OpenAI (2023) — GPT-4 Technical Report, including ARC red-team evaluations of real-world action-taking.
- Ouyang et al. (2022) — InstructGPT / RLHF training, the technique that makes the Planner reliably emit structured `GOOGLE`/`PYTHON`/`DOCUMENTATION`/`EXPERIMENT` actions.
- Urbina, Lentzos, Invernizzi, Ekins (2022, Nat Mach Intell) — dual-use of AI drug discovery (the cytotoxicity-flip paper); motivates the safety section.
- Lin et al. (2023, Science) — ESM-2 / atomic-level protein structure from a language model; cited as evidence for LLM-class models in biology.
- Opentrons Python Protocol API v2 — the hardware-doc corpus on which the OT-2 RAG was built.
