---
type: source
kind: paper
title: "DeepEye: A Steerable Self-driving Data Agent System"
authors: Boyan Li, Yiran Peng, Yupeng Xie, Sirong Lu, Yizhang Zhu, Xing Mu, Xinyu Liu, Yuyu Luo
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.28889
source_local: ../raw/2026-li-deepeye-steerable-self-driving-data.pdf
topic: general-knowledge
cites:
---

# arXiv:2603.28889v1[cs.DB]30Mar2026

## DeepEye: A Steerable Self-driving Data Agent System

Boyan Li

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China bli303@connect.hkust-gz.edu.cn

Yiran Peng

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China yiranpeng@hkust-gz.edu.cn

Yupeng Xie

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China yxie740@connect.hkust-gz.edu.cn

Sirong Lu

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China slu075@connect.hkust-gz.edu.cn

Yizhang Zhu

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China yzhu305@connect.hkust-gz.edu.cn

Xing Mu

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China xmu159@connect.hkust-gz.edu.cn

Xinyu Liu

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China xliu371@connect.hkust-gz.edu.cn

Yuyu Luo

The Hong Kong University of Science and Technology (Guangzhou) Guangzhou, China yuyuluo@hkust-gz.edu.cn

#### Abstract

Large Language Models (LLMs) have revolutionized natural language interaction with data. The “holy grail” of data analytics is to build autonomous Data Agents that can self-drive complex data analysis workflows. However, current implementations are still limited to linear “ChatBI” systems. These systems struggle with joint analysis across heterogeneous data sources (e.g., databases, documents, and data files) and often encounter “context explosion” in complex and iterative data analysis workflows. To address these challenges, we present DeepEye, a production-ready data agent system that adopts a workflow-centric architecture to ensure scalability and trustworthiness. DeepEye introduces a Unified Multimodal Orchestration protocol, enabling seamless integration of structured and unstructured data sources. To mitigate hallucinations, it employs Hierarchical Reasoning with context isolation, decomposing complex intents into autonomous AgentNodes and deterministic ToolNodes. Furthermore, DeepEye incorporates a database-inspired Workflow Engine (comprising a Compiler, Validator, Optimizer, and Executor) that guarantees structural correctness and accelerates execution via runtime topological optimization. In this demonstration, we showcase DeepEye’s ability to orchestrate complex workflows to generate diverse multimodal outputs – including Data Videos, Dashboards, and Analytical Reports – highlighting its advantages in transparent execution, automated optimization, and human-in-the-loop reliability.

#### CCS Concepts

##### • Information systems → Information integration.

This work is licensed under a Creative Commons Attribution 4.0 International License. SIGMOD Companion ’26, Bengaluru, India

© 2026 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-2450-3/2026/05 https://doi.org/10.1145/3788853.3801612

#### Keywords

Data Agents; Workflow Orchestration; Natural Language Interfaces; Multimodal Data Analysis

ACM Reference Format:

Boyan Li, Yiran Peng, Yupeng Xie, Sirong Lu, Yizhang Zhu, Xing Mu, Xinyu Liu, and Yuyu Luo. 2026. DeepEye: A Steerable Self-driving Data Agent System. In Companion of the International Conference on Management of Data (SIGMOD Companion ’26), May 31-June 05, 2026, Bengaluru, India. ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3788853.3801612

#### 1 Introduction

The rapid evolution of Large Language Models (LLMs) has fundamentally transformed the landscape of data analytics, shifting the paradigm from rigid, menu-driven interfaces to flexible natural language interactions. Enterprises increasingly demand “Data Agents” capable of autonomously interpreting user intents, querying vast data repositories, and generating actionable insights [5]. Unlike traditional Business Intelligence (BI) tools that require manual operation, these intelligent agents promise to automate the end-to-end analysis pipeline, democratizing access to data insights for non-technical users [3].

Prior Art & Limitations. To realize this vision, recent advancements have primarily diverged into two streams: specialized Textto-SQL methods for structured databases [1, 2] and general-purpose Agent frameworks that utilize LLMs for tool orchestration [4]. However, deploying these systems in production environments remains elusive. Most existing solutions operate either as siloed query translators or linear “ChatBI” bots. Their inherent fragility in handling complex, multi-step workflows and opacity in execution logic hinder their adoption in trustworthy enterprise scenarios.

Challenges. We attribute these limitations to three fundamental challenges that current architectures fail to address: (C1) The Heterogeneity Gap. Real-world decision-making rarely relies on a

### DeepEye

![image 1](<2026-li-deepeye-steerable-self-driving-data_images/imageFile1.png>)

