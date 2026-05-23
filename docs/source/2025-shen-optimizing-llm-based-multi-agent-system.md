---
type: source
kind: paper
title: "Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development"
authors: Ming Shen, Raphael Shu, Anurag Pratik, James Gung, Yubin Ge, Monica Sunkara, Yi Zhang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.16086
source_local: ../raw/2025-shen-optimizing-llm-based-multi-agent-system.pdf
topic: general-knowledge
cites:
---

# arXiv:2505.16086v2[cs.AI]6Aug2025

## Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development

Ming Shen♥∗, Raphael Shu♦, Anurag Pratik♦, James Gung♦, Yubin Ge♦, Monica Sunkara♦, Yi Zhang♦

♥Arizona State University ♦Amazon Web Services

### Abstract

We have seen remarkable progress in large language models (LLMs) empowered multi-agent systems solving complex tasks necessitating cooperation among experts with diverse skills. However, optimizing LLM-based multi-agent systems remains challenging. In this work, we perform an empirical case study on group optimization of role-based multi-agent systems utilizing natural language feedback for challenging software development tasks under various evaluation dimensions. We propose a two-step agent prompts optimization pipeline: identifying underperforming agents with their failure explanations utilizing textual feedback and then optimizing system prompts of identified agents utilizing failure explanations. We then study the impact of various optimization settings on system performance with two comparison groups: online against offline optimization and individual against group optimization. For group optimization, we study two prompting strategies: one-pass and multi-pass prompting optimizations. Overall, we demonstrate the effectiveness of our optimization method for role-based multi-agent systems tackling software development tasks evaluated on diverse evaluation dimensions, and we investigate the impact of diverse optimization settings on group behaviors of the multi-agent systems to provide practical insights for future development.

### 1 Introduction

Autonomous agents utilizing large language models have achieved promising results on tasks across various domains such as reasoning Yao et al. (2023); Shinn et al. (2023); Ge et al. (2025), code generation Shinn et al. (2023), tool usage Cai et al. (2023), and embodied AI Ahn et al. (2022). Recent studies have demonstrated that incorporating synergistic agents into multi-agent collaboration frameworks substantially further enhances NLP problem-solving abilities Zhuge et al. (2023); Liang et al. (2023); Du et al. (2024); Wu et al. (2024b); Wang et al. (2024b); Li et al. (2023a); Hao et al. (2023); Zhang et al. (2024a); Dong et al. (2024); Jiang et al. (2023); Wu et al. (2024a); Chen et al. (2024) and successfully addresses complex real-world challenges, including human behavior simulation Park et al. (2023), software development Qian et al. (2024); Hong et al. (2024), code issue resolving Tao et al. (2024), and web task execution Zhang et al. (2024b). In our study, we focus on role-based multi-agent systems, where LLM-based agents are assigned distinct roles to accomplish a task collaboratively.

A primary constraint inherent to LLMs is their reliance on prompt design Brown et al. (2020); Reynolds & McDonell (2021); Si et al. (2023), which also extends to LLM-based agents. Specifically, it is crucial for developers to meticulously curate agent prompts, considering their respective roles and responsibilities in the collaboration framework. To this end, various automatic agent prompt optimization methods have been proposed in recent works, such as DSPy Khattab et al. (2024), GPTSwarm Zhuge et al. (2024), and TextGrad Yuksekgonul et al. (2024). However, none of these works have conclusively demonstrated the efficacy of their approaches within a genuine role-based multi-agent system, wherein agents take on various roles to tackle a complex task collaboratively. Furthermore, current

∗Work done during internship at Amazon

works primarily focus on traditional NLP benchmarks such as MMLU Hendrycks et al. (2021a), MATH Hendrycks et al. (2021b), and HumanEval Chen et al. (2021). In contrast, our study aims to address the more intricate real-world software development task.

In this work, we propose a two-step agent prompt optimization framework utilizing natural language feedback of the multi-agent system along various evaluation criteria for software development tasks (§4.2). In the first step, we employ an LLM-based locator to pinpoint underperforming agents, taking into account their roles and natural language feedback of the multi-agent system. The locator also provides fine-grained explanations for their underperformance. In the second step, we utilize an LLM-based optimizer Zhou et al.

- (2023); Pryzant et al. (2023); Yang et al. (2024) to optimize the system prompts of identified underperforming agents based on fine-grained explanations. We demonstrate the efficacy of our proposed optimization pipeline across various evaluation dimensions pertinent to software development tasks. For each evaluation dimension, we collect natural language feedback using either model-based or rule-based methods.


Considering the inherent complexity of the multi-agent system, we further explore the impact of different optimization settings on the multi-agent system’s performance (§4.3). Concretely, we investigate two comparison groups: online against offline optimization and individual against group optimization. In the online setting, agents interact with the environment to collect feedback during optimization; however, feedback is collected beforehand in the offline setting. In the individual optimization setting, one agent is optimized at a time during each optimization step, and in the group setting, all agents are optimized in each step. For group optimization, we further investigate two prompting strategies during the optimization step: one-pass and multi-pass prompting. In one-pass group optimization, agents are optimized together with one inference pass, whereas in multi-pass group optimization, agents are optimized with separate inference passes. We show that online and offline optimizations are both effective, although offline performs slightly worse than online. We then show that optimizing all agents at each optimization step is necessary for our pipeline to outperform baselines consistently. Finally, we don’t observe apparent performance differences between one-pass and multi-pass prompting, so one could choose one-pass prompting optimization for efficiency.

The contributions of our work are as follows:

- • We investigate optimizing a role-based multi-agent system on a complex real-world problem - software development. We show that the LLM-based multi-agent system can be effectively optimized utilizing textual feedback.
- • We study the software development optimization problem along five distinct dimensions, whereas existing literature mainly focuses on a single evaluation metric for simpler tasks.
- • We propose a two-step optimization pipeline by first locating and then optimizing underperforming agents. Experiment results show that our proposed pipeline outperforms baselines along the evaluation dimensions we study.
- • We compare optimization effectiveness in various settings, including online against offline and individual against group optimization. We demonstrate online and group optimizations as more effective settings than individual and offline.


### 2 Related Works

#### 2.1 LLM-Based Agents

LLM-based agents Yao et al. (2023); Shinn et al. (2023) have achieved impressive results on various NLP tasks. Applications Richards (2023) utilizing a single LLM-based agent, such as AutoGPT Richards (2023) and LangChain Chase (2022), can accomplish more functionalities and provide opportunities to a diverse audience spectrum, including developers and even non-technical users. More recently, collaborations among multiple LLM-based agents demonstrated even more capabilities. Liang et al. (2023) and Du et al. (2024) incorporate multiple LLM-based agents into a debate framework, aiming to stimulate divergent thinking and enhance both factuality and reasoning capabilities. Utilizing the unique strengths and knowledge of each individual agent, LLM-based agents can also be synergistically integrated

to collaboratively enhance problem-solving capabilities on a broad range of tasks Hao et al.

- (2023); Zhuge et al. (2023); Zhang et al. (2024a); Ge et al. (2023); Dong et al. (2024); Wu et al. (2024b); Zhang et al. (2024b). In our work, we focus on role-based multi-agent system Wang et al. (2024b); Li et al. (2023a); Park et al. (2023); Qian et al. (2024); Wu et al. (2024a); Tao et al. (2024); Chen et al. (2024), in which individual agent components are assigned distinct roles to interact and collaborate to accomplish a task effectively. Among the above role-based multi-agent systems, Hong et al. (2024) and Qian et al. (2024) design agent roles inspired by Standardized Operating Procedures (SOPs) to solve software development tasks collaboratively.

