---
type: source
kind: paper
title: Towards an AI co-scientist
authors: Juraj Gottweis, Wei-Hung Weng, A. Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, D. Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, A. Carroll, Kavita Kulkarni, Nenad Tomašev, Yuan Guan, Vikram Dhillon, E. D. Vaishnav, Byron Lee, Tiago R. D. Costa, José R. Penadés, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, A. Karthikesalingam, Vivek Natarajan
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.18864
source_local: ../raw/2025-gottweis-towards-co-scientist.pdf
topic: general-knowledge
cites:
---

# Towards an AI co-scientist

**Authors:** Juraj Gottweis, Wei-Hung Weng, A. Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, D. Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, A. Carroll, Kavita Kulkarni, Nenad Tomašev, Yuan Guan, Vikram Dhillon, E. D. Vaishnav, Byron Lee, Tiago R. D. Costa, José R. Penadés, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, A. Karthikesalingam, Vivek Natarajan  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.18864

## One-line
A Gemini 2.0-based multi-agent system that generates, debates, and evolves novel scientific hypotheses in a tournament loop, validated end-to-end on three biomedical discovery tasks.

## Key claim
A "generate → debate → rank → evolve" multi-agent architecture with asynchronous task execution and tournament-based self-play scales test-time compute monotonically with hypothesis quality (Elo), and produces wet-lab-validated novel hypotheses in drug repurposing (AML), epigenetic target discovery (liver fibrosis), and bacterial gene transfer (cf-PICI host-range expansion — recapitulating an unpublished experimental result in ~2 days vs. ~10 years).

## Method
Six specialized LLM agents — Generation (literature exploration + simulated scientific debate), Reflection (full review / simulation / deep verification), Ranking (Elo tournament with pairwise scientific debate), Evolution (cross-inspiration, simplification, extension), Proximity (relatedness clustering), and Meta-review (synthesis + feedback to other agents) — operate over a shared memory via an asynchronous task framework. The Ranking tournament surfaces win/loss patterns that the Meta-review distills into feedback, closing a self-improving loop. Tool use (web search, AlphaFold for structural plausibility) grounds outputs; scientist stays in the loop via chat and seed-idea injection.

## Result
On 15 expert-curated open scientific goals, automated Elo evaluations show hypothesis quality rising monotonically with test-time compute, outperforming SOTA reasoning baselines. Three wet-lab validations: (1) repurposing candidates (Binimetinib, Pacritinib, KIRA6, Leflunomide) inhibit MOLM13 AML proliferation at clinically applicable IC50 concentrations; (2) novel epigenetic targets reduce fibrogenesis in human hepatic organoids; (3) the system independently proposed that cf-PICIs interact with diverse phage tails to expand host range — matching unpublished experimental findings.

## Why it matters here
General background; no direct arena tie. The architecture is a candidate blueprint for the einstein autonomous-loop agent's own structure — particularly the **tournament-evolution + meta-review feedback loop** (parallels einstein's council-dispatch → gap-detect → self-improvement-loop) and the explicit separation of Generation / Reflection / Ranking / Evolution / Meta-review roles, which could inform how persona-council outputs are ranked and how findings are promoted. Math/optimization content: none.

## Open questions / connections
- Does a tournament-Elo ranker over hypotheses translate to math-problem hypotheses (e.g., ranking candidate Cohn–Elkies magic functions or basin parameterizations), or does it require a falsifiable scalar score?
- The "scientific debate" self-play here is multi-agent natural-language; einstein's persona council currently writes parallel questions without adversarial pairing — would adding pairwise debate improve question quality?
- Meta-review's distillation of win/loss patterns into prompt-level feedback is a possible mechanism for einstein's `docs/agent/skill-library.md` to feed back into cycle priors automatically.
- AlphaFold-as-validator pattern (specialized model gates general LLM proposal) ≈ einstein's triple-verify principle (independent evaluator gates optimizer claim).

## Key terms
multi-agent system, AI co-scientist, Gemini 2.0, tournament evolution, Elo ranking, scientific debate self-play, test-time compute scaling, hypothesis generation, meta-review feedback loop, drug repurposing, AlphaFold tool use, scientist-in-the-loop
