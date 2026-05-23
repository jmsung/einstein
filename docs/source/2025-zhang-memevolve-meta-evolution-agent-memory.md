---
type: source
kind: paper
title: "MemEvolve: Meta-Evolution of Agent Memory Systems"
authors: Guibin Zhang, Haotian Ren, Chong Zhan, Zhen Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng Yan
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2512.18746
source_local: ../raw/2025-zhang-memevolve-meta-evolution-agent-memory.pdf
topic: general-knowledge
cites:
---

![image 1](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile1.png>)

### MemEvolve: Meta-Evolution of Agent Memory Systems

OPPO AI Agent Team, LV-NUS lab

# arXiv:2512.18746v1[cs.CL]21Dec2025

#### Abstract

Self-evolving memory systems are unprecedentedly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the staticity of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents’ experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior research and foster openness in future selfevolving systems, we introduce EvolveLab, a unified self-evolving memory codebase that distills twelve representative memory systems into a modular design space (encode, store, retrieve, manage), providing both a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks demonstrate that MemEvolve achieves (I) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to 17.06%; and (II) strong cross-task and cross-LLM generalization, designing memory architectures that transfer effectively across diverse benchmarks and backbone models.

Date: December 23, 2025 Code: https://github.com/bingreeky/MemEvolve

![image 2](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile2.png>)

![image 3](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile3.png>)

![image 4](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile4.png>)

xbench-DS WebWalkerQA GAIA

Figure 1 The comparison between MemEvolve and several popular self-evolving agent memory systems across benchmarks. The underlying framework is Flash-Searcher (Qin et al., 2025)+GPT-5-Mini.

![image 5](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile5.png>)

Human Learners

Solution

Task

Error Notebook

![image 6](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile6.png>)

Tasks

###### Solutions

Task

![image 7](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile7.png>)

###### Solutions

###### Tasks

Evaluate $(1+2i)6-3i$.

The answer seems to be 6-9i.

![image 8](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile8.png>)

Disgard

The answer seems to be 6-9i. Feedback:

Evaluate $(1+2i)6-3i$.

![image 9](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile9.png>)

![image 10](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile10.png>)

Solution

![image 11](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile11.png>)

![image 12](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile12.png>)

Solution Template

![image 13](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile13.png>)

![image 14](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile14.png>)

![image 15](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile15.png>)

![image 16](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile16.png>)

Error Notebook

Adapitve Learner

Mediocre Learner

Skillful Learner

![image 17](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile17.png>)

Previous Trajectories

Tips & Inisghts

![image 18](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile18.png>)

Previous Traj.

![image 19](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile19.png>)

e.g., MemoryBank, JARVIS-1,

e.g., Expel, G-Memory, ChemAgent

![image 20](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile20.png>)

Skills & Tools e.g., SkillWeaver, Alita

Trajs. & Solutions

... Solution Solution

![image 21](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile21.png>)

Error Reflection

![image 22](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile22.png>)

![image 23](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile23.png>)

![image 24](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile24.png>)

![image 25](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile25.png>)

![image 26](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile26.png>)

![image 27](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile27.png>)

MobileGPT, Voyager, Mem^p,

...

Tasks

Disgard Tasks

![image 28](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile28.png>)

![image 29](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile29.png>)

Reusable Insights

![image 30](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile30.png>)

![image 31](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile31.png>)

Agent Memory

Agents without memory

Figure 2 The paradigm of agent self-evolution admits a natural analogy to human learning. At one extreme, a mediocre learner fails to benefit from experience (agents without memory). More capable skillful learners can extract reusable skills from past experience, albeit through a fixed and pre-defined abstraction scheme. In contrast, an adaptive learner simultaneously accumulates experience and dynamically adjusts the strategy by which experience is consolidated and utilized. This final regime precisely characterizes the objective of MemEvolve.

#### 1 Introduction

Language agents and agent systems, empowered by increasingly capable foundation models (Team et al., 2025a,b) and sophisticated scaffolding (Wang et al., 2024a; LangChain, 2023), have advanced rapidly, demonstrating unprecedented performance across complex tasks such as deep research (Chen et al., 2025), scientific discovery (Bai et al., 2025; Wei et al., 2025b), and industrial report generation (Zhang et al., 2025g). A key driving force behind this success is the agent memory system (Zhang et al., 2024b; Hu et al., 2025c), which persistently captures interactions between the agent and environment, distilling them into diverse forms of knowledge and skills, and thereby enabling large language model (LLM)-based agents to evolve continuously in task solving and world exploration (Wu et al., 2025c).

Naturally, the choice of memory paradigm plays a decisive role in shaping an agent’s capacity for on-the-fly selfevolution. Initial designs centered on raw trajectory storage and few-shot prompting (Zhong et al., 2024; Wen

- et al., 2024), which were later superseded by more abstracted textual artifacts such as tips, shortcuts, and reasoning templates (Ouyang et al., 2025; Zhang et al., 2025b; Ye et al., 2025; Tang et al., 2025). Recent advances have also explored structured tool interfaces (e.g., APIs (Zheng et al., 2025), MCPs (Qiu et al., 2025b,a; Zhang et al., 2025h)) and code-level repositories (Zhang et al., 2025e; Wang et al., 2025a) as memory carriers. Amid this growing diversity, an inquisitive practitioner might ask: What kind of memory architecture most effectively drives agent self-improving?

We posit that no universally optimal memory architecture exists. For instance, a memory system that distill reusable APIs from past trajectories may excel in tasks such as web browsing, yet offer limited utility for mathematical and scientific reasoning. Conversely, memories predicated on self-critique, while powerful in reasoning-intensive domains (Cai et al., 2025), show diminished efficacy in coding and tool-use scenarios, as empirically discussed in (Zhang

- et al., 2025d). We contend that these trade-offs arise from the static nature of current memory systems. Researchers typically design a fixed memory pipeline (i.e., memory ingestion/abstraction/retrieval (Zhang et al., 2025i)) and embed it within an agent, assuming it will sustain long-term evolution through mere exposure to new experiences. Yet this overlooks a crucial reality: distinct tasks are coupled with distinct memory affordances. A memory system that cannot adapt itself to the task at hand is fundamentally misaligned with the very premise of open-ended agent evolution.


To elucidate this dilemma, consider the analogy of human learning. Both high- and low-performing students inevitably make mistakes, yet their distinction lies in the meta-cognitive strategies they employ to learn from these errors. An underperforming student might resort to rote memorization, superficially recording an error without genuine comprehension (Zhong et al., 2024; Orhan, 2023). In contrast, a more skillful student engages in higher-order learning: they not only record errors but also distill transferable insights through reflection (Shinn et al., 2023; Zhao et al., 2024) or derive reusable schemas (Zheng et al., 2025; Qiu et al., 2025b)). Current memory systems effectively model a skillful

learner. Herein lies the critical gap: the most effective human learners are not merely skillful, but adaptive. They dynamically alter their learning strategies based on the subjects, for instance, prioritizing memorization for literary analysis while abstracting solution templates for mathematics. It is precisely this transition, from a skillful to an adaptive learner (as shown in Figure 2), that we argue agent memory systems must undergo. To put it more formally:

How can a memory system not only facilitate the agent system’s evolution but also meta-evolve its own architecture to achieve superior task-domain performance gains while preserving generalizability?

To address the challenge, we introduce MemEvolve, a framework that facilitates the dual evolution of an agent’s experience and its memory architecture. Conceptually, MemEvolve operates as a bilevel optimization process: the inner loop performs a first-order evolution, where the agent, guided by a fixed memory system, adapts to a continuous stream of new tasks by populating its experience base. The outer loop drives a second-order evolution, meta-learning a more effective memory architecture to accelerate future learning. This allows the agent not only to evolve, but to evolve more efficiently and intelligently over time.

However, the vast and heterogeneous design space of memory systems (e.g., knowledge graphs, skill libraries, vector databases) presents a significant challenge to controllable optimization. To render this optimization tractable, we introduce a modular design, decomposing any memory architecture into four key components: ♣ Encode (perceiving and formatting experiences), ♦ Store (committing information), ♥ Retrieve (context-aware recall), and ♠ Manage (consolidation and forgetting). MemEvolve evolves the programmatic implementations of these modules in a modeldriven fashion, using feedback from the agent’s performance in the inner loop. This process establishes a virtuous cycle: an improved memory architecture from the outer loop enhances the agent’s learning efficiency. In turn, a more capable agent generates higher-quality trajectories, providing a more precise fitness signal for the outer loop to drive the next round of architectural evolution.

To ground our framework within the diverse landscape of existing self-improving agent memories, we systematically re-implement twelve representative architectures in a unified modular design space, including ExpeL (Zhao et al.,

- 2024), Agent Workflow Memory (Wang et al., 2024b), and Dynamic Cheatsheet (Suzgun et al., 2025). The resulting framework, denoted as EvolveLab, serves both as an empirical foundation for MemEvolve’s evolutionary process and as a standardized codebase to facilitate future research on self-evolving agents. Our contributions are as follows:


❶ Unified Codebase: We introduce EvolveLab, a modular design space for self-improving agent memory systems encompassing four key components (encoding, storage, retrieval, and management), providing unified implementations and benchmark support for a wide range of prevailing agent memory systems.

❷ Meta-Evolution Framework: We propose MemEvolve, a meta-evolutionary framework that jointly evolves both agents’ experiential knowledge and their underlying memory architecture, in which agent systems not only accumulate experience but also progressively refine their mechanism for learning from it.

❸ Experimental Evaluation: Extensive experiments on four challenging agentic benchmarks demonstrate that MemEvolve delivers (I) substantial performance gains, improving frameworks such as SmolAgent and FlashSearcher by up to 17.06%; and (II) cross-domain, cross-framework and cross-LLM generalization, where memory systems evolved on TaskCraft yield 2.0 − 9.09% gains with unseen benchmarks and backbone models.

#### 2 Related Work

LLM Agent Systems. The past two years have witnessed rapid advances in LLM-based agent systems across multiple dimensions (Tran et al., 2025; Fang et al., 2025a). In terms of system complexity, development has progressed from early single-agent setups with manually defined workflows and limited tool configurations (Wu et al., 2023; Significant-Gravitas, 2023) to sophisticated multi-agent architectures featuring diverse MCP integrations and automated orchestration (Zhang et al., 2024a, 2025a; Wang et al., 2025b; Zhang et al., 2025c). From the perspective of task domains, capabilities have expanded from relatively constrained areas such as coding and mathematical reasoning (Hong et al., 2024; Yin et al., 2023) to more challenging domains, including deep research and scientific discovery (Du et al., 2025; Ghareeb et al., 2025). Today, numerous open-source multi-agent systems demonstrate competitive performance on demanding benchmarks such as GAIA (Mialon et al., 2023), HLE (Phan et al., 2025), BrowseComp (Wei et al., 2025a), and xBench (Chen et al., 2025), including CAMEL’s OWL (Hu et al., 2025a), Tencent’s CK-Pro (Fang et al., 2025c), Skywork’s AgentOrchestra (Zhang et al., 2025f), and ByteDance’s AIME (Shi et al., 2025b), among others.