2.2 Prompt Optimization

Studies have demonstrated the critical role of prompt engineering in unlocking the potential of LLMs Brown et al. (2020); Gao et al. (2021); Wei et al. (2022); Liu et al. (2023). However, manually curating prompts with human effort is both time-consuming and expensive. Hence, investigating methods to perform prompt engineering automatically becomes a viable solution Shin et al. (2020); Deng et al. (2022); Prasad et al. (2023). In our work, we adopt the recent trend of adopting LLMs as optimizers to optimize system prompts of the underperforming agents identified in the locator step. As summarized by Ma et al.

- (2024), recent works focusing on LLMs as optimizers can be classified into two categories: resampling-based and reflection-based. Resampling-based methods Zhou et al. (2023); Li et al. (2023b) sample around the current best prompts for better prompt candidate generation using LLMs while keeping the semantic meanings. On the other hand, reflection-based methods Pryzant et al. (2023); Sun et al. (2023); Ye et al. (2024); Wang et al. (2024a); Yang et al.


- (2024); Guo et al. (2024) explicitly or implicitly leverage feedback or historical information to refine current prompts. Our optimization step falls in the reflection-based category.


#### 2.3 Agent Optimization

We have seen various prompt optimization methods in §2.2, and it is also a critical topic for agent optimization. DSPy Khattab et al. (2024) views LLM-based systems as programs and proposes to build and optimize them in a programmatic fashion. DSPy can optimize LLM inference prompts, including few-shot examples and system instructions, through search algorithms in a combinatorial space. TextGrad Yuksekgonul et al. (2024) takes a different perspective of backpropagation being a general and powerful framework to optimize the LLM-based agent system based on natural language feedback. However, none of them proves the effectiveness of their methods in a role-based multi-agent system setting through their experimental results. Research works in another agent optimization direction, such as DyLAN Liu et al. (2024) and GPTSwarm Zhuge et al. (2024), focus on optimizing the workflow of multi-agent systems. They usually view multi-agent systems as directed graphs and optimize the graph by selecting or pruning existing edges that represent information exchange between agents. However, a fundamental limitation of such an optimization paradigm is that it relies on the assumption of the multi-agent system being decentralized, where all the agent components can draw conclusions regarding a given task, and later, the final output is generated using a consensus schema such as majority voting. This optimization paradigm is less applicable in scenarios where information flows are predefined or where agent components assume varied responsibilities to accomplish a task collaboratively, particularly in the context of real-world tasks. Finally, a significant difference between our work and all the above works is that other than traditional NLP tasks, we study optimization for software development tasks, which are complex, open-ended tasks.

### 3 Software Developemt Task

In our work, we choose software development as the case study task for optimizing LLMbased multi-agent systems. Software development tasks require complete software solution code based on detailed software requirement descriptions spanning a broad range of applications, such as board games and social networking.

#### 3.1 Why Software Development?

The reasons we choose software development tasks are three-fold. First, unlike traditional NLP tasks such as natural language understanding and mathematical reasoning, software development is a more suitable test bed for role-based multi-agent collaboration since it necessitates cooperation among multiple agents with diverse skills. For example, Hong et al. (2024) designs a product manager for natural language description understanding, engineers for code reasoning, and code reviewers for code revision to tackle software engineer tasks collaboratively. Second, given the difficulty of evaluating solution code for open-ended software descriptions, there is generally no annotated ground-truth solution and standard evaluation metrics, unlike traditional NLP tasks. However, this gives us the flexibility to demonstrate the effectiveness of our optimization pipeline along various user-defined evaluation dimensions. Third, although previous works explored LLM-based agent optimization, group optimization of agents in a complex role-based multi-agent collaboration environment for real-world software development tasks has never been addressed.

#### 3.2 Optimization Dimensions

In our study, we explore optimization along five evaluation dimensions pertinent to software development tasks. In this section, we first introduce these five dimensions.

- • Functionality – Functionality is the most crucial criterion for judging the quality of software code. It judges whether the software code meets all the requirements and specifications outlined in the software description.
- • Robustness – Through the robustness dimension, we aim to measure whether the software is reliable enough to handle various unexpected user inputs or exceptions.
- • Test Case Coverage – Test cases are essential for software code. To improve code quality and coverage, they help verify and validate whether the code is functioning as expected and identify bugs and errors in the code. We aim to optimize the software code to contain test cases to cover all aspects of the task description.
- • Documentation – To make it easier for developers to understand, maintain, and collaborate on the solution code, we aim to optimize the system to generate enough proper documentation, such as comments and docstrings.
- • Code Style Violation – Finally, to enhance code readability and consistency, we aim to optimize the software code to follow PEP 8 1, a style guide for Python code.


### 4 Group Optimization of LLM-Based Multi-Agent System with Feedback

#### 4.1 Problem Formulation

We model an LLM-based multi-agent system as a directed graph G = {N, E}, where N is a set of nodes and E is a set of edges that are ordered pairs of nodes E ⊆ {(u, v)∣(u, v) ∈ N × N, u ≠ v}. Each node n ∈ N is a LLM agent that takes in natural language form input In combined with its agent prompt Pn to generate a response On = LLM(In ⊕ Pn), where ⊕ stands for string combination. For role-based multi-agent systems, the role of agent n is reflected in its prompt Pn. The prompts of all agent nodes in the graph form prompt group P = {Pn∣n ∈ N}. An edge (u, v) ∈ E represents that agent u sends its response output Ou to agent v. Suppose all the antecedent nodes for agent node n are A(n) = {m ∈ N∣(m, n) ∈ E}, the input In for agent n consists of all outputs of the antecedent agents {Om∣m ∈ A(n)}. Please refer to §A in Appendix for more details regarding the concrete role-based multi-agent system architecture we adopt in our work.

Consider a training set Dtrain = {Xi}∣i=T1∣ without ground-truth labels drawn from a software development task T , the multi-agent system G takes each Xi as input, processes Xi given the graph structure and current agents prompt group, and outputs a final response Yi = G(Xi,P). Given a user-defined evaluation dimension based on the user’s need, a critic

1https://peps.python.org/pep-0008/

Textual Feedback

![image 1](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile1.png>)

Software

Critic

Solution

![image 2](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile2.png>)

Description

![image 3](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile3.png>)

![image 4](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile4.png>)

![image 5](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile5.png>)

![image 6](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile6.png>)

![image 7](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile7.png>)

![image 8](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile8.png>)

![image 9](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile9.png>)

![image 10](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile10.png>)

![image 11](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile11.png>)

![image 12](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile12.png>)

![image 13](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile13.png>)

![image 14](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile14.png>)

![image 15](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile15.png>)

![image 16](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile16.png>)

Agent Failure

![image 17](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile17.png>)

![image 18](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile18.png>)

![image 19](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile19.png>)

Explanation

![image 20](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile20.png>)

Agent Failure

![image 21](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile21.png>)

![image 22](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile22.png>)

Locator

Explanation

Optimizer

1

- Figure 1: A high-level workflow of our two-step optimization pipeline. Please refer to §4.2 for more details.


mechanism f targeting this evaluation dimension generates a scalar score Ui that directly assesses the utility of Yi (performance of the multi-agent system) and natural language feedback Ii explaining the scalar score based on the task input: Ui, Ii = f(Yi, Xi). In our work, we study 5 evaluation dimensions as introduced in §3.2, and we will describe the concrete implementations of their corresponding critic mechanisms in §5.2. Our goal is to find an optimal prompt group P∗ drawn from the natural language space such that the expectation of utility Ui is maximized over Dtrain utilizing Ii:

