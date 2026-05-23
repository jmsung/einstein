---
type: source
kind: paper
title: "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning"
authors: Peng Xia, Jianwen Chen, Han Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, Huaxiu Yao
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2602.08234
source_local: ../raw/2026-xia-skillrl-evolving-agents-recursive.pdf
topic: general-knowledge
cites:
---

# arXiv:2602.08234v1[cs.LG]9Feb2026

## SKILLRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

Peng Xia1* Jianwen Chen1* Hanyang Wang12* Jiaqi Liu1 Kaide Zeng1 Yu Wang3 Siwei Han1 Yiyang Zhou1 Xujiang Zhao4 Haifeng Chen4 Zeyu Zheng5 Cihang Xie6 Huaxiu Yao1

![image 1](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile1.png>)

### Abstract

![image 2](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile2.png>)

![image 3](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile3.png>)

![image 4](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile4.png>)

Large Language Model (LLM) agents have shown stunning results in complex tasks, yet they often operate in isolation, failing to learn from past experiences. Existing memory-based methods primarily store raw trajectories, which are often redundant and noise-heavy. This prevents agents from extracting high-level, reusable behavioral patterns that are essential for generalization. In this paper, we propose SKILLRL, a framework that bridges the gap between raw experience and policy improvement through automatic skill discovery and recursive evolution. Our approach introduces an experience-based distillation mechanism to build a hierarchical skill library SKILLBANK, an adaptive retrieval strategy for general and task-specific heuristics, and a recursive evolution mechanism that allows the skill library to co-evolve with the agent’s policy during reinforcement learning. These innovations significantly reduce the token footprint while enhancing reasoning utility. Experimental results on ALFWorld, WebShop and seven search-augmented tasks demonstrate that SKILLRL achieves stateof-the-art performance, outperforming strong baselines over 15.3% and maintaining robustness as task complexity increases. Code is available at this https://github.com/aiming-lab/SkillRL.

Base Model

![image 5](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile5.png>)

![image 6](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile6.png>)

Environment

![image 7](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile7.png>)

- (a)

![image 8](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile8.png>)

![image 9](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile9.png>)

Trajectory

![image 10](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile10.png>)

![image 11](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile11.png>)

![image 12](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile12.png>)

![image 13](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile13.png>)

Expert

![image 14](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile14.png>)

Discard

Memory Skills

![image 15](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile15.png>)

Evolve

- (b)


![image 16](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile16.png>)

![image 17](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile17.png>)

Higher Performance Faster Convergence

![image 18](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile18.png>)

![image 19](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile19.png>)

![image 20](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile20.png>)

![image 21](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile21.png>)

Figure 1. (a) Overview of the SKILLRL pipeline. Unlike previous methods (gray dashed lines) that store raw trajectories and discard failures, SKILLRL employs an experience-based distillation mechanism to transform diverse experiences into structured skills. (b) Performance on ALFWorld validation set (Shridhar et al.). SKILLRL achieves faster convergence and superior success rates compared to vanilla GRPO and memory-augmented RL.

by interacting with complex environments through natural language. Despite these advances, each task execution remains largely episodic. Current LLM agents operate in isolation, unable to learn from past successes or failures (Zhang et al., 2025b), which significantly hinders their evolution. Consequently, a fundamental challenge remains: how can agents efficiently learn from experience and transfer that knowledge to other tasks?

The existing memory-based methods for LLM agents primarily involve saving raw trajectories directly into external databases during the sampling process to serve as references for similar future tasks (Shinn et al., 2023; Zhao et al., 2024). While intuitive, these raw trajectories are often lengthy and contain significant redundancy and noise (Chhikara et al., 2025), making it difficult for the model to extract critical information. Recent work has attempted to compress trajectories and update the memory bank via online training (Zhang et al., 2025b; 2026), improving memory efficiency. However, these methods merely mimic past solutions and they fail to distill core principles or adapt the agent’s internal policy to leverage memory for guided decision-making. As depicted in the dashed flow of Figure 1(a), such approaches often struggle with the trade-off between information den-

### 1. Introduction

Large language model (LLM) agents (Yao et al., 2022b; Shinn et al., 2023) have demonstrated remarkable capabilities across various sophisticated tasks, such as web navigation (Google, 2025; OpenAI, 2025c) and deep research (OpenAI, 2025b; Google, 2024; Team et al., 2025),

1UNC-Chapel Hill 2University of Chicago 3University of California San Diego 4NEC Labs America 5University of California Berkeley 6University of California Santa Cruz. Correspondence to: Peng Xia <pxia@cs.unc.edu>, Huaxiu Yao <huaxiu@cs.unc.edu>.

Preprint. February 10, 2026.

sity and noise, leading to sub-optimal performance or even degradation as shown in Figure 1(b).

We argue that these approaches miss a crucial insight: effective experience transfer requires abstraction. Human experts do not memorize every action in every situation; instead, they develop skills (Anthropic, 2024), compact and reusable strategies that capture the essence of how to accomplish specific subtasks. Inspired by this observation, we propose SKILLRL, a framework that bridges the gap between raw experience and efficient policy improvement through automatic skill discovery and recursive skill evolution.

SKILLRL first introduces an experience-based skill distillation mechanism, which gathers diverse trajectories from environment rollouts and applies differential processing: successful episodes are preserved as demonstrations, while failed ones are synthesized into concise failure lessons to mitigate context noise. Secondly, we transform these experiences into a hierarchical skill library SKILLBANK, differentiating between general skills for universal strategic guidance and task-specific skills for task-level heuristics. This abstraction allows the agent to adaptively retrieve relevant skills during decision-making, significantly reducing the token footprint while enhancing reasoning utility. Lastly, SKILLRL incorporates a recursive skill evolution mechanism during reinforcement learning (RL), where the skill library is treated as a dynamic component rather than a static knowledge source. By analyzing failure modes after each validation epoch to generate new skills or refine existing ones, our approach ensures the skill library and the agent’s policy co-evolve, maintaining robustness as task complexity increases. As demonstrated in Figure 1(b), SKILLRL achieves substantially faster convergence and higher asymptotic performance.

The primary contribution is SKILLRL, a framework that enables LLM agents to bridge the gap between raw experience and policy improvement through automatic skill discovery and recursive evolution. By distilling redundant trajectories into a hierarchical SKILLBANK, our method abstracts general and task-specific skills to guide decision-making efficiently. Furthermore, we introduce a recursive evolution mechanism that ensures the skill library and agent policy coevolve during reinforcement learning. Empirical results on ALFWorld, WebShop, and seven search-augmented benchmarks demonstrate that SKILLRL achieves state-of-the-art performance with 15.3% improvements, significantly outperforming current memory-based agent-tuning baselines in both task success and reasoning utility.

### 2. Preliminaries

LLM Agents. We consider an agent operating in an interactive environment E. At each timestep t, the agent observes

a state ot ∈ O, selects an action at ∈ A, and receives a reward rt and next observation ot+1. A trajectory τ = (o0,a0,r0,...,oT,aT,rT) captures one episode of interaction. Tasks are specified by natural language descriptions d. An LLM-based agent parameterized by θ implements a policy πθ(at|o≤t,d,c) where c represents additional context (e.g., skills, demonstrations). Our goal is to learn a policy that maximizes expected return maxθ Eτ∼π

T t=0 γtrt

θ

subject to context length constraints |c| ≤ Lmax.

Group Relative Policy Optimization (GRPO). GRPO (Shao et al., 2024) is a reinforcement learning method that avoids training a critic by using intra-group relative rewards to optimize the policy. For each query x, the model samples G responses {y(1),...,y(G)}, which are scored to obtain rewards {R1,...,RG}. GRPO computes normalized advantages and updates the policy with a PPO-style clipped objective (Schulman et al., 2017):

JGRPO(θ) = Ex,{yi}

G

1 G

min riAi,

i=1

clip(ri, 1 − ϵ, 1 + ϵ)Ai − βDKL(πθ∥πref) ,

(1)

where ri = ππθ(yi|x)

old(yi|x) is the importance ratio, Ai =

Ri−mean({Rj}Gj=1)

std({Rj}Gj=1) is the normalized advantage, ϵ, β are hyperparameters, and πold is the policy before the current update.

### 3. SKILLRL

In this section, as illustrated in Figure 2, we propose SKILLRL, a framework designed to bridge the gap between raw interaction experience and policy improvement through automatic skill discovery and recursive evolution. SKILLRL consists of three core components. First, we develop an experience-based skill distillation mechanism to transform redundant trajectories into concise, actionable knowledge. Second, we organize these distilled experiences into a hierarchical skill library S, enabling efficient retrieval of general and task-specific expertise. Lastly, we introduce a recursive skill evolution mechanism that leverages RL to dynamically refine the skill library in tandem with the agent’s policy. We detail these components as follows:

#### 3.1. Experience-based Skill Distillation

Raw trajectories τ collected from environment interactions are verbose, containing exploratory actions, backtracking, and redundant steps that obscure the critical decisions leading to success or failure. To transform these experiences into actionable knowledge, we employ a teacher model MT to distill trajectories into compact, reusable skills.

Specifically, we first deploy a base LLM agent πbase in the

![image 22](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile22.png>)

![image 23](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile23.png>)

###### SKILLRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

![image 24](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile24.png>)

![image 25](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile25.png>)

Successful Episodes

a1 a2 ⋯ an

![image 26](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile26.png>)

![image 27](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile27.png>)

Lessons from Failure

Base Model Environment Trajectory

Memory

![image 28](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile28.png>)

![image 29](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile29.png>)

![image 30](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile30.png>)

![image 31](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile31.png>)

![image 32](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile32.png>)

Take what you see

![image 33](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile33.png>)

Skills

Cold Start

![image 34](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile34.png>)

Prioritize exploring unvisited nodes

![image 35](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile35.png>)

![image 36](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile36.png>)

General Skills

For cleaning tasks, follow this process: Locate -> Obtain -> Clean the pool -> Place this item

Evolved Model Environment

SFT Model Task-Specific Skills

![image 37](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile37.png>)

![image 38](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile38.png>)

![image 39](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile39.png>)

![image 40](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile40.png>)

Update SkillBank Create New or Refine

![image 41](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile41.png>)

![image 42](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile42.png>)

Figure 2. Overview of the SKILLRL framework. We collect trajectories using a base model, distill them into a hierarchical skill library, perform cold-start SFT to enable skill utilization, and then conduct RL training with dynamic skill evolution based on validation failures.

target environment E to collect diverse trajectories. Unlike prior approaches that retain only successful episodes, we deliberately preserve both successful trajectories T + = {τi : r(τi) = 1} and failed trajectories T − = {τi : r(τi) = 0}, where r(τ) denotes the binary task success indicator. Failed trajectories reveal failure modes and boundary conditions, i.e., information difficult to infer from successes alone.

ciples applicable across all task types within an environment. These typically include exploration strategies (e.g., systematic search patterns, prioritizing unvisited locations), state management principles (e.g., verifying preconditions before actions), and goal-tracking heuristics (e.g., maintaining progress counters, terminating only upon verified completion). General skills provide foundational guidance that transfers across different task categories. 2) Task-Specific Skills Sk encode specialized knowledge for task category k. These capture domain-specific action sequences, taskparticular preconditions and constraints, common failure modes unique to the task type, and optimized procedures that exploit task structure. By organizing trajectories by task type during collection, we enable extraction of fine-grained, category-specific strategies that complement the broader general skills.

We apply differential processing based on trajectory outcomes. For successful trajectories τ+ ∈ T +, we extract the strategic patterns that led to task completion:

s+ = MT(τ+, d). (2)

The teacher model identifies critical decision points, the reasoning behind correct actions, and generalizable patterns that transfer beyond the specific task instance.

For failed trajectories τ− ∈ T −, direct inclusion in context is infeasible due to their length and noise. Instead, we synthesize concise failure lessons:

The complete skill library SKILLBANK is Sg ∪ Kk=1 Sk. Each skill s ∈ SKILLBANK is structured with: a concise

name (e.g., systematic exploration), a principle describing the strategy, and when to apply conditions specifying applicability. This format enables efficient retrieval while providing clear guidance for application.

s− = MT(τ−,d). (3) The analysis identifies: (1) the point of failure, (2) the flawed reasoning or action, (3) what should have been done, and (4) general principles to prevent similar failures. This transforms verbose failed episodes into counterfactuals.

Skill Retrieval. At inference, given a task description d, the agent retrieves relevant skills to augment its context. General skills Sg are always included as foundational guidance. Task-specific skills are retrieved via semantic similarity:

- 3.2. Hierarchical Skill Library (SKILLBANK) Construction


Following the design principles of Agent Skills (Anthropic, 2024), we organize the distilled knowledge into a hierarchical skill library SKILLBANK that enables efficient retrieval of relevant expertise during decision-making.

Sret = TopK({s ∈ Sk : sim(ed,es) > δ},K), (4)

where ed,es are embeddings of the task description and skill respectively, δ is a similarity threshold, and K controls the number of retrieved skills. The policy then conditions on

Skill Organization. We structure SKILLBANK into two levels: 1) General Skills Sg capture universal strategic prin-

Algorithm 1 SKILLRL: Recursive Skill-Augmented RL

(SFT) stage (Ouyang et al., 2022), where the teacher model MT generates N skill-augmented reasoning traces DSFT = {(di,Si,τi∗)}Ni=1 demonstrating how to retrieve, interpret, and apply skills during decision-making. The base model is then fine-tuned on these demonstrations:

Require: Base model πbase, teacher MT, environment E Ensure: Trained policy πθ∗, evolved skill library SKILLBANK∗

- 1: ▷ Experience-based Skill Distillation
- 2: T +, T − ← Rollout(πbase, E)
- 3: for all τ+ ∈ T + do
- 4: s+ ← MT(τ+)
- 5: end for
- 6: for all τ− ∈ T − do
- 7: s− ← MT(τ−)
- 8: end for
- 9: ▷ Hierarchical Skill Library Construction
- 10: Sg ← general skills from distilled experiences
- 11: for all task type k do
- 12: Sk ← task-specific skills for category k
- 13: end for
- 14: SKILLBANK ← Sg ∪ k Sk
- 15: ▷ Recursive Skill Evolution via RL
- 16: // Cold-start initialization
- 17: DSFT ← MT(E, SKILLBANK)
- 18: θ ← SFT(πbase, DSFT); πref ← πθ
- 19: // RL with recursive evolution
- 20: for epoch = 1 to N do
- 21: for all task d do
- 22: Sret ← Retrieve(d, SKILLBANK)
- 23: Sample {τ(i)}Gi=1 ∼ πθ(·|d, Sg, Sret)
- 24: Compute {Ri}Gi=1 and update θ via GRPO
- 25: end for
- 26: if validation epoch then
- 27: Tval− ← failed validation trajectories
- 28: Snew ← MT(Tval−, SKILLBANK)
- 29: SKILLBANK ← SKILLBANK ∪ Snew
- 30: end if
- 31: end for
- 32: return πθ, SKILLBANK


LCE(DSFT;θ), (6)

θsft = arg min

θ

where LCE denotes the cross-entropy loss. The resulting model πθ

serves as both the starting point for RL training and the reference policy πref for KL regularization.

sft

Recursive Skill Evolution. A static skill library cannot anticipate all scenarios the agent will encounter. As the policy improves and explores new state regions, it faces situations where existing skills provide insufficient guidance. We introduce recursive skill evolution to address this limitation. The process begins with an initial skill library containing baseline task-action principles.

After each validation epoch, we monitor the success rate Acc(C) for each task category C. To ensure targeted growth, the evolution is triggered only for categories where Acc(C) < δ. We then collect failed trajectories Tval− = {τj : r(τj) = 0}Mj=1 using a diversity-aware stratified sampling strategy: trajectories are grouped by category, prioritized by the severity of failure (negative rewards), and selected via round-robin sampling to maintain categorical entropy. Then we will analyze these samples to identify gaps:

the retrieved skills:

at ∼ πθ(at|o≤t,d,Sg,Sret). (5)

Notably, skill distillation achieves 10–20× token compression compared to raw trajectories while enhancing rather than degrading the utility of the original experience. This compression allows the agent to leverage rich experiential knowledge within limited context windows.

#### 3.3. Recursive Skill Evolution

A static skill library cannot anticipate all scenarios the agent will encounter. As the policy improves and explores new state regions, it faces situations where existing skills provide insufficient guidance. We introduce recursive skill evolution during reinforcement learning to address this limitation, enabling the skill library and agent policy to co-evolve.

Cold-Start Initialization. Before RL training, we address a critical challenge: the base agent has not learned how to effectively utilize skills. Simply providing skills to an unchanged model yields limited benefit (Guo et al., 2025). We therefore perform a cold-start supervised fine-tuning

Snew = MT(Tval−, SKILLBANK). (7)

