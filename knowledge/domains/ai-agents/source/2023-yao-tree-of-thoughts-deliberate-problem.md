<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
authors: [Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan]
year: 2023
doi: 10.48550/arXiv.2305.10601
source_url: https://doi.org/10.48550/arXiv.2305.10601
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

## TL;DR
Tree of Thoughts (ToT) generalizes chain-of-thought prompting by letting an LLM explore a tree of intermediate "thoughts," self-evaluate partial solutions, and use BFS/DFS with lookahead and backtracking — lifting GPT-4's Game of 24 success rate from 4% (CoT) to 74%.

## Key findings
- **Core framing.** ToT casts problem solving as search over a tree where each node is a state `s = [x, z₁…ᵢ]` (input plus thoughts so far). A "thought" is a coherent semantic unit — a word, an equation line, or a writing-plan paragraph — sized to be diverse enough to sample yet meaningful enough to evaluate. Four design choices instantiate it: thought decomposition, thought generation, state evaluation, and search algorithm.
- **Thought generation** uses either i.i.d. sampling from a CoT prompt (rich spaces, e.g. paragraphs) or a sequential "propose prompt" (constrained spaces, avoids duplication).
- **State evaluation** is the novel contribution: the LM itself serves as the search heuristic, either *valuing* each state independently (e.g. "sure/maybe/impossible" toward reaching 24) or *voting* across states (better when success is hard to score directly, e.g. passage coherence). This is a third path beyond programmed (Deep Blue) and learned (AlphaGo) heuristics — more flexible and sample-efficient.
- **Search algorithms**: BFS (keep best `b` states/step; shallow trees T≤3) for Game of 24 and Creative Writing; DFS (explore most-promising, prune when deemed impossible, backtrack) for Crosswords.
- **Game of 24** (100 hard games, GPT-4): IO 7.3%, CoT 4.0%, CoT-SC(k=100) 9.0%, **ToT b=1 = 45%, b=5 = 74%**. Best-of-100 CoT only reaches 49%. Error analysis: ~60% of CoT samples already fail at the first step, exposing the weakness of left-to-right decoding (Fig 3b).
- **Creative Writing** (100 inputs, coherence): GPT-4 scores IO 6.19, CoT 6.93, **ToT 7.56**; in a blind human study humans preferred ToT over CoT in 41/100 pairs vs 21/100. Iterative-refine stacks on top (ToT → 7.91).
- **Mini Crosswords** (5×5, 20 games): word-level success IO/CoT <16%, **ToT 60%**, solving 4/20 games (7/20 with oracle output state). Ablations confirm both pruning and backtracking are critical (−backtrack drops to 20% word-level).
- **Generality**: IO, CoT, CoT-SC, and self-refine are all special cases of ToT (limited-depth/breadth trees). No extra training; off-the-shelf LM only. Holds across models — "ToT > CoT > IO" persists on GPT-3.5 (Game of 24: 19% vs GPT-4's 74%, generation being the bottleneck).

## Methods (brief)
All experiments use Chat-mode GPT-4 (temperature 0.7), May 2023. Three newly invented tasks were chosen specifically to defeat IO/CoT prompting even with GPT-4. Evaluation combined automatic metrics (success rate, GPT-4 1–10 coherence scores) with blind human pairwise judgments. Systematic ablations isolate breadth `b`, pruning, backtracking, and generation-vs-evaluation model choice.

## Limitations
Only three relatively simple, hand-crafted tasks; ToT is unnecessary where GPT-4 already excels (GSM8K/StrategyQA gains are marginal). Cost is 5–100× more generated tokens than CoT (~$0.74/Game-of-24 case). Search depth is shallow (≤10 steps); advanced algorithms (A*, MCTS) left to future work; the DFS pruning heuristic is imperfect (prunes some solvable boards with rare words).

## Citations of interest
- Wei et al. 2022 [38] — Chain-of-Thought prompting, the method ToT generalizes.
- Wang et al. 2022 [36] — Self-consistency with CoT (CoT-SC), the ensemble baseline.
- Newell, Shaw & Simon 1959/1972 [21,22] — classical problem-solving-as-tree-search, the conceptual lineage.
- Hao et al. 2023 [9] — RAP, concurrent MCTS-based "reasoning as planning with world model."
- Shinn et al. 2023 [28] / Madaan et al. 2023 [20] — Reflexion / Self-Refine, the self-reflection feedback line.
- Yao et al. 2022 [41] — ReAct, related reasoning-and-acting harness by overlapping authors.