Exi∼Dtrain[Ui]

P∗ = argmax

P

Finally, we use the optimized agent prompt group P∗ to perform evaluation on a testing set based on utility scores generated by the same critic mechanism: Exi∼Dtest[Ui].

- 4.2 Optimization Pipeline We propose a two-step pipeline to optimize a role-based multi-agent system. As shown in


- Figure 1, utilizing natural language feedback I of the multi-agent system’s output generated by the critic mechanism f , we perform prompt optimization for participation agents in the system. Specifically, we first use a locator L to identify the underperforming agents, and , that are not performing well and generate explanations of their failures, utilizing textual feedback I (§4.2.1). Then, an optimizer O optimizes the system prompts of the identified underperforming agents utilizing explanations of their failures (§4.2.2).


![image 23](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile23.png>)

![image 24](<2025-shen-optimizing-llm-based-multi-agent-system_images/imageFile24.png>)

#### 4.2.1 Locating

Natural language feedback I for the multi-agent system’s output provides guidance regarding which directions to improve agents in the system. However, it is hard to improve individual agents solely based on global feedback of the final collaboration output. As a result, we design an LLM-based locator L capable of generating fine-grained explanations to guide agent optimization. Our locator takes three major components as inputs: software task description X, global natural language feedback I, and multi-agent collaboration details G. Collaboration details include two major components: role descriptions and communication trajectories of all participation agents. With a carefully designed prompt (see Figure 11 in Appendix), the locator focuses on the negative aspects of the global feedback and navigates to underperforming agents Nf ⊆ N responsible for the negative aspects of feedback. The locator also generates specific failure explanations E = {En∣n ∈ Nf} of identified underperforming agents as fine-grained signals to better guide the later optimization step. Overall, the input and output workflow of the locator is Nf, E = L(X, I, G).

#### 4.2.2 Optimizing

After identifying the underperforming agents and fine-grained explanations of their failures from the locator in the previous step, we utilize an LLM-based optimizer O to optimize

the system prompts of underperforming agents. For each underperforming agent n, the optimizer takes two critical components as input: input-output pair Mn and fine-grained failure explanations En of this agent. The input-output pair includes the system message Pn, all user messages, and the output of the agent. We carefully design the prompt (see Figure 12 in Appendix) to guide the optimizer O to optimize the system prompt of underperforming agents in the direction where the fine-grained failure explanations can be mitigated: Pn = O(Pn, En,...).

#### 4.3 Optimization Settings

Based on our proposed two-step optimization pipeline, we proceed to investigate the impact of various optimization settings on the performance of the multi-agent system using two comparison groups: online against offline (§4.3.1) and individual against group (§4.3.2) optimization. For group optimization setting, we further investigate two different prompting methods: one-pass against multi-pass optimization prompting.

#### 4.3.1 Online against Offline Optimization

Inspired by the main difference between online and offline reinforcement learning Levine et al. (2020) where data for learning is collected in real-time by agents interacting with the environment under online setting, whereas collected beforehand under offline setting, we apply the online versus offline setting to our study. The difference between our online and offline settings lies in how the textual feedback is collected during each optimization step (each training instance in our case). For the online setting, we use the optimized prompts at the current step to derive the solution code so that agents must interact with the environment (the critic) to retrieve real-time feedback. However, for offline setting, we use the default initial agent prompts to derive solution codes and retrieve feedback for all training instances beforehand. This offline feedback collection process fits into open-ended tasks like software development, where high-quality human-annotated feedback can be collected beforehand.

#### 4.3.2 Individual against Group Optimization

During the locating step, multiple agents are usually identified as underperforming agents. We aim to investigate whether optimizing all of them or disentangling the optimization by individually updating each agent is more effective. One can image group optimization as a complete optimization process as it optimizes all components in each step; however, it also potentially brings problems such as overfitting, and individual optimization setting in our study can mitigate this concern by reducing the optimization complexity and gradually optimizing one agent at a time. Concretely, we randomly sample one underperforming agent for optimization and leave other underperforming agents untouched during each optimization step.

One-Pass versus Multi-Pass Prompting. For group optimization, we study two prompting methods. For all identified underperforming agents, we optimize each with a separate LLM inference call, which we call multi-pass prompting. We can also optimize all agents jointly with a single LLM inference call, which we call one-pass prompting. Multi-pass prompting could be more accurate than one-pass prompting, as one-pass prompting introduces irrelevant information about other agents. However, one-pass prompting could utilize the interconnection between agent components, and it is more efficient as it consumes fewer API calls.

### 5 Experiments

#### 5.1 Dataset

We use SRDD (Software Requirement Description Dataset) Qian et al. (2024) as the software requirement descriptions dataset in our study. SRDD comprises 1,200 software task prompts extracted from ChatGPT, spanning 5 major categories, including education, work, life, game, and creation. We randomly shuffle and split the entire dataset into train, development, and test splits with a ratio of 6:2:2.

###### Functionality (↑) Robustness (↑) Coverage (↑) Documentation (↑) Violation (↓)

Unoptimized 6.90 6.75 0.32 3.80 6.62 One-Shot 6.66 7.47 7.00 15.33 3.80 Direct Optimization (TextGrad) 6.74 7.11 6.31 16.07 6.90

Our Optimization Offline Setting

Individual 6.81 7.20 7.27 19.46 5.18 Group w/ Multi-Pass 7.22 7.63 7.64 17.92 4.35 Group w/ One-Pass 7.06 7.77 6.99 19.92 4.82

Online Setting

Individual 7.02 7.55 6.95 20.14 5.34 Group w/ Multi-Pass 7.26 7.60 6.48 20.15 3.03 Group w/ One-Pass 7.26 7.74 7.81 20.33 3.24

- Table 1: Evaluation scores under all optimization settings across all evaluation dimensions for baselines and our proposed two-step optimization pipeline. Bold numbers indicate best-performing results, and underlined numbers indicate second-best results. Note that the score range for the first three dimensions is 0-10, and the last two are simply positive integers.


#### 5.2 Critic Mechanism Implementation

We explore various evaluation dimensions pertinent to software development tasks. For each dimension, a critic mechanism generates both a scalar utility score and natural language feedback to the solution as described in §4.1. During implementation, scores and feedback are generated simultaneously or separately for different dimensions. Overall, they are generated using two high-level methodologies. First is rule-based method, where scores or feedback are generated based on heuristic rules or external tools. Second is model-based method, following recent works of LLMs as judges Zheng et al. (2023); Dubois et al. (2023); McAleese et al. (2024), where we guide LLMs to evaluate solution code with carefully designed prompts.

For functionality, robustness, and test case coverage dimension, we generate scores on a scale from 0 to 10 and natural language feedback at the same time using GPT-4 OpenAI (2023) as judge. For the documentation dimension, we use GPT-4 to generate natural language feedback; however, we directly use the number of lines of comments and docstrings in the solution code as the scalar score. For code style violation dimension, we utilize an external tool, pycodestyle2, to check the software code against style conventions in PEP 8. We define the total number of violations and the corresponding explanations the checker identifies as score and feedback. Please refer to Appendix B for more details of prompts for obtaining scores and feedback using GPT-4.

#### 5.3 Experiment Setting