Agent Memory Architectures. Agent memory systems can be broadly divided by objective into personalized memory and self-improving memory (Zhang et al., 2024b; Hu et al., 2025c). The former enables agent chatbots to dynamically capture user-specific information and preferences, while the latter focuses on distilling knowledge and skills from continual interactions with the environment to enhance performance, a focus adopted in this work. Self-improving memories are primarily differentiated by their storage modality. Early systems stored raw agent trajectories as few-shot examples (Wang et al., 2023; Zhong et al., 2024; Packer et al., 2023); subsequent designs abstracted these experiences into higher-level lessons, insights (Yang et al., 2025; Sun and Zeng, 2025; Wu et al., 2025b), procedural tips (Wang et al., 2025c; Zheng et al., 2025; Fang et al., 2025b), and more recently, reusable tools and structured repositories (Zhao et al., 2025; Qiu et al., 2025a,b; Zhang et al., 2025e). Despite their differences in representation, there approaches share the same ambition, i.e., to enable agents to learn, adapt, and improve in a human-esque manner.

#### 3 EvolveLab: A Unified Codebase for Self-Evolving Memory

In this section, we first formalize the LLM-based agentic system and its associated memory architecture, then present the modular design space of EvolveLab, which comprehensively captures the characteristics of existing self-evolving agent memories, and finally introduce the unified codebase EvolveLab.

##### 3.1 Preliminary

Wedenotesformalizethe sharedan LLM-basedstate space,agenticA= ⋃systemi∈I Ai representsas M = ⟨Ithe,Sjoint,A,Ψaction,Ω⟩, wherespace, IandindexesΨ(st+1the∣ st{,a1,t⋯,µ,N(t))} agents,describesS the environment dynamics with µ(t)∈I indicating the active agent at time step t. The system leverages a memory

module Ω, which maintains a continuously evolving memory state Mt. At each step, the active agent observes the current state st, considers a task-specific query Q, and interacts with Ω to retrieve contextually relevant memory ct, conditioned on its interaction history Ht. The agent µt’s policy πµ

then delivers an action: at = πµ(t)(st,Ht,Q,ct), ct ∼ Ω(Mt,st,Ht,Q).

t

Following task execution, a trajectory τ =(s0,a0,...,sT) is recorded, with an overall performance evaluated via a terminal reward R(τ). The memory system assimilates new experience units ϵ, which can vary in granularity (from individual state-action transitions to aggregated segments or complete trajectories), and updates the memory state as

Mt+1 = Ω(Mt,ϵ),

where Ω abstracts the memory’s mechanisms for integrating and organizing new experiences or knowledge.

##### 3.2 Modular Design Space of Memory Systems

The heterogeneous and rapidly evolving landscape of self-improving agent memories presents challenges for systematic analysis and controlled experimentation. To address this, we propose a modular design space that decomposes any memory system Ω into four functionally distinct yet interdependent components: Ω =(E,U,R,G), representing encode, store, retrieve, and manage operations, respectively.

- • Encode (E): Transforms raw experiences, such as trajectory segments τt =(st,at,st+1), tool outputs, or selfcritiques, into structured representations et =E(ϵt). Encoding may be as simple as compressing raw traces (Zheng et al., 2023) or as sophisticated as extracting generalizable lessons (Zheng et al., 2025).
- • Store (U): Integrates encoded experiences into the persistent memory Mt, yielding Mt+1 =U(Mt,et). Storage can be vector databases (Zhao et al., 2024), knowledge graphs (Zhang et al., 2025b; Rasmussen et al., 2025), or others.
- • Retrieve (R): Provides task-relevant memory content, formalized as ct =R(Mt,st,Q), which informs the agent’s policy decision at. Retrieved content may include reusable tools (Zhang et al., 2025f), planning experience (Tang et al., 2025), or distilled procedural knowledge (Wu et al., 2025b; Yang et al., 2025; Fang et al., 2025b).
- • Manage (G): Performs offline and asynchronous operations such as consolidation, abstraction, or selective forgetting to maintain long-term memory quality and efficiency, denoted as Mt′ =G(Mt).


This modular abstraction allows us to represent each memory system as a specific combination of programmatic implementations for (E,U,R,G), forming a “genotype” that facilitates the meta-evolutionary process of MemEvolve.

Table 1 A taxonomy of self-improving agent memory systems implemented in EvolveLab. In the “Mul.” column, ♂ indicates support for single-agent settings, while ♂♂ denotes compatibility with multi-agent systems. “Gran.” specifies the granularity at which memory is provided (step-wise vs. trajectory-wise), and “Online” indicates whether memory is updated on-the-fly ( ) or maintained as an offline experience repository ( ).

Method Date Mul. Gran. Online Encode Store Retrieve Manage

- I. Voyager 2023.5 ♂ traj. Traj. & Tips Vector DB Semantic Search N/A

- II. ExpeL 2023.8 ♂ traj. Traj. & Insights Vector DB Contrastive Comparison N/A

- III. Generative 2023.10 ♂♂ traj. Traj. & Insights Vector DB Semantic Search N/A

- IV. DILU 2024.2 ♂ traj. Traj. Vector DB Semantic Search N/A

- V. AWM 2024.9 ♂ traj. Workflows Vector DB Semantic Search N/A

- VI. Mobile-E 2025.1 ♂ step Tips & Shortcuts Vector DB Semantic Search N/A

- VII. Cheatsheet 2025.4 ♂ traj. Tips & Shortcuts JSON Semantic Search N/A

- VIII. SkillWeaver 2025.4 ♂ traj. APIs Tool Library Function Matching Skill Pruning

- IX. G-Memory 2025.6 ♂♂ traj. Tips & Workflow Graph Graph/Semantic Search Episodic Consolidation

- X. Agent-KB 2025.7 ♂♂ step Tips & Workflow Hybrid DB Hybrid Search Deduplication

- XI. Memp 2025.8 ♂ step. Tips & Workflow JSON Semantic Search Failure-driven Adjustment

- XII. EvolveR 2025.10 ♂ step. Tips & Workflow JSON Contrastive Comparison Update & Pruning


- 3.3 EvolveLab Codebase

Based on the above design space, we introduce EvolveLab, a unified and extensible codebase designed for the systematic implementation and evaluation of self-evolving memories, serving as a standardized resource for the community.

Implementation. The cornerstone of EvolveLab is its modular and hierarchical design. Every memory architecture re-implemented in our codebase (see Table 1) inherits from a singular abstract base class, BaseMemoryProvider, which enforces the unified four-component interface: ♣ Encode, ♦ Store, ♥ Retrieve, and ♠ Manage. This ensures that diverse memory mechanisms can be managed, modified, and evolved under a consistent programmatic structure. More details on the implementations can be found at Section A.

Evaluation. Beyond unified implementation, EvolveLab provides a standardized testbed for rigorously assessing memory architectures across diverse agentic tasks. The framework offers out-of-the-box support for multiple challenging benchmarks, including GAIA (Mialon et al., 2023), xBench (Chen et al., 2025), and DeepResearchBench (Du et al., 2025). EvolveLab accommodates two evaluation paradigms: an ■ online mode, where the experiential memory base is updated on-the-fly as the agent system processes a continuous stream of tasks, and an ■ offline mode, where the memory system first accumulates experience from a static set of trajectories before being assessed on separate, unseen tasks. To ensure robust and versatile assessment, we support multiple evaluation protocols, including exact string matching and flexible LLM-as-a-Judge.

- 4 MemEvolve: A Meta-Evolving Memory Framework


- 4.1 Dual-Evolution Process


Traditional self-improving memory systems operate under a fixed memory architecture, where the memory interface Ω is predefined and remains static. Within this architecture, the agent iteratively populates and updates its memory state Mt through interaction with the environment and task experiences. For a trajectory τ induced by a query Q, the memory evolution follows

Mt+1 = Ω(Mt,ϵτ), ϵτ ∈E(τ),

where E(⋅) denotes an experience extraction operator that maps a trajectory to a set of experience units, and ϵτ is an element sampled from this set. While this enables the accumulation of knowledge, it fundamentally precludes architectural adaptation, as the memory interface Ω itself remains immutable.

To transcend this limitation, we propose a dual-evolution process that jointly evolves (i) the agent’s memory base and (ii) the underlying memory architectures (as illustrated in Figure 3). Instead of a single static Ω, we maintain, at each

evolutionary iteration k, a finite set of candidate memory systems {Ω(jk)}j∈J(k), where each Ω(jk) is instantiated as a concrete realization of the four-component memory interface Ω(jk) ≜(Ej(k),Uj(k),R(jk),Gj(k)). The initial iteration start from a singleton set ∣J (0)∣= 1, corresponding to a hand-designed baseline memory, while later iterations admit

###### D&D Evolution

###### Search Space MemEvolve Evolution

![image 32](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile32.png>)

![image 33](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile33.png>)

Store

Encode

![image 34](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile34.png>)

###### Retrieve

Memory Candidates:

Traj. (seg) → Units

![image 35](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile35.png>)

semantic→hybrid search

Traj.

Trajectory

![image 36](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile36.png>)

Task semanticskill-based&

![image 37](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile37.png>)

![image 38](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile38.png>)

Memory Unit

Iter 2,

![image 39](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile39.png>)

Performance API cost Exec. Delay

- Cand. 1

Iter 2,

- Cand. 2

Iter 2,

- Cand. 3


probe

![image 40](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile40.png>)

Pareto-ranking

![image 41](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile41.png>)

JSON Database

![image 42](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile42.png>)

![image 43](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile43.png>)

Store

(Moreiterations)...

![image 44](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile44.png>)

Vec. Database

![image 45](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile45.png>)

Iter 1,

- Cand. 1

Iter 1,

- Cand. 2


Logs:

![image 46](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile46.png>)

... ...

![image 47](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile47.png>)

Look-up

Memory Unit

Task qjs19ab Status:

KG Database

![image 48](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile48.png>)

![image 49](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile49.png>)

Meta Evolver

![image 50](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile50.png>)

![image 51](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile51.png>)

Base Mem System

Task cod77mx Status: Task dcs01yyb Status:

![image 52](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile52.png>)

Support Diagnosis Report

InitializeMemorySystem

![image 53](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile53.png>)

Retrieve

![image 54](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile54.png>)

![image 55](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile55.png>)

![image 56](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile56.png>)

![image 57](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile57.png>)

![image 58](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile58.png>)

![image 59](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile59.png>)

![image 60](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile60.png>)

States

Task Query