![image 2](<2026-li-deepeye-steerable-self-driving-data_images/imageFile2.png>)

||……<br><br>Generator<br><br>SQL<br><br>Generator<br><br>Video<br><br>Generator<br><br>Dashboard<br><br>Generator<br><br>Report<br><br>Executor<br><br>Code<br><br>Operator<br><br>File System<br><br>Search<br><br>Knowledge<br><br>Read<br><br>Datasource<br><br>……<br><br>Agent Node Tool Node|
|---|
<br><br>|Short-term Long-term<br><br>|
|---|
<br><br>Read<br><br>Datasource<br><br>Generator<br><br>Video<br><br>Generator<br><br>Dashboard<br><br>Generator<br><br>Report<br><br>Generator<br><br>SQL<br><br>Operator<br><br>File System<br><br>Executor<br><br>Code<br><br>Search<br><br>Knowledge<br><br>Orchestrate<br><br>Feedback<br><br>Workﬂow<br><br>Workﬂow Engine<br><br>|Planner<br><br>![image 3](<2026-li-deepeye-steerable-self-driving-data_images/imageFile3.png>)|
|---|
<br><br>|1. Compiler<br><br>3. Oprimizer<br><br>2. Validator<br><br>4. Executor<br><br>|Planner<br><br>![image 4](<2026-li-deepeye-steerable-self-driving-data_images/imageFile4.png>)| |
|---|---|
| | |
<br><br>![image 5](<2026-li-deepeye-steerable-self-driving-data_images/imageFile5.png>)<br><br>info<br><br>![image 6](<2026-li-deepeye-steerable-self-driving-data_images/imageFile6.png>)<br><br>1<br><br>2<br><br><br>3 4<br><br>5<br><br>6<br><br><br>![image 7](<2026-li-deepeye-steerable-self-driving-data_images/imageFile7.png>)<br><br>1<br><br>2<br><br>4<br><br>3<br><br>1<br><br>2<br><br>4<br><br>3<br><br>![image 8](<2026-li-deepeye-steerable-self-driving-data_images/imageFile8.png>)<br><br>![image 9](<2026-li-deepeye-steerable-self-driving-data_images/imageFile9.png>)<br><br>![image 10](<2026-li-deepeye-steerable-self-driving-data_images/imageFile10.png>)<br><br>![image 11](<2026-li-deepeye-steerable-self-driving-data_images/imageFile11.png>)<br><br>1<br><br>2<br><br>4<br><br>3<br><br>|
|---|
<br><br>![image 12](<2026-li-deepeye-steerable-self-driving-data_images/imageFile12.png>)<br><br>Memory<br><br>![image 13](<2026-li-deepeye-steerable-self-driving-data_images/imageFile13.png>)<br><br>Node|
|---|


![image 14](<2026-li-deepeye-steerable-self-driving-data_images/imageFile14.png>)

![image 15](<2026-li-deepeye-steerable-self-driving-data_images/imageFile15.png>)

Data

Data Video

Structured

![image 16](<2026-li-deepeye-steerable-self-driving-data_images/imageFile16.png>)

![image 17](<2026-li-deepeye-steerable-self-driving-data_images/imageFile17.png>)

![image 18](<2026-li-deepeye-steerable-self-driving-data_images/imageFile18.png>)

###### …

![image 19](<2026-li-deepeye-steerable-self-driving-data_images/imageFile19.png>)

![image 20](<2026-li-deepeye-steerable-self-driving-data_images/imageFile20.png>)

Semi-structured

…

![image 21](<2026-li-deepeye-steerable-self-driving-data_images/imageFile21.png>)

![image 22](<2026-li-deepeye-steerable-self-driving-data_images/imageFile22.png>)

![image 23](<2026-li-deepeye-steerable-self-driving-data_images/imageFile23.png>)

![image 24](<2026-li-deepeye-steerable-self-driving-data_images/imageFile24.png>)

Dashboard

Unstructured

…

![image 25](<2026-li-deepeye-steerable-self-driving-data_images/imageFile25.png>)

![image 26](<2026-li-deepeye-steerable-self-driving-data_images/imageFile26.png>)

![image 27](<2026-li-deepeye-steerable-self-driving-data_images/imageFile27.png>)

![image 28](<2026-li-deepeye-steerable-self-driving-data_images/imageFile28.png>)

![image 29](<2026-li-deepeye-steerable-self-driving-data_images/imageFile29.png>)

Konwledge

Kownledge Doc Meta-data SOP Experience

Analytical Report

……

