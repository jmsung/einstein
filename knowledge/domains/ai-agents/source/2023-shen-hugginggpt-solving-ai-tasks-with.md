<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face"
authors: [Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang]
year: 2023
doi: 10.48550/arXiv.2303.17580
source_url: https://doi.org/10.48550/arXiv.2303.17580
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

## TL;DR
HuggingGPT uses an LLM (ChatGPT) as a central controller that plans a task graph from a user request, selects expert models from the Hugging Face hub by their natural-language descriptions, executes them, and summarizes the results — turning "language as a generic interface" into a working orchestration layer over hundreds of specialist models.

## Key findings
- **Four-stage pipeline**: (1) *task planning* — ChatGPT parses the request into a structured JSON task list with `task`, `id`, `dep` (dependencies), and `args` slots; (2) *model selection* — assigns an expert model per task via in-context single-choice over candidate model cards; (3) *task execution* — runs the models on hybrid (local + cloud) endpoints, resolving inter-task resource dependencies; (4) *response generation* — LLM integrates structured predictions into a friendly natural-language answer (Fig. 2).
- **Global vs. iterative planning** is the key design distinction from contemporaries (AutoGPT/BabyAGI/AgentGPT, Table 12): HuggingGPT generates the *entire* task queue in one query rather than predicting tasks step-by-step. Tradeoff: global planning always yields a plan per request but can't guarantee step correctness or plan optimality; iterative+reflexion planning costs many LLM calls and can loop endlessly on an error.
- **Resource dependency mechanism**: a `<resource>-task_id` symbol injected at planning time is dynamically replaced at execution with the prerequisite task's output, enabling chained tasks (e.g., pose-detection → pose-conditional text-to-image). Dependency-free tasks run in parallel for speed.
- **Model selection heuristic**: filter candidate models by task type, then rank by Hugging Face download count and keep top-K — used as a proxy for popularity/quality and to fit the context-length budget.
- **Planning is the controller bottleneck.** On GPT-4-annotated datasets (1,450 single / 1,917 sequential / 130 graph requests, 3,497 total), GPT-3.5 dominates open models: single-task F1 54.45 vs. Vicuna-7b 29.44 / Alpaca-7b 4.88 (Table 3); sequential-task F1 51.92 vs. ~22 (Table 4); graph-task GPT-4 Score 50.48 vs. 19.17 / 13.14 (Table 5).
- **Large gap to human annotation** (Table 6, 46 expert examples): even GPT-4 reaches only 41.36% sequential accuracy and 58.33 graph accuracy — better than GPT-3.5 (18.18 / 20.83) but far from a ceiling, underscoring planning as the open research problem.
- **Human evaluation** (130 requests, Table 8): GPT-3.5 success rate 63.08% with task-planning passing rate 91.22% / rationality 78.47% — vastly above Vicuna-13b (15.64%) and Alpaca-13b (6.92%).
- **Demonstrations help, with diminishing returns**: increasing demo variety (task types) moderately improves planning (Table 7); few-shot count gains plateau beyond ~4 shots (Fig. 3).
- Supports **24 AI tasks** across NLP, CV, audio, and video (Table 13).

## Methods (brief)
LLMs (gpt-3.5-turbo, text-davinci-003, gpt-4, plus Alpaca-7b/13b and Vicuna-7b/13b) prompted at temperature 0 with `logit_bias` 0.2 on JSON delimiters to enforce structured output. Specification-based instruction (JSON slot-filling) plus demonstration-based parsing drive task planning. Evaluation uses F1/accuracy (single), normalized edit distance (sequential), and a GPT-4-as-critic "GPT-4 Score" (graph), validated against a 46-example human-annotated set and 130-request human subjective study.

## Limitations
Planning quality is wholly bottlenecked by the controller LLM and is far below human (GPT-4 sequential acc only 41%). Multiple LLM round-trips per request raise latency and cost; context-length limits cap how many model descriptions fit; LLM output is unstable/uncontrollable, causing workflow exceptions. Evaluation datasets are LLM-pseudo-labeled (GPT-4) except a small 46-example human set.

## Citations of interest
- Toolformer (Schick et al. 2023) — pioneering LLM tool-use via inline API tags; the tool-augmentation lineage HuggingGPT extends.
- Visual ChatGPT (Wu et al. 2023) and ViperGPT / Visual Programming — prior LLM+vision-model integration via foundation models or generated code.
- Brown et al. 2020 (GPT-3) & OpenAI 2023 (GPT-4) — the controller LLMs whose in-context/few-shot ability the method depends on.
- Chain-of-Thought (Wei et al. 2022) — reasoning-prompting foundation behind task decomposition.
- Vicuna (Chiang et al. 2023) — source of the GPT-4-as-critic evaluation methodology adopted for the GPT-4 Score.
