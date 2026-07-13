<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "A Comprehensive Review of AI Agents: Transforming Possibilities in Technology and Beyond"
authors: [Xiaodong Qu, Andrews Damoah, Joshua Sherwood, Peiyan Liu, Christian Shun Jin, Lulu Chen, Minjie Shen, Nawwaf Aleisa, Zeyuan Hou, Chenyu Zhang, Lifu Gao, Yanshu Li, Qikai Yang, Qun Wang, Cristabelle De Souza]
year: 2025
doi: 10.48550/arxiv.2508.11957
source_url: https://doi.org/10.48550/arxiv.2508.11957
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# A Comprehensive Review of AI Agents: Transforming Possibilities in Technology and Beyond

## TL;DR
A PRISMA-guided survey synthesizing the architectural components (memory, tools, planning, perception) and learning paradigms of contemporary AI agents — from symbolic/RL roots to LLM-driven reasoning — across business, education, science, and entertainment, with a beginner-oriented step-by-step research guide and a catalog of open safety/interpretability/ethics challenges.

## Key findings
- **Core architecture = four components.** Modern agents are framed around **memory, tools, actions, and planning** (Fig. 2, following Lilian Weng's formulation). Memory splits into short-term/textual (bounded by the transformer context window) and long-term/parametric (declarative facts + procedural skills). Tools are external modules (search engines, code interpreters, calculators, robotic arms) the LLM calls dynamically.
- **Planning techniques surveyed.** Chain-of-Thought prompting (Wei et al.) for multi-step reasoning; **Reflexion** (Shinn et al.) — verbal self-reflection via linguistic feedback + a heuristic function, improving reasoning without fine-tuning; **Chain of Hindsight** (Liu et al.) — trains a causal Transformer on sequences of past outputs + feedback, masking feedback tokens so only non-feedback tokens are predicted; reported to surpass RLHF/SFT on summarization and dialogue. Hierarchical RL decomposes decisions into macro-actions for long-horizon tasks.
- **Learning lineage.** Traces symbolic systems (1950s–60s) → statistical/probabilistic methods (1980s–90s) → RL → DeepRL (Atari, AlphaGo superhuman play) → LLM-based reasoning agents. Cites value-based (DQN), policy-gradient (PPO, SAC), meta-learning (MAML), and continual learning to combat catastrophic forgetting.
- **Application domains (six).** *Healthcare* — diagnostic/decision-support agents (radiology, dermatology melanoma, diabetic retinopathy), patient chatbots, surgical robots. *Business* — customer service, supply-chain forecasting (Amazon inventory), fraud detection, algorithmic trading, credit scoring. *Education* — co-learners improving cognitive/social presence, Mentigo mentoring agent, MAIC ("Massive AI Course") tested with 500 volunteers across 2 courses using teacher/assistant/classmate/analyzer/manager agents. *Science* — autonomous labs, multi-agent robotic chemists, "AI Scientist" attempting fully automated research; biomedical discovery agents (Gao et al., *Cell* 2024). *Public services/urban planning* and *entertainment/creativity* (DesignGPT, SIMA, NPCs).
- **Design directions.** Cognitive-inspired hybrid symbolic–neural architectures; hierarchical/modular decomposition for scalability, reusability, and interpretability.
- **Challenges (Sec. 7.2).** Safety/robustness under distribution shift and adversarial perturbation; opaque decision-making (interpretability); bias/fairness/privacy/accountability; out-of-distribution generalization and transfer; compute/energy cost limiting accessibility and sustainability.

## Methods (brief)
Systematic literature review following PRISMA guidelines, conducted by topic (core components, applications, paradigm-shifting designs) and merged into one diagram (Fig. 1). Searches ran on Google Scholar (and Papers with Code) across four application domains — business, education, science, entertainment — using terms like "AI Agent," "Autonomous Agent," "Multi-Agent System." Three stages: scholar search by relevance ranking, title/abstract screening, full-text review. Exclusions: non-full-text/paywalled, off-scope, non-English (full query list in Appendix A).

## Limitations
A broad, shallow survey rather than an empirical study — it reports no benchmarks, no new system, and no quantitative comparison of its own; coverage is English-only Google Scholar results, and the reference list is heterogeneous (many cited works are tangential to AI agents). Claims about technique superiority (e.g., CoH vs RLHF) are restated from primary sources, not independently verified here.

## Citations of interest
- Wei et al., *Chain-of-thought prompting* (NeurIPS 2022) — step-by-step reasoning elicitation in LLMs.
- Shinn et al., *Reflexion: Language agents with verbal reinforcement learning* (NeurIPS 2023) — self-reflection loop without fine-tuning.
- Liu, Sferrazza & Abbeel, *Chain of Hindsight aligns language models with feedback* (2023) — feedback-conditioned causal-LM training.
- Lu et al., *The AI Scientist* (2024) — fully automated open-ended scientific discovery agent.
- Gao et al., *Empowering biomedical discovery with AI agents* (*Cell* 2024) — agent framework for biomedical research.
- Wang et al., *A survey on LLM-based autonomous agents* (Frontiers of Computer Science 2024) — foundational prior review of agent construction/applications/evaluation.
