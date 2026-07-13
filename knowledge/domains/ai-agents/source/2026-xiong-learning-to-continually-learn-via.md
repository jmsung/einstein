<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Learning to Continually Learn via Meta-learning Agentic Memory Designs
authors: [Yiming Xiong, Shengran Hu, Jeff Clune]
year: 2026
doi: 10.48550/arXiv.2602.07755
source_url: https://doi.org/10.48550/arXiv.2602.07755
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Learning to Continually Learn via Meta-learning Agentic Memory Designs

## TL;DR
ALMA uses a Meta Agent to search code-space for agentic memory designs (database schemas + update/retrieve logic) through open-ended exploration, automatically discovering domain-specialized memory architectures that outperform all state-of-the-art hand-crafted memory systems across four sequential decision-making benchmarks.

## Key findings
- **Core idea**: Replace hand-engineered agent memory with *learned* memory designs. A Meta Agent (GPT-5) samples prior designs from an archive, reflects on their evaluation logs/success rates, proposes and codes a new design in Python, debugs it (up to 3 trial-run retries), evaluates it, and adds it back to the archive (Figure 1).
- **Search space**: Code (Turing-complete Python), constrained by a light abstraction — sub-modules (`Sub_memo_layer`) each with their own optional database (Chroma vector DB or NetworkX graph) and `update()`/`retrieve()`, orchestrated by `general_update()`/`general_retrieve()` (Appendix A.1).
- **Two-phase evaluation**: a *Memory Collection Phase* (run agent memory-free, build static memory) then a *Deployment Phase* (retrieve memory per task, measure success); deployment runs in **static** (fixed memory) or **dynamic** (online-updating) mode. Learning uses static mode to cut variance.
- **Benchmarks**: ALFWorld, TextWorld, Baba Is AI, MiniHack — all text/grid sequential decision-making, requiring experience not in FM pretraining. 11 learning steps → 43 designs; up to 5 designs sampled per step.
- **Results (GPT-5-nano agent, Table 1 Top)**: ALMA overall avg **12.3%** vs no-memory 6.1% (+6.2), beating best baseline G-Memory (7.7). On ALFWorld: **12.4%** vs G-Memory 7.6, no-memory 2.9.
- **Transfer to GPT-5-mini (Table 1 Bottom)**: ALMA overall **53.9%** (+12.8 over no-memory 41.1), again topping all baselines. The larger gain on the stronger FM (12.8 vs 6.2, delta 6.6) exceeds every human baseline's delta — learned memory helps capable agents *more*.
- **Cost efficiency (Figure 6)**: ALMA averages 53.9% success at **$0.09** end-to-end memory cost with ~1,319 retrieved tokens — cheaper than most baselines (Trajectory Retrieval $1.5+/9,149 tokens, G-Memory $6,095 tokens) despite no explicit cost optimization.
- **Scaling & adaptation**: learned designs reach higher success faster with limited collection data and scale better (Figure 4); under task distribution shift (dynamic mode, valid-seen→valid-unseen) ALMA hits **84.1%** on ALFWorld, beating all baselines (Figure 5).
- **Domain specialization (Figure 3)**: object-interaction tasks (ALFWorld/TextWorld) yield fine-grained spatial/affordance memory; reasoning-heavy tasks (Baba Is AI/MiniHack) yield abstract strategy libraries and plan-synthesis modules.
- **Open-endedness matters**: ablation vs greedy search (always refine the current best) is worse — ALFWorld 11.9% vs 12.4% (nano), 77.1% vs 87.1% (mini) — confirming moderate-success designs act as stepping stones (Appendix C.2, Table 2).

## Methods (brief)
Meta Agent = GPT-5; agent-under-test = GPT-5-nano (learning) / GPT-5-mini (transfer); memory sub-modules may call GPT-4o-mini, GPT-4.1, and text-embedding-3-small. Archive sampling assigns probability rising with normalized success rate and falling with visit count (softmax over scores, α=0.5, T=0.5), keeping all designs reachable for exploration (Appendix A.4). Designs run in isolated sandboxes with human oversight for safety; reported success rates are means ± SE over 3 deployment runs.

## Limitations
Memory designs are learned offline on a pre-defined learning set, not online during deployment (online learning skipped for compute cost); the learned-design search is in code space and bounded by the underlying FM's capability; only token-level memory is studied (not parametric/latent); absolute success rates remain low on the nano agent (single-digit % on several benchmarks).

## Citations of interest
- **Hu, Lu & Clune 2025 (ADAS)** — automated design of agentic systems via code; direct methodological parent.
- **Zhang et al. 2025 (Darwin Gödel Machine)** — open-ended evolution of self-improving agents; basis for archive sampling.
- **Clune 2020 (AI-GAs)** — AI-generating-algorithms paradigm framing the whole approach.
- **Ouyang et al. 2025 (ReasoningBank)** & **Zhang et al. 2025 (G-Memory)** — strongest hand-crafted memory baselines.
- **Suzgun et al. 2025 (Dynamic Cheatsheet)** — cumulative global-memory baseline.
- **Paglieri et al. 2025 (BALROG)** — benchmark harness/prompts for TextWorld, Baba Is AI, MiniHack.