Infra: MySQL PostgreSQL Redis AmonzonS3 Celery Docker Kubernetes FastAPI Vite React

![image 30](<2026-li-deepeye-steerable-self-driving-data_images/imageFile30.png>)

Figure 1: The System Architecture of DeepEye.

single data modality. A comprehensive analysis often requires crossreferencing structured data (e.g., sales records in SQL) with unstructured knowledge (e.g., market reports in PDF). Current systems are mostly siloed: Text-to-SQL handles only databases, while RAG handles only documents, lacking unified frameworks capable of joint analysis across heterogeneous sources. (C2) Context Explosion in Complex Reasoning. Complex analytical tasks involve multi-step reasoning and diverse tool usage. Traditional Single-Agent architectures force the descriptions of all available tools, intermediate observations, and reasoning history into a single global context window. This “Context Explosion” inevitably leads to LLM hallucinations, loss of focus, and failure to follow instructions as the workflow complexity increases. (C3) Unreliability and Inefficiency. The non-deterministic nature of LLMs clashes with the requirement for rigorous data engineering. Existing agents often generate “black-box” execution chains that are difficult to validate, debug, or optimize. Furthermore, they often execute tasks sequentially, missing opportunities for parallelism (e.g., fetching data while summarizing text), leading to higher latency.

Our Approach: DeepEye. To address these challenges, we present DeepEye, a steerable data agent system. Departing from linear chat paradigms, DeepEye adopts a workflow-centric architecture that orchestrates data analysis as transparent Directed Acyclic Graphs (DAGs). DeepEye introduces three key innovations. First, tackling C1, DeepEye features Unified Multimodal Orchestration. Its standardized node protocol bridges heterogeneous components (AgentNodes/ToolNodes), enabling seamless joint analysis of DB, File, and Knowledge Bases, and synthesizing results into Data Videos, Dashboards, and Analytical Reports. Second, addressing C2, DeepEye employs Hierarchical Reasoning. It decomposes intents into context-isolated sub-agents; the planner manages global dependencies while sub-agents handle local reasoning, effectively mitigating context overflow. Third, solving C3, DeepEye integrates a Database-Inspired Workflow Engine. Through static validation and runtime topological optimization (e.g., automatic parallelization), the engine ensures trustworthy and efficient execution.

Demonstration Scenarios. We showcase DeepEye via a “Global Sales Performance Analysis” case. First, Automated Multimodal Analysis demonstrates how explicit context binding (via “@”) triggers parallel database and document processing to synthesize Data Videos, Dashboards, and Reports. Second, Human-in-the-Loop Refinement highlights transparency by allowing users to inspect node internals (e.g., generated SQL) and use the Validator to prevent schema mismatches during manual edits. A demonstration video is available online1.

#### 2 System Architecture

DeepEye implements a workflow-centric architecture that bridges the gap between flexible LLM reasoning and rigid data engineering. As shown in Figure 1, the system is structured into four vertically integrated layers, underpinned by a cloud-native infrastructure.

#### 2.1 Unified Node Protocol and Isolation

To enable the Unified Multimodal Orchestration, DeepEye abstracts all analytical capabilities into a formal Unified Node Protocol. Formally, we define a generic node N as a 5-tuple:

N = ⟨D, I, O, C, Φ⟩ (1) where:

- • D denotes the Node Semantic Description, a natural language stringdescribingthenode’sfunctionality (e.g.,“GeneratesaPython script to visualize data”). The Planner relies on D for semantic retrieval and tool selection.
- • I = {𝑝1, . . .,𝑝𝑚} is the set of Input Ports. Each port is strictly defined by a schema triplet ⟨Key, Type, Desc⟩ (e.g., ⟨“query”, str, “The natural language question”⟩). The description Desc guides the Planner in accurately filling parameters from user context.
- • O = {𝑞1, . . .,𝑞𝑛} is the set of Output Ports, similarly defined by schema and description, representing the standardized artifacts produced by the node.


1https://drive.google.com/file/d/1TvPbqv-JBfcSceXjlE26_f1LTovVvt-K/view?usp= sharing

DeepEye: A Steerable Self-driving Data Agent System SIGMOD Companion ’26, May 31-June 05, 2026, Bengaluru, India

![image 31](<2026-li-deepeye-steerable-self-driving-data_images/imageFile31.png>)

##### Figure 2: The Demonstration of DeepEye.

- • C denotes the Configuration Parameters (e.g., model temperature), which are static environment settings.
- • Φ : (I × C) → O represents the internal execution logic. Based on how Φ is implemented, we classify nodes into two types:


ToolNodes (Deterministic Operators). These nodes encapsulate rule-based atomic operations. Their execution logic Φ𝑡𝑜𝑜𝑙 is deterministic, i.e., O = 𝑓𝑐𝑜𝑑𝑒(I, C). Examples include DataConnector and CodeExecutor. Without probabilistic components, Φ𝑡𝑜𝑜𝑙 guarantees idempotency and requires no reasoning context.

AgentNodes (Probabilistic Reasoners). These nodes are LLMdriven autonomous sub-agents. Their execution logic Φ𝑎𝑔𝑒𝑛𝑡 involves probabilistic reasoning or a nested sub-workflow (Sub-DAG). Formally, Φ𝑎𝑔𝑒𝑛𝑡 uses a private context window𝑊𝑙𝑜𝑐𝑎𝑙 and internal tools𝑇𝑖𝑛𝑡𝑒𝑟𝑛𝑎𝑙 to derive:

O ∼ 𝑃(· | I, C,𝑊𝑙𝑜𝑐𝑎𝑙,𝑇𝑖𝑛𝑡𝑒𝑟𝑛𝑎𝑙) (2)

Crucially, DeepEye enforces Context Isolation: the global planner only perceives the standardized I/O interfaces (I, O) and remains agnostic to 𝑊𝑙𝑜𝑐𝑎𝑙. This encapsulation shields the global system from intermediate reasoning noise, mitigating context overflow.

#### 2.2 Memory-Augmented Planner

The Planner translates high-level user requests (R) into executable workflow DAGs (G) using a dual-memory architecture:

• Working Memory (Short-term): Maintains the Context Stack, includingmulti-turndialoguehistory, intermediate variable states, and runtime feedback from the engine.

• Knowledge Base (Long-term): A vector database storing (1) Schema Metadata; (2) Domain Documentation; and (3) SOP Experience (verified historical workflows).

Retrieval-Augmented Planning (Pre-Execution). Upon receiving R, the Planner retrieves relevant SOPs and domain knowledge from the Knowledge Base. These retrieved contexts are injected as In-Context Demonstrations. The Planner either reuses an existing template or synthesizes a new topology, depending on the task.

Self-Correction via Feedback (Runtime). As shown in Figure 1, the Planner forms a closed loop with the Workflow Engine. If execution fails (e.g., SQL syntax error), the error trace is fed back into the Working Memory. The Planner then triggers Re-planning, using the feedback to adjust node parameters or modify the DAG structure.

ExperienceAccumulation(Post-Execution).The systemevolves over time. (1) Auto-Archiving: Successfully executed workflows are automatically serialized and indexed into the Knowledge Base. (2) Manual Creation: Expert-refined workflows from the GUI canvas can be manually saved as high-quality SOP templates, allowing the system to learn from human expertise.

#### 2.3 The DeepEye Workflow Engine

At the core of the system, the Workflow Engine transforms the Planner’s logical plan into reliable, optimized execution through four phases inspired by modern DBMS query engines:

Phase 1: Compilation. The Compiler parses the logical JSON plan generated by the Planner into a structural DAG Object. During this

phase, it resolves variable references (e.g., linking the output artifact of a SQLNode to the input port of a downstream DashboardNode) and instantiates the concrete Node classes defined in the Protocol.

- Phase 2: Validation (Static Analysis). To ensure safety before execution, the Validator performs rigorous structural and semantic checks: (1) Cycle Detection: It employs Depth-First Search (DFS) to verify that the graph structure is acyclic. (2) Schema Consistency: It checks type compatibility between connected ports, ensuring that a downstream node receives data strictly matching its defined Input Schema ⟨𝐾𝑒𝑦,𝑇𝑦𝑝𝑒⟩. (3) Completeness: It verifies that all required secrets (e.g., DB credentials) are present in the secure vault. Any violation is reported before execution, preventing runtime failures.
- Phase 3: Optimization (Runtime). Unlike linear-chain agents, DeepEye uses a runtime Optimizer that analyzes the DAG with Kahn’sAlgorithm.Basedondatadependencies,theoptimizer groups nodes into Execution Layers. Nodes within the same layer share no dependencies and are marked for Parallel Execution. For instance, independent SQL and document tasks can be dispatched in parallel, reducing end-to-end latency.
- Phase 4: Execution. The Executor functions as the scheduler. It dispatches the optimized layers to the underlying asynchronous infrastructure (powered by Celery/Redis). The Executor manages the data flow via a shared object store, handles retries for transient failures (e.g., API timeouts), and captures execution logs. If a nontransient error occurs, the error trace is fed back to the Planner, triggering the Self-Correction mechanism in Section 2.2.


