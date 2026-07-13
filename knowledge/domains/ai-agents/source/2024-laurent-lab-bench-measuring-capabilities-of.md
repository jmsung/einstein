<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "LAB-Bench: Measuring Capabilities of Language Models for Biology Research"
authors: [Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, Michael J. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, Samuel G. Rodriques]
year: 2024
doi: null
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# LAB-Bench: Measuring Capabilities of Language Models for Biology Research

## TL;DR
LAB-Bench is a >2,400-question multiple-choice benchmark from FutureHouse that evaluates LLMs on practical biology research tasks (literature recall, figure/table interpretation, database lookup, DNA/protein sequence manipulation, protocol troubleshooting, molecular cloning scenarios). Frontier models without tools underperform PhD-level human experts across nearly every category, and apparent multiple-choice success often masks poor reasoning revealed by open-response evaluation.

## Key findings
- **Benchmark composition** (Table 1, total 2,457 questions): LitQA2 (248), SuppQA (102), FigQA (226), TableQA (305), DbQA (650, 10 subtasks), ProtocolQA (135), SeqQA (750, 15 subtasks), CloningScenarios (41). ~80% public / ~20% held private for contamination monitoring.
- **Models evaluated without tools**: GPT-4o, GPT-4-Turbo, Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku, Gemini 1.5 Pro, Llama-3-70B-Instruct. Zero-shot chain-of-thought prompting; an "Insufficient information" option enables coverage/precision measurement.
- **Humans beat models on most categories** (Figure 3). PhD-level evaluators outperform in both accuracy and precision while maintaining higher coverage.
- **LitQA2**: All models score ~40%+ precision (above random) but accuracy collapses for frontier models because they refuse to answer (some <20% coverage). Prior FutureHouse work showed RAG substantially outperforms tool-free LLMs on LitQA.
- **SuppQA**: Lowest coverage of any category — supplemental material appears underrepresented in training corpora.
- **FigQA**: Hardest category for most models; near-random precision except **Claude 3.5 Sonnet**, which significantly leads.
- **TableQA**: Easiest category; Claude 3.5 Sonnet **equals human accuracy and narrowly beats human precision**.
- **DbQA**: Low accuracy from high refusal rates; latest large models top the chart but none excel.
- **SeqQA**: Aggregate ~40–50% precision across models, well above random. Subtask variance is huge — >90% on PCR-seq-enzprimers (primer choice from explicit sequence) but performance collapses when only a gene *name* is given (PCR-gene-enzprimers), indicating poor sequence recall. RE-seq-numfrags, RE-seq-lenfrags, PCR-primers-len (long-sequence manipulation) are worst.
- **CloningScenarios**: All models well below human; Gemini 1.5 Pro and GPT-4-Turbo have low coverage *and* low precision. Models often succeed only by eliminating implausible distractors and guessing common defaults (e.g., Ampicillin, BsaI, Carbenicillin).
- **ProtocolQA**: Models cluster ~50–60% precision with high coverage — no lookup required.
- **Open-response check** (§2.4) on CloningScenarios, ProtocolQA, FigQA: Claude 3.5 Sonnet and GPT-4o drop to **0.20 accuracy on CloningScenarios** and 0.30 on FigQA; both got the same 2/10 cloning questions right, in each case by guessing the most common enzyme/antibiotic. Confirms MCQ scores overstate real reasoning.

## Methods (brief)
SeqQA and DbQA questions generated programmatically (BioPython Restriction package, E. coli ASM584v2 genome, MSigDB gene sets, ClinVar, DisGeNet, miRDB, P-HIPSter, etc.). LitQA2, SuppQA, FigQA, TableQA, ProtocolQA, and CloningScenarios written manually by authors and contracted experts, sometimes seeded with model-suggested drafts that were then revised. Human baseline collected from PhD-level evaluators on Airtable quizzes (20–140 questions each, 5–8 days, $50–$100/hr equivalent), allowed any non-AI tools including a DNA-editing app (ApE). Models accessed via API with no tools, 0-shot CoT, answer-tag regex parsing (chem-bench harness).

## Limitations
- Models evaluated without tools, while human evaluators had web/software access — comparison is asymmetric and likely underestimates tool-augmented model performance.
- Distractor quality strongly affects measured precision; some apparent skill is test-taking heuristics, not reasoning.
- Human baseline for CloningScenarios is likely under-measured because expert annotators found 10–60-min questions not worth their time; authors propose "human proofs-of-possibility" as a substitute.
- Coverage of the benchmark by human evaluators is partial (35% on DbQA, 64% on SeqQA, 82% on TableQA per Table 1).

## Citations of interest
- Boiko et al. 2023 (Nature) — autonomous chemical research with LLMs; sister work in agentic chemistry.
- Mirza et al. (ChemBench, ref [35]) — chemistry MCQ benchmark whose eval harness LAB-Bench adapts.
- Lála et al. (PaperQA / LitQA, ref [30]) — RAG-vs-LLM gap on biology literature questions.
- Srivastava et al. (BIG-bench, ref [50]) — broad capability benchmark and canary-string convention LAB-Bench extends.
- Liang et al. (HELM, ref [28]) — uncertainty/coverage methodology adopted for the "Insufficient information" option.
- Notin et al. (ProteinGym, ref [38]) — substitution variant dataset used to construct DbQA pathogenicity questions.
- Bran et al. (ChemCrow, ref [5]) — LLM agent with chemistry tools; cited as the agent-augmentation direction LAB-Bench is built to measure.
