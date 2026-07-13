<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts
authors: [Hjalmar Wijk, T. Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Joshua Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Megan Kinniment, Aron Lajko, Seraphina Nix, L. Sato, William Saunders, M. Taran, Ben West, Elizabeth Barnes]
year: 2024
source_url: https://arxiv.org/abs/2411.15114
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
RE-Bench, AI R&D automation, METR, score@k, best-of-k, Triton kernel optimization, prefix sum, scaling laws, Chinchilla, Claude 3.5 Sonnet, o1-preview, early warning evaluation, human baseline, agent scaffolding