![image 61](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile61.png>)

Lack tool/skill condensation

... ...

Memory Base

![image 62](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile62.png>)

![image 63](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile63.png>)

semantic search

![image 64](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile64.png>)

Too lengthy memory content Vague filtration Strategy

Memory Units

![image 65](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile65.png>)

summary tools shortcuts

![image 66](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile66.png>)

![image 67](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile67.png>)

Traj.

![image 68](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile68.png>)

Manage

Evolve into

Raw traj. store→multigranular abstraction

Consolidation Update

![image 69](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile69.png>)

Apply to

![image 70](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile70.png>)

![image 71](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile71.png>)

Proposed Evolution

![image 72](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile72.png>)

![image 73](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile73.png>)

![image 74](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile74.png>)

Retrieve

Store

![image 75](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile75.png>)

![image 76](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile76.png>)

###### Retrieve

Encode

###### Store

![image 77](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile77.png>)

![image 78](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile78.png>)

![image 79](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile79.png>)

![image 80](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile80.png>)

![image 81](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile81.png>)

3 level→ 5 levels

Add LLM Guard

Forget

Iteration 1 Iteration 2 Iteration 3

JSON→Graph

Figure 3 The overview of our proposed MemEvolve.

multiple competing candidates. Given a batch of trajectories Tj(k) independently generated by executing the agent with memory system Ω(jk), the dual-evolution process consists of two nested loops:

- • Inner Loop (Experience Evolution). For each candidate memory system Ω(jk), the associated memory state Mt,j(k), initialized as an empty memory at the beginning of iteration k, is updated along trajectories τ ∈Tj(k) via

Mt(+k1),j = Ω(jk)(Mt,j(k),ϵτ), ϵτ ∈Ej(k)(τ).

Executing the agent with Ω(jk) over Tj(k) yields, for each trajectory τ, a feedback vector fj(τ) ∈ Rd, where d = 3 corresponds to the number of evaluation metrics (i.e., task success, token consumption, and latency). An

aggregation operator S summarizes the inner-loop outcomes for each candidate as

F(jk) =S({fj(τ)}τ∈T (k)

j ), j ∈J (k).

- • Outer Loop (Architectural Evolution). The set of memory architectures is then updated based on the collection


of summaries {F(jk)}j∈J(k). A meta-evolution operator F selects high-performing candidates and proposes new variants, producing the next iteration’s candidate set:

{Ω(jk′ +1)}j′∈J(k+1) =F({Ω(jk)}j∈J(k), {F(jk)}j∈J(k)).

Specifically, F ranks candidates according to F(jk), retains the top-K memory systems, and generates new architectures by modifying or recombining all four components (E,U,R,G) of the selected candidates, where K

denotes a fixed survivor budget. We detail the implementation of F(⋅) in Section 4.2.

Unified view. At a higher level, each iteration k alternates between (i) evolving the memory experience base from an empty initialization under a fixed set of architectures, and (ii) evolving the memory architectures themselves based on the induced performance:

({∅}j∈J(k), {Ω(jk)}j∈J(k))   →inner ({Mt(+k1),j}j∈J(k), {Ω(jk)}j∈J(k))   →outer ({Mt(+k1),j}j∈J(k), {Ω(jk′ +1)}j′∈J(k+1)).

By iterating this dual-evolution process, the agent does not merely accumulate experience within a fixed memory system; instead, both the memory base and the governing memory architectures co-evolve, yielding increasingly adaptive and resource-aware memory-driven behavior over time.

##### 4.2 Diagnose-and-Design Evolution

We now detail the meta-evolution operator F, which governs the architectural update in each evolutionary iteration. Conceptually, F decomposes into two coordinated components: (i) architectural selection, which identifies a subset of high-performing memory systems to serve as evolutionary parents, and (ii) diagnose-and-design evolution, which generates new memory architectures from each selected parent through a structured diagnosis procedure followed by a constrained redesign within the modular memory design space.

Architectural Selection. Given the candidate set {Ω(jk)}j∈J(k) and their corresponding summaries {F(jk)}, we define each summary vector as

F(jk) ≜(Perf(jk), −Cost(jk), −Delay(jk)),

where higher values are preferred in all dimensions. Candidates are first ranked by non-dominated sorting over F(jk), yielding a Pareto rank ρ(jk). Within the same Pareto rank, candidates are further ordered by the primary performance metric Perf(jk). The top-K candidates are selected as the parent set:

(ρ(jk), Perf(jk)).

P(k) = Top-K

j∈J (k)

This selection step ensures that architectural evolution is guided by systems that exhibit favorable trade-offs between task effectiveness and resource efficiency, while prioritizing task performance among Pareto-equivalent candidates.

Diagnose-and-Design Evolution. For each parent architecture Ω(pk) ∈ P(k), F generates a set of S descendants {Ω(p,sk+1)}Ss=1 through a two-phase process:

- • Diagnosis. Each parent architecture is examined using trajectory-level evidence from its own execution batch

Tp(k). For each trajectory, the agent provides outcome statistics (e.g., success indicators, token costs) together with a structured description of the associated task query. A replay interface grants access to the corresponding

trajectories τ ∈Tp(k), enabling targeted inspection of memory behavior, including retrieval failures, ineffective abstractions, or storage inefficiencies. The diagnosis phase thus produces a structured defect profile D(Ω(pk)), characterizing architectural bottlenecks across the four memory components (Ep(k),Up(k),R(pk),Gp(k)).

- • Design. Conditioned on the defect profile D(Ω(pk)), a redesigned architecture is constructed by modifying only the permissible implementation sites within the modular interface, thereby ensuring compatibility and isolating architectural changes to the designated design space. The design step produces S variants by instantiating distinct but valid configurations of the four components:


Ω(p,sk+1) = Design(Ω(pk), D(Ω(pk)), s), s ∈{1,...,S}.

These variants differ in encoding strategies, storage rules, retrieval constraints, or management policies, yet all conform to the unified memory-system interface and remain executable by the agent.

Resulting update. Aggregating all descendants across parents yields the next set of candidate architectures:

{Ω(jk′ +1)}j′∈J(k+1) = ⋃

{Ω(p,sk+1)}Ss=1.

Ω(pk)∈P(k)

This diagnose-and-design evolution operationalizes F for producing increasingly adaptive memory systems, ensuring that architectural updates are both empirically grounded and structurally constrained within the unified design space.

#### 5 Experiments

- 5.1 Experiment Setup Benchmarks. We evaluate the proposed framework across four challenging agentic benchmarks, including GAIA (Mialon et al., 2023), WebWalkerQA (Wu et al., 2025a), xBench-DeepSearch (xBench-DS) (Chen et al., 2025), as well as TaskCraft (Shi et al., 2025a). Further statistics and details are provided in Section B.1.


Table 2 Performance of various agent frameworks on the WebWalerQA, xBench-Ds, TaskCraft, and GAIA benchmarks.

GAIA Avg. Level 1 Level 2 Level 3

WebWalker QA

xBench -DS

Task Craft

Framework Model Family

Closed-source Agent Frameworks

Langfun Claude 3.7 etc. - - - 71.52 83.02 68.60 57.69 TraseAgent Claude etc. - - - 70.30 83.02 69.77 46.15 OpenAI Deep Research o1, o3 etc. - - - 67.36 74.29 69.06 47.60 h2oGPTe Claude-3.5 - - - 63.64 67.92 67.44 42.31 Desearch GPT-4o - - - 56.97 71.70 58.14 23.08 Open-Source Agent Frameworks

OWL Workforce (pass@3) GPT-4o+o3-mini 57.64 55.0 58.33 60.61 81.14 58.14 26.92 OWL RP (pass@3) GPT-4o+o3-mini - - - 58.18 81.14 54.65 23.08 TapeAgents Claude 3.7 etc. - - - 55.76 71.70 53.49 30.77 AutoAgent Claude 3.5 etc. - - - 55.15 71.70 53.40 26.92 Smolagents GPT-4.1 - - - 55.15 67.92 53.49 34.62 Smolagents GPT-5-mini 58.82 51.0 64.00 55.75 69.81 54.65 30.77 Magnetic-1 OpenAI o1 etc. - - - 46.06 56.60 46.51 23.08 Cognitive Kernel-Pro (pass@1) Claude-3.7 etc. 60.64 56.0 66.00 60.00 79.25 56.98 30.77 Cognitive Kernel-Pro (pass@3) Claude-3.7 etc. - - - 75.15 84.91 73.26 61.54 OAgents Claude-3.7 etc. 58.23 47.0 - 66.67 77.36 66.28 46.15 JoyAgents Claude-4, o4-mini - - - 75.2 86.8 77.9 42.3

![image 82](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile82.png>)

![image 83](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile83.png>)

- Agent KB (pass@1) GPT-4.1 60.59 48.0 61.67 61.21 79.25 58.14 34.62

- Agent KB (pass@2) GPT-4.1 68.82 58.0 72.67 67.27 83.02 67.44 34.62

- Agent KB (pass@3) GPT-4.1 73.53 68.0 75.33 73.94 84.91 73.26 53.85 Flash-Searcher (pass@1) GPT-5-mini 71.18 69.0 69.67 69.09 79.25 69.77 46.15 Flash-Searcher (pass@1) Kimi K2 52.35 66.0 58.00 52.12 58.49 52.33 34.62 Flash-Searcher (pass@1) DeepSeek V3.2 69.41 68.0 69.33 60.61 79.25 53.49 46.15


![image 84](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile84.png>)

![image 85](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile85.png>)

![image 86](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile86.png>)

- MemEvolve + (pass@1) GPT-5-mini 61.18 57.0 67.67 64.24 83.02 58.14 46.15

![image 87](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile87.png>)

- MemEvolve + (pass@2) GPT-5-mini 67.06 63.0 75.00 67.88 84.91 63.95 46.15

![image 88](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile88.png>)

- MemEvolve + (pass@3) GPT-5-mini 71.18 68.0 77.00 72.12 88.68 68.60 50.00


![image 89](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile89.png>)

- MemEvolve + (pass@1) GPT-5-mini 74.71 74.0 72.00 73.33 83.02 73.26 53.85

![image 90](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile90.png>)

- MemEvolve + (pass@2) GPT-5-mini 79.41 77.0 75.00 77.58 92.45 74.42 57.69

![image 91](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile91.png>)

- MemEvolve + (pass@3) GPT-5-mini 81.18 78.0 79.33 80.61 94.34 79.07 57.69


![image 92](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile92.png>)

MemEvolve + (pass@1) Kimi K2 69.41 68.0 68.00 61.21 67.92 63.95 38.46 MemEvolve + (pass@1) DeepSeek V3.2 72.35 70.0 72.67 67.88 83.02 63.95 50.00

![image 93](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile93.png>)

![image 94](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile94.png>)

