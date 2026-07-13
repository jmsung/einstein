<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
authors: [Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, Chi Wang]
year: 2023
doi: 10.48550/arXiv.2308.08155
source_url: https://doi.org/10.48550/arXiv.2308.08155
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

## TL;DR
AutoGen is an open-source framework that builds LLM applications as conversations between customizable, conversable agents — each backed by LLMs, humans, tools, or combinations — programmed via a "conversation programming" paradigm that fuses natural language and code to express flexible (static and dynamic) interaction patterns.

## Key findings
- **Two core abstractions.** (1) *Conversable agents* — entities with a role that send/receive messages and `generate_reply`, configurable with LLM, human, and/or tool back-ends. The `ConversableAgent` base class subclasses into `AssistantAgent` (LLM-backed solver) and `UserProxyAgent` (human-input + code/function execution). (2) *Conversation programming* — splitting development into defining agents and programming their interaction via conversation-centric computation + conversation-driven control flow.
- **Auto-reply mechanism** gives decentralized control: an agent auto-invokes `generate_reply` on receiving a message and replies unless a termination condition is met — no separate control plane. Control flow is expressible in natural language (LLM prompting), Python code, or transitions between the two (e.g., LLM function calls).
- **Dynamic group chat** via `GroupChatManager`: repeatedly selects a speaker (role-play prompt), collects its response, broadcasts to all. A pilot on 12 complex tasks showed role-play speaker selection beats task-based selection on success rate and uses fewer LLM calls.
- **Empirical results across 6 applications (Fig. 4):**
  - **A1 Math (MATH dataset, GPT-4):** AutoGen's out-of-the-box two-agent system reached **69.48%** on the full test set vs GPT-4's **55.18%**; beat ChatGPT+Code Interpreter, ChatGPT+Plugin (Wolfram), Multi-Agent Debate, and LangChain ReAct on 120 level-5 problems.
  - **A2 Retrieval-augmented QA/code:** a novel *interactive retrieval* feature ("UPDATE CONTEXT" re-retrieval) outperformed the "I don't know" ablation and DPR; ~19.4% of Natural Questions triggered an Update Context call.
  - **A3 ALFWorld decision-making:** adding a third *grounding agent* (injecting commonsense after 3 repeated actions) gave a **~15% average gain** over the two-agent design and over ReAct (3-agent best-of-3 = 77% all-tasks vs ReAct 66%).
  - **A4 Multi-agent coding (OptiGuide):** Commander/Writer/Safeguard design reduced core workflow code from **>430 lines to 100** (~4×), saved ~3× user time, cut interactions 3–5×, and boosted unsafe-code F1 by **8% (GPT-4) / 35% (GPT-3.5)** vs a single agent.
  - **A6 Conversational Chess:** a board agent for move validation/grounding prevented illegal-move game disruptions seen with prompt-only grounding.
  - **A7 MiniWoB++ browser tasks:** two-agent MiniWobChat hit 52.8% across 49 tasks, only 3.6% below the task-specialized RCI SOTA.
- **Differentiators (Table 1):** AutoGen is generic infrastructure supporting *flexible* (static + dynamic) conversation patterns, code execution, and chat/skip human involvement — unlike Multi-Agent Debate, CAMEL, BabyAGI (all static), and MetaGPT (specialized to software dev).

## Methods (brief)
Framework paper with empirical benchmarking. Evaluations span MATH, Natural Questions (RAG, F1/Recall), ALFWorld (134 unseen tasks, success rate), an OptiGuide coding/safeguard dataset, MiniWoB++, plus ablations isolating the grounding agent, interactive retrieval, multi- vs single-agent design, and role-play vs task-based speaker selection. Base models are GPT-3.5-turbo and GPT-4; comparisons against AutoGPT, LangChain ReAct, CAMEL, BabyAGI, MetaGPT, RCI, and ChatGPT plugins.

## Limitations
Authors note the work is "early experimental." Benchmarks use small samples in places (120 level-5 math problems, 12 group-chat tasks, ~10-question user study). Many baselines are fast-moving open-source projects evaluated at one snapshot. No systematic guidance yet on optimal agent topology/count, and fully autonomous multi-agent chats raise unaddressed safety/oversight risks (cascading failures, reward hacking).

## Citations of interest
- Yao et al. 2022, **ReAct** — reasoning+acting prompting; integrated as the A3 baseline and into AutoGen's ALFWorld agent.
- Liang et al. 2023 / Du et al. 2023, **Multi-Agent Debate** — prior evidence that multiple agents improve divergent thinking, factuality, reasoning; a static-pattern baseline.
- Li et al. 2023a, **OptiGuide** — supply-chain optimization system re-implemented as AutoGen's A4 multi-agent coding case.
- Shridhar et al. 2021, **ALFWorld** — text-world embodied decision-making benchmark used in A3.
- Hong et al. 2023, **MetaGPT** — multi-agent software-dev framework, the closest specialized comparator in Table 1.
- Lewis et al. 2020, **RAG** — retrieval-augmented generation, basis for the A2 Retrieval-augmented Chat.