The teacher model is prompted to: (1) identify failure patterns not addressed by current skills, (2) propose new skills to cover these gaps, and (3) suggest refinements to existing skills that proved ineffective. The library is then updated: SKILLBANK ← SKILLBANK ∪ Snew.

This creates a virtuous cycle: as the agent improves, it encounters new challenges, which drive skill library expansion, which enables further improvement.

RL-based Policy Optimization. We optimize the skillaugmented policy using GRPO. For each task with description d, the agent first retrieves relevant skills and then samples G complete trajectories {τ(1),...,τ(G)} from the current policy πθ. Each trajectory τ(i) receives a binary reward Ri = r(τ(i)) ∈ {0,1} indicating task successfulness. The normalized advantage for each trajectory is computed as:

Ri − mean({Rj}Gj=1) std({Rj}Gj=1)

. (8)

Ai =

The policy is updated according to:

J (θ) = Ed,{τ(i)}

1 G

G

min ρiAi,

i=1

clip(ρi,1 − ϵ,1 + ϵ)Ai − βDKL(πθ∥πref) ,

(9)

(i)|d,Sg,Sret)

where ρi = πθ(τ

πold(τ(i)|d,Sg,Sret) is the importance ratio computed over the skill-augmented context. The KL penalty anchored to πref = πθ

ensures that RL optimization preserves the learned skill utilization capabilities while improving task performance. The complete training procedure is summarized in Algorithm 1.

sft

### 4. Experiments

We evaluate SKILLRL on nine challenging benchmarks for LLM agents: ALFWorld, WebShop, and seven searchaugmented QA tasks. Our experiments address the following questions: 1) How does SKILLRL compare to stateof-the-art methods? 2) What is the contribution of each component? 3) How does the skill library evolve during training? 4) Does skills accelerate model convergence?

#### 4.1. Experimental Setup

Environments. ALFWorld (Shridhar et al.) is a text-based game aligned with the ALFRED embodied AI benchmark. Agents must complete household tasks by navigating and interacting with objects through text commands. WebShop (Yao et al., 2022a) simulates web shopping. Agents navigate a realistic web interface to find and purchase products matching user specifications. In addition, we also evaluate the performance of SKILLRL on search-augmented QA tasks, including single-hop QA datasets (NQ (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), and PopQA (Mallen et al., 2023)) and multi-hop QA datasets (HotpotQA (Yang et al., 2018), 2Wiki (Ho et al., 2020), MuSiQue (Trivedi et al., 2022), and Bamboogle (Press et al., 2023)).

Baselines. We compare SKILLRL against four categories of competitive methods. First, we include closed-source LLMs, specifically GPT-4o (OpenAI, 2024) and Gemini2.5-Pro (Comanici et al., 2025), which represent the state-ofthe-art in general-purpose reasoning and instruction following. Second, we evaluate prompt-based agentic or memorybased methods, including ReAct (Yao et al., 2022b) and Reflexion (Shinn et al., 2023), which rely on in-context prompting for multi-step reasoning, as well as Mem0 (Chhikara et al., 2025), ExpeL (Zhao et al., 2024), and MemP (Fang et al., 2025), which utilize external memory or experience pools to guide behavior without parameter updates. Third, we consider RL-based methods, including group-based online RL algorithms such as RLOO (Ahmadian et al., 2024)

and GRPO (Shao et al., 2024) that optimize policies via advantage estimation over trajectory groups. Finally, we compare against memory-augmented RL-based methods, such as EvolveR (Wu et al., 2025), MemRL (Zhang et al., 2026), and the combination of Mem0+GRPO and SimpleMem (Liu et al., 2026)+GRPO, which integrate persistent memory mechanisms directly into the reinforcement learning optimization process to handle long-term dependencies. For search-augmented QA, we compare SKILLRL with R1-Instruct, Search-o1 (Li et al., 2025), Search-R1 (Jin et al., 2025), ZeroSearch (Sun et al., 2025), and StepSearch (Zheng et al., 2025).

Implementation Details. We use Qwen2.5-7BInstruct (Bai et al., 2023) as our base model and OpenAI o3 (OpenAI, 2025a) as the teacher model for skill distillation and SFT data generation. For RL training, we use GRPO with learning rate 1×10−6, batch size 16, group size 8, and 4 gradient accumulation steps. We set K = 6 for task-specific skill retrieval and δ = 0.4 for the collection of failed trajectories. For more detailed information on training hyperparameters, please see Appendix B.1.

#### 4.2. Main Results

Comparison with Baselines. We compare SKILLRL with baseline methods across two benchmarks as shown in Table 1. Our method consistently outperforms all baselines, with key observations as follows:

- 1) Significant Gains over Prompt-based Methods. SKILLRL achieves a 89.9% success rate on ALFWorld and 72.7% on WebShop, outperforming the best prompt-based baselines by a large margin. This gap suggests that while in-context learning can leverage past experiences, it often fails to distill actionable knowledge from verbose trajectories or fundamentally adapt the agent’s policy.
- 2) Superiority over Vanilla RL. RL training brings substantial gains, yet SKILLRL consistently surpasses standard RL baselines. Compared to PPO, RLOO, and GRPO, SKILLRL achieves the best overall performance. Notably, since SKILLRL utilizes GRPO as its base optimizer, the 12.3% absolute improvement over GRPO on ALFWorld (from 77.6% to 89.9%) is directly attributable to our skillaugmentation mechanism rather than algorithmic variance. In complex subtasks like Cool and Pick2, SKILLRL outperforms GRPO by 23.0% and 22.8% respectively, proving that structured skill priors effectively accelerate and enhance policy learning in sparse-reward environments.
- 3) Advantage over Memory-Augmented RL. SKILLRL substantially outperforms existing memory-augmented RL frameworks, which differ in how they manage and update experience. MemRL, which uses RL solely to update its memory bank while keeping the policy frozen, fails to adapt


- Table 1. Performance on ALFWorld and WebShop. For ALFWorld, we report the average success rate (%) for each subtask as well as the overall result. For WebShop, we report both the average score and the average success rate (%). ∗ denotes the results replicated from (Feng et al., 2025). The best results and second best results are highlighted in red and blue , respectively.


ALFWorld WebShop

Method

Pick Look Clean Heat Cool Pick2 All Score Succ. Closed-source LLMs

GPT-4o 75.3 60.8 31.2 56.7 21.6 49.8 48.0 31.8 23.7 Gemini-2.5-Pro 92.8 63.3 62.1 69.0 26.6 58.7 60.3 42.5 35.9

Qwen2.5-7B-Instruct Qwen2.5 33.4 21.6 19.3 6.90 2.80 3.20 14.8 26.4 7.80 Prompt-based Agentic or Memory-based Methods

ReAct∗ 48.5 35.4 34.3 13.2 18.2 17.6 31.2 46.2 19.5 Reflexion∗ 62.0 41.6 44.9 30.9 36.3 23.8 42.7 58.1 28.8 Mem0 54.0 55.0 26.9 36.4 20.8 7.69 33.6 23.9 2.00 ExpeL 21.0 67.0 55.0 52.0 71.0 6.00 46.3 30.9 11.2 MemP 54.3 38.5 48.1 56.2 32.0 16.7 41.4 25.3 6.40 SimpleMem 64.5 33.3 20.0 12.5 33.3 3.84 29.7 33.2 8.59 RL-based Methods

RLOO∗ 87.6 78.2 87.3 81.3 71.9 48.9 75.5 80.3 65.7 GRPO∗ 90.8 66.1 89.3 74.7 72.5 64.7 77.6 79.3 66.1 Memory-Augmented RL-based Methods

MemRL 62.8 38.5 22.2 12.5 8.00 0.00 21.4 29.5 9.20 EvolveR 64.9 33.3 46.4 13.3 33.3 33.3 43.8 42.5 17.6 Mem0+GRPO 78.1 54.8 56.1 31.0 65.0 26.9 54.7 58.1 37.5 SimpleMem+GRPO 89.5 36.3 60.0 50.0 64.9 26.3 62.5 67.8 46.9 SKILLRL 97.9 71.4 90.0 90.0 95.5 87.5 89.9 85.2 72.7

to complex environments, yielding only 21.4% on ALFWorld. EvolveR, which jointly updates the policy and memory bank, shows improvement (43.8%) but remains limited by its reliance on rough trajectory storage. To provide a more competitive baseline, we implemented Mem0+GRPO, which combines a state-of-the-art prompt-based memory mechanism with an optimized policy model. While this hybrid approach improves performance to 54.7% on ALFWorld and 37.5% on WebShop, it still trails SKILLRL by a wide margin (about 35.2% absolute success rate gap). These results validate our core hypothesis: effective experience transfer requires high-level skill abstraction and a co-evolving library rather than simple trajectory compression or prompt-based memory retrieval.

