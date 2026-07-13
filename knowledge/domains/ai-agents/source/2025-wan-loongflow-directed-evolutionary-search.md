<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning, sci-math]
title: "LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm"
authors: [Chunhui Wan, X. Dai, Zhuo Wang, Minglei Li, Yanpeng Wang, Yinan Mao, Yushi Lan, Zhiwen Xiao]
year: 2025
source_url: https://arxiv.org/abs/2512.24077
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm

**Authors:** Chunhui Wan, X. Dai, Zhuo Wang, Minglei Li, Yanpeng Wang, Yinan Mao, Yushi Lan, Zhiwen Xiao  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2512.24077

## One-line
LoongFlow is an LLM-driven evolutionary search framework that replaces "blind mutation" with a Plan-Execute-Summarize (PES) reasoning loop plus a hybrid Island/MAP-Elites/Boltzmann memory, and reports new bests on several AlphaEvolve math problems including Autocorrelation II.

## Key claim
On the AlphaEvolve benchmark suite, LoongFlow (with DeepSeek-R1) edges past AlphaEvolve on multiple problems — Autocorrelation II $0.9027$ vs $0.8962$, Erdős minimum-overlap $0.380913$ vs $0.380924$, Uncertainty Inequality $0.352099104421$ vs $0.352099104422$, hexagon packing side $3.92$ vs $3.93$ — while requiring $\sim 258$ vs $\sim 783$ evaluations to reach Circle Packing (Square) score $\geq 0.99$ (≈60% fewer evals), and breaking the $>1.0$ "theoretical barrier" in 3/3 runs within 100-iter budgets where OpenEvolve and ShinkaEvolve fail.

## Method
The agent loop is formalized as an MDP over a discrete code space $\mathcal{C}$ with the LLM policy $\pi_\theta$ factored into three operators — Planner ($b\sim\pi_\theta(b\mid s_t,M_t,I_{\text{plan}})$ with lineage-based context retrieval over parent `generate_plan` + `summary` fields), Executor (polymorphic Chat/ReAct "Fuse" mode with a fast-fail local verification step), and Summarizer (abductive reflection producing insights $z$ that update memory $M_{t+1}\leftarrow M_t\cup\{z\}$). Population management is a three-layer hybrid: a ring-topology Multi-Island model with diversity-gated migration of top-$k\%$ elites, a MAP-Elites archive per island over interpretable behavior descriptors $\Phi(s)=(\text{cyclomatic complexity},\text{code length})$, and Adaptive Boltzmann parent selection $P(s_i)\propto\exp(R(s_i)/\tau)$ with entropy-modulated temperature $\tau(t)\propto\exp(-\lambda H(P_t))$ (low entropy ⇒ high $\tau$ ⇒ explore).

## Result
SOTA-by-a-hair improvements on 7 AlphaEvolve problems with DeepSeek-R1 (notably Autocorrelation II $+0.0065$, hexagon packing $-0.01$ on side length, Erdős-min-overlap $-1.1\times 10^{-5}$) and 14 MLE-Bench gold medals using Gemini-3.0-flash / Claude-Opus-4.5. Ablations on Circle Packing (Square) show the Planner ablation stagnates below $0.96$ and inflates time-to-top-1 from $9.67{\to}14.67$ h; removing the Summarizer causes cyclical errors and failure to break $0.95$ after 35 h; the Fuse-mode Executor reaches the asymptotic $0.998$ that pure Chat or pure ReAct miss.

## Key terms
LoongFlow, Plan-Execute-Summarize, PES paradigm, MAP-Elites, Island model, Boltzmann selection, entropy regularization, evolutionary memory, AlphaEvolve benchmark, Autocorrelation II, circle packing in square, hexagon packing, Erdős minimum overlap, uncertainty inequality, lineage-based retrieval, ReAct, Reflexion, FunSearch, OpenEvolve, ShinkaEvolve, directed evolutionary search, self-evolving agent, behavioral diversity, premature convergence
