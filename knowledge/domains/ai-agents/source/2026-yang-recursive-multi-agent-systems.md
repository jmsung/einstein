<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Recursive Multi-Agent Systems
authors: [Xiyuan Yang, Jiaru Zou, Rui Pan, Ruizhong Qiu, Pan Lu, Shizhe Diao, Jindong Jiang, Hanghang Tong, Tong Zhang, Markus J. Buehler, Jingrui He, James Zou]
year: 2026
doi: null
source_url: https://arxiv.org/abs/2604.25917
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Recursive Multi-Agent Systems

## TL;DR
RecursiveMAS recasts an entire LLM multi-agent system as a single recursive latent-space computation — each agent acts like a recursive-language-model "layer" passing hidden states (not text) to the next via a lightweight learnable link — yielding +8.3% average accuracy, 1.2×–2.4× inference speedup, and 34.6%–75.6% fewer tokens versus text-mediated multi-agent baselines.

## Key findings
- **Core idea:** Treat the whole multi-agent system (MAS) as a recursive loop where agents exchange *last-layer latent embeddings* rather than decoded text. Only the final agent in the final recursion round decodes textual output; all intermediate collaboration happens in continuous latent space.
- **RecursiveLink module** is the only thing trained (all LLM agent parameters frozen). Two variants, both two-layer residual projections:
  - *Inner link* `R_in(h) = h + W₂σ(W₁h)` — feeds an agent's last-layer embedding back as its next-step input (latent thought generation).
  - *Outer link* `R_out(h) = W₃h + W₂σ(W₁h)` — bridges heterogeneous agents with different hidden dims (the extra W₃ maps source→target embedding space).
- **Inner-Outer Loop training:** inner loop warm-starts each agent's latent-thought generation via a cosine-similarity regression to the input-embedding distribution of the ground-truth text (Eq. 5); outer loop unrolls the full system for *n* rounds and optimizes all outer links with a single end-to-end cross-entropy loss (Eq. 6), backpropagating shared credit across the recursion trace.
- **Theory — efficiency (Prop. 3.1):** text-based recursive MAS costs Θ(N(m|V|d_h + …)) per the expensive m|V|d_h vocabulary-decoding term; RecursiveMAS replaces it with a latent transform m·d_h², and since d_h ≪ |V|, this is the dominant saving.
- **Theory — gradient stability (Thm. 4.1):** under confident tokens (entropy ≤ ε), text-based SFT recursion has gradient norm ≤ O(ε) → vanishing; RecursiveLink keeps gradient norm ≥ Ω(1 − √((1/d_h)log(1/δ))) ≈ 1, stable across rounds.
- **Empirics:** evaluated on 9 benchmarks (MATH500, AIME2025/2026, GPQA-Diamond, MedQA, LiveCodeBench-v6, MBPP+, HotpotQA, Bamboogle) across 4 collaboration patterns. At r=3 (Table 3) it beats the strongest baseline by avg 8.3%, with notable gains on AIME2025 (+18.1%) and AIME2026 (+13.0%) vs TextGrad/LoopLM.
- **Recursion scaling:** accuracy rises monotonically with recursion depth r=1→3 while the text baseline degrades; gains over Recursive-TextMAS grow from 8.1% (r=1) to 20.2% (r=3). Joint training×inference recursion scaling shows a complementary frontier (Fig. 1).
- **Cost (Table 5):** lower peak GPU mem (15.29 GB), only 13.12M trainable params (0.31%), $4.27 estimated cost, and *higher* accuracy (74.9%) than LoRA (66.9%) or Full-SFT (68.6%).
- **Ablations:** 2-layer + residual link is best (88.0% MATH500 vs 85.6% without residual); latent-thought length saturates around m=80.

## Methods (brief)
Off-the-shelf frozen LLM agents (Qwen3/3.5, Llama-3, Gemma3, Mistral, sub-1.5B "Light" to 5–10B "Scaled") composed into 4 MAS patterns: Sequential (Planner/Critic/Solver), Mixture (domain specialists + Summarizer), Distillation (Expert→Learner), Deliberation (Reflector + Tool-Caller with Python/search APIs). Only RecursiveLink trained (AdamW, lr 5e-4, batch 4) on s1K/m1K/OpenCodeReasoning/ARPO-SFT; HuggingFace + vLLM backends on H100/A100; mean over 5 runs.

## Limitations
Benchmarks are reasoning/code/QA, not scientific discovery; gains shown only up to r=3. Requires heterogeneous-agent training with curated role-specific supervision; latent transfer assumes access to model hidden states (not API-only black-box models). Theory relies on idealized assumptions (W₃=I, Kaiming init, confident-token regime).

## Citations of interest
- Zhu et al. 2025 (LoopLM, arXiv:2510.25741) — looped/recursive language models in latent space; the single-model precursor extended here.
- Zhang, Kraska & Khattab 2025 (Recursive Language Models, arXiv:2512.24601) — the RLM framing RecursiveMAS generalizes to systems.
- Wang et al. 2025b (Mixture-of-Agents) — text-based MAS baseline.
- Yuksekgonul et al. 2025 (TextGrad, *Nature*) — textual-gradient MAS optimization baseline.
- Zou et al. 2025 (Latent Collaboration in MAS, arXiv:2511.20639) — related latent-interface multi-agent coordination.
- Motwani et al. 2024 (MALT) — per-agent training alternative the paper contrasts against.