We use gpt-4-0613 version of GPT-4 as the LLM everywhere in our study with a temperature of 0.1. We randomly sample 5 task descriptions 3 from the training set. At each optimization step, we optimize the current agent system prompts to a new group of prompts, which will be optimized in the next step. Unless mentioned explicitly, we always randomly sample 100 task descriptions from the testing set to report evaluation results due to budget constraints.

#### 5.4 Baselines

We consider the unoptimized system and two baselines for comparisons. Unoptimized: we use default agent system prompts to run the pipeline for code generation without optimization directly. One-shot: We randomly sample one agent communication trajectory and feedback pair from the training set into the system prompts of all agents as a demonstration and ask them to avoid making similar mistakes presented in the feedback. Direct optimization (TextGrad): We consider another baseline that directly optimizes all system prompts given textual feedback. This aligns with TextGrad Yuksekgonul et al. (2024), which backpropagates textual feedback to improve individual components of a compound AI system.

2https://pycodestyle.pycqa.org/en/latest/ 3We found more steps of optimization unnecessary; please refer to §C in Appendix for more details

Test Case Coverage (↑)

Functionality (↑)

Documentation (↑)

Violation (↓)

Robustness (↑)

EvaluationScores

30

10

10

- 6.5
- 7

- 7.5
- 8


- 8.5


train dev

25

8

8

20

6

6

15

4

4

10

2

2

train dev

train dev

train dev

train dev

5

0

0

- 6

- 6.5
- 7

7.5

8

- 8.5




0

0% 20% 40% 60% 80% 100%

0% 20% 40% 60% 80% 100%

0% 20% 40% 60% 80% 100%

0% 20% 40% 60% 80% 100%

0% 20% 40% 60% 80% 100%

Optimization Steps (%)

Optimization Steps (%)

Optimization Steps (%)

Optimization Steps (%)

Optimization Steps (%)

- Figure 2: Training and development evaluation score curves analysis for all evaluation dimensions under online group optimization with one-pass prompting.


Note that the key difference lies in that TextGrad does not identify the underperforming agents as the locator in our framework does and directly utilizes the textual feedback for optimization. Another related work is DSPy Khattab et al. (2024), a programming model that abstracts LLM pipelines as text transformation graphs, i.e., imperative computational graphs where LLMs are invoked through declarative modules. However, the evaluation metric must output numerical values instead of textual feedback, which cannot fit our setting. Therefore, we leave adapting it to our setting as future work.

- 5.5 Main Results

We show the main results in Table 1. Both one-shot and direct optimization baselines cannot consistently outperform unoptimized system across all evaluation dimensions. They both fail on the functionality dimension, which is probably the most important evaluation dimension for software development. Direct optimization also fails on the code violation dimension. However, our proposed method effectively optimizes the multi-agent system evaluated on all optimization dimensions and settings except only for offline individual setting on the functionality dimension, where we observe only 0.1 behind the unoptimized system. Our best-performing optimization setting, online group optimization with one-pass prompting, is always better than the two baselines. Our method outperforms the one-shot baseline in 22 out of the total of 30 cases across all evaluation dimensions and optimization settings, and it always outperforms the direct optimization baseline.

Next, we compare the performance of our optimization pipeline under all optimization settings. First, the most effective strategy seems to be online group optimization with onepass prompting, whose performance is consistently among the top two across all evaluation dimensions. Secondly, individual optimization is definitely worse than group optimization in most cases; however, it is still an effective optimization strategy compared with unoptimized system in all cases only except for offline setting for functionality dimension. This means optimizing all underperforming agents at each step is a better practice than gradually optimizing a single agent component along the optimization steps under our case study. It is possible because an LLM-based multi-agent system is still not complex enough to bring up issues like overfitting compared with more complicated systems such as neural networks. Thirdly, although counterintuitive in our case study, the offline setting is still an effective optimization strategy. Offline setting is generally worse than the online setting only across 2 out of 5 evaluation dimensions. As discussed in Section 4.3.1, this enables human intervention by providing high-quality feedback annotation beforehand. This is even more beneficial when the required training data size is only a few, meaning less human-effort required for annotation. This is very similar to our case, and we leave investigating whether human-annotated high-quality feedback leads to even better optimization for future work. Finally, we don’t observe a consistent performance difference between one-pass and multi-pass optimization prompting for group optimization setting across all evaluation dimensions. This probably suggests that although the single LLM call of the one-pass prompting contains irrelevant information about other agents, it does not affect the overall optimization process under our current setup. As a result, one could choose one-pass optimization for higher efficiency without sacrificing performance.

- 5.6 Analyses


- 5.6.1 Optimization Curve Analysis


In this section, we plot the optimization curves of the average evaluation scores on the training and development set with respect to each optimization step. Due to budget limits, we are not able to plot curves for all development examples, so we randomly sample 30 examples from the development set.

Online Multi-Pass Online One-Pass Offline Multi-Pass Offline One-Pass

12

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


EvaluationScores()↓

10

8

6

- Figure 2 shows the optimization curves for all evaluation dimensions under the online group optimization with one-pass prompting setting. We chose this setting as it gives superior performances compared with other settings as discussed in previous section. First, we can tell that there is no over-fitting happening during training, as the trends for both training and development curves are consistent across all evaluation dimensions. Second, we observe that complete model-based critic mechanisms (first three) tend to show less stable training than rule-based critic mechanisms (last two), as they oscillate more often. Finally, it shows that training curves are less stable than development curves, possibly due to the sparsity of training data compared with development data. Figure 3 shows the optimization training curves under major optimization settings (we use group optimization as default) for code style violation dimension since it has a complete model-free score and feedback generation process to avoid potential bias raised by model-based evaluation. We observe that online setting shows much better stability than offline settings under both one-pass and multi-pass prompting, as their curves oscillate much less.


4

2

0% 20% 40% 60% 80% 100%

Optimization Steps

Figure 3: Training curve analysis for code style violation evaluation dimension under major optimization settings.

#### 5.6.2 Starting from "Empty" Prompts

Instead of starting optimization from a default prompt, we study whether our optimization pipeline is still effective when the prompt to optimize starts from empty. Note that the "empty" prompts are not completely empty as they still contain very basic contexts (prompts in black) as shown in Figures 5 and 6. We slightly increase the optimization steps from the default number of 5 to 8. We analyze online group optimization with one-pass promoting across all evaluation dimensions. As shown in Table 4, starting from an "empty" prompt, our pipeline is still able to optimize the multi-agent system to a level that is on par or just slightly worse than the system optimized starting from an informative default starting prompt.

Unoptimized Default Empty

Func. (↑) 6.90 7.26 7.06 Rob. (↑) 6.75 7.74 7.77 Cov. (↑) 0.32 7.81 7.31 Doc. (↑) 3.80 20.33 19.8

Comp. (↓) 6.62 3.24 4.61

Figure 4: The effect of starting optimization from an "empty" agent prompt instead of a default prompt.

#### 5.6.3 Case Study

We provide optimized agent prompts at the final step for functionality, robustness, and code style violation evaluation dimensions for the two agent roles: the programmer agent in Table 2 and the software test engineer agent in Table 4 in the Appendix. We generally observe agent prompts being optimized under the desired evaluation dimension, as highlighted in green text. For example, under the functionality dimension, the system prompt of the solver agent is optimized to contain "ensure that all functionalities mentioned in the task description are implemented", and system prompt of the reviewer agent is optimized to contain "provide more detailed feedback on any missing functionalities or areas for improvement". Under the dimension of code violation, the system prompt of the solver agent is optimized to contain "break down long lines of code into multiple lines to improve readability and maintainability", and the reviewer agent is optimized to contain "review the code for adherence to style guides like PEP8, including line length, and provide feedback on this aspect". In future work, we aim to improve the generalization of the optimized prompt. For example, we observe that the optimized prompt sometimes contains instance-specific content of the training instances such as "consider the lifecycle of any temporary files created during the process".

