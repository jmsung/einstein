---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://www.nature.com/articles/s41586-023-06924-6
source_local: sources/2023-romera-paredes-funsearch.pdf
cites:
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2025-ellenberg-generative-math.md
  - ../papers/2025-georgiev-math-exploration.md
  - problem-1-erdos-overlap/literature.md
  - problem-6-kissing-number/literature.md
  - problem-19-difference-bases/literature.md
---

[[../home]] | [[../index]]

# Romera-Paredes et al. — Mathematical discoveries from program search with large language models (FunSearch)

**Authors:** Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg, Pengming Wang, Omar Fawzi, Pushmeet Kohli, Alhussein Fawzi
**Year:** 2023 (Nature 625:468, 18 January 2024)
**arXiv:** —

## Summary

FunSearch ("function search") is the direct predecessor of AlphaEvolve. It pairs a pretrained LLM with a systematic evaluator inside an evolutionary loop: the LLM proposes mutations to a *program* (not a solution), the evaluator scores the program by running it, and the population evolves toward higher-fitness programs. The key insight — searching in *function space* rather than *solution space* — produces interpretable artifacts (Python heuristics) that domain experts can read and refine.

Headline results: (1) new lower bounds for the **cap set problem** in finite-dimensional spaces, surpassing the best human-known constructions in extremal combinatorics; (2) new heuristics for **online bin packing** that beat widely used baselines (best-fit, first-fit-decreasing). Both demonstrations are directly relevant to discrete-geometry / combinatorial optimization problems on the Einstein Arena.

## Key Techniques

- **Programs as candidates** — evolve Python functions, not raw solutions; the program is a generator/scorer of candidates
- **Island model** — multiple sub-populations to maintain diversity (precursor to AlphaEvolve's database)
- **Skeleton + evolve block** — fix the harness, only mutate a delimited code region (used identically in AlphaEvolve)
- **LLM-mediated mutation** — sample completions from a pretrained code LLM (Codey/PaLM 2 in original)
- **Best-program prompting** — prompts include top-scoring programs as in-context examples
- **Async distributed evaluation** — programs scored in parallel; long sampling tails do not block the loop

## Relevance to Einstein Arena

### Direct precursor to AlphaEvolve
AlphaEvolve (`../papers/2025-novikov-alphaevolve.md`) is FunSearch + (full-file mutations, multiple LLMs, richer evaluator feedback, formal verification hooks). Understanding FunSearch first makes the AlphaEvolve paper readable. CHRONOS-class agents on the arena likely use FunSearch-style architectures.

### Cap set → extremal combinatorics
Cap-set is the prototypical "easy to evaluate, hard to solve" extremal problem — same shape as Erdős minimum overlap (P1), Sidon sets / difference bases (P2, P19), and kissing numbers (P6, P22). The FunSearch approach (heuristic generator program, scored by an evaluator) maps onto our problem-N strategies almost directly.

### Bin packing → packing problems
The bin-packing demonstration is methodologically close to the Heilbronn (P15, P16) and circle/hexagon packing (P14, P17) problems on the arena.

### Method library
FunSearch's published Python harness (skeleton + evolve block + island sampler) is a reference implementation pattern we should emulate when building agent-driven search loops.

## Limitations

- LLM-bottlenecked — quality of mutations is bounded by the underlying LLM
- Computationally expensive — millions of LLM samples per problem
- Fitness function design is the hard part; the system can only optimize what you can score automatically
- The published cap-set bounds were later partially superseded; FunSearch results are floors, not ceilings

## See Also

- [[2025-novikov-alphaevolve]] — successor system
- [[2025-ellenberg-generative-math]] — open-source FunSearch reimplementation
- [[2025-georgiev-math-exploration]] — adjacent benchmark for LLM math discovery
- [[../problem-1-erdos-overlap/literature]]
- [[../problem-6-kissing-number/literature]]
- [[../problem-19-difference-bases/literature]]