#### 2.4 Scalable Cloud-Native Infrastructure

DeepEye uses a cloud-native stack for scalable deployment. Specifically, it adopts containerized microservices with Docker, Docker Compose, and a FastAPI backend for consistent deployment and asynchronous request handling. To support long-running tasks without blocking the interface, the system uses Celery and Redis for asynchronous scheduling. It further combines PostgreSQL for structured metadata and MinIO/S3 for unstructured artifacts through a unified storage interface. For security, ToolNode execution runs in sandboxed containers with limited network access, while user data remains logically isolated.

3 Demonstration

We demonstrate DeepEye on a “Global Sales Performance Analysis” task through the interface in Figure 2, covering the full pipeline from heterogeneous data ingestion to multimodal output generation.

#### 3.1 Scenario 1: Automated Multimodal Analysis

Goal. To showcase the system’s ability to autonomously orchestrate heterogeneous data sources and optimize workflow execution for diverse outputs.

Workflow. The demonstration begins with data preparation. We upload sales records into the Data Sources Panel (Fig. 2-B) and domain knowledge documents into the Knowledge Base (Fig. 2-A). Intent Understanding with Context Binding: In the Chat Panel (Fig. 2-C), the user utilizes the system’s “@” referencing feature to explicitly bind the analysis context. By selecting @Sales Database and

@Financial Metrics (as shown in the figure), the user effectively grounds the subsequent natural language query: "Help me analyze the 2025 global sales performance." This mechanism resolves ambiguity in data selection before planning begins.

Orchestration & Optimization: The Planner analyzes the request and the bound contexts, as shown in Fig. 2-D. It generates a logical plan which the Workflow Engine compiles into a DAG, visualized in the Workflow Canvas (Fig. 2-E). Highlight: We will draw attention to the Runtime Optimizer. The audience will observe that the generated workflow branches out: a Knowledge Search Node (for metrics) and a Datasource Read Node (for the database) are arranged in the same execution layer. This visually demonstrates the engine’s ability to identify independent tasks and execute them in parallel. Multimodal Synthesis: Upon successful execution, DeepEye synthesizes the results into a data video, dashboard, and analytical report (Fig. 2-G), effectively bridging structured querying and multimodal content generation.

#### 3.2 Scenario 2: Human-in-the-Loop Refinement

Goal. To demonstrate the transparency, editability, and trustworthiness of the workflow-centric architecture.

Workflow. Unlike “black-box” ChatBI tools, DeepEye allows users to inspect and intervene at any stage.

Transparent Inspection: The user clicks on the SQL Generator Node in the canvas. The Inspector Panel (Fig. 2-F) opens, revealing the node’s internal state. Here, the user can inspect the node’s I/O schema and parameters. We integrated our Text-to-SQL technique, DeepEye-SQL [1], to ensure high-accuracy query generation.

Interactive Debugging: We then simulate a manual SQL edit in the Inspector. When the edited node is connected to an incompatible downstream node, the Validator immediately raises a “Schema Mismatch” error.

Execution Feedback: Finally, we re-run the refined workflow. The Process Monitor (Fig. 2-D) displays real-time logs and “ThoughtAction” traces of the Planner, proving that the reasoning process is fully transparent and auditable.

#### Acknowledgments

This work was supported by the NSF of China (Grant No. 62402409).

#### References

- [1] Boyan Li, Chong Chen, Zhujun Xue, Yinan Mei, and Yuyu Luo. 2026. DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework. Proc. ACM Manag. Data 4, 3 (2026). doi:10.1145/3802035
- [2] Boyan Li, Jiayi Zhang, Ju Fan, Yanwei Xu, Chong Chen, Nan Tang, and Yuyu Luo.

2025. Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search. In ICML (Proceedings of Machine Learning Research). PMLR / OpenReview.net.

- [3] Tianqi Luo, Chuhan Huang, Leixian Shen, Boyan Li, Shuyu Shen, Wei Zeng, Nan Tang, and Yuyu Luo. 2025. nvBench 2.0: Resolving Ambiguity in Text-toVisualization through Stepwise Reasoning. In The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and Benchmarks Track.
- [4] Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, and Chenglin Wu. 2025. AFlow: Automating Agentic Workflow Generation. In ICLR. OpenReview.net.
- [5] Yizhang Zhu, Liangwei Wang, Chenyu Yang, Xiaotian Lin, Boyan Li, et al. 2025. A Survey of Data Agents: Emerging Paradigm or Overstated Hype? CoRR abs/2510.23587 (2025).


