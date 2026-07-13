<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Augmenting large language models with chemistry tools
authors: [Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller]
year: 2024
doi: 10.1038/s42256-024-00832-8
source_url: https://doi.org/10.1038/s42256-024-00832-8
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Augmenting large language models with chemistry tools

## TL;DR
ChemCrow couples GPT-4 with 18 expert-designed chemistry tools via a ReAct-style reason–act–observe loop, letting an LLM plan and autonomously execute syntheses (insect repellent, three organocatalysts) on a cloud robotic platform and guide discovery of a novel chromophore — outperforming tool-less GPT-4 on chemical accuracy as judged by expert chemists.

## Key findings
- **Architecture.** A single LLM (GPT-4, temperature 0.1) is prompted in the **Thought → Action → Action Input → Observation** format (ReAct/MRKL), iterating until a final answer. Implemented on **LangChain**; the LLM is given tool names, descriptions, and I/O specs and chooses which tool to call. The reframing turns the LLM from "a hyperconfident—although typically wrong—information source" into a reasoning engine grounded by exact tool outputs.
- **18 tools** in five classes (Fig. 1b): *general* (WebSearch via SerpAPI, LitSearch via paper-qa + OpenAI embeddings/FAISS, Python REPL, Human), *molecule* (Name2SMILES, SMILES2Price, Name2CAS, Similarity/Tanimoto on ECFP2, ModifyMol via SynSpace, PatentCheck via molbloom bloom filter, FuncGroups, SMILES2Weight via RDKit), *safety* (ControlledChemicalCheck, ExplosiveCheck, SafetySummary), and *reaction* (NameRXN, ReactionPredict, ReactionPlanner, ReactionExecute — all on IBM RXN4Chemistry / Molecular Transformer).
- **Autonomous synthesis with physical execution.** From plain-language prompts, ChemCrow planned and ran syntheses of **DEET** and three thiourea organocatalysts (Schreiner's, Ricci's, Takemoto's) on IBM's cloud-connected **RoboRXN** robot — among the first LLM-agent interactions with the physical world for chemistry. It autonomously queried platform validation data and iteratively fixed invalid robot actions (e.g. "not enough solvent") without human intervention.
- **Human–AI discovery.** Instructed to clean chromophore data, train a random-forest model (Morgan fingerprints), and propose a molecule near a target absorption of **369 nm** (model RMSE 37 nm), ChemCrow suggested a compound that was synthesized and measured at **336 nm** — a confirmed new chromophore.
- **Evaluation.** On a panel of expert-designed tasks (synthesis, molecular design, chemical logic), expert chemists (n = 4 per task) scored on chemical accuracy, reasoning quality, and task completion. **ChemCrow beat tool-less GPT-4 on chemical accuracy/factuality**, especially for complex/novel tasks; GPT-4 only won on easy memorized targets (paracetamol, aspirin, DEET). Reasoning quality was similar by design (ChemCrow relies on GPT-4 to reason).
- **EvaluatorGPT failure mode.** An LLM evaluator favored GPT-4's fluent but hallucinated answers, inverting the expert ranking — the authors conclude LLM-based evaluation is **unreliable for factuality-critical scientific tasks** and cannot replace expert assessment.

## Methods (brief)
GPT-4 via OpenAI API, temperature 0.1, orchestrated through LangChain agents in ReAct format. Tools wrap external APIs/packages (RXN4Chemistry, PubChem, ChemSpace, OPSIN, RDKit, molbloom, paper-qa). Validation combined wet-lab robotic synthesis (RoboRXN), one experimentally confirmed chromophore, and a dual human-expert + LLM grading protocol across 14 tasks.

## Limitations
Single LLM backbone (GPT-4) and only 18 tools; results depend heavily on underlying tool quality and the agent's reasoning. Evaluation is small (n = 4 experts/task, 14 tasks) with possible task-selection bias, and closed-API GPT-4 makes individual runs non-reproducible. Safety relies on bloom-filter/list checks plus prompted guidelines, not exhaustive coverage. Public release exposes 12 of the 18 tools.

## Citations of interest
- Yao et al., *ReAct* (ICLR 2023) — the reason+act prompting loop ChemCrow is built on.
- Karpas et al., *MRKL systems* (2022) — modular neuro-symbolic LLM-plus-tools architecture.
- Schick et al., *Toolformer* (NeurIPS 2023) — LLMs teaching themselves to call tools.
- Boiko et al., *Autonomous chemical research with LLMs* (Nature 2023) — contemporaneous LLM+cloud-lab agent.
- Schwaller et al., *Molecular Transformer* (ACS Cent. Sci. 2019) — reaction-prediction engine behind the RXN tools.
- White et al., *Assessment of chemistry knowledge in code-generating LLMs* (Digital Discovery 2023) — evidence LLMs alone fail at chemistry.
- Liu et al., *G-Eval* (EMNLP 2023) — LLM-as-evaluator method whose limits this paper exposes.