Method Configurations. We run the dual-evolution process for Kmax = 3 iterations. In the outer loop, the survivor budget is set as K = 1; at each iteration, only the top-ranked architecture is retained and expanded to S = 3 descendants.

In the inner loop, each candidate architecture Ω(jk) is evaluated on a batch Tj(k) of 60 task trajectories, consisting of 40 newly sampled tasks and 20 tasks reused from the previous iteration to stabilize inter-iteration comparison.

Agent Framework. We integrate MemEvolve into two representative agentic frameworks: SmolAgent (Roucher et al., 2025), a lightweight two-agent architecture, and Flash-Searcher (Qin et al., 2025), a high-performance single-agent deep research system. To assess the generalization and plug-and-play capability of MemEvolve, we further evaluate it on two held-out multi-agent systems: Tencent’s Cognitive Kernel-Pro (CK-Pro) (Fang et al., 2025c), a three-agent framework comprising main/file/web agents; and OWL (Hu et al., 2025b), a hierarchical system including planner, coordinator, web, document, and coding agents. This diversity in architecture and system complexity enables a comprehensive examination of the adaptability of MemEvolve across heterogeneous agentic scaffolds.

![image 95](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile95.png>)

![image 96](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile96.png>)

![image 97](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile97.png>)

![image 98](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile98.png>)

Model Configurations. We instantiate MemEvolve using GPT-5-mini (OpenAI, 2025) as the LLM backbone for the underlying agentic frameworks, and for supporting the meta-evolution operator F(⋅). To further evaluate the crossLLM generalization capability of MemEvolve, we additionally consider alternative backbones, including DeepSeek V3.2 (DeepSeek-AI et al., 2025), and Kimi K2 (Team et al., 2025a). For clarity, we explicitly report the specific LLM backbone used by each agentic framework in the following experiments.

Table 3 Performance, cost, delay, and steps across datasets under different memory settings for Flash-Searcher. Here, cost denotes the average API cost incurred per task query, delay measures the average execution latency (seconds) per task, and #steps reports the number of agent interaction steps required to complete each task.

![image 99](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile99.png>)

GAIA xBench WebWalkerQA

Memory Setting

Perf. Cost Delay #Steps Perf. Cost Delay #Steps Perf. Cost Delay #Steps

No-Memory 69.09 0.086 505.46 10.44 69.00 0.141 523.05 14.69 71.18 0.048 251.57 6.91 Generative 66.67 0.061 436.26 8.87 70.00 0.131 818.37 13.45 72.35 0.045 268.56 6.64 Voyager 69.70 0.060 499.89 9.25 68.00 0.117 553.46 12.71 73.53 0.049 333.69 6.99 DILU 66.67 0.059 444.62 8.91 69.00 0.134 500.72 13.83 72.94 0.046 272.16 6.96 ExpeL 66.06 0.059 500.11 8.68 64.00 0.123 710.32 13.05 69.41 0.076 385.28 10.96 AWM 67.27 0.062 584.88 10.23 71.00 0.138 761.33 14.12 72.35 0.068 397.20 11.40 Mobile-E 69.09 0.065 321.80 9.35 68.00 0.120 537.18 13.16 71.76 0.059 296.01 6.52 Cheatsheet 68.48 0.069 559.81 9.72 65.00 0.174 818.07 15.99 72.94 0.057 367.13 7.59 MemEvolve 73.33 0.085 693.33 10.14 74.00 0.136 773.06 14.20 74.71 0.040 332.49 6.64

##### 5.2 Main Results

![image 100](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile100.png>)

![image 101](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile101.png>)

We report the pass@1–3 performance of MemEvolve integrated with SmolAgent and Flash-Searcher in Table 2, together with its generalization results when paired with unseen LLMs (Kimi K2, DeepSeek V3.2). Notably, on the relatively simple TaskCraft benchmark, we evolve two distinct memory systems using MemEvolve+ and MemEvolve+ , respectively. These evolved memory systems are then fixed and evaluated on WebWalkerQA and xBench-DS, i.e., without conducting dataset-specific meta-evolution.

![image 102](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile102.png>)

![image 103](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile103.png>)

![image 104](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile104.png>)

![image 105](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile105.png>)

Figure 4 The cross-framework generalization analysis. We transfer the memory system evolved on TaskCraft+ to and . Red percentages denote the relative score gains of each framework after integrating MemEvolve over its memory-free counterpart.

![image 106](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile106.png>)

![image 107](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile107.png>)

![image 108](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile108.png>)

Memory System Matters For Agent Systems. As shown in Table 2, equipping agentic systems with effective memory architectures is critical to performance. On xBench, +GPT-5-Mini achieves an initial pass@1 of 51%; after integrating MemEvolve, pass@1 increases by 6%, while pass@3 goes up to 68.0%. Similarly, +GPT-5-Mini improves from 69% to 74% on xBench when augmented with MemEvolve. These results clearly demonstrate the substantial impact of a well-designed memory system on agent performance. At the same time, memory is not a panacea and remains bounded by the capabilities of the underlying agentic framework. On GAIA, MemEvolve + attains a pass@3 of 72.12%, comparable to AgentKB, while avoiding the construction of large and costly offline knowledge bases. In contrast, the gains with MemEvolve + are even more pronounced, achieving a pass@3 of 80.61%, surpassing several strong multi-agent systems such as OWL-Workforce and CK-Pro under the same metric.

![image 109](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile109.png>)

![image 110](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile110.png>)

![image 111](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile111.png>)

![image 112](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile112.png>)

MemEvolve Exhibits Cross-Task, Cross-Model, and Cross-Framework Generalization. Recall that the memory systems used on WebWalkerQA and xBench are directly inherited from those evolved on TaskCraft, without any task-specific meta-evolution. Nevertheless, these transferred memories yield consistent gains on more challenging benchmarks (WebWalkerQA+ : 58.82 → 61.18%; xBench+ : 69.0 → 74.0%), indicating that MemEvolve captures task-agnostic principles of memory design rather than overfitting to individual datasets. MemEvolve also demonstrates strong cross-LLM generalization. Although meta-evolution is conducted using GPT-5-Mini, memory systems evolved on TaskCraft+ transfer effectively to Kimi K2 and DeepSeek V3.2 without manual adaptation. Notably, Kimi K2+ improves by 17.06% on WebWalkerQA and 10.0% on TaskCraft. Finally, MemEvolve exhibits compelling crossframework generalization. As shown in Figure 4, directly transferring the memory system evolved on TaskCraft+ to heterogeneous agentic frameworks, including and , consistently improves performance despite substantial architectural differences. These results demonstrate that MemEvolve learns framework-agnostic memory abstractions that are readily pluggable across diverse agentic systems.

![image 113](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile113.png>)

![image 114](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile114.png>)

![image 115](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile115.png>)

![image 116](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile116.png>)

![image 117](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile117.png>)

![image 118](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile118.png>)

![image 119](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile119.png>)

![image 120](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile120.png>)

![image 121](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile121.png>)

![image 122](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile122.png>)

- Figure 5 Evolution of cumulative accuracy across question indices. Cumulative accuracy at index i is defined as the average accuracy over the first i questions. The curves exhibit larger fluctuations at early indices due to limited sample size, and gradually stabilize as more questions are accumulated.

: AKB Mem

Encode: freeze Store: freeze Retrieve: reasonretrieve-refine Manage: N/A

![image 123](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile123.png>)

![image 124](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile124.png>)

![image 125](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile125.png>)

![image 126](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile126.png>)

: Adaptive Decision

Encode: 9 skills Store: JSON Retrieve: Hybrid Retrieval + LLM refinement Manage: N/A

![image 127](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile127.png>)

![image 128](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile128.png>)

![image 129](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile129.png>)

![image 130](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile130.png>)

: Meta Mem

Encode: tasks/ strategy/ops/ checks Store: JSON Retrieve: Hybrid

![image 131](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile131.png>)

![image 132](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile132.png>)

![image 133](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile133.png>)

Retrieval+Meta Guardrail Manage: N/A

![image 134](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile134.png>)

![image 135](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile135.png>)

. .

![image 136](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile136.png>)

![image 137](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile137.png>)

Meta evolve

Meta evolve

Memory System Meta-Evolution Path (on TaskCraft)

: Domain Mem

Encode: failure

modes/guidance Store: Item list Retrieve: Context-

![image 138](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile138.png>)

![image 139](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile139.png>)

![image 140](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile140.png>)

aware scorer + LLM guider Manage: LLMranker

![image 141](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile141.png>)

: Riva

Encode: by domain, semantic

![image 142](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile142.png>)

![image 143](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile143.png>)

Store: Database Retrieve: Guide+ Probe+Gating Manage: N/A

![image 144](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile144.png>)

![image 145](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile145.png>)

Meta . . evolve

![image 146](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile146.png>)

![image 147](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile147.png>)

Meta evolve

![image 148](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile148.png>)

: Cerebra Mem

Encode: graph Store: Success traj->semantic Retrieve: text/tool bi-routing Manage: node/edge pruning/consolidate

![image 149](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile149.png>)

![image 150](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile150.png>)

![image 151](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile151.png>)

![image 152](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile152.png>)

: Omni-Mem

Encode: traj, tag summary

![image 153](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile153.png>)

![image 154](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile154.png>)

Store: JSON Retrieve: refine+ reason+synthesize Manage: N/A

![image 155](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile155.png>)

![image 156](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile156.png>)

. .

![image 157](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile157.png>)

Meta evolve

Meta evolve

![image 158](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile158.png>)

![image 159](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile159.png>)

- Figure 6 Illustration of the progressive evolution from the fixed AgentKB architecture to increasingly agentic and efficient memory architectures. Each stage reflects structural and functional modifications in memory encoding, storing, retrieval, and maintenance, culminating in high-performing systems such as Riva and Cerebra.


##### 5.3 Self-Evolving Memory Comparison

We further compare the memory systems automatically evolved by MemEvolve against prevailing human-designed self-improving memory systems. In Table 3, we integrate seven representative self-improving memory systems implemented in EvolveLab with Flash-Searcher, and comprehensively report performance, per-task cost/execution latency/execution steps. Results for MemEvolve are obtained using the system evolved on TaskCraft+ +GPT-5-Mini.

![image 160](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile160.png>)

Existing Memory Systems Fail to Deliver Consistent Gains. Despite faithful re-implementations aligned with the original designs, many existing memory systems do not yield stable improvements. For example, DILU improves performance on xBench and WebWalkerQA, yet degrades GAIA by 2.42%. Dynamic Cheatsheet achieves a 1.76% gain on WebWalkerQA via skill condensation, but performs poorly on GAIA and xBench. More extreme cases are also observed: ExpeL underperforms on all three benchmarks. Upon closer inspection, this is unsurprising, as ExpeL was originally designed for relatively simple embodied or QA settings (e.g., ALFWorld, HotpotQA), and its prompts and mechanisms are ill-suited for long-horizon, long-context deep research. These results underscore the necessity of task-aware memory design.

