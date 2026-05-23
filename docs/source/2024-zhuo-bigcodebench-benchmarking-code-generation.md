---
type: source
kind: paper
title: BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions
authors: Terry Yue Zhuo, Minh Chien Vu, Jenny Chim, Han Hu, Wenhao Yu, Ratnadira Widyasari, Imam Nur Bani Yusuf, Haolan Zhan, Junda He, Indraneil Paul, Simon Brunner, Chen Gong, Thong Hoang, A. Zebaze, Xiao-ke Hong, Wen-Ding Li, Jean Kaddour, Minglian Xu, Zhihan Zhang, Prateek Yadav, Naman Jain, Alex Gu, Zhoujun Cheng, Jiawei Liu, Qian Liu, Zijian Wang, David Lo, Binyuan Hui, Niklas Muennighoff, Daniel Fried, Xiao-Nan Du, H. D. Vries, L. V. Werra
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.15877
source_local: ../raw/2024-zhuo-bigcodebench-benchmarking-code-generation.pdf
topic: general-knowledge
cites:
---

# BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions

**Authors:** Terry Yue Zhuo, Minh Chien Vu, Jenny Chim, Han Hu, Wenhao Yu, Ratnadira Widyasari, Imam Nur Bani Yusuf, Haolan Zhan, Junda He, Indraneil Paul, Simon Brunner, Chen Gong, Thong Hoang, A. Zebaze, Xiao-ke Hong, Wen-Ding Li, Jean Kaddour, Minglian Xu, Zhihan Zhang, Prateek Yadav, Naman Jain, Alex Gu, Zhoujun Cheng, Jiawei Liu, Qian Liu, Zijian Wang, David Lo, Binyuan Hui, Niklas Muennighoff, Daniel Fried, Xiao-Nan Du, H. D. Vries, L. V. Werra  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.15877

## One-line
Introduces BigCodeBench, a 1,140-task Python benchmark stressing LLMs on multi-library function-call composition under complex instructions, with rigorous unit tests (avg 5.6 tests, 99% branch coverage).

## Key claim
Even the best LLM (GPT-4o) only solves ~60% of BigCodeBench-Complete and <50% of BigCodeBench-Instruct, vs ~97% human pass rate, exposing a large gap in compositional tool use and instruction-following that HumanEval/MBPP have saturated and obscured.

## Method
Human-LLM collaboration pipeline in three stages: (1) GPT-4 synthesizes self-contained tasks from ODEX seed snippets with obfuscation + back-translation to mitigate model bias; (2) iterative Code Interpreter sessions refactor programs and generate unittest-based tests with 13 annotators providing feedback; (3) 7-person cross-check curation, doctest validation, and GitHub CI sandbox runs. An Instruct variant rewrites docstrings into NL-style prompts via parsing rules.

## Result
Benchmark spans 723 function calls across 139 libraries in 7 domains (Computation 63%, General 44%, Visualization 31%, System 30%, Time 10%, Network 8%, Cryptography 5%); ground-truth solutions avg 10 lines / cyclomatic complexity 3.1, far above HumanEval. Evaluation of 60 LLMs shows strong correlation with MBPP+ (Pearson 0.963) and HumanEval+ (0.849); zero-shot CoT does not help and often hurts; rephrased less-structured instructions cause large drops (e.g., Qwen2.5-Coder-32B-Instruct -18.9 points), revealing brittleness to natural phrasing. Failure modes include misuse of `itertools.cycle`/`zip_longest`, `isinstance` semantics, `os.path.dirname`, encoding mismatches, and wrong-API selection (`np.mean` vs `np.nanmean`).

## Why it matters here
General background; no direct arena tie — the paper is about evaluating LLM coding ability, not math optimization. Tangentially relevant as a reminder that the JSAgent's reliance on diverse library APIs (numpy, scipy, mpmath, HiGHS, torch, modal) means real-world failure modes (wrong-API selection, encoding/precision mismatches) match those documented here; reinforces the triple-verify axiom.

## Open questions / connections
- Does pass-rate on BigCodeBench predict success at long-horizon scientific-computing agents (e.g., optimizer-as-tool composition for arena problems)?
- Extends HumanEval/MBPP/DS-1000 lineage; complements LiveCodeBench (contamination-free) and SWE-bench (repo-level) by targeting library composition at function granularity.
- Open: why does CoT degrade performance on compositional library tasks, and which fine-tuning recipes recover the gap to humans (97%) without overfitting?

## Key terms
BigCodeBench, code generation benchmark, function call composition, tool use, instruction following, Python libraries, unit test coverage, cyclomatic complexity, HumanEval, MBPP, DS-1000, LiveCodeBench, GPT-4o, chain-of-thought, LLM evaluation