Comparison with Closed-Source Models. Remarkably, SKILLRL with Qwen2.5-7B-Instruct significantly outperforms much larger closed-source models, as shown in Table 1. On ALFWorld, our method exceeds GPT-4o (OpenAI, 2024) by 41.9% and Gemini-2.5-Pro (Comanici et al., 2025) by 29.6%. This demonstrates that effective skill learning can compensate for model scale, enabling smaller opensource models to achieve superior task performance through structured experiential knowledge.

Performance on Search-Augmented QA. As shown in

Table 2, SKILLRL achieves a state-of-the-art average score of 47.1%, significantly outperforming Search-R1 (38.5%) abd EvolveR (43.1%). Key observations include: 1) Superior multi-hop Reasoning: SKILLRL excels in complex tasks like Bamboogle, surpassing EvolveR by 19.4%. This demonstrates that hierarchical skills effectively guide multistep information synthesis. 2) Strong generalization: Despite being trained on limited datasets (NQ, HotpotQA), SKILLRL maintains competitive performance on OOD tasks like TriviaQA and 2Wiki, confirming that distilled search strategies are task-agnostic.

#### 4.3. Analysis

In this section, we provide detailed analysis of each module’s effectiveness and the skill evolution dynamics.

Ablation Studies. We conduct ablation experiments to evaluate each component’s contribution, with results in Table 3. According to the results: (1) Removing hierarchical structure (i.e., task-specific skills only) decreases performance by 13.1% on ALFWorld and 11.3% on WebShop, indicating universal strategic principles provide essential foundational guidance. (2) Replacing the skill library with raw trajectories causes the largest degradation (up to 25%), which

- Table 2. Performance on search-augmented QA tasks. SKILLRL is trained on NQ and HotpotQA. † and ⋆ indicate in-domain and out-of-domain datasets, respectively. ∗ denotes the results replicated from (Sun et al., 2025).

Method

Single-Hop QA Multi-Hop QA

Avg. NQ† TriviaQA⋆ PopQA⋆ HotpotQA† 2Wiki⋆ MuSiQue⋆ Bamboogle⋆

Qwen2.5-7B-Instruct Qwen2.5∗ 11.6 35.6 1.20 16.4 22.2 4.80 14.4 15.2

|CoT∗ 12.8 35.6 3.80 RAG∗ 27.4 58.2 17.8 Search-o1∗ 19.4 40.6 11.4 R1-Instruct 21.0 44.9 17.1 Search-R1 39.3 61.0 39.7 ZeroSearch 43.6 61.8 51.5 StepSearch - - EvolveR 43.5 63.4 44.6<br><br>|16.2 22.6 6.60 24.0 25.8 23.2 9.40 16.8<br>17.0 27.0 8.60 30.4 20.8 27.5 6.00 19.2<br><br><br>37.0 40.1 14.6 36.8 34.6 35.2 18.4 27.8<br><br>38.6 36.6 22.6 40.0 38.2 42.0 15.6 54.4<br><br><br>|17.4 25.5 22.1 22.4 38.5 39.1 43.1<br><br>|
|---|---|---|
|SKILLRL 45.9 63.3 45.9<br><br>|43.2 40.3 20.2 73.8<br><br>|47.1|


- Table 3. Ablation study results. We report average success rate (%) on ALFWorld and WebShop.


###### Skill Library Evolution

Total Skills

Heat Cool Pick2 Mistakes

| |
|---|


120

General Pick Look Clean

| |
|---|


| |
|---|


Method ALFWorld WebShop SKILLRL 89.9 72.7 Skill Library Ablations

| |
|---|


| |
|---|


100

| |
|---|


100

94

88

83

###### NumberofSkills

77

80

71

w/o Hierarchical Structure 76.8 61.4 w/o Skill Library (Raw Trajectories) 61.7 50.2

66

60

55

60

Training Pipeline Ablations

w/o Cold-Start SFT 65.2 46.5 w/o Dynamic Evolution 84.4 70.3

40

20

0

0 20 40 60 80 100 120 140 150

directly supports our motivation that abstraction is superior to memorization. Raw experiences introduce significant redundancy and noise that hinder effective knowledge transfer.

Training Steps

###### Figure 3. Evolution of skill library size during RL training. Dynamic skill evolution adds skills at validation checkpoints.

- (3) Cold-start SFT proves critical (20% drop without it), confirming that the base model requires an initial explicit demonstration phase to learn how to adaptively retrieve and utilize the abstracted skills before entering the RL stage.
- (4) Dynamic evolution contributes a 5.5% improvement by ensuring the skill library is a dynamic component rather than a static database. This co-evolution allows the agent to iteratively refine its internal policy by addressing emergent failure modes that were not covered by the initial skill set.


skills show a steadier increase (from 12 to 20). Notably, we observe a balanced expansion across various task categories, ensuring the agent develops specialized expertise for each environment rollout. This overall expansion reflects the agent’s increasing ability to refine its repertoire and tackle diverse scenarios within specific task types.

Context Efficiency. To evaluate the impact of skill abstraction on inference overhead, we compare the average prompt length of SKILLRL with a memory-augmented baseline using raw trajectories (Qwen2.5-7B with Raw Memory) in

Per-Task Analysis on ALFWorld. Table 1 breaks down ALFWorld performance by task type. The largest gains are on PickTwo (+23%), Cool (+22%) and Heat (+15%), which are among the most challenging tasks requiring multi-step planning and state tracking. Task-specific skills are particularly valuable here, capturing strategies like “when picking two objects, verify the first is secured before searching for the second” that address common failure modes.

##### Figure 4. The results reveal that while the raw memory approach suffers from a high and fluctuating token footprint (averaging ∼1,450 tokens), SKILLRL maintains a significantly leaner prompt (averaging <1,300 tokens), achieving approximately a 10.3% reduction in context length. This efficiency stems from our distillation mechanism, which compresses verbose environment interactions into high-density, actionable skills. Notably, SKILLRL requires less context than the memory-based baseline to achieve superior performance, demonstrating that skill abstraction effectively mitigates the context-bloat problem common in traditional memory-based agents.

Skill Library Growth. Figure 3 shows how the skill library evolves during training. The initial skill library contains 55 skills (12 general, 43 task-specific). Through dynamic evolution, this grows to 100 skills by the end of training (Step 150). The growth is predominantly driven by taskspecific skills (increasing from 43 to 80), while general

![image 43](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile43.png>)

Figure 4. Comparison of prompt length (tokens) between raw memory retrieval and our distilled skill abstraction. SKILLRL consistently reduces context overhead while maintaining reasoning utility.

![image 44](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile44.png>)

Figure 5. Success rate on ALFWorld validation set. The recursive skill evolution significantly accelerates convergence and enhances the overall performance ceiling.

Evolution Dynamics. Figure 5 illustrates the reinforcement learning training curves with and without the recursive skill evolution mechanism. We observe that while SKILLRL without evolution shows steady improvement, SKILLRL with skill evolution exhibits a notably higher learning rate and superior asymptotic performance. Specifically, SKILLRL achieves a success rate of over 80% within 60 training steps, whereas the baseline requires approximately 90 steps to reach a lower peak. This acceleration in convergence suggests that the dynamic introduction of new skills and refinement of existing ones effectively provide the agent with timely strategic guidance to overcome local optima. Furthermore, the higher performance ceiling validates that the co-evolution of the skill library and the policy allows the agent to adapt to increasingly complex task scenarios that static memory methods fail to resolve.

Qualitative Analysis. To further investigate how SKILLRL utilizes the learned knowledge, we visualize the reasoning process on ALFWorld and WebShop in Figure 6. The case studies demonstrate that our trained agent can effectively retrieve and execute relevant skills from the SKILLBANK to guide its decision-making. For instance, in the WebShop task, the agent invokes general strategies like “Prioritize Core Keywords” alongside task-specific heuristics

“Focus Key Query” to ensure the product meets all constraints within a limited budget. Similarly, in ALFWorld, the agent coordinates hierarchical skills, i.e., using “Progressive Goal Decomposition” for high-level planning and “No Appliance Before Object” to avoid common logical pitfalls. This seamless integration of general and specific skills confirms that the agent does not merely memorize trajectories, but rather develops a structured understanding of task logic, allowing for more robust and efficient problem-solving.

### 5. Related Work

LLM Agents. The emergence of capable LLMs has catalyzed rapid development in autonomous agent systems (Wei et al., 2026). ReAct (Yao et al., 2022b) interleaves reasoning and acting, enabling chain-of-thought style plan-