###### Task Query (from GAIA)

Task Query (from xBench)

Find the Wikipedia page for the 2019 game that won the British Academy Games Awards. How many revisions did that page have before the month listed as the game's release date on that Wikipedia page (as of the most recent entry from 2022)?

有⼀个景点，是⼀个⽼太太花了很多年的⼼⾎，⽤⼀⽚⽚瓷⽚建 成的。这个景点的⻔票上，印着⼀⾏字，请问这⾏字是什么？

###### Agent Execution Trajectory

###### Agent Execution Trajectory

Task Status

- Step 1: Planning

![image 161](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile161.png>)

- Step 2: Locating Viewpoint

![image 162](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile162.png>)

- Step 3: Finding Text


...

Step 3: Locate article

![image 163](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile163.png>)

Step 1: Planning

Step 2: Locate Wiki page

![image 164](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile164.png>)

![image 165](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile165.png>)

The attraction has been identiﬁed as 瓷 宫. The objective of this subtask is to

determine the speciﬁc line of text printed on its admission ticket.

Provided Memory

Provided Memory (by Lightweight)

Provided Memory (by Lightweight)

###### Possibile Source

A retrieved memory states: “Past tasks found image captions and tourism listings often include ticket text when articles omit it.” This suggests that when textual descriptions fail to mention ticket inscriptions, such information is frequently available in image captions or online travel booking listings.

