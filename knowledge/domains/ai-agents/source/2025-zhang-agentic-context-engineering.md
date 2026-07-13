<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
authors: [Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, Kunle Olukotun]
year: 2025
doi: null
source_url: https://arxiv.org/abs/2510.04618
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

## TL;DR
ACE adapts LLM behavior by evolving the *context* (system prompts, agent memory) rather than weights, treating it as an incrementally-updated "playbook" built by a Generator/Reflector/Curator loop — yielding +10.6% on agent tasks and +8.6% on finance benchmarks while cutting adaptation latency ~86.9%, and matching a top production agent on AppWorld with a smaller open-source model.

## Key findings
- **Two failure modes of prior context adaptation are named and diagnosed**: (1) *brevity bias* — optimizers (e.g., GEPA) collapse toward short generic prompts that drop domain heuristics; (2) *context collapse* — monolithic LLM rewriting erodes detail over iterations. Documented case (Fig. 2): on AppWorld, context at step 60 held 18,282 tokens @ 66.7 acc, then collapsed at step 61 to 122 tokens @ 57.1 acc — worse than the 63.7 no-adaptation baseline.
- **ACE architecture (Fig. 4)**: three specialized roles share one LLM — *Generator* produces reasoning trajectories, *Reflector* distills lessons from successes/failures, *Curator* merges insights into the context. Inspired by Dynamic Cheatsheet but adds a dedicated Reflector.
- **Incremental delta updates**: context is a set of itemized bullets, each with metadata (unique ID + helpful/harmful counters) and content (a strategy, concept, or failure mode). The Curator writes only new bullets, merged deterministically by non-LLM logic — enabling localization, parallel batched merges, and avoiding full rewrites.
- **Grow-and-refine**: new bullets appended, existing ones updated in place; periodic/lazy de-duplication via semantic embeddings prunes redundancy.
- **Agent benchmark (AppWorld, DeepSeek-V3.1, Table 1)**: ReAct+ACE beats ReAct+ICL and ReAct+GEPA offline by 12.3% and 11.9%; online beats Dynamic Cheatsheet by 7.6%. Works **without ground-truth labels** (+14.8% over ReAct using execution feedback alone). On the Sept-2025 leaderboard, ACE (59.4% avg, DeepSeek-V3.1) matches IBM CUGA (60.3%, GPT-4.1) and surpasses it on test-challenge.
- **Domain benchmarks (finance, Table 2)**: offline ACE beats ICL/MIPROv2/GEPA by avg 10.9% (FiNER 70.7→78.3, Formula 67.5→85.5); online beats DC by 6.2%. Also generalizes — DDXPlus medical 75.2→90.2 (+15.0), BIRD-SQL +5.1.
- **Cost/speed (Table 4)**: vs GEPA offline on AppWorld, 82.3% lower latency, 75.1% fewer rollouts, 80.8%/83.6% lower input/output tokens. vs DC online on FiNER, 91.5% lower latency, 83.6% lower token dollar cost.
- **KV cache reuse** makes longer contexts cheap: 91.8% of ACE input tokens served from cache at eval (GPT-5.1), cutting billed input cost 82.6% — so longer context ≠ higher serving cost.
- **Ablations (Table 3, 18)**: removing incremental delta updates drops AppWorld test-normal by −11.7% TGC / −27.8% SGC; Reflector + multi-epoch + offline warmup each add gains. Robust across DeepSeek-V3.1, GPT-OSS-120B, GPT-5.1, Llama-3.3-70B; tolerant of noisy/weak Reflectors except under fully adversarial corruption every iteration.

## Methods (brief)
Empirical evaluation on AppWorld (interactive coding agent), FiNER/Formula (XBRL financial reasoning), and StreamBench DDXPlus/BIRD-SQL, comparing against ICL, MIPROv2, GEPA, and Dynamic Cheatsheet baselines. To isolate the benefit of context construction, the same backbone LLM (default DeepSeek-V3.1, non-thinking) serves as Generator, Reflector, and Curator. Offline (train-then-test pass@1) and online (sequential predict-then-update) regimes are both tested, with and without ground-truth labels.

## Limitations
Gains hinge on a "reasonably strong" Reflector and on reliable feedback signals — without ground-truth labels or execution outcomes (e.g., FiNER without supervision), both ACE and DC can degrade below baseline as context is polluted by spurious signals. ACE is most beneficial for detail-heavy, tool-use, or environment-specific tasks; for tasks with concise fixed strategies (HotPotQA, Game of 24) rich contexts add little. Benchmarks are non-biological; no domain-science transfer is claimed.

## Citations of interest
- Suzgun et al. 2025, *Dynamic Cheatsheet* (arXiv:2504.07952) — test-time adaptive external memory; the direct architectural inspiration and key online baseline.
- Agrawal et al. 2025, *GEPA* (arXiv:2507.19457) — reflective prompt evolution optimizer; the main offline baseline and the exemplar of brevity bias.
- Shinn et al. 2023, *Reflexion* — verbal reinforcement learning via reflection on failures.
- Yao et al. 2023, *ReAct* — reasoning+acting agent framework on which all AppWorld baselines are built.
- Trivedi et al. 2024, *AppWorld* — controllable interactive coding-agent benchmark.
- Yuksekgonul et al. 2025, *TextGrad* (Nature) — optimizing prompts via gradient-like textual feedback.
- Xu et al. 2025, *A-MEM* — Zettelkasten-style agentic memory with linked, attributed entries.