ning during interaction, while Reflexion (Shinn et al., 2023) introduces verbal reinforcement through self-reflection on past failures. Frameworks like AutoGen (Wu et al., 2024) and CAMEL (Li et al., 2023) demonstrate general-purpose multi-agent capabilities, featuring automated orchestration and diverse tool integration. While initial efforts focused on constrained tasks like coding or basic arithmetic, these approaches primarily rely on in-context learning (ICL) (Dong et al., 2024). However, these agents struggle to scale as tasks become more complex, as they treat every interaction as an isolated event and must start each new task from scratch without any prior knowledge.

Memory Mechanisms in Agents. To overcome the limitations of finite context windows and the inability of agents to learn from experience, external memory architectures have become a cornerstone of agent design (Hu et al., 2025; Wang, 2025). Early systems primarily utilized a static RAG paradigm or stored raw trajectories as few-shot examples (Wang et al.; Chhikara et al., 2025; Zhang et al.,

- 2025a; Wang et al., 2024). However, raw trajectories are often token-heavy and contain significant redundancy and noise, which can lead to performance degradation. Current research has moved toward self-improving memory, distilling interactions into higher-level insights or procedural tips (Wang & Chen, 2025; Tang et al., 2025; Fang et al., 2025; Zhao et al., 2024; Ouyang et al., 2025; Wei et al., 2025). While some recent work explores updating memory banks via online training to improve efficiency (Zhang et al.,
- 2025b; 2026), many existing methods still struggle to distinguish high-value experiences from noise or fail to distill core principles that can guide internal decision-making.


Evolution of Agentic Skills and Reinforcement Learning. The development of agentic skills (Anthropic, 2024), which are compact, reusable strategies that capture the essence of subtasks, is increasingly viewed through the lens of Continual Learning (CL) and RL. Traditional CL (Parisi et al., 2019) focuses on knowledge preservation in predefined tasks, but self-evolving agents (Gao et al., 2025; Xia et al., 2025; Liu et al., 2025) aim for active skill acquisition in open-ended environments (Fang et al., 2025; Wang et al.,

![image 45](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile45.png>)

![image 46](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile46.png>)

###### WebShop ALFWorld

Task: I need a women's long sleeve button-down shirt in navy blue, size large, machine washable, price lower than $40.00

###### Task: heat some egg and put it in countertop.

--- Retrieved Skills --Detected Task Type: heat [General Skills] … [Task-Specific Skills]

--- Retrieved Skills --Detected Task Type: apparel [General Skills] … [Task-Specific Skills]

-----Step 1 Observation: You are in the middle of a room. Looking quickly around you…

------

Step 1

Observation: WebShop homepage. Search bar available. <think>Following skill [gen_001] 'Prioritize Core Keywords' and [app_001] 'Focus Key Query': I should include product type + must-have attributes. My query should be …</think>

<think>Per [gen_010] 'Progressive Goal Decomposition': sub-goals are … Per [hea_004] 'No Appliance Before Object': I must NOT go to microwave first. Per [hea_001] 'Secure Exact Target First': find the egg. It's food — check fridge and countertops.</think>

…

<action>search[women long sleeve button down shirt navy blue machine …]</action> Step 9 Observation: Product page updated: Color = Navy Blue, Size = L. Price: $29.99

<action>go… tocountertop1</action>

Step 8 Observation: You arrive at countertop 1 <think>Per [hea_005]: place the heated egg directly.</think> <action>put egg 1 in/on countertop 1</action>

<think>Applying skill [app_004] 'Check Variant Price': price for Navy Blue / L is $29.99, which is under the $40 budget. Also per [app_005] 'Confirm Hidden Specs': … $29.99 < $40. Per skill [gen_013] 'Purchase Decisively', I should buy now.</think>

![image 47](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile47.png>)

![image 48](<2026-xia-skillrl-evolving-agents-recursive_images/imageFile48.png>)

<action>click[Buy Now]</action>

Figure 6. Case studies of SKILLRL on WebShop and ALFWorld. The examples illustrate how the agent adaptively retrieves and integrates General Skills and Task-Specific Skills within its reasoning process to achieve precise and efficient task execution.

2025). While RL is widely used to align LLMs (Schulman et al., 2017; Ouyang et al., 2022), or improve reasoning via rule-based verifiers (Shao et al., 2024), applying it to agentic skills remains challenging due to sparse rewards and long horizons. Unlike previous memory-augmented RL which treats memory as a static or auxiliary source, recent trends suggest that the key to efficient experience transfer lies in abstraction (Wu et al., 2025). Our work builds on this by treating the skill library as a dynamic component that co-evolves with the agent’s policy, utilizing RL to refine structured skills through recursive failure analysis.

2024.

Anthropic. The claude 3 model family: Opus, sonnet, haiku, 2024. URL https://www.anthropic. com/news/claude-3-family.

Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F., et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.

Chhikara, P., Khant, D., Aryan, S., Singh, T., and Yadav, D. Mem0: Building production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413, 2025.

### 6. Conclusion

We introduced SKILLRL, a framework for skill-augmented reinforcement learning in LLM agents. By distilling raw trajectories into compact, reusable skills and enabling dynamic skill evolution during training, SKILLRL achieves state-of-the-art performance on ALFWorld and WebShop while using substantially less context than memory-based approaches. Our work demonstrates that the abstraction from experience to skill is a powerful principle for building capable, sample-efficient agents.

### Acknowledgement

This work was partially supported by the Amazon Research Award, the Cisco Faculty Research Award, NEC Laboratories America Research Grant, and Coefficient Giving.

### References

Ahmadian, A., Cremer, C., Gall´e, M., Fadaee, M., Kreutzer, J., Pietquin, O., Ust¨¨ un, A., and Hooker, S. Back to basics: Revisiting reinforce-style optimization for learning from human feedback in llms. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 12248–12267,

Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., Blistein, M., Ram, O., Zhang, D., Rosen, E., et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.

Dong, Q., Li, L., Dai, D., Zheng, C., Ma, J., Li, R., Xia, H., Xu, J., Wu, Z., Chang, B., et al. A survey on incontext learning. In Proceedings of the 2024 conference on empirical methods in natural language processing, pp. 1107–1128, 2024.

Fang, R., Liang, Y., Wang, X., Wu, J., Qiao, S., Xie, P., Huang, F., Chen, H., and Zhang, N. Memp: Exploring agent procedural memory. arXiv preprint arXiv:2508.06433, 2025.

Feng, L., Xue, Z., Liu, T., and An, B. Group-in-group policy optimization for llm agent training. arXiv preprint arXiv:2505.10978, 2025.

Gao, H.-a., Geng, J., Hua, W., Hu, M., Juan, X., Liu, H., Liu, S., Qiu, J., Qi, X., Wu, Y., et al. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046, 2025.

Google. Try deep research and our new experimental model in gemini, your ai assistant, 2024. URL https://blog.google/products/ gemini/google-gemini-deep-research/.

Google. Introducing the gemini 2.5 computer use model, 2025. URL https://blog. google/technology/google-deepmind/ gemini-computer-use-model/.

Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

Ho, X., Nguyen, A.-K. D., Sugawara, S., and Aizawa, A. Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps. In Proceedings of the 28th International Conference on Computational Linguistics, pp. 6609–6625, 2020.

Hu, Y., Liu, S., Yue, Y., Zhang, G., Liu, B., Zhu, F., Lin, J., Guo, H., Dou, S., Xi, Z., et al. Memory in the age of ai agents. arXiv preprint arXiv:2512.13564, 2025.

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., and Han, J. Search-r1: Training llms to reason and leverage search engines with reinforcement learning. arXiv preprint arXiv:2503.09516, 2025.

Joshi, M., Choi, E., Weld, D. S., and Zettlemoyer, L. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1601–1611, 2017.

Kwiatkowski, T., Palomaki, J., Redfield, O., Collins, M., Parikh, A., Alberti, C., Epstein, D., Polosukhin, I., Devlin, J., Lee, K., et al. Natural questions: a benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:453–466, 2019.

Li, G., Hammoud, H., Itani, H., Khizbullin, D., and Ghanem, B. Camel: Communicative agents for” mind” exploration of large language model society. Advances in Neural Information Processing Systems, 36:51991–52008, 2023.

Li, X., Dong, G., Jin, J., Zhang, Y., Zhou, Y., Zhu, Y., Zhang, P., and Dou, Z. Search-o1: Agentic search-enhanced large reasoning models. arXiv preprint arXiv:2501.05366, 2025.