Anti-ambiguity Consider ﬁrst locating the canonical Wikipedia article with targeted site:wikipedia.org queries (use the game title plus keywords like \"BAFTA\" or \"British Academy Games Awards\") to avoid ambiguity.

###### Tool-use Suggestion

Use the MediaWiki API revisions with rvend cutoff to list and count revisions up to the release-month cutoff.

Context Reminder Located the canonical Wikipedia article: 'Outer Wilds' at https://en.wikipedia.org/wiki/Outer\_Wilds, conﬁrmed matching the 2019 BAFTA winner.

Tool-use Suggestion Based on similar tasks, use the MediaWiki API/history endpoints to list revisions and apply a cutoff (rvend or equivalent) at the release-month datetime so you can count all revisions up to that month.

![image 166](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile166.png>)

Context Reminer Article body lists month-year dates: May 2019 (Windows, Xbox One); October 2019 (PS4); September 2022 (PS5/Xbox); December 2023 (Switch).

Planning Advice

Decompose the work into locate → extract revisions → count up-to-cutoff → corroborate with an archived snapshot (Wayback/Wikidata) and save exact URLs/oldids so the result is auditable.

Guided by this memory, the agent systematically queried tourism platforms such as Trip.com and Qunar, focusing on structured ﬁelds in attraction listings and ticket sales pages.

![image 167](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile167.png>)

- Figure 7 Illustration of how evolved memories are instantiated during real-world tasks from GAIA and xBench. The memory system adaptively provides stage-specific guidance, ranging from high-level planning and task decomposition to fine-grained tool-use suggestions and salient context recall, thereby steering the agent toward efficient and successful task completion.


MemEvolve Delivers Robust and Consistent Improvements. In contrast to prior approaches, MemEvolve yields stable and robust performance gains. Although the underlying memory system is evolved on TaskCraft, it consistently achieves improvements of 3.54% ∼ 5.0% across all three evaluated benchmarks. Importantly, these gains are not achieved by substantially increasing the per-task cost. As shown in Table 3, MemEvolve maintains API costs comparable to the No-Memory baseline across all benchmarks (e.g., GAIA: $0.085 vs. $0.086; xBench: $0.136 vs. $0.141), while its execution delay remains on a similar scale to other self-improving baselines (e.g., GAIA: 693.33s vs. 584.88s for AWM and 559.81s for Cheatsheet; xBench: 773.06s vs. 761.33s for AWM and 818.07s for Cheatsheet). Figure 5 further illustrates the cumulative success rate of different self-evolving memory systems as task execution progresses. Although performance exhibits higher variance in the early stages due to limited sample size, MemEvolve gradually stabilizes and converges to a consistently superior performance regime. This indicates that MemEvolve discovers principled and effective memory designs rather than relying on brittle, task-specific heuristics.

At first glance, such generalization may appear to conflict with our original motivation that memory systems cannot generalize across all domains and therefore require task-specific evolution. We argue this is not the case. Memory systems evolved on TaskCraft are unlikely to transfer effectively to fundamentally different task families (e.g., embodied action), where environments, action space and tool sets differ substantially. Nevertheless, MemEvolve enables the discovery of broadly applicable memory architectures within a shared task regime, while retaining the capacity for further task-specific adaptation when required.

##### 5.4 Meta-Evolving Dynamics

Having established the substantial performance gains delivered by MemEvolve, we further examine how metaevolution is executed in practice and which components are modified or enhanced during the evolutionary process. As illustrated in Figure 6, MemEvolve starts from the predefined structure of AgentKB and iteratively evolves toward increasingly efficient memory architectures. Figures 9 and 10 highlights two high-performing memory systems discovered along this trajectory, denoted as Riva and Cerebra. Figure 8 presents a system evolved from the simplest few-shot example memory baseline, referred to as Lightweight.

Agents Spontaneously Evolve Efficient Memory Architectures. As illustrated in Figure 6, the initial AgentKB memory system adopts a frozen design for both encoding and storage, lacking the capability to assimilate new experiences.

Starting from this baseline, MemEvolve explores a spectrum of evolutionary directions. Some candidates are relatively aggressive (e.g., Ω(11), an Adaptive Decision System that decomposes a single agent trajectory into nine skill granularities), while others are more conservative (e.g., Ω(31), an Meta Memory System that stores trajectories at four levels and introduces an LLM-based meta-guardrail during retrieval to filter irrelevant information). The latter emerges as the winner in the first evolutionary round. The defining characteristic of this stage is agentic: both memory encoding and decoding increasingly rely on agent-driven decisions rather than predefined pipelines. The third evolution round introduces two further advances. Evolving from Ω(32) Riva to Ω(13) Cerebra, the memory system learns to distill not only textual insights but also reusable tools from past experience, while incorporating periodic maintenance of the memory database. Together, these enhancements provide faster evolutionary momentum for underlying agentic frameworks.

Evolved Memory Systems Are Effective in Practice. We further present concrete memory examples produced by the Lightweight system during real executions, as shown in Figure 7. The results illustrate that Lightweight delivers memory content at varying levels of granularity, adaptively tailored to different task stages. During early planning, the memory provides high-level guidance, such as task decomposition strategies. As execution proceeds, it offers more fine-grained recommendations for tool-use, along with a form of working memory that highlights salient information from previous turns. Notably, Lightweight also exhibits predictive behavior by anticipating that target information may appear within image content on online travel websites, successfully guiding the agent to locate the evidence on trip.com. Together, these examples demonstrate the practical effectiveness of memory systems evolved by MemEvolve.

#### 6 Conclusion

This work provides a unified implementation and design space for the rapidly growing field of self-evolving agent memory, together with a standardized codebase, termed EvolveLab, upon which we further build MemEvolve, a meta-evolutionary memory framework. Departing from the conventional paradigm of manually crafting a single self-improving memory architecture and expecting it to generalize across all domains, MemEvolve instead embraces adaptive, architecture-level evolution driven by empirical interaction feedback. Extensive experiments across diverse agentic benchmarks and backbone models demonstrate the effectiveness, robustness, and generalization of this approach. Moreover, analysis of the automatically evolved memory systems reveals several instructive design principles, including increased agentic involvement, hierarchical organization, and multi-level abstraction. We hope that MemEvolve serves as a step toward more automated, principled, and meta-evolutionary pathways for building continually improving agentic intelligence.

#### 7 Contributions

Core Contributors

- • Guibin Zhang
- • Haotian Ren


Contributors

- • Chong Zhan
- • Zhenhong Zhou
- • Junhao Wang
- • He Zhu


Corresponding Authors

- • Wangchunshu Zhou
- • Shuicheng Yan


If you have any questions regarding the code, paper details, or other aspects of this work, you are very welcome to contact the authors at guibinz@outlook.com or via raising a Github issue.

#### References

Bai, L., Cai, Z., Cao, Y., Cao, M., Cao, W., Chen, C., Chen, H., Chen, K., Chen, P., Chen, Y., Chen, Y., Cheng, Y., Chu, P., Chu, T., Cui, E., Cui, G., Cui, L., Cui, Z., Deng, N., Ding, N., Dong, N., Dong, P., Dou, S., Du, S., Duan, H., Fan, C., Gao, B., Gao, C., Gao, J., Gao, S., Gao, Y., Gao, Z., Ge, J., Ge, Q., Gu, L., Gu, Y., Guo, A., Guo, Q., Guo, X., He, C., He, J., Hong, Y., Hou, S., Hu, C., Hu, H., Hu, J., Hu, M., Hua, Z., Huang, H., Huang, J., Huang, X., Huang, Z., Jiang, Z., Kong, L., Li, L., Li, P., Li, P., Li, S., Li, T., Li, W., Li, Y., Lin, D., Lin, J., Lin, T., Lin, Z., Liu, H., Liu, J., Liu, J., Liu, J., Liu, K., Liu, K., Liu, K., Liu, S., Liu, S., Liu, W., Liu, X., Liu, Y., Liu, Z., Lu, Y., Lv, H., Lv, H., Lv, H., Lv, Q., Lv, Y., Lyu, C., Ma, C., Ma, J., Ma, R., Ma, R., Ma, R., Ma, X., Ma, Y., Ma, Z., Mi, S., Ning, J., Ning, W., Pang, X., Peng, J., Peng, R., Qiao, Y., Qiu, J., Qu, X., Qu, Y., Ren, Y., Shang, F., Shao, W., Shen, J., Shen, S., Song, C., Song, D., Song, D., Su, C., Su, W., Sun, W., Sun, Y., Tan, Q., Tang, C., Tang, H., Tang, K., Tang, S., Tong, J., Wang, A., Wang, B., Wang, D., Wang, L., Wang, R., Wang, W., Wang, W., Wang, J., Wang, Y., Wang, Z., Wu, L.-I., Wu, W., Wu, Y., Wu, Z., Xiao, L., Xing, S., Xu, C., Xu, H., Xu, J., Xu, R., Xu, W., Yang, G., Yang, Y., Ye, H., Ye, J., Ye, S., Yu, J., Yu, J., Yu, J., Yuan, F., Zang, Y., Zhang, B., Zhang, C., Zhang, C., Zhang, H., Zhang, J., Zhang, Q., Zhang, Q., Zhang, S., Zhang, T., Zhang, W., Zhang, W., Zhang, Y., Zhang, Z., Zhao, H., Zhao, Q., Zhao, X., Zhao, X., Zhou, B., Zhou, D., Zhou, P., Zhou, Y., Zhou, Y., Zhu, D., Zhu, L., and Zou, Y. (2025). Intern-s1: A scientific multimodal foundation model.

Cai, Y., Cai, S., Shi, Y., Xu, Z., Chen, L., Qin, Y., Tan, X., Li, G., Li, Z., Lin, H., Mao, Y., Li, K., and Sun, X. (2025). Training-free group relative policy optimization.

Chen, K., Ren, Y., Liu, Y., Hu, X., Tian, H., Xie, T., Liu, F., Zhang, H., Liu, H., Gong, Y., Sun, C., Hou, H., Yang, H., Pan, J., Lou, J., Mao, J., Liu, J., Li, J., Liu, K., Liu, K., Wang, R., Li, R., Niu, T., Zhang, W., Yan, W., Wang, X., Zhang, Y., Hung, Y.-H., Jiang, Y., Liu, Z., Yin, Z., Ma, Z., and Mo, Z. (2025). xbench: Tracking agents productivity scaling with profession-aligned real-world evaluations.

DeepSeek-AI, Liu, A., Mei, A., Lin, B., Xue, B., Wang, B., Xu, B., Wu, B., Zhang, B., Lin, C., Dong, C., Lu, C., Zhao, C., Deng, C., Xu, C., Ruan, C., Dai, D., Guo, D., Yang, D., Chen, D., Li, E., Zhou, F., Lin, F., Dai, F., Hao, G., Chen, G., Li, G., Zhang, H., Xu, H., Li, H., Liang, H., Wei, H., Zhang, H., Luo, H., Ji, H., Ding, H., Tang, H., Cao, H., Gao, H., Qu, H., Zeng, H., Huang, J., Li, J., Xu, J., Hu, J., Chen, J., Xiang, J., Yuan, J., Cheng, J., Zhu, J., Ran, J., Jiang, J., Qiu, J., Li, J., Song, J., Dong, K., Gao, K., Guan, K., Huang, K., Zhou, K., Huang, K., Yu, K., Wang, L., Zhang, L., Wang, L., Zhao, L., Yin, L., Guo, L., Luo, L., Ma, L., Wang, L., Zhang, L., Di, M. S., Xu, M. Y., Zhang, M., Zhang, M., Tang, M., Zhou, M., Huang, P., Cong, P., Wang, P., Wang, Q., Zhu, Q., Li, Q., Chen, Q., Du, Q., Xu, R., Ge, R., Zhang, R., Pan, R., Wang, R., Yin, R., Xu, R., Shen, R., Zhang, R., Liu, S. H., Lu, S., Zhou, S., Chen, S., Cai, S., Chen, S., Hu, S., Liu, S., Hu, S., Ma, S., Wang, S., Yu, S., Zhou, S., Pan, S., Zhou, S., Ni, T., Yun, T., Pei, T., Ye, T., Yue, T., Zeng, W., Liu, W., Liang, W., Pang, W., Luo, W., Gao, W., Zhang, W., Gao, X., Wang, X., Bi, X., Liu, X., Wang, X., Chen, X., Zhang, X., Nie, X., Cheng, X., Liu, X., Xie, X., Liu, X., Yu, X., Li, X., Yang, X., Li, X., Chen, X., Su, X., Pan, X., Lin, X., Fu, X., Wang, Y. Q., Zhang, Y., Xu, Y., Ma, Y., Li, Y., Li, Y., Zhao, Y., Sun, Y., Wang, Y., Qian, Y., Yu, Y., Zhang, Y., Ding, Y., Shi, Y., Xiong, Y., He, Y., Zhou, Y., Zhong, Y., Piao, Y., Wang, Y., Chen, Y., Tan, Y., Wei, Y., Ma, Y., Liu, Y., Yang, Y., Guo, Y., Wu, Y., Wu, Y., Cheng, Y., Ou, Y., Xu, Y., Wang, Y., Gong, Y., Wu, Y., Zou, Y., Li, Y., Xiong, Y., Luo, Y., You, Y., Liu, Y., Zhou, Y., Wu, Z. F., Ren, Z. Z., Zhao, Z., Ren, Z., Sha, Z., Fu, Z., Xu, Z., Xie, Z., Zhang, Z., Hao, Z., Gou, Z., Ma, Z., Yan, Z., Shao, Z., Huang, Z., Wu, Z., Li, Z., Zhang, Z., Xu, Z., Wang, Z., Gu, Z., Zhu, Z., Li, Z., Zhang, Z., Xie, Z., Gao, Z., Pan, Z., Yao, Z., Feng, B., Li, H., Cai, J. L., Ni, J., Xu, L., Li, M., Tian, N., Chen, R. J., Jin, R. L., Li, S. S., Zhou, S., Sun, T., Li, X. Q., Jin, X., Shen, X., Chen, X., Song, X., Zhou, X., Zhu, Y. X., Huang, Y., Li, Y., Zheng, Y., Zhu, Y., Ma, Y., Huang, Z., Xu, Z., Zhang, Z., Ji, D., Liang, J., Guo, J., Chen, J., Xia, L., Wang, M., Li, M., Zhang, P., Chen, R., Sun, S., Wu, S., Ye, S., Wang, T., Xiao, W. L., An, W., Wang, X., Sun, X., Wang, X., Tang, Y., Zha, Y., Zhang, Z., Ju, Z., Zhang, Z., and Qu, Z. (2025). Deepseek-v3.2: Pushing the frontier of open large language models.

Du, M., Xu, B., Zhu, C., Wang, X., and Mao, Z. (2025). Deepresearch bench: A comprehensive benchmark for deep research agents. Fang, J., Peng, Y., Zhang, X., Wang, Y., Yi, X., Zhang, G., Xu, Y., Wu, B., Liu, S., Li, Z., Ren, Z., Aletras, N., Wang, X., Zhou, H., and

Meng, Z. (2025a). A comprehensive survey of self-evolving ai agents: A new paradigm bridging foundation models and lifelong agentic systems.

Fang, R., Liang, Y., Wang, X., Wu, J., Qiao, S., Xie, P., Huang, F., Chen, H., and Zhang, N. (2025b). Memp: Exploring agent procedural memory.

Fang, T., Zhang, Z., Wang, X., Wang, R., Qin, C., Wan, Y., Ma, J.-Y., Zhang, C., Chen, J., Li, X., Zhang, H., Mi, H., and Yu, D. (2025c). Cognitive kernel-pro: A framework for deep research agents and agent foundation models training.

Ghareeb, A. E., Chang, B., Mitchener, L., Yiu, A., Szostkiewicz, C. J., Laurent, J. M., Razzak, M. T., White, A. D., Hinks, M. M., and Rodriques, S. G. (2025). Robin: A multi-agent system for automating scientific discovery.

Hong, S., Zhuge, M., Chen, J., Zheng, X., Cheng, Y., Wang, J., Zhang, C., Wang, Z., Yau, S. K. S., Lin, Z., Zhou, L., Ran, C., Xiao, L., Wu, C., and Schmidhuber, J. (2024). MetaGPT: Meta programming for a multi-agent collaborative framework. In The Twelfth International Conference on Learning Representations.

Hu, M., Zhou, Y., Fan, W., Nie, Y., Xia, B., Sun, T., Ye, Z., Jin, Z., Li, Y., Chen, Q., Zhang, Z., Wang, Y., Ye, Q., Ghanem, B., Luo, P., and Li, G. (2025a). Owl: Optimized workforce learning for general multi-agent assistance in real-world task automation.

Hu, M., Zhou, Y., Fan, W., Nie, Y., Xia, B., Sun, T., Ye, Z., Jin, Z., Li, Y., Zhang, Z., Wang, Y., Ye, Q., Luo, P., and Li, G. (2025b). Owl: Optimized workforce learning for general multi-agent assistance in real-world task automation.

Hu, Y., Liu, S., Yue, Y., Zhang, G., Liu, B., Zhu, F., Lin, J., Guo, H., Dou, S., Xi, Z., Jin, S., Tan, J., Yin, Y., Liu, J., Zhang, Z., Sun, Z., Zhu, Y., Sun, H., Peng, B., Cheng, Z., Fan, X., Guo, J., Yu, X., Zhou, Z., Hu, Z., Huo, J., Wang, J., Niu, Y., Wang, Y., Yin, Z., Hu, X., Liao, Y., Li, Q., Wang, K., Zhou, W., Liu, Y., Cheng, D., Zhang, Q., Gui, T., Pan, S., Zhang, Y., Torr, P., Dou, Z., Wen, J.-R., Huang, X., Jiang, Y.-G., and Yan, S. (2025c). Memory in the age of ai agents.

LangChain (2023). Langchain: Build context-aware reasoning applications. [Online]. https://github.com/langchain-ai/

###### langchain.

Mialon, G., Fourrier, C., Wolf, T., LeCun, Y., and Scialom, T. (2023). Gaia: a benchmark for general ai assistants. In The Twelfth

International Conference on Learning Representations. OpenAI (2025). Introducing GPT-5 — openai.com. https://openai.com/index/introducing-gpt-5/. [Accessed 16-12-2025]. Orhan, A. E. (2023). Recognition, recall, and retention of few-shot memories in large language models. Ouyang, S., Yan, J., Hsu, I.-H., Chen, Y., Jiang, K., Wang, Z., Han, R., Le, L. T., Daruki, S., Tang, X., Tirumalashetty, V., Lee, G.,

Rofouei, M., Lin, H., Han, J., Lee, C.-Y., and Pfister, T. (2025). Reasoningbank: Scaling agent self-evolving with reasoning memory. Packer, C., Fang, V., Patil, S., Lin, K., Wooders, S., and Gonzalez, J. (2023). Memgpt: Towards llms as operating systems. Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C. B. C., Shaaban, M., Ling, J., Shi, S., et al. (2025). Humanity’s last exam.

arXiv preprint arXiv:2501.14249. Qin, T., Chen, Q., Wang, S., Xing, H., Zhu, K., Zhu, H., Shi, D., Liu, X., Zhang, G., Liu, J., Jiang, Y. E., Gao, X., and Zhou, W. (2025). Flash-searcher: Fast and effective web agents via dag-based parallel execution. Qiu, J., Juan, X., Wang, Y., Yang, L., Qi, X., Zhang, T., Guo, J., Lu, Y., Yao, Z., Wang, H., Liu, S., Jiang, X., Leqi, L., and Wang, M. (2025a). Agentdistill: Training-free agent distillation with generalizable mcp boxes. Qiu, J., Qi, X., Zhang, T., Juan, X., Guo, J., Lu, Y., Wang, Y., Yao, Z., Ren, Q., Jiang, X., et al. (2025b). Alita: Generalist agent enabling scalable agentic reasoning with minimal predefinition and maximal self-evolution. arXiv preprint arXiv:2505.20286. Rasmussen, P., Paliychuk, P., Beauvais, T., Ryan, J., and Chalef, D. (2025). Zep: A temporal knowledge graph architecture for agent memory. Roucher, A., del Moral, A. V., Wolf, T., von Werra, L., and Kaunismäki, E. (2025). ‘smolagents‘: a smol library to build great agentic systems. https://github.com/huggingface/smolagents. Shi, D., Cao, J., Chen, Q., Sun, W., Li, W., Lu, H., Dong, F., Qin, T., Zhu, K., Yang, M., Yang, J., Zhang, G., Liu, J., Zhang, C., Wang, J., Jiang, Y. E., and Zhou, W. (2025a). Taskcraft: Automated generation of agentic tasks. Shi, Y., Wang, M., Cao, Y., Lai, H., Lan, J., Han, X., Wang, Y., Geng, J., Li, Z., Xia, Z., et al. (2025b). Aime: Towards fully-autonomous multi-agent framework. arXiv preprint arXiv:2507.11988. Shinn, N., Labash, B., and Gopinath, A. (2023). Reflexion: an autonomous agent with dynamic memory and self-reflection. arXiv

preprint, abs/2303.11366. Significant-Gravitas (2023). Autogpt. [Online]. https://github.com/Significant-Gravitas/AutoGPT. Sun, H. and Zeng, S. (2025). Hierarchical memory for high-efficiency long-term reasoning in llm agents. Suzgun, M., Yuksekgonul, M., Bianchi, F., Jurafsky, D., and Zou, J. (2025). Dynamic cheatsheet: Test-time learning with adaptive

memory. Tang, X., Hu, T., Ye, M., Shao, Y., Yin, X., Ouyang, S., Zhou, W., Lu, P., Zhang, Z., Zhao, Y., Cohan, A., and Gerstein, M. (2025). Chemagent: Self-updating library in large language models improves chemical reasoning.

Team, K., Bai, Y., Bao, Y., Chen, G., Chen, J., Chen, N., Chen, R., Chen, Y., Chen, Y., Chen, Y., Chen, Z., Cui, J., Ding, H., Dong, M., Du, A., Du, C., Du, D., Du, Y., Fan, Y., Feng, Y., Fu, K., Gao, B., Gao, H., Gao, P., Gao, T., Gu, X., Guan, L., Guo, H., Guo, J., Hu, H., Hao, X., He, T., He, W., He, W., Hong, C., Hu, Y., Hu, Z., Huang, W., Huang, Z., Huang, Z., Jiang, T., Jiang, Z., Jin, X., Kang, Y., Lai, G., Li, C., Li, F., Li, H., Li, M., Li, W., Li, Y., Li, Y., Li, Z., Li, Z., Lin, H., Lin, X., Lin, Z., Liu, C., Liu, C., Liu, H., Liu, J., Liu, J., Liu, L., Liu, S., Liu, T. Y., Liu, T., Liu, W., Liu, Y., Liu, Y., Liu, Y., Liu, Y., Liu, Z., Lu, E., Lu, L., Ma, S., Ma, X., Ma, Y., Mao, S., Mei, J., Men,

X., Miao, Y., Pan, S., Peng, Y., Qin, R., Qu, B., Shang, Z., Shi, L., Shi, S., Song, F., Su, J., Su, Z., Sun, X., Sung, F., Tang, H., Tao, J., Teng, Q., Wang, C., Wang, D., Wang, F., Wang, H., Wang, J., Wang, J., Wang, J., Wang, S., Wang, S., Wang, Y., Wang, Y., Wang, Y.,

- Wang, Y., Wang, Y., Wang, Z., Wang, Z., Wang, Z., Wei, C., Wei, Q., Wu, W., Wu, X., Wu, Y., Xiao, C., Xie, X., Xiong, W., Xu, B., Xu, J., Xu, J., Xu, L. H., Xu, L., Xu, S., Xu, W., Xu, X., Xu, Y., Xu, Z., Yan, J., Yan, Y., Yang, X., Yang, Y., Yang, Z., Yang, Z., Yang, Z., Yao, H., Yao, X., Ye, W., Ye, Z., Yin, B., Yu, L., Yuan, E., Yuan, H., Yuan, M., Zhan, H., Zhang, D., Zhang, H., Zhang, W., Zhang, X.,

- Zhang, Y., Zhang, Y., Zhang, Y., Zhang, Y., Zhang, Y., Zhang, Y., Zhang, Z., Zhao, H., Zhao, Y., Zheng, H., Zheng, S., Zhou, J., Zhou, X., Zhou, Z., Zhu, Z., Zhuang, W., and Zu, X. (2025a). Kimi k2: Open agentic intelligence.


Team, M. L., Bayan, Li, B., Lei, B., Wang, B., Rong, B., Wang, C., Zhang, C., Gao, C., Zhang, C., Sun, C., Han, C., Xi, C., Zhang, C., Peng, C., Qin, C., Zhang, C., Chen, C., Wang, C., Ma, D., Pan, D., Bu, D., Zhao, D., Kong, D., Liu, D., Huo, F., Li, F., Zhang, F., Dong, G., Liu, G., Xu, G., Li, G., Tan, G., Lin, G., Jing, H., Fu, H., Yan, H., Wen, H., Zhao, H., Liu, H., Shi, H., Hao, H., Tang, H., Lv, H., Su, H., Li, J., Liu, J., Li, J., Yang, J., Wang, J., Yang, J., Tan, J., Sun, J., Zhang, J., Fu, J., Yang, J., Hu, J., Qin, J., Wang, J., He, J., Kuang, J., Mei, J., Liang, K., He, K., Zhang, K., Wang, K., He, K., Gao, L., Shi, L., Ma, L., Qiu, L., Kong, L., Si, L., Lyu, L., Guo, L., Yang, L., Yan, L., Xia, M., Gao, M., Zhang, M., Zhou, M., Shen, M., Tuo, M., Zhu, M., Li, P., Pei, P., Zhao, P., Jia, P., Sun, P., Gu, Q., Li, Q., Li, Q., Huang, Q., Duan, Q., Meng, R., Weng, R., Shao, R., Li, R., Wu, S., Liang, S., Wang, S., Dang, S., Fang, T., Li, T., Chen, T., Bai, T., Zhou, T., Xie, T., He, W., Huang, W., Liu, W., Shi, W., Wang, W., Wu, W., Zhao, W., Zan, W., Shi, W., Nan, X., Su, X., Li,

- X., Mei, X., Ji, X., Xi, X., Huang, X., Li, X., Fu, X., Liu, X., Wei, X., Cai, X., Chen, X., Liu, X., Li, X., Shi, X., Li, X., Wang, X., Chen,

- X., Hu, X., Miao, X., He, X., Zhang, X., Hao, X., Cao, X., Cai, X., Yang, X., Feng, Y., Bai, Y., Chen, Y., Yang, Y., Huo, Y., Sun, Y., Lu,
- Y., Zhang, Y., Zang, Y., Zhai, Y., Li, Y., Yin, Y., Lv, Y., Zhou, Y., Yang, Y., Xie, Y., Sun, Y., Zheng, Y., Wei, Y., Qian, Y., Liang, Y., Tai,


- Y., Zhao, Y., Yu, Z., Zhang, Z., Yang, Z., Zhang, Z., Xia, Z., Zou, Z., Zeng, Z., Su, Z., Chen, Z., Zhang, Z., Wang, Z., Jiang, Z., Zhao,
- Z., Wang, Z., and Su, Z. (2025b). Longcat-flash technical report.


Tran, K.-T., Dao, D., Nguyen, M.-D., Pham, Q.-V., O’Sullivan, B., and Nguyen, H. D. (2025). Multi-agent collaboration mechanisms: A survey of llms.

Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv e-prints, page arXiv:2305.16291.

- Wang, W., Piękos, P., Nanbo, L., Laakom, F., Chen, Y., Ostaszewski, M., Zhuge, M., and Schmidhuber, J. (2025a). Huxley-gödel machine: Human-level coding agent development by an approximation of the optimal self-improving machine.
- Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., Lin, J., Brennan, R., Peng, H., Ji, H., and Neubig, G. (2024a). OpenHands: An Open Platform for AI Software Developers as Generalist Agents.
- Wang, Y., Yang, L., Li, G., Wang, M., and Aragam, B. (2025b). Scoreflow: Mastering llm agent workflows via score-based preference optimization.
- Wang, Z., Xu, H., Wang, J., Zhang, X., Yan, M., Zhang, J., Huang, F., and Ji, H. (2025c). Mobile-agent-e: Self-evolving mobile assistant for complex tasks.


- Wang, Z. Z., Mao, J., Fried, D., and Neubig, G. (2024b). Agent workflow memory.


Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., and Glaese, A. (2025a). Browsecomp: A simple yet challenging benchmark for browsing agents. arXiv preprint arXiv:2504.12516.

Wei, J., Yang, Y., Zhang, X., Chen, Y., Zhuang, X., Gao, Z., Zhou, D., Wang, G., Gao, Z., Cao, J., Qiu, Z., He, X., Zhang, Q., You, C., Zheng, S., Ding, N., Ouyang, W., Dong, N., Cheng, Y., Sun, S., Bai, L., and Zhou, B. (2025b). From ai for science to agentic science: A survey on autonomous scientific discovery.

Wen, L., Fu, D., Li, X., Cai, X., Ma, T., Cai, P., Dou, M., Shi, B., He, L., and Qiao, Y. (2024). Dilu: A knowledge-driven approach to autonomous driving with large language models.

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., and Huang, F. (2025a). Webwalker: Benchmarking llms in web traversal.

- Wu, Q., Bansal, G., Zhang, J., Wu, Y., Zhang, S., Zhu, E., Li, B., Jiang, L., Zhang, X., and Wang, C. (2023). Autogen: Enabling next-gen llm applications via multi-agent conversation framework.
- Wu, R., Wang, X., Mei, J., Cai, P., Fu, D., Yang, C., Wen, L., Yang, X., Shen, Y., Wang, Y., and Shi, B. (2025b). Evolver: Self-evolving llm agents through an experience-driven lifecycle.


Wu, Y., Liang, S., Zhang, C., Wang, Y., Zhang, Y., Guo, H., Tang, R., and Liu, Y. (2025c). From human memory to ai memory: A survey on memory mechanisms in the era of llms.

Yang, C., Yang, X., Wen, L., Fu, D., Mei, J., Wu, R., Cai, P., Shen, Y., Deng, N., Shi, B., Qiao, Y., and Li, H. (2025). Learning on the job: An experience-driven self-evolving agent for long-horizon tasks.

Ye, S., Yu, C., Ke, K., Xu, C., and Wei, Y. (2025). H2r: Hierarchical hindsight reflection for multi-task llm agents. arXiv preprint arXiv:2509.12810.

Yin, Z., Sun, Q., Chang, C., Guo, Q., Dai, J., Huang, X., and Qiu, X. (2023). Exchange-of-thought: Enhancing large language model capabilities through cross-model communication.

Zhang, G., Chen, K., Wan, G., Chang, H., Cheng, H., Wang, K., Hu, S., and Bai, L. (2025a). Evoflow: Evolving diverse agentic workflows on the fly. arXiv preprint arXiv:2502.07373.

Zhang, G., Fu, M., Wan, G., Yu, M., Wang, K., and Yan, S. (2025b). G-memory: Tracing hierarchical memory for multi-agent systems. Zhang, G., Niu, L., Fang, J., Wang, K., Bai, L., and Wang, X. (2025c). Multi-agent architecture search via agentic supernet. arXiv

preprint arXiv:2502.04180. Zhang, G., Wang, J., Chen, J., Zhou, W., Wang, K., and Yan, S. (2025d). Agentracer: Who is inducing failure in the llm agentic systems?

Zhang, J., Hu, S., Lu, C., Lange, R., and Clune, J. (2025e). Darwin godel machine: Open-ended evolution of self-improving agents. Zhang, J., Xiang, J., Yu, Z., Teng, F., Chen, X., Chen, J., Zhuge, M., Cheng, X., Hong, S., Wang, J., Zheng, B., Liu, B., Luo, Y., and Wu,

C. (2024a). AFlow: Automating Agentic Workflow Generation. arXiv:2410.10762. Zhang, W., Cui, C., Zhao, Y., Hu, R., Liu, Y., Zhou, Y., and An, B. (2025f). Agentorchestra: A hierarchical multi-agent framework for general-purpose task solving. Zhang, W., Li, X., Zhang, Y., Jia, P., Wang, Y., Guo, H., Liu, Y., and Zhao, X. (2025g). Deep research: A survey of autonomous research agents. Zhang, W., Zeng, L., Xiao, Y., Li, Y., Cui, C., Zhao, Y., Hu, R., Liu, Y., Zhou, Y., and An, B. (2025h). Agentorchestra: Orchestrating hierarchical multi-agent intelligence with the tool-environment-agent(tea) protocol.

- Zhang, Z., Bo, X., Ma, C., Li, R., Chen, X., Dai, Q., Zhu, J., Dong, Z., and Wen, J.-R. (2024b). A survey on the memory mechanism of large language model based agents. arXiv preprint arXiv:2404.13501.


Zhang, Z., Dai, Q., Chen, X., Li, R., Li, Z., and Dong, Z. (2025i). Memengine: A unified and modular library for developing advanced memory of llm-based agents.

Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J., and Huang, G. (2024). Expel: Llm agents are experiential learners. In Proceedings of

the AAAI Conference on Artificial Intelligence, volume 38, pages 19632–19642. Zhao, S., Zhang, H., Lin, S., Li, M., Wu, Q., Zhang, K., and Wei, C. (2025). Pyvision: Agentic vision with dynamic tooling. Zheng, B., Fatemi, M. Y., Jin, X., Wang, Z. Z., Gandhi, A., Song, Y., Gu, Y., Srinivasa, J., Liu, G., Neubig, G., and Su, Y. (2025).

Skillweaver: Web agents can self-improve by discovering and honing skills. Zheng, L., Wang, R., Wang, X., and An, B. (2023). Synapse: Trajectory-as-exemplar prompting with memory for computer control. arXiv preprint arXiv:2306.07863. Zhong, W., Guo, L., Gao, Q., Ye, H., and Wang, Y. (2024). Memorybank: Enhancing large language models with long-term memory. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 19724–19731.

## Appendix

#### A EvolveLab Implementation

EvolveLab is designed as a modular and extensible codebase to support the systematic study of self-evolving agent memory systems. It provides a unified interface that abstracts the complexities of diverse memory architectures, enabling standardized implementation, evaluation, and meta-evolution.

##### A.1 Unified Interface and Abstract Base Class

The cornerstone of EvolveLab is the BaseMemoryProvider abstract base class (ABC), which defines the fundamental protocol for all memory systems. As shown in the code snippet below, the interface enforces two primary operations that map to the modular design space (Encode, Store, Retrieve, Manage):

- • Retrieve (provide_memory): Handles context-aware memory recall. It accepts a MemoryRequest containing the current task query, execution context, and system status, and returns a MemoryResponse containing a list of relevant MemoryItems.
- • Encode & Store (take_in_memory): Orchestrates the ingestion of new experiences. This method processes a TrajectoryData object, which encapsulates the complete history of a task execution, extracts structural insights or tools (Encode), and persists them into the underlying storage medium (Store).


While take_in_memory primarily integrates the Encode and Store stages, the Manage functionality that is responsible for offline consolidation or selective forgetting is typically implemented as auxiliary methods within the provider classes or invoked during specific lifecycle events.

- 1 class BaseMemoryProvider(ABC):

- 2 """Abstract base class for memory providers"""

- 3

- 4 def __init__(self , memory_type: MemoryType , config: Optional[dict] = None):

- 5 self.memory_type = memory_type

- 6 self.config = config or {}

- 7

- 8 @abstractmethod

- 9 def provide_memory(self , request: MemoryRequest) −> MemoryResponse:

- 10 """

- 11 Retrieve relevant memories based on query , context and status

- 12 Args:

- 13 request: MemoryRequest containing query , context , status and optional params

- 14 Returns:

- 15 MemoryResponse containing relevant memories

- 16 """

- 17 pass

- 18

- 19 @abstractmethod

- 20 def take_in_memory(self , trajectory_data: TrajectoryData) −> tuple[bool , str]:

- 21 """

- 22 Store/ingest new memory from trajectory data

- 23 Args:

- 24 trajectory_data: TrajectoryData containing query , trajectory and metadata

- 25 Returns:

- 26 tuple[bool , str]: (Success status of memory ingestion , Description of absorbed memory)

- 27 """

- 28 pass

- 29

- 30 @abstractmethod

- 31 def initialize(self) −> bool:

- 32 """

- 33 Initialize the memory provider (load existing data , setup indices , etc.)

- 34 Returns:

- 35 bool: Success status of initialization

- 36 """

- 37 pass


- 38

- 39 def get_memory_type(self) −> MemoryType:

- 40 """Get the type of this memory provider"""

- 41 return self.memory_type

- 42

- 43 def get_config(self) −> dict:

- 44 """Get the configuration of this memory provider"""

- 45 return self.config.copy() Listing 1 The Abstract Base Class of Memory Providers


##### A.2 Standardized Data Carriers

To ensure seamless interoperability across heterogeneous memory designs and agent frameworks, EvolveLab utilizes standardized memory data carriers. These structures act as the "universal language" of the framework:

- • MemoryItem: The fundamental unit of information, capable of representing raw text, distilled insights, or executable code (APIs). Each item includes metadata such as creation timestamps, confidence scores, and source identifiers.
- • TrajectoryData: A comprehensive container for task execution history, including the initial query, full interaction traces (state-action pairs), and terminal rewards. It serves as the raw substrate for memory evolution.
- • MemoryRequest/Response: Standardized envelopes for retrieval queries and results, ensuring that any agent system can interact with any memory provider without architecture-specific modifications.


##### A.3 Implementation Examples: ExpeL and SkillWeaver

The versatility of the EvolveLab interface is demonstrated by our implementation of twelve distinct memory systems. Two representative examples are:

- • ExpeLProvider: Implements a contrastive learning-based memory. Its take_in_memory function identifies successful and failed trajectories to distill high-level "insights" into a textual format. These insights are stored in a vector database and retrieved via semantic similarity during provide_memory to guide the agent away from previous mistakes.
- • SkillWeaverProvider: Operates in a tool-centric design space. Its take_in_memory logic uses an LLM to synthesize reusable Python functions (skills) from successful trajectories. These skills are stored as executable code-level repositories and are dynamically retrieved and injected into the agent’s action space through the unified MemoryItem interface.


- B Experiment Details B.1 Dataset Details The four datasets used in this study are described and summarized as follows:


- • GAIA (Mialon et al., 2023) consists of 165 tasks, including 53 Level-1, 86 Level-2, and 26 Level-3 problems. For evaluating MemEvolve on GAIA+ and GAIA+ , the memory systems are evolved using GAIA Level-1 tasks together with 67 TaskCraft queries. Meta-evolution is conducted for three rounds, with 40 trajectories per round.

![image 168](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile168.png>)

![image 169](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile169.png>)

- • WebWalkerQA (Wu et al., 2025a) evaluates an agent’s ability to handle complex, multi-turn web interactions, comprising 680 real-world queries across four domains and over 1,373 webpages. We sample a subset of 170 queries for evaluation, with the sampling script released in our codebase. All memory systems used for WebWalkerQA are meta-evolved on TaskCraft.
- • xBench-DeepSearch (xBench-DS) (Chen et al., 2025) contains 100 tasks that assess agentic planning, tool use, and reasoning. Similar to WebWalkerQA, the memory systems used for xBench-DS evaluation are entirely meta-evolved on TaskCraft.


- • TaskCraft (Shi et al., 2025a) is a synthetic benchmark generated via an autonomous data pipeline. We collect 300 queries as a working subset and use 120 of them for three rounds of meta-evolution, with 40 queries per round. Meta-evolution for and is performed independently.


![image 170](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile170.png>)

![image 171](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile171.png>)

#### C Memory System Demonstration

To provide a concrete and intuitive understanding of the memory architectures evolved by MemEvolve, we visualize three representative systems discovered along different evolutionary trajectories, as shown in Figures 8 to 10. These examples highlight how MemEvolve progressively transforms simple, static memory mechanisms into more expressive and adaptive architectures by modifying memory encoding, retrieval, and management strategies. Together, they illustrate the diversity of memory designs that can emerge under the same meta-evolutionary framework.

![image 172](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile172.png>)

- Figure 8 Illustration of the Lightweight memory system evolved by MemEvolve. The evolutionary starting point is a minimal few-shot trajectory memory, similar to MemoryBank, where each completed trajectory is stored verbatim. For a new task, the agent retrieves the top-k most similar trajectories via vector similarity and directly conditions on them. MemEvolve progressively refines this baseline into a more structured and stage-aware memory system.


![image 173](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile173.png>)

###### Figure 9 Illustration of the Riva memory system evolved by MemEvolve. Its evolutionary initialization follows an AgentKB-style architecture, but without inheriting the large and costly offline knowledge base. Through meta-evolution, Riva develops more agent-centric encoding and retrieval strategies while remaining lightweight and fully online.

![image 174](<2025-zhang-memevolve-meta-evolution-agent-memory_images/imageFile174.png>)

###### Figure 10 Illustration of the Cerebra memory system evolved by MemEvolve. Starting from the same AgentKB-style initialization (without the offline knowledge base), Cerebra further evolves to distill both reusable tools and abstract knowledge from experience, and incorporates working memory maintenance mechanisms to support long-horizon agent evolution.