###### Functionality

As a Programmer, your task is to provide a comprehensive solution to the given software task. Your solution should be versatile, capable of handling different sports, player positions, and strategies. It should also allow users to drag and drop players to specific positions and add notes and annotations to each play. Ensure that all methods outlined in the initial structure are fully implemented and functional. Pay special attention to the user interface and ensure it is user-friendly. Test your code to ensure it works as expected and meets all the requirements of the task description. Additionally, ensure that all functionalities mentioned in the task description are implemented, and consider the user experience when designing the interface and functionality of the software. After receiving feedback from other agents, make sure to incorporate their suggestions into your final solution.

Robustness

As a Programmer, your task is to provide a new solution code to the given software task. If the history is not empty, your new solution code must be based upon your previous solution and teammates’ feedback in the history. While developing your solution, ensure to incorporate robust error handling, especially for user inputs in any user interface elements. Consider all possible edge cases and potential user errors to enhance the robustness of your solution. Additionally, pay attention to the feedback from your teammates regarding the robustness of your code, particularly in areas such as error handling, input validation, and handling of unexpected exceptions. Also, consider the lifecycle of any temporary files created during the process and ensure they are properly managed to prevent unnecessary storage usage. Remember to think thoroughly about the different ways the software could be used or misused, and add appropriate error handling and input validation to cover these scenarios. Furthermore, consider the integrity and validity of the data being processed, including checks for invalid or duplicate inputs, and robust handling of data storage and retrieval.

Violation

As a programmer, your task is to provide a new solution code to the given software task. If the history is not empty, your new solution code must be based upon your previous solution and teammates’ feedback in the history. While writing the code, ensure that it adheres to the PEP8 style guide, especially the rule about maximum line length. Break down long lines of code, including comments and docstrings, into multiple lines to improve readability and maintainability. Use a linter or code formatter to automatically check and correct your code style. Also, manually check your code against the PEP8 style guide before submitting it. In addition, when revising your code based on feedback, make sure to address all the points raised by your teammates, especially those related to code style and organization.

- Table 2: We list optimized system prompts for the solver agent whose role is described as a programmer along functionality, robustness, and code violation evaluation dimensions. Green text indicates agent prompts are being optimized under the evaluation dimension.


### 6 Conclusion

In this work, we present a case study on group behavior optimization with multiple LLMbased agents utilizing natural language feedback on software development. We first propose a two-step optimization framework to effectively optimize a role-based multi-agent system under various user-defined evaluation dimensions. We then investigate the impacts of various optimization settings and provide valuable insights regarding group optimization behaviors under those settings.

### References

Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David, Chelsea Finn, Keerthana Gopalakrishnan, Karol Hausman, Alexander Herzog, Daniel Ho, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Eric Jang, Rosario M Jauregui Ruano, Kyle Jeffrey, Sally Jesmonth, Nikhil Jayant Joshi, Ryan C. Julian, Dmitry Kalashnikov, Yuheng Kuang, Kuang-Huei Lee, Sergey Levine, Yao Lu, Linda Luu, Carolina Parada,

Peter Pastor, Jornell Quiambao, Kanishka Rao, Jarek Rettinghouse, Diego M Reyes, Pierre Sermanet, Nicolas Sievers, Clayton Tan, Alexander Toshev, Vincent Vanhoucke, F. Xia, Ted Xiao, Peng Xu, Sichun Xu, and Mengyuan Yan. Do as i can, not as i say: Grounding language in robotic affordances. In Conference on Robot Learning, 2022. URL https:

//api.semanticscholar.org/CorpusID:247939706.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Advances in Neural Information Processing Systems, volume 33, pp. 1877–1901. Curran Associates, Inc., 2020. URL https://proceedings.neurips.cc/paper_files/paper/2020/ file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.

Tianle Cai, Xuezhi Wang, Tengyu Ma, Xinyun Chen, and Denny Zhou. Large language models as tool makers. ArXiv, abs/2305.17126, 2023. URL https://api.semanticscholar. org/CorpusID:258947222.

Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan Liu. Chateval: Towards better LLM-based evaluators through multi-agent debate. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=FQepisCUWu.

Harrison Chase. LangChain, 2022. URL https://github.com/langchain-ai/langchain.

Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pondé, Jared Kaplan, Harrison Edwards, Yura Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, David W. Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William H. Guss, Alex Nichol, Igor Babuschkin, Suchir Balaji, Shantanu Jain, Andrew Carr, Jan Leike, Joshua Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew M. Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code. ArXiv, abs/2107.03374, 2021. URL https://api.semanticscholar.org/ CorpusID:235755472.

Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie Zhou. Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=EHg5GDnyq1.

Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yihan Wang, Han Guo, Tianmin Shu, Meng Song, Eric Xing, and Zhiting Hu. RLPrompt: Optimizing discrete text prompts with reinforcement learning. In Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (eds.), Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pp. 3369–3391, Abu Dhabi, United Arab Emirates, December 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.emnlp-main.222. URL https://aclanthology.org/2022.emnlp-main.222.

Yihong Dong, Xue Jiang, Zhi Jin, and Ge Li. Self-collaboration code generation via chatgpt. ACM Trans. Softw. Eng. Methodol., jun 2024. ISSN 1049-331X. doi: 10.1145/3672459. URL https://doi.org/10.1145/3672459. Just Accepted.

Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. Improving factuality and reasoning in language models through multiagent debate, 2024. URL https://openreview.net/forum?id=QAwaaLJNCk.

Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy Liang, and Tatsunori Hashimoto. Alpacafarm: A simulation framework for methods that learn from human feedback. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. URL https://openreview.net/forum?id=4hturzLcKX.

Tianyu Gao, Adam Fisch, and Danqi Chen. Making pre-trained language models better few-shot learners. In Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (eds.), Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 3816–3830, Online, August 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.acl-long.295. URL https://aclanthology.org/2021.acl-long.295.

Yubin Ge, Ziang Xiao, Jana Diesner, Heng Ji, Karrie Karahalios, and Hari Sundaram. What should I ask: A knowledge-driven approach for follow-up questions generation in conversational surveys. In Chu-Ren Huang, Yasunari Harada, Jong-Bok Kim, Si Chen, Yu-Yin Hsu, Emmanuele Chersoni, Pranav A, Winnie Huiheng Zeng, Bo Peng, Yuxi Li, and Junlin Li (eds.), Proceedings of the 37th Pacific Asia Conference on Language, Information and Computation, pp. 113–124, Hong Kong, China, December 2023. Association for Computational Linguistics.

Yubin Ge, Salvatore Romeo, Jason Cai, Raphael Shu, Yassine Benajiba, Monica Sunkara, and Yi Zhang. TReMu: Towards neuro-symbolic temporal reasoning for LLM-agents with memory in multi-session dialogues. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (eds.), Findings of the Association for Computational Linguistics: ACL 2025, Vienna, Austria, July 2025. Association for Computational Linguistics.

Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao Song, Xu Tan, Guoqing Liu, Jiang Bian, and Yujiu Yang. Connecting large language models with evolutionary algorithms yields powerful prompt optimizers. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=ZG3RaNIsO8.

