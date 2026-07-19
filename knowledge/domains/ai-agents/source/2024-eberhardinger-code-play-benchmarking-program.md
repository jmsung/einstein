---
type: source
kind: paper
title: From Code to Play: Benchmarking Program Search for Games Using Large Language Models
authors: Manuel Eberhardinger, J. Goodman, Alexander Dockhorn, Diego Pérez-Liébana, Raluca D. Gaina, Duygu cCakmak, Setareh Maghsudi, Simon Lucas
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2412.04057
source_local: ../raw/2024-eberhardinger-code-play-benchmarking-program.pdf
topic: general-knowledge
cites:
---

# From Code to Play: Benchmarking Program Search for Games Using Large Language Models

**Authors:** Manuel Eberhardinger, J. Goodman, Alexander Dockhorn, Diego Pérez-Liébana, Raluca D. Gaina, Duygu cCakmak, Setareh Maghsudi, Simon Lucas  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.04057

## One-line
An empirical benchmark of 11 LLMs across 29 game-related tasks (Python + Java) using an LLM-driven hill-climbing program-search loop, measuring how well current models synthesize directly-executable game code.

## Key claim
LLM performance on game program synthesis depends more on task than model size, and **many short restarts beat one long run** — with 10 trials × 10 iterations consistently outperforming a single 100-iteration trial, and 1000-iteration long runs showing high inter-trial variance that favors restarting.

## Method
Neurosymbolic hill-climbing: an LLM proposes/mutates a candidate program (the "seed" and each "mutation" are LLM calls), the program is compiled/executed in a sandboxed subprocess, fitness (game reward or tournament win-rate) is evaluated, and the prompt is updated with the best-so-far program plus runtime errors or trace data for the next iteration (Algorithms 1–2). For Java/TAG games, automatic Javadoc-via-reflection API extraction and PDF-rulebook chunked summarization make the prompt game-agnostic. Evaluated 11 models (GPT-4o/4o-mini/o1-mini, Claude 3.5 Sonnet/Haiku, Gemini 2.0 Flash/Flash-Lite, Mistral Large/Small, Llama 3.1/3.3 70B) on Minatar (5 Atari minis), Baba Is You (10 levels), an Asteroids-style vehicle task, maze PCG, and 12 TAG tabletop games.

## Result
o1-mini ranks #1 overall (best on Minatar and maze generation); Gemini 2.0 Flash wins TAG (Java) at ~1/15 the cost of OpenAI models; Mistral models lead vehicle driving; smaller models sometimes beat their larger siblings (e.g., Claude Haiku > Sonnet on Seaquest/Freeway; GPT-4o-mini wins 2 TAG games). Across 12 TAG games, success rate of iterations producing compiling+running code ranges 8–63%; card-game APIs (`Deck<>`) consistently induce hallucinated method calls. 1000-iteration Minatar runs improve only Seaquest/Space Invaders substantially over the 10-iter best; on Freeway/Asterix more iterations don't help, confirming restart-dominance.

## Why it matters here
General background; no direct arena tie. The restart-beats-long-run finding is structurally relevant to the autonomous-loop agent's compute strategy — when the search landscape has high inter-trial variance, parallel many-restart > one-deep-run, which mirrors the multistart-vs-long-trajectory tradeoff in basin-hopping / parallel tempering on the arena problems. Also a reference point for LLM-as-mutation-operator in any future program-search optimizer.

## Open questions / connections
- Does the restart-dominance hold for problems where the fitness landscape is *not* heavily multimodal? (Their Freeway result hints no.)
- Can agentic decomposition (sub-modules with documented interfaces, then composition) beat single-pass generation? Explicitly raised as future work.
- Extends Romera-Paredes et al.'s FunSearch (ref [44], *Nature* 2024) — same LLM-mutation hill-climb pattern, different problem domain. FunSearch's math-discovery framing is the closer arena analog.
- How does prompt-only "creativity" (default temperature) compare to explicit population/diversity operators?

## Key terms
program synthesis, LLM-guided search, hill-climbing, neurosymbolic programming, FunSearch, restart-vs-iteration tradeoff, multistart, benchmark, Minatar, TAG tabletop games, MCTS heuristic synthesis, o1-mini, Gemini 2.0 Flash, mutation operator, Python, Java