Liu, J., Xiong, K., Xia, P., Zhou, Y., Ji, H., Feng, L., Han, S., Ding, M., and Yao, H. Agent0-vl: Exploring selfevolving agent for tool-integrated vision-language reasoning. arXiv preprint arXiv:2511.19900, 2025.

Liu, J., Su, Y., Xia, P., Han, S., Zheng, Z., Xie, C., Ding, M., and Yao, H. Simplemem: Efficient lifelong memory for llm agents. arXiv preprint arXiv:2601.02553, 2026.

Mallen, A., Asai, A., Zhong, V., Das, R., Khashabi, D., and Hajishirzi, H. When not to trust language models: Investigating effectiveness of parametric and non-parametric memories. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 9802–9822, 2023.

OpenAI. Gpt-4o system card, 2024. https://openai. com/index/gpt-4o-system-card/.

OpenAI. Introducing o3 and o4-mini, 2025a. https://openai.com/index/ introducing-o3-and-o4-mini/.

OpenAI. Openai deep research system card, 2025b. URL https://openai.com/index/ introducing-deep-research/.

OpenAI. Openai computer-using agent, 2025c. URL https://openai.com/index/ computer-using-agent/.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems, 35:27730–27744, 2022.

Ouyang, S., Yan, J., Hsu, I., Chen, Y., Jiang, K., Wang, Z., Han, R., Le, L. T., Daruki, S., Tang, X., et al. Reasoningbank: Scaling agent self-evolving with reasoning memory. arXiv preprint arXiv:2509.25140, 2025.

Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., and Wermter, S. Continual lifelong learning with neural networks: A review. Neural networks, 113:54–71, 2019.

Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N. A., and Lewis, M. Measuring and narrowing the compositionality gap in language models. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 5687–5711, 2023.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and Yao, S. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36:8634–8652, 2023.

Shridhar, M., Yuan, X., Cote, M.-A., Bisk, Y., Trischler, A., and Hausknecht, M. Alfworld: Aligning text and embodied environments for interactive learning. In International Conference on Learning Representations.

Sun, H., Qiao, Z., Guo, J., Fan, X., Hou, Y., Jiang, Y., Xie, P., Zhang, Y., Huang, F., and Zhou, J. Zerosearch: Incentivize the search capability of llms without searching. arXiv preprint arXiv:2505.04588, 2025.

Tang, X., Qin, T., Peng, T., Zhou, Z., Shao, D., Du, T., Wei, X., Xia, P., Wu, F., Zhu, H., et al. Agent kb: Leveraging cross-domain experience for agentic problem solving. arXiv preprint arXiv:2507.06229, 2025.

Team, T. D., Li, B., Zhang, B., Zhang, D., Huang, F., Li, G., Chen, G., Yin, H., Wu, J., Zhou, J., et al. Tongyi deepresearch technical report. arXiv preprint arXiv:2510.24701, 2025.

Trivedi, H., Balasubramanian, N., Khot, T., and Sabharwal,

- A. Musique: Multihop questions via single-hop question composition. Transactions of the Association for Computational Linguistics, 10:539–554, 2022.


Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. Voyager: An open-ended embodied agent with large language models. Transactions on Machine Learning Research.

Wang, Y. From Static Parameters to Updatable Memory: Enabling Large Language Model Agents to Remember, Adapt, and Learn. PhD thesis, University of California, San Diego, 2025.

Wang, Y. and Chen, X. Mirix: Multi-agent memory system for llm-based agents. arXiv preprint arXiv:2507.07957, 2025.

- Wang, Y., Takanobu, R., Liang, Z., Mao, Y., Hu, Y., McAuley, J., and Wu, X. Mem-{\alpha}: Learning memory construction via reinforcement learning. arXiv preprint arXiv:2509.25911, 2025.
- Wang, Z. Z., Mao, J., Fried, D., and Neubig, G. Agent workflow memory. arXiv preprint arXiv:2409.07429,


- 2024.

Wei, T., Sachdeva, N., Coleman, B., He, Z., Bei, Y., Ning, X., Ai, M., Li, Y., He, J., Chi, E. H., et al. Evo-memory: Benchmarking llm agent test-time learning with selfevolving memory. arXiv preprint arXiv:2511.20857,

- 2025.

Wei, T., Li, T.-W., Liu, Z., Ning, X., Yang, Z., Zou, J., Zeng, Z., Qiu, R., Lin, X., Fu, D., et al. Agentic reasoning for large language models. arXiv preprint arXiv:2601.12538,

- 2026.


- Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., et al. Autogen: Enabling next-gen llm applications via multi-agent conversations. In First Conference on Language Modeling, 2024.
- Wu, R., Wang, X., Mei, J., Cai, P., Fu, D., Yang, C., Wen, L., Yang, X., Shen, Y., Wang, Y., et al. Evolver: Self-evolving llm agents through an experience-driven lifecycle. arXiv


- preprint arXiv:2510.16079, 2025.

Xia, P., Zeng, K., Liu, J., Qin, C., Wu, F., Zhou, Y., Xiong, C., and Yao, H. Agent0: Unleashing self-evolving agents from zero data via tool-integrated reasoning. arXiv

- preprint arXiv:2511.16043, 2025.


Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W., Salakhutdinov, R., and Manning, C. D. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 conference on empirical methods in natural language processing, pp. 2369–2380, 2018.

Yao, S., Chen, H., Yang, J., and Narasimhan, K. Webshop: Towards scalable real-world web interaction with grounded language agents. Advances in Neural Information Processing Systems, 35:20744–20757, 2022a.

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., and Cao, Y. React: Synergizing reasoning and acting in language models. In The eleventh international conference on learning representations, 2022b.

Zhang, G., Fu, M., Wan, G., Yu, M., Wang, K., and Yan, S. G-memory: Tracing hierarchical memory for multi-agent systems. arXiv preprint arXiv:2506.07398, 2025a.

Zhang, G., Ren, H., Zhan, C., Zhou, Z., Wang, J., Zhu, H., Zhou, W., and Yan, S. Memevolve: Meta-evolution of agent memory systems. arXiv preprint arXiv:2512.18746,

- 2025b.

Zhang, S., Wang, J., Zhou, R., Liao, J., Feng, Y., Zhang, W., Wen, Y., Li, Z., Xiong, F., Qi, Y., et al. Memrl: Self-evolving agents via runtime reinforcement learning on episodic memory. arXiv preprint arXiv:2601.03192,

- 2026.


Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J., and Huang, G. Expel: Llm agents are experiential learners. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 19632–19642, 2024.

Zheng, X., An, K., Wang, Z., Wang, Y., and Wu, Y. Stepsearch: Igniting llms search ability via step-wise proximal policy optimization. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 21816–21841, 2025.

Appendix

- A. Prompts


In this section, we provide the full prompt templates used throughout the different phases of our framework. These templates are designed to ensure consistent agent behavior and structured data generation across various environments.

#### A.1. Agent Execution Prompts

The following prompts are used during the online inference phase. These templates provide the agent with the current task description, a history of previous interactions, and a set of retrieved skills (experiences) to guide its decision-making process. The prompts explicitly enforce a Chain-of-Thought (CoT) reasoning step before action selection.

|Prompt A.1: ALFWorld Agent Execution with Skills<br><br>|
|---|
|System Prompt: You are an expert agent operating in the ALFRED Embodied Environment. Your task is to: {task description}<br><br>## Retrieved Relevant Experience {retrieved memories}<br><br>## Current Progress Prior to this step, you have already taken {step count} step(s). Below are the most recent {history length} observations and the corresponding actions you took: {action history} You are now at step {current step} and your current observation is: {current observation} Your admissible actions of the current situation are: [{admissible actions}].<br><br>Now it’s your turn to take an action. You should first reason step-by-step about the current situation. This reasoning process MUST be enclosed within <think> </think> tags. Once you’ve finished your reasoning, you should choose an admissible action for current step and present it within <action> </action> tags.|


|Prompt A.2: WebShop Agent Execution with Skills<br><br>|
|---|
|System Prompt: You are an expert autonomous agent operating in the WebShop e-commerce environment. Your task is to: {task description}.<br><br>## Retrieved Relevant Experience {retrieved memories}<br><br>## Current Progress Prior to this step, you have already taken {step count} step(s). Below are the most recent {history length} observations and the corresponding actions you took: {action history} You are now at step {current step} and your current observation is: {current observation} Your admissible actions of the current situation are: [ {available actions} ].<br><br>Now it’s your turn to take one action for the current step. You should first reason step-by-step about the current situation, then think carefully which admissible action best advances the shopping goal. This reasoning process MUST be enclosed within <think> </think> tags. Once you’ve finished your reasoning, you should choose an admissible action for current step and present it within <action> </action> tags.|