Rui Hao, Linmei Hu, Weijian Qi, Qingliu Wu, Yirui Zhang, and Liqiang Nie. Chatllm network: More brains, more intelligence. ArXiv, abs/2304.12998, 2023. URL https: //api.semanticscholar.org/CorpusID:258309449.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. In International Conference on Learning Representations, 2021a. URL https://openreview.net/forum?id= d7KBjmI3GmQ.

Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2), 2021b. URL https://openreview.net/forum?id=7Bywt2mQsCe.

Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. MetaGPT: Meta programming for a multi-agent collaborative framework. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=VtmBAGCN7o.

Dongfu Jiang, Xiang Ren, and Bill Yuchen Lin. LLM-blender: Ensembling large language models with pairwise ranking and generative fusion. In Anna Rogers, Jordan BoydGraber, and Naoaki Okazaki (eds.), Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 14165–14178, Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.acl-long.792. URL https://aclanthology.org/2023.acl-long.792.

Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan A, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, and Christopher Potts. DSPy: Compiling declarative

language model calls into state-of-the-art pipelines. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=sY5N0zY5Od.

Sergey Levine, Aviral Kumar, G. Tucker, and Justin Fu. Offline reinforcement learning: Tutorial, review, and perspectives on open problems. ArXiv, abs/2005.01643, 2020. URL https://api.semanticscholar.org/CorpusID:218486979.

Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. CAMEL: Communicative agents for ”mind” exploration of large language model society. In Thirty-seventh Conference on Neural Information Processing Systems, 2023a. URL https://openreview.net/forum?id=3IyL2XWDkG.

Moxin Li, Wenjie Wang, Fuli Feng, Yixin Cao, Jizhi Zhang, and Tat-Seng Chua. Robust prompt optimization for large language models against distribution shifts. In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 1539–1554, Singapore, December 2023b. Association for Computational Linguistics. doi: 10.18653/v1/2023.emnlp-main.95. URL https://aclanthology.org/2023.emnlp-main.95.

Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and Shuming Shi. Encouraging divergent thinking in large language models through multi-agent debate. ArXiv, abs/2305.19118, 2023. URL https://api. semanticscholar.org/CorpusID:258967540.

Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Comput. Surv., 55(9), jan 2023. ISSN 0360-0300. doi: 10.1145/ 3560815. URL https://doi.org/10.1145/3560815.

Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi Yang. A dynamic LLM-powered agent network for task-oriented agent collaboration. In First Conference on Language Modeling,

2024. URL https://openreview.net/forum?id=XII0Wp1XA9.

Ruotian Ma, Xiaolei Wang, Xin Zhou, Jian Li, Nan Du, Tao Gui, Qi Zhang, and Xuanjing Huang. Are large language models good prompt optimizers? ArXiv, abs/2402.02101,

2024. URL https://api.semanticscholar.org/CorpusID:267413214.

Nat McAleese, Rai Michael Pokorny, Juan Felipe Cer’on Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. ArXiv, abs/2407.00215, 2024. URL https://api.semanticscholar.org/CorpusID:270844127.

OpenAI. Gpt-4 technical report. 2023. URL https://api.semanticscholar.org/CorpusID: 257532815.

Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, 2023. URL https://api.semanticscholar.org/CorpusID:258040990.

Archiki Prasad, Peter Hase, Xiang Zhou, and Mohit Bansal. GrIPS: Gradient-free, editbased instruction search for prompting large language models. In Andreas Vlachos and Isabelle Augenstein (eds.), Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics, pp. 3845–3864, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.eacl-main.277. URL https://aclanthology.org/2023.eacl-main.277.

Reid Pryzant, Dan Iter, Jerry Li, Yin Lee, Chenguang Zhu, and Michael Zeng. Automatic prompt optimization with “gradient descent” and beam search. In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 7957–7968, Singapore, December 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.emnlp-main.494. URL https:

- //aclanthology.org/2023.emnlp-main.494.


Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. ChatDev: Communicative agents for software development. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 15174–15186, Bangkok, Thailand, August 2024. Association for Computational Linguistics. URL https:

- //aclanthology.org/2024.acl-long.810.


Laria Reynolds and Kyle McDonell. Prompt programming for large language models: Beyond the few-shot paradigm. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems, CHI EA ’21, New York, NY, USA, 2021. Association for Computing Machinery. ISBN 9781450380959. doi: 10.1145/3411763.3451760. URL https://doi.org/10.1145/3411763.3451760.

Toran Bruce Richards. AutoGPT, 2023. URL https://github.com/Significant-Gravitas/ AutoGPT.

Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric Wallace, and Sameer Singh. AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts. In Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu (eds.), Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 4222–4235, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.346. URL https://aclanthology.org/2020.emnlp-main.

346.

Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik R Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. URL https://openreview.net/ forum?id=vAElhFcKW6.

Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan Lee BoydGraber, and Lijuan Wang. Prompting GPT-3 to be reliable. In The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/forum?id= 98p5x51L5af.

Hong Sun, Xue Li, Yi Xu, Youkow Homma, Qinhao Cao, Min man Wu, Jian Jiao, and Denis Xavier Charles. Autohint: Automatic prompt optimization with hint generation. ArXiv, abs/2307.07415, 2023. URL https://api.semanticscholar.org/CorpusID:259924936.

Wei Tao, Yucheng Zhou, Wenqiang Zhang, and Yu-Xi Cheng. Magis: Llm-based multiagent framework for github issue resolution. ArXiv, abs/2403.17927, 2024. URL https: //api.semanticscholar.org/CorpusID:268691664.

Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric Xing, and Zhiting Hu. Promptagent: Strategic planning with language models enables expert-level prompt optimization. In The Twelfth International Conference on Learning Representations, 2024a. URL https://openreview.net/forum?id=22pyNMuIoa.

Zhenhailong Wang, Shaoguang Mao, Wenshan Wu, Tao Ge, Furu Wei, and Heng Ji. Unleashing the emergent cognitive synergy in large language models: A task-solving agent through multi-persona self-collaboration. In Kevin Duh, Helena Gomez, and Steven Bethard (eds.), Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 257–279, Mexico City, Mexico, June 2024b. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.15. URL https://aclanthology.org/2024.naacl-long.15.

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed H. Chi, Quoc V Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), Advances in Neural Information Processing Systems, 2022. URL https://openreview.

net/forum?id=_VjQlMeSB_J.

Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W White, Doug Burger, and Chi Wang. Autogen: Enabling next-gen LLM applications via multiagent conversation. In ICLR 2024 Workshop on Large Language Model (LLM) Agents, 2024a. URL https://openreview.net/forum?id=uAjxFFing2.

Yiran Wu, Feiran Jia, Shaokun Zhang, Hangyu Li, Erkang Zhu, Yue Wang, Yin Tat Lee, Richard Peng, Qingyun Wu, and Chi Wang. Mathchat: Converse to tackle challenging math problems with LLM agents. In ICLR 2024 Workshop on Large Language Model (LLM) Agents, 2024b. URL https://openreview.net/forum?id=S7vIB7OGQe.

Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun Chen. Large language models as optimizers. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=Bb4VGOWELI.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/ forum?id=WE_vluYUL-X.

Qinyuan Ye, Mohamed Ahmed, Reid Pryzant, and Fereshte Khani. Prompt engineering a prompt engineer. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Findings of the Association for Computational Linguistics ACL 2024, pp. 355–385, Bangkok, Thailand and virtual meeting, August 2024. Association for Computational Linguistics. URL https://aclanthology.org/2024.findings-acl.21.

Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, and James Zou. Textgrad: Automatic "differentiation" via text. ArXiv, abs/2406.07496,

