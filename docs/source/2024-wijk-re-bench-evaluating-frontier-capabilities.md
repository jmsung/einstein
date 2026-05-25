---
type: source
kind: paper
title: RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts
authors: Hjalmar Wijk, T. Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Joshua Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Megan Kinniment, Aron Lajko, Seraphina Nix, L. Sato, William Saunders, M. Taran, Ben West, Elizabeth Barnes
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2411.15114
source_local: ../raw/2024-wijk-re-bench-evaluating-frontier-capabilities.pdf
topic: general-knowledge
cites:
---

# RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts

**Authors:** Hjalmar Wijk, T. Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Joshua Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Megan Kinniment, Aron Lajko, Seraphina Nix, L. Sato, William Saunders, M. Taran, Ben West, Elizabeth Barnes  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2411.15114

## One-line
Benchmarks LLM agents against 61 human ML experts on 7 hand-crafted 8-hour AI R&D engineering environments, finding agents win short budgets but humans win long ones.

## Key claim
Best AI agents score $4\times$ human experts at 2-hour budgets but humans score $2\times$ the best agent at 32-hour budgets (across multiple attempts via best-of-$k$); 82% of expert attempts achieve nonzero score, 24% match/exceed reference solutions.

## Method
Seven novel environments (kernel optimization in Triton, LLM finetuning script speedup, embedding recovery, Chinchilla-style scaling-law prediction, restricted-primitives MLM, GPT-2 RLHF, GPT-3.5 Rust CodeContests scaffolding), each with a starting solution, hidden reference solution, and scoring function. Scores linearly normalized so start $=0$, reference $=1$. Compares humans vs o1-preview and Claude 3.5 Sonnet via score@$k$ (best of $k$ independent runs) under matched 1–6×H100 hardware and time budgets from 30 min to 8 h.

## Result
Agents submit solutions $>10\times$ faster than humans at much lower cost and occasionally find superior approaches (both o1-preview and Claude found Triton kernels beating all 9 humans). But returns to time scale better for humans: agents plateau, humans keep improving. Mean expert normalized score is $0.5$–$1.5$ per env over 8 h; observed agent normalized scores stay $\le 2$.

## Why it matters here
General background; no direct arena tie. The methodology is relevant as a template for the einstein agent's own evaluation — score-normalization against a reference solution, score@$k$ vs wall-clock, and explicit "agents are fast/cheap but plateau while humans climb" framing inform how cycle-log.md should track agent-vs-human comparisons over compute budgets.

## Open questions / connections
- Why do agents' returns to time saturate while humans' don't? Suggests scaffolding/long-horizon planning is the binding constraint, not raw token cost.
- Best-of-$k$ allocation differs by agent (Claude favors many short runs, o1-preview favors fewer longer runs, humans favor longest single runs) — analogous question for einstein optimizer multistarts vs deeper polish.
- Score normalization that caps near reference may hide a heavy right tail; relevant to triple-verify when one of three numbers is an "above-ceiling" outlier.

## Key terms
RE-Bench, AI R&D automation, METR, score@k, best-of-k, Triton kernel optimization, prefix sum, scaling laws, Chinchilla, Claude 3.5 Sonnet, o1-preview, early warning evaluation, human baseline, agent scaffolding