#### A.2. Skill Generation and Distillation Prompts

These prompts are utilized during the skill discovery and library initialization phases. They guide a high-capability teacher model to analyze interaction trajectories, identify failure modes, and distill reusable, actionable skills into a structured JSON format.

|Prompt B.1: Dynamic Skill Discovery from Failures<br><br>|
|---|
|Analyze these failed {env description} agent trajectories and suggest NEW skills to add.<br><br>FAILED TRAJECTORIES: {failure examples} EXISTING SKILL TITLES: {existing titles}<br><br>Generate 1-3 NEW actionable skills that would help avoid these failures. Each skill must have: skill id, title (3-5 words), principle (1-2 sentences), when to apply. The skill id should be unique and follow the pattern: ”dyn 001”, ”dyn 002”, etc.<br><br>Return ONLY a JSON array of skills, no other text.|


|Prompt B.2: Initial Skill Distillation (ALFWorld)<br><br>|
|---|
|You are an expert at distilling agent behavior patterns into concise, actionable skills. Analyze these successful and failed trajectories from an embodied AI agent operating in household environments (ALFWorld).<br><br>SUCCESSFUL TRAJECTORIES: {success patterns} FAILED TRAJECTORIES: {failure patterns}<br><br>Generate 8-12 GENERAL SKILLS that apply across ALL task types. These should be: 1. Concise; 2. Actionable; 3. Transferable;<br><br>4. Failure-aware. Focus on: Navigation, object manipulation, state tracking, error recovery, and container interaction rules. Return ONLY the JSON array, no other text.|


|Prompt B.3: Initial Skill Distillation (WebShop)<br><br>|
|---|
|You are an expert at distilling agent behavior patterns into concise, actionable skills. Analyze these successful and failed trajectories from an AI agent operating in an online shopping environment (WebShop).<br><br>SUCCESSFUL TRAJECTORIES: {success patterns} FAILED TRAJECTORIES: {failure patterns}<br><br>Generate 10-15 GENERAL SKILLS. Focus on: Search query formulation, product selection heuristics, option configuration (size, color, etc.), constraint verification, navigation patterns, and price handling.<br><br>Return ONLY the JSON array, no other text.|


#### A.3. Cold-start Trajectory Generation Prompts

To bridge the gap between a base model and the target performance, we use the following prompts to generate high-quality synthetic trajectories for Supervised Fine-Tuning (SFT). These prompts instruct the teacher model to solve tasks while explicitly demonstrating the application of specific skills, thereby providing a clear learning signal for the student model.

|Prompt C.1: Synthetic Trajectory Generation (ALFWorld)<br><br>|
|---|
|You are an expert agent in the ALFRED embodied environment. You will be given a task and relevant skills to apply. Your goal is to generate a successful trajectory that demonstrates proper use of these skills.<br><br>You should generate a step-by-step trajectory that:<br><br>1. Uses the provided skills appropriately;<br>2. Takes realistic actions in the environment;<br>3. Completes the task successfully;<br>4. Demonstrates good planning and systematic exploration. For each step, you should:<br><br><br>• Think through the current situation using <think></think> tags.<br>• Choose an appropriate action using <action></action> tags.<br>• The action should be a simple command like ”go to cabinet 1”, ”open drawer 2”, ”take apple 1”, ”put apple 1 in/on countertop 1”. Generate a complete trajectory from start to finish. Stop when the task is complete.<br>|


|Prompt C.2: Synthetic Trajectory Generation (WebShop)<br><br>|
|---|
|You are an expert shopping agent in the WebShop e-commerce environment. You will be given a shopping task and relevant skills to apply. Your goal is to generate a successful trajectory that demonstrates proper use of these skills.<br><br>You should generate a step-by-step trajectory that:<br><br>1. Uses the provided skills appropriately;<br>2. Takes realistic actions in the WebShop environment;<br>3. Successfully finds and purchases the requested product;<br>4. Demonstrates good search strategies and product evaluation. For each step, you should:<br><br><br>• Think through the current situation using <think></think> tags.<br>• Choose an appropriate action using <action></action> tags.<br>• Actions can be: search[query], click[element], or buy now. Generate a complete trajectory from start to finish. Stop when the purchase is complete.<br>|


### B. Additional Experimental Details

- B.1. Hyperparameters Table 4. Hyperparameters for SKILLRL.


Hyperparameter Value Cold-Start SFT Learning rate 1 × 10−4 Batch size 16 Epochs 3 SFT examples 7,500 (AlfWorld) / 2,400 (WebShop) RL Training Learning rate 1 × 10−6 Batch size 64 KL loss Coef 0.01 Invalid Action Penalty Coef 0.1 Max Prompt Length 6,000 Max Response Length 1,024 Epoch 150 Skill Retrieval Top-K retrieval 6 Validation interval 5 Steps Update Threshold δ 0.4 Max failures analyzed 10 (SR < 0.4) / 5 (SR > 0.4) Max new skills per evolution 3

- B.2. Compute Resources All experiments were conducted on a cluster with 8 NVIDIA H100 80GB GPUs. Training times:


- • Trajectory collection: 3 hours
- • Skill distillation: 0.5 hours
- • Cold-start SFT: 2 hour
- • RL training: 24 hours


Table 5. Example distilled skills from SKILLBANK for ALFWorld (Shridhar et al.). This table summarizes general patterns and application logic derived from raw trajectories.

###### ID Skill Title Principle (Actionable Pattern) When to Apply

General Exploration & Acquisition Skills

- gen 001 Systematic Exploration Search every plausible surface or container exactly once before

revisiting; prioritize unseen locations.

Anytime the goal count is not met and unexplored areas remain.

- gen 002 Immediate Acquisition As soon as a required object becomes visible and reachable,

take it immediately.

Upon first visual confirmation of a goal-relevant object.

- gen 003 Destination First Policy After picking up a goal object, navigate directly to the known


Holding any goal object while target location is identified.

target receptacle and place it.

State-Changing & Spatial Relation Skills

- gen 005 Use State-Changing

Tools Early

Acquire the object, then immediately use the nearest suitable appliance (heat/cool/clean) before placement.

After picking up an object requiring temperature or cleanliness change.

- gen 006 Establish Spatial Rela-


First locate the reference object, adjust its state if needed, then search or place in the specified region.

Tasks containing prepositions like “under”, “inside”, or “on”.

tions

Reliability & Error Recovery

- gen 014 Loop Escape Trigger If the last 3–5 actions do not change the state, switch to an

untried search branch or action type.

After several consecutive noprogress observations.

- gen 015 Pre-Action Sanity


Confirm prerequisites (hand free, capacity, power) before executing manipulative commands.

Right before issuing any command that could legally fail.

Check

Table 6. Common Agent Failures and Mitigation Strategies for ALFWorld.

ID Failure Description Root Cause (Why it happens) Mitigation (How to avoid) err 001 Redundant Revisit Lacks explicit memory of explored areas; strat-

Maintain an exploration map; prioritize unvisited candidates.

egy degenerates into local loops.

err 006 Skipping State Changes Conflates object presence with goal satisfac-

Integrate state precondition checks into the planner before placement.

tion; omits cleanliness/temp checks.

Total wall-clock time: approximately 30 hours per experiment.

### C. Illustration of Skill Library

In this section, we provide some example catalog of distilled skills and error taxonomies for both the ALFWorld and WebShop environments. Tables 5 and 7 detail the general skills distilled for embodied manipulation and web-based shopping, respectively, highlighting the actionable principles required for systematic exploration and constraint satisfaction. Furthermore, we provide a structured analysis of failure cases in Table 6 and Table 8, which categorizes common mistakes, ranging from spatial reasoning loops in ALFWorld to price-shift oversights in WebShop, alongside their root causes and proposed mitigation strategies.

Table 7. Example distilled skills for WebShop Navigation (Yao et al., 2022a). These skills represent the strategic patterns used by the agent to handle large-scale product search and constraint satisfaction.

###### ID Skill Title Principle (Actionable Pattern) When to Apply

Search & Query Engineering

- gen 001 Prioritize Core Keywords Include product type, 1-2 functional attributes, and hard

constraints; omit secondary descriptors.

Before issuing the first search or refining over-specific queries.

- gen 002 Iterative Refinement Adjust keywords or apply site filters instead of repeat-

ing the same failed query.

When results are irrelevant or repeat despite multiple searches.

Product Evaluation & Verification

- gen 003 Scan Before You Click Read titles, thumbnails, and prices in results to ensure

plausibility before opening a link.

On search results pages when choosing the next product to inspect.