2024. URL https://api.semanticscholar.org/CorpusID:270380429.

Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong Zhou, Yilun Du, Joshua B. Tenenbaum, Tianmin Shu, and Chuang Gan. Building cooperative embodied agents modularly with large language models. In The Twelfth International Conference on Learning Representations, 2024a. URL https://openreview.net/forum?id=EnXJfQqy0K.

Yao Zhang, Zijian Ma, Yunpu Ma, Zhen Han, Yu Wu, and Volker Tresp. Webpilot: A versatile and autonomous multi-agent system for web task execution with strategic exploration. ArXiv, abs/2408.15978, 2024b. URL https://api.semanticscholar.org/ CorpusID:271974824.

Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging LLM-as-a-judge with MT-bench and chatbot arena. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2023. URL https://openreview.net/forum?id=uccHPGDlao.

Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba. Large language models are human-level prompt engineers. In The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/ forum?id=92gvk82DE-.

Mingchen Zhuge, Haozhe Liu, Francesco Faccio, Dylan R. Ashley, Róbert Csordás, Anand Gopalakrishnan, Abdullah Hamdi, Hasan Abed Al Kader Hammoud, Vincent Herrmann, Kazuki Irie, Louis Kirsch, Bing Li, Guohao Li, Shuming Liu, Jinjie Mai, Piotr Pi˛ekos, Aditya Ramesh, Imanol Schlag, Weimin Shi, Aleksandar Stanic´, Wenyi Wang, Yuhui Wang, Mengmeng Xu, Deng-Ping Fan, Bernard Ghanem, and Jürgen Schmidhuber. Mindstorms in natural language-based societies of mind. In R0-FoMo:Robustness of Few-shot and Zeroshot Learning in Large Foundation Models, 2023. URL https://openreview.net/forum?id= zd2qE6BBdU.

Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jürgen Schmidhuber. GPTSwarm: Language agents as optimizable graphs. In Forty-first

System Prompt: You are ${role description}. You are in a multi-agent collaboration environment.

You are given a software development task description: ${task description}

You will also be given the chat history of you and other teammates (history could be empty).

<TO IMPROVE> Your task is to provide a new solution code to the given software task. If the history is not empty, your new solution code must be based on your previous solution and teammates’ feedback in the history. </TO IMPROVE>

