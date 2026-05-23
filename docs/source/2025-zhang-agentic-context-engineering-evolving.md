---
type: source
kind: paper
title: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
authors: Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, V. Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, K. Olukotun
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.04618
source_local: ../raw/2025-zhang-agentic-context-engineering-evolving.pdf
topic: general-knowledge
cites:
---

# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

**Authors:** Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, V. Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, K. Olukotun  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.04618

## One-line
ACE adapts an LLM's *context* (not its weights) by growing a structured playbook of bulleted strategies through a Generator → Reflector → Curator loop with incremental delta updates, avoiding the brevity bias and context collapse of monolithic prompt rewriters.

## Key claim
Treating context as an ever-growing, itemized playbook with localized delta merges (rather than full LLM rewrites) yields +10.6% on agent tasks (AppWorld) and +8.6% on financial reasoning (FiNER, Formula) over strong prompt-optimizer baselines (GEPA, MIPROv2, Dynamic Cheatsheet, ICL), while cutting adaptation latency by 86.9% — and matches the GPT-4.1-based IBM-CUGA leaderboard top-1 while using only open-source DeepSeek-V3.1.

## Method
Three-role agentic loop over a context represented as bulleted items with metadata (id, helpful/harmful counters, content). Generator runs the task and flags which bullets helped or misled; Reflector diagnoses successes/failures from execution traces (using GT labels when available, else execution signals like code errors), iteratively refining lessons; Curator emits small JSON-shaped *delta* operations (ADD/UPDATE) merged deterministically by non-LLM logic. A grow-and-refine step deduplicates via embedding similarity, either eagerly or lazily on overflow.

## Result
On AppWorld with DeepSeek-V3.1-671B + ReAct, ACE lifts average score from 42.4% → 59.5% (online, no GT labels) — a +17.1% absolute gain, surpassing IBM-CUGA's 60.3% on test-challenge TGC by +8.4%. On FiNER/Formula, ACE (offline + GT) reaches 78.3% / 85.5% vs. base 70.7% / 67.5%, beating GEPA by 4.8% / 14.0%. Context collapse is concretely documented: Dynamic Cheatsheet collapsed from 18,282 tokens / 66.7% acc to 122 tokens / 57.1% acc in a single rewrite step. Ablations confirm Reflector, multi-epoch refinement, and incremental delta each contribute substantial gains.

## Why it matters here
Directly informs the autonomous-loop agent architecture being built on this branch (`feat/autonomous-loop`): the wiki *is* the playbook, and ACE's grow-and-refine + incremental delta pattern is a principled alternative to monolithic `/wiki-learn` rewrites — preserving the detailed dead-end findings and triple-verify lore that brevity-biased rewrites would erase. Suggests adding bullet-level metadata (helpful/harmful counters) to wiki findings to enable Reflector-style attribution across cycles.

## Open questions / connections
- Can the Generator/Reflector/Curator split replace the current single-pass `/wiki-learn` flow without losing the human-attribution honesty layer (`author: agent|human|hybrid`)?
- ACE works without GT labels via execution feedback — analog for arena math: triple-verify disagreement as the Reflector signal instead of arena submission outcome.
- Bullet-level helpful/harmful counters resemble the cite-count promotion threshold (3+ cites → concept) in `wiki-attribution.md`; could be unified into one provenance system.
- Extends GEPA (Agrawal 2025) and Dynamic Cheatsheet (Suzgun 2025); compare against TextGrad (Yuksekgonul 2025) and Reflexion (Shinn 2023) for the council-dispatch loop.

## Key terms
agentic context engineering, ACE, context adaptation, prompt optimization, playbook, incremental delta updates, grow-and-refine, brevity bias, context collapse, Generator-Reflector-Curator, Dynamic Cheatsheet, GEPA, self-improving agents, AppWorld, FiNER, execution feedback