- gen 004 Verify Early, Abort Fast Immediately check category, attributes, and price on

the product page; leave if any constraint is violated.

Within the first observation on every product detail page.

- gen 006 Confirm Hidden Attributes Open Description/Features sections to ensure non-

visible specs (e.g., material) meet constraints.

When constraints are not evident from the title or variant list.

Configuration & Transaction gen 005 Set Mandatory Variants Always select required options (size, color, etc.) before

evaluating price or purchasing.

After confirming product match but before any purchase action.

- gen 007 Check Variant Pricing For price ranges, select the exact variant combination




Whenever price changes with variant selection or shows as a range.

to verify the specific price is within budget.

gen 013 Purchase Decisively Execute ’Buy Now’ immediately once all constraints

After validating every constraint on the current product variant.

and prices are confirmed on a variant.

Table 8. Common Failures in Web-based Shopping Tasks.

###### ID Failure Description Root Cause Mitigation Strategy

err 001 Missing Constraints in

Omits size or price caps, leading to overwhelming or irrelevant result sets.

Assemble full requirement list first; ensure every hard constraint is in the query string.

Query

- err 004 Price Shift Oversight Fails to notice price changes after selecting a

specific size or color variant.

Re-read the price element after every option change before proceeding to checkout.

- err 005 Premature Purchase Clicks “Buy Now” without setting mandatory


Validate that every required dropdown/radio option is explicitly selected before buying.

variants, leading to errors or wrong items.

err 009 Ignoring Stock Status Attempts to purchase out-of-stock items by

Verify that the ’Add to Cart’ button is enabled and no ’Out of Stock’ message is present postselection.

ignoring disabled buttons or stock labels.

err 011 Sponsored Link Distraction Clicks loosely matched ads, diverting the

Implement ad-label detection; prioritize organic listings for higher constraint reliability.

workflow from organic, suitable products.

### D. Additional Cases

- Case 1: WebShop Footwear (Functional Constraints) Task: I want a pair of men’s black slip-resistant work shoes, size 10, rubber sole, price lower than $50.00.

Skills [foo 002] Verify features in description; [foo 004] Confirm price after variant selection. Avoid [err 001] Omitting price cap; [err 003] Selecting wrong product category.

Agent Trajectory with Skill-Guided Reasoning

- Step 1 Obs: WebShop homepage. Think: Per [gen 001], I’ll include key constraints (type, function, color, price) in the query. Action: search[men black slip resistant work shoes rubber sole under 50]

- Step 2 Obs: Results: [1] Chef Shoes $38.99; [2] Kitchen Shoes $42.50; [3] Steel Toe Boots $55.99. Think: [gen 003] Item [1] is under budget and matches function. Item [3] is over budget (skip). Action: click[Item 1]

- Step 3 Obs: Product page. Price: $35.99-$45.99. Colors: Black, White. Sizes: 7-12. Think: [foo 002] Description confirms rubber sole. Now selecting Black and Size 10 [foo 003]. Action: click[Black] → click[10]


Step 5 Obs: Selected: Black, Size 10. Price updated to $38.99. Think: [foo 004] $38.99 ¡ $50. All constraints (color, size, function, price) are satisfied. Action: click[Buy Now]

Result: SUCCESS — Purchased at $38.99. Key Skills: [foo 002] (Verification), [foo 004] (Price Check).

- Case 2: Electronics (Speaker with Abort-and-Retry) Task: I need a portable bluetooth speaker, waterproof, black color, price lower than $30.00.


Skills [ele 001] Constraint-rich search; [ele 004] Bail on mismatch fast; [gen 002] Iterative refinement. Avoid [err 002] Overly specific variant names in search; [ele 006] Avoid click loops.

###### Agent Trajectory: Handling Missing Constraints

- Step 1 Obs: WebShop homepage. Think: [ele 001] Packing all mandatory attributes: portable, bluetooth, waterproof, black, ¡$30. Action: search[portable bluetooth speaker waterproof black under 30]

- Step 2 Obs: Results: [1] Waterproof Speaker $28.99; [2] Mini LED Speaker $19.99; [3] 20W Speaker $35.50. Think: [ele 005] Item [1] matches most keywords and price. Action: click[Item 1]

- Step 3 Obs: Product page (Item 1). Colors: Blue, Red, Green, Army Green. Black unavailable. Think: [gen 004] Verify Early, Abort Fast: No black option! [ele 004] Bail immediately to find another candidate. Action: click[Back to Search]

- Step 4 Obs: Back on search results. Think: [gen 002] Iterative refinement. Item [2] $19.99 is the next best candidate. Action: click[Item 2]

- Step 5 Obs: Product page (Item 2). Colors: Black, Blue, Red. Specs: IPX5 Waterproof. Think: [ele 002] Black is available! IPX5 confirms waterproof. Selecting Black. Action: click[Black]

- Step 6 Obs: Black selected. Final price: $19.99. Think: [ele 003] $19.99 ¡ $30. All specs (black, portable, waterproof) verified. Action: click[Buy Now]


Result: SUCCESS — Efficiently handled attribute mismatch via early exit. Key Skills Applied: [gen 004] (Abort Fast), [ele 004] (Bail on Mismatch).

#### Case 1: ALFWorld Clean Task (Lettuce → Sink → Countertop) Task: Clean some lettuce and put it in countertop.

Core Skills [cle 001] Phase-ordered plan (Locate → Clean → Place); [cle 006] Use location priors (Fridge for food). Mistakes Avoided [err 002] Skipping closed containers; [err 003] Ignoring visible target objects.

Step 1-3 Obs: Fridge 1 is closed. Action: open fridge 1 → take lettuce 1

Reasoning: Per [cle 006], food is likely in the fridge. [gen 002] Grab lettuce immediately on sight. Step 4-6 Obs: Arrive at sinkbasin 1. Action: clean lettuce 1 with sinkbasin 1

Reasoning: Per [cle 001] Phase 2: bring to water source. [cle 003] Go straight to sink. Step 7 Obs: Arrive at countertop 1. Action: put lettuce 1 in/on countertop 1

Reasoning: Per [gen 003] Destination First: place cleaned object immediately to finish.

- Result: SUCCESS (7 Steps) — Skills used: [gen 010] (Decomposition), [cle 003] (Sink First).

Case 2: ALFWorld Heat Task (Egg → Microwave → Countertop)

Task: Heat some egg and put it in countertop. Core Skills [hea 001] Secure exact target first; [hea 003] Open-Place-Heat sequence; [hea 004] No appliance before object. Step 1-3 Obs: Countertop 1 (no egg) → Countertop 2 (egg found). Action: take egg 1

Reasoning: [hea 004] Avoid microwave until object is held. [hea 002] Systematic search of surfaces. Step 4-6 Obs: Microwave 1 is closed. Action: open microwave 1 → heat egg 1

Reasoning: [hea 003] Correct sequence: open door first, then initiate state change. Step 7-8 Obs: Egg is heated. Action: go to countertop 1 → put egg 1

Reasoning: [hea 005] Direct Post-Heat Placement: move to target without detours.

- Result: SUCCESS (8 Steps) — Skills used: [hea 001] (Target First), [hea 004] (Sequence Control).


#### Case 3: ALFWorld Examine Task (Pencil ⊕ Desklamp → Success) Task: Look at pencil under the desklamp.

Core Skills [loo 001] Seek lamp surfaces (Desk/Sidetable); [loo 002] Switch lamp on; [exa 001] Pair objects early

(Target & Tool co-location).

Mistakes Avoided [err 003] Ignoring reachable targets; [loo 005] Preventing action loops (Toggle only once).

###### Agent Trajectory: High-Efficiency Co-location Handling

- Step 1 Obs: Mid-room. Visible: desk 1/2, drawer 1-3, sidetable 1, etc. Reasoning: [loo 001] Desklamps usually sit on desks. Prioritizing desk 1 to find both pencil and lamp in one go. Action: go to desk 1

- Step 2 Obs: On desk 1: alarmclock 1, desklamp 1, pencil 1. Reasoning: [exa 001] Successful co-location! Both objects are present. [exa 002] Pick up target first before interacting with the tool. Action: take pencil 1 from desk 1

- Step 3 Obs: Holding pencil 1. Reasoning: [loo 002] Toggle the lamp state to satisfy the ”under light” condition. [exa 004] Single toggle rule ensures no repeated actions. Action: use desklamp 1


Result: SUCCESS (Optimal 3 Steps) — Demonstrates superior spatial reasoning and zero-waste navigation. Key Skills: [exa 001] (Object Pairing), [loo 001] (Spatial Priors).