User Prompt: Start your response now and write your code step by step in ```python markdown quotes.

- Figure 5: System and user prompt for solver agent whose responsibility is to write the main solution code given a software task description.


International Conference on Machine Learning, 2024. URL https://openreview.net/forum? id=uTC9AFXIhg.

### A Role-based Multi-Agent System

Various decision-making structures among agents Chan et al. (2024); Wu et al. (2024a) have been investigated. Following AgentVerseChen et al. (2024), we adopt the vertical decisionmaking structure as it is a better fit for software development. Inside the vertical structure, given the software task description X, a solver agent S proposes a solution Yt at iteration t. Other agents, as reviewer agents R, provide feedback F = {rti = Ri(Yt)∣Ri ∈ R} regarding solution Yt to the solver agent. Finally, the solver agent refines its solution based on the feedback Yt+1 = S(X,Yt,F). Such a review iteration can go on for a few rounds. In the current case study, we use a total of 2 reviewer agents and a single review iteration. To determine the concrete role descriptions for solver and reviewer agents, we utilize a recruiter agent A to select role descriptions for the solver and reviewer agents from a pre-defined expert pool based on the current task description. The agent role description pool we use is adapted from ChatDev Qian et al. (2024). In our study, we aim to optimize the system prompts of all agents in the vertical decision-making structure.

The concrete prompt for the solver agent is shown in Figure 5, and the prompt for reviewer agents is shown in Figure 6. The system prompts we aim to optimize are shown in red, and we wrap them with <TO IMPROVE> tags to instruct LLM to optimize only text between the tags so that other text is untouched. For the recruiting stage, the role description pool we use is directly presented in the prompt for the recruiter agent, as shown in Figure 8. Note that we restrict the solver agent specifically associated with the role of "Programmer who can write/create computer software or applications with extensive computing and coding experience ..." since this is the only appropriate role for writing solution code.

### B Prompt for Model-Based Evaluation

We show the evaluation prompts for generating scalar scores and feedback for functionality, robustness, and test case coverage dimensions in Figure 9, and for generating feedback for documentation dimension in Figure 10. Critical components in the evaluation prompt include the evaluation dimension’s name and definition, software task description, and

#### System Prompt:

You are ${role description}. You are in a multi-agent collaboration environment aiming to solve a given software development task: ${task description}.

You are also given the chat history of you and other teammates below.

<TO IMPROVE> Based only on your expertise, please provide your feedback on the most recent solution code to the software task given. Ensure your feedback is specific and detailed enough instead of just general opinions. </TO IMPROVE>

User Prompt: Start your response now.

- Figure 6: System and user prompt for reviewer agent whose responsibility is to review the solution code written by solver agent and provide feedback to solver agent given a software task description.


Dimension Name Dimension Definition

Functionality Is the code able to achieve all the goals specified in the task description?

Robustness Is the code snippet able to handle different unexpected inputs or other exceptions? Test Case Coverage Does the solution contain test cases to cover all the software solution code?

Documentation Does the solution code contain enough comments or docstrings to explain itself? Code Style Violation Does the solution code follow code style conventions defined in PEP 8?

Table 3: concrete definitions of all evaluation dimensions we study in our work.

software solution code. We list concrete definitions of all evaluation dimensions we study in Table 3.

### C Are More Optimization Steps Needed?

We investigate whether more steps of optimization are beneficial compared with the current default steps of 5. We choose functionality and code style violation dimensions under the online group optimization with one-pass prompting setting and optimize for 10 steps. We plot the optimization curve on training and development set in Figure 7. We observe that for both dimensions, the training and development optimization curves tend towards either a stable or declining trend. This shows more steps of optimization are not necessary in our case study.

Functionality (↑)

| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |train dev| |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |


EvaluationScores

- 6

- 6.5
- 7

7.5

8

- 8.5




0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%

Violation (↓)

12

| | | | | | | | | |train| |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |
| | | | | | | | | |dev| |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |


10

EvaluationScores

8

6

4

2

0

0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%

- Figure 7: Curve analysis for doubling the training steps for functionality and code style violation evaluation dimensions under online group with one-pass promoting optimization.


###### Functionality

As a Software Test Engineer, your task is to provide detailed and specific feedback on the most recent solution code to the software task given. Your feedback should focus on the functionality, security, and versatility of the software. Test the software with different sports, player positions, and strategies, and with different user inputs. Also, test the user interface to ensure it is user-friendly and intuitive. Your feedback will guide the programmer in improving the solution and ensuring it meets the requirements of a wide range of users. Additionally, ensure your testing procedures cover all aspects of the task description and user experience, and provide more detailed feedback on any missing functionalities or areas for improvement After providing feedback, ensure that the programmer has understood and incorporated your suggestions into the final solution.

###### Robustness

As a Software Test Engineer, your task is to provide detailed and specific feedback on the most recent solution code to the software task given. Your feedback should focus on potential areas of robustness that may have been overlooked, such as error handling, input validation, and handling of unexpected exceptions. Also, consider the lifecycle of any temporary files created during the process and ensure they are properly managed to prevent unnecessary storage usage. Your feedback should help to ensure that the final solution is as robust and reliable as possible. You should have a deeper understanding of the code and the potential edge cases and error scenarios, and provide more detailed and specific feedback to the programmer agent. Furthermore, consider the integrity and validity of the data being processed, and suggest improvements to the data handling processes, including checks for invalid or duplicate inputs, and robust handling of data storage and retrieval.

###### Violation

As a Software Test Engineer, your role is to provide specific and detailed feedback on the most recent solution code to the software task given. While focusing on the functionality and robustness of the software, also consider the readability and maintainability of the code. Review the code for adherence to style guides like PEP8, including line length, and provide feedback on this aspect. If you notice any violations, point them out and suggest possible corrections. Also, consider the feedback from other teammates and reinforce any important points they might have raised.

Table 4: We list optimized system prompts for the reviewer agent whose role is described as a software test engineer along functionality, robustness, and code violation evaluation dimensions. Green text indicates agent prompts are being optimized under the evaluation dimension.

System Prompt: User Prompt: You are faced with a software engineer task: ${task description}

You are also given a pool of experts: [Experts pool]

- 1. Chief executive officer whose main responsibilities include being an active decision-maker on users’ demands and other key policy issues, leader, manager, and executor.
- 2. Chief product officer who is responsible for all product-related matters, including product design, product strategy, product vision, product innovation, project management, and product marketing.
- 3. Counselor whose main responsibilities include asking what users and customers think and providing valuable suggestions.
- 4. Chief technology officer who is very familiar with information technology and will make high-level decisions for the overarching technology infrastructure that closely aligns with the organization’s goals.
- 5. Chief human resource officer who oversees all aspects of human resource management and industrial relations policies, practices and operations for an organization.
- 6. Programmer who can write/create computer software or applications with extensive computing and coding experience in many varieties of programming languages and platforms, such as Python, Java, C, C++, HTML, CSS, JavaScript, XML, SQL, PHP, etc.
- 7. Code reviewer who can help programmers assess source codes for software troubleshooting, fix bugs to increase code quality and robustness, and offer proposals to improve the source codes.
- 8. Software test engineer who can use the software as intended to analyze its functional properties, design manual and automated test procedures to evaluate each software product, build and implement software evaluation test programs, and run test programs to ensure that testing protocols evaluate the software correctly.
- 9. Chief creative officer who directs the company’s creative software and develops the artistic design strategy that defines the company’s brand. [/Experts pool]


You need to recruit a total of ${number of agents} experts from the above expert pool to collaboratively solve the given task. The first expert member you recruit must always be the programmer (index 6) since the programmer is responsible for developing the software code. The remaining expert members are responsible for providing feedback on the software code developed by the programmer. You can only select each expert once.

Please use a comma to separate selected expert member indices without space. Always put the programmer at the beginning. Don’t provide any reason for your selection. For example, if you recruit programmer, chief technology officer, and chief creative officer, you should output: 6,4,9

- Figure 8: System and user prompt we use for the role selection agent for selecting concrete roles for solver and reviewer agents.


System Prompt: You are a professional and strict code reviewer.

User Prompt: You will evaluate the solution code to a software engineer task from the following dimensions:

${dimension name}: ${dimension definition} The task description is: ${task description} The solution code is: [Solution code] ${solution code} [/Solution code] Now, you need to give a rating from 0 to 10 with detailed reasons for your rating regarding the evaluation dimensions. You must only output one line which contains the score and detailed reasons why you gave this score. You must put detailed reasons inside <Reasons> tag. The exact output format you need to follow is shown below:

1. ${dimension}: a score (from 0 to 10) + <Reasons> detailed reasons </Reasons> Make sure your score and explanations of the score are only based on the evaluation dimension, not anything else. Also, make sure that you only give a high score when the solution code is really good at satisfying the definition of the evaluation dimension.

- Figure 9: Evaluation system and user prompt for generating utility scores and textual feedback for functionality, robustness, and test case coverage dimensions.


System Prompt: You are a professional and strict code reviewer.

User Prompt: You will evaluate the solution code to a software engineer task from the following criterion:

A good solution code always comes with abundant comments and docstrings to explain the purpose and functionality of each class, method, and function.

The task description is: ${task description}

The solution code is: [Solution code] ${solution code} [/Solution code]

You must use detailed natural language to describe how the solution code performs in terms of the above evaluation criterion. Make sure your evaluation is only related to the above evaluation criterion, nothing else.

- Figure 10: Evaluation system and user prompt for generating textual feedback for documentation dimension.


System Prompt: You are a professional error agent locator who can accurately identify agents not functioning well in a multi-agent collaboration system.

###### User Prompt:

You are given a software engineer task description, a group of agents that collaboratively solve this task with their communication trajectory, and accurate external feedback to the **final** solution code regarding some evaluation dimensions:

[Task description] ${task description} [/Task description]

[Agents with their role descriptions]

- Agent 1: ${agent 1 role description}
- Agent 2: ${agent 2 role description}
- Agent 3: ${agent 3 role description}


... ${high-level responsibilities of each agents} [/Agents with their role descriptions]

[Agents communication trajectory] ${communication trajectory} [/Agents communication trajectory]

[Feedback to final solution code] ${evaluation score with feedback} [/Feedback to final solution code]

You can assume all agents can possibly make mistakes when writing solution code or providing feedback to code, but the external feedback to the final solution is objective and robust.

If the above external feedback to the final solution code contains negative feedback, please identify all agent(s) causing the negative feedback and provide detailed explanations of why each identified agent leads to the negative feedback. Explanations must satisfy the following criteria:

- - If the identified agent improves itself based on the explanations, the negative feedback can be somehow mitigated, thus increasing the evaluation dimension score according to the definition of the evaluation dimension.
- - Make sure the explanations are specific and detailed instead of just general explanations.
- - Do not simply use ’agent 1’ or ’agent 2’ to describe agents in the explanations; instead, use their role descriptions, such as programmer and chief product officer, to describe.
- - Explanations should be based on what already happened in the trajectory instead of asking for more interactions between agents in the future.


First, output the identified agent index, then provide detailed explanations. For example, if two agents, the programmer agent (Agent 1) and the code reviewer agent (Agent 3), are identified, the output must be two lines following the format below:

- 1. Agent 1: detailed explanations of why programmer leads to negative feedback
- 2. Agent 3: detailed explanations of why code reviewer leads to negative feedback


If the feedback is completely positive, you can return a string of "None", meaning no agent is making mistakes.

Figure 11: System and user prompt for the locator.

System Prompt: You are a professional system prompt optimizer for large language model agents. Don’t be afraid to be creative.

User Prompt: Below are the input system message, input user messages, and output of a large language model agent:

[Agent system message] ${agent system prompt} [/Agent system message]

[Agent user messages] ${agent user prompts} [/Agent user messages]

[Agent output] ${agent output} [/Agent output]

Below is the feedback for the above large language model agent activity trajectory:

[Fine-grained feedback] ${agent fine-grained feedback} [/Fine-grained feedback]

Based on the above feedback for this large language model agent, please ONLY update the system prompt wrapped between the <TO IMPROVE> tag in the agent system message so that the agent can improve based on the feedback.

You need to carefully think about what is useful in the feedback for you to optimize the agent system prompt and make sure that this optimization not only benefits the current software development task but can also generally benefit other software development tasks in the future. You must keep the new prompt clear, concise, informative, and descriptive. Also, make sure not to change the agent’s original goal.

Since your output will directly replace the text wrapped between the <TO IMPROVE> tag in the system prompt, make sure you ONLY output the improved prompt. DO NOT output anything else, such as the <TO IMPROVE> tag.

Figure 12: System and user prompt for the optimizer.

