---
type: source
kind: paper
title: Recursive Multi-Agent Systems (RecursiveMAS)
authors: Jiaru Zou et al.
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.25917
source_local: ../raw/2026-zou-recursive-multi-agent-systems.pdf
topic: agentic-harness
cites:
---

## arXiv:2604.25917v1[cs.AI]28Apr2026

![image 1](<2026-zou-recursive-multi-agent-systems_images/imageFile1.png>)

# Recursive Multi-Agent Systems

Xiyuan Yang1,*, Jiaru Zou1,2,*†, Rui Pan1, Ruizhong Qiu1, Pan Lu2, Shizhe Diao3, Jindong Jiang3, Hanghang Tong1, Tong Zhang1, Markus J. Buehler4, Jingrui He1 , James Zou2 1UIUC 2Stanford University 3NVIDIA 4MIT

*Equal Contribution, Alphabetical Order †Project Lead Corresponding Authors

Project Page: https://recursivemas.github.io

![image 2](<2026-zou-recursive-multi-agent-systems_images/imageFile2.png>)

Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. To optimize our framework, we develop an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses of runtime complexity and learning dynamics establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Empirically, we instantiate RecursiveMAS under 4 representative agent collaboration patterns and evaluate across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2×–2.4× end-to-end inference speedup, and 34.6%–75.6% token usage reduction.

RecursiveMAS Scaling Law

![image 3](<2026-zou-recursive-multi-agent-systems_images/imageFile3.png>)

###### Sequential-Style (Light)

![image 4](<2026-zou-recursive-multi-agent-systems_images/imageFile4.png>)

![image 5](<2026-zou-recursive-multi-agent-systems_images/imageFile5.png>)

![image 6](<2026-zou-recursive-multi-agent-systems_images/imageFile6.png>)

![image 7](<2026-zou-recursive-multi-agent-systems_images/imageFile7.png>)

Inference Recursion Round

Accuracy (%)

Training Recursion Round Training Recursion Round Training Recursion Round Training Recursion Round

Collaboration Patterns

![image 8](<2026-zou-recursive-multi-agent-systems_images/imageFile8.png>)

![image 9](<2026-zou-recursive-multi-agent-systems_images/imageFile9.png>)

![image 10](<2026-zou-recursive-multi-agent-systems_images/imageFile10.png>)

![image 11](<2026-zou-recursive-multi-agent-systems_images/imageFile11.png>)

![image 12](<2026-zou-recursive-multi-agent-systems_images/imageFile12.png>)

![image 13](<2026-zou-recursive-multi-agent-systems_images/imageFile13.png>)

![image 14](<2026-zou-recursive-multi-agent-systems_images/imageFile14.png>)

Speed-up 1.6×

1.5×

1.5×

1.5×

1.4×

Figure 1 | Performance Landscape of RecursiveMAS across Training/Inference Recursion Depths (Top): The lightweight RecursiveMAS with sub-1.5B agents shows a clean scaling trend as recursion deepens. Generalization across Common Collaboration Patterns (Bottom): The Scaled RecursiveMAS with stronger LLM agents (5-10B) seamlessly adapts to diverse multi-agent system structures.

Contact: jiaru@stanford.edu, xiyuany4@illinois.edu

##### 1. Introduction

To tackle complex tasks, a single language model often falls short due to limited capacity, myopic generation, or inefficient exploration of the solution space (Li et al., 2025b; Shojaee et al., 2025; Song et al., 2026). Once intelligence reaches a threshold, a natural direction is to treat individual models as specialized agents and organize them as a collaborative system (Tran et al., 2025; Xu et al., 2025). A multi-agent system (MAS) (Wang et al., 2025b; Wu et al., 2024) can scale performance by enabling individuals to work together and contribute complementary strengths. Consider a set of heterogeneous agents, each assigned a distinct role and expertise. The system can either arrange agents into a sequential pipeline (Gu et al., 2025; Qian et al., 2024) to progressively decompose and solve a problem, or engage and integrate multiple domain-specialized agents (Babu et al., 2025; Qian et al., 2025; Ye et al., 2025b) for the task.

While MAS establishes a structural foundation, the next question is how to enable the system to evolve over time and adapt to different scenarios. Prior work has explored prompt-based adaptation (Shen et al., 2025; Zhang et al., 2025b; Zhou et al., 2025), where model interactions are improved through the iterative refinement of shared context. Although these updated prompts can help agents generate more aligned responses to the question, each agent itself cannot improve. A more principled line of work is to optimize agents through learning (Motwani et al., 2024; Subramaniam et al., 2025; Zhao et al., 2025). However, training entire agents inside the system is hard, as updating all model parameters is non-trivial (Hu et al., 2025), and the sequential dependency in text-based interactions introduces substantial latency when agents must wait for others to complete generation.

Instead of improving each agent’s capabilities as a standalone component, we adopt a higher-level learning perspective and aim to co-evolve and scale the entire system as an integrated whole. We recast agent collaboration through the lens of recursive language models (RLMs) (Jolicoeur-Martineau, 2025; Zhang et al., 2025a; Zhu et al., 2025), where a shared set of layers is iteratively applied and optimized within a continuous latent space. In this view, the entire multi-agent system can be treated as a recursive computation, where each agent acts like an RLM layer, iteratively passing latent representations to the next and forming a looped interaction process.

We call this new system-level agentic recursion framework RecursiveMAS. Without updating all model parameters, agents are connected and iteratively optimized solely via the lightweight RecursiveLink, a two-layer residual projection module for latent states transmission and refinement. An inner RecursiveLink within each agent first consolidates the model’s ongoing latent thoughts between input and output spaces during auto-regressive generation. An outer RecursiveLink then bridges hidden representations across heterogeneous agents built on different model types and sizes, enabling seamless cross-agent interaction. Together, all agents are chained in a unified loop to perform iterative latent collaboration, with only the last agent producing the textual output in the final recursion round.

Correspondingly, we pair RecursiveMAS with an Inner-Outer Loop training paradigm for progressive co-optimization. The inner loop provides a preliminary model-level warm start for each agent, by training its inner RecursiveLink to better align with latent thoughts generation. The outer loop then trains the outer RecursiveLink across agents at the system-level, with gradients recursively backpropagated through the full computation traces over recursion rounds. By exposing each agent to the feedback of itself and others from previous rounds, RecursiveMAS learns to leverage RecursiveLink for iterative refinement of collaboration, thus enabling the entire system to optimize in a unified manner.

To justify why recursion should occur in latent space rather than text-mediated interaction, we provide two theoretical analyses on runtime complexity and learning dynamics. From an architectural standpoint, RecursiveLink enables direct transformation of latent-space information, avoiding repeated decoding of intermediate agents with more efficient runtime complexity. From the learning perspective,

latent-space connections in RecursiveMAS maintain stable gradient propagation flow across recursion rounds during training, avoiding the gradient vanishing induced by text-based interactions.

Empirically, we evaluate RecursiveMAS on 9 benchmarks spanning mathematics, science, medicine, search, and code generation. We instantiate RecursiveMAS with diverse model families, including Qwen3/3.5, LLama-3, Gemma3, and Mistral, and adapt our framework to 4 representative MAS collaboration scenarios: step-by-step sequential reasoning, mixture-of-experts collaboration, expert-tolearner knowledge distillation, and tool-integrated deliberation. As illustrated in Figure 1, compared with advanced recursive language models and MAS baselines, RecursiveMAS achieves an average accuracy improvement of 8.3%, while delivering 1.2×–2.4× inference speedup and reducing token usage by 34.6%–75.6%. In addition, RecursiveMAS is structure-agnostic and can generalize to various agent collaboration patterns with effective performance. Our additional detailed analyses of scaling laws with deeper recursion, RecursiveLink architectures, semantic distributions across recursions, and training cost further validate the efficiency and performance scalability of the RecursiveMAS.

##### 2. Preliminary

Auto-regressive Generation in Latent Space. Let 𝑓𝜃(·) denote a standard Transformer model (Vaswani et al., 2017) parameterized by 𝜃. Given a question 𝑥 with corresponding input embeddings 𝐸 = [𝑒1, . . . , 𝑒𝑡] ∈ ℝ𝑡×𝑑

ℎ, the model computes the last-layer hidden state ℎ𝑡 through the forward pass. In standard auto-regressive decoding, ℎ𝑡 is projected to the vocabulary space to predict the next token. In contrast, latent generation keeps the recurrence entirely in continuous representation space by directly feeding the previously generated latent embedding ℎ𝑡 back into the next forward pass. Formally, the next latent generation at step 𝑡 + 1 is:

ℎ𝑡+1 = 𝑓𝜃([𝐸≤𝑡; ℎ𝑡]). (1) We refer to the newly generated latent state ℎ𝑡+1 as the model’s ongoing latent thought.

Recursive Computation. A recursive language model (RLM) increases reasoning depth by reusing the same transformation across recurrent steps. Consider a Transformer 𝑓𝜃 with 𝐿 layer blocks, denoted as 𝑓𝜃 = M𝐿 ◦ · · · ◦ M1. Instead of passing the input through the 𝐿-layer stack only once to obtain the last representation, a recursive model reuses the same stack for 𝑛 times of forward iterations, i.e.,

𝐻(0) = 𝐸, 𝐻(𝑟) = 𝑓𝜃 𝐻(𝑟−1) , 𝑟 = 1, . . . , 𝑛. (2)

The last round of latent representation 𝐻(𝑛) is obtained through recursive refinement over the same shared Transformer layers, and is subsequently used for the final prediction.

LLM-based Multi-Agent Evolution. We define a multi-agent system S (Tran et al., 2025; Zou et al., 2025) composed of 𝑁 agents denoted as A = {𝐴1, . . . , 𝐴𝑁}, where each LLM agent 𝐴𝑖 corresponds to 𝑓𝜃𝑖 with its own last-layer representations 𝐻𝑖. We then denote the collective latent state of the system by H = {𝐻1, . . . , 𝐻𝑁}. Given any input problem 𝑥 with the ground-truth 𝑦, the system S orchestrates interactions among agents to collaboratively produce a final prediction. With this setup in place, we now formalize the evolution of agents under recursive computation.

###### Definition 2.1: Recursive Multi-Agent Evolution

A recursive evolution is the progressive refinement of H, where each agent adjusts its latent representation through iterative interaction with others and its own reasoning state, so that the updated

(2)

(1)

(𝑛)

· · · 𝐻

S(1) 𝐻

system is better aligned for the given problem, i.e. S(0) 𝐻

###### S(𝑛).

###### −−−−→

###### −−−−→

###### −−−−→

Evolve

Evolve

Evolve

Collaboration Pattern. As MAS architectures are generally not fixed and can vary across tasks, we do not restrict the collaboration pattern to a single style. In this paper, we consider four commonly

Latent Thoughts of A1 (Last-layer Embs)

Latent Thoughts of A2

Decode for Outputs

…

…

ℎ% ℎ%&'

ℎ%&(

(Final Round n)

Agent A1

###### …

(Recursion Rounds <n)

Agent A1

Agent A2

|Agent AN|
|---|


A2-aligned Input Embs

A1-aligned Input Embs

… …

…

#! #" ## …

##%! ##%"

Contexts

![image 15](<2026-zou-recursive-multi-agent-systems_images/imageFile15.png>)

Input Contexts

| | | | |
|---|---|---|---|
|O|ute|r Link| |
| | | | |
| | |…| |


![image 16](<2026-zou-recursive-multi-agent-systems_images/imageFile16.png>)

![image 17](<2026-zou-recursive-multi-agent-systems_images/imageFile17.png>)

Inner Link

Inner Link

###### Looping…

![image 18](<2026-zou-recursive-multi-agent-systems_images/imageFile18.png>)

(Instruction, Question, etc.)

…

ℎ% ℎ%&'

…

Condition Generated on A1

Figure 2 | Overall Architecture of RecursiveMAS. Each agent first leverages the inner RecursiveLink to perform latent thoughts generation, and then transfers the generated information to the next agent through the outer RecursiveLink. After the last agent finishes generation, its latent thoughts are fed back to the first agent, thereby forming a recursive loop within the multi-agent system.

![image 19](<2026-zou-recursive-multi-agent-systems_images/imageFile19.png>)

Looping… Looping…

![image 20](<2026-zou-recursive-multi-agent-systems_images/imageFile20.png>)

adopted collaboration patterns in multi-agent systems: (i) Sequential Style, where we follow the chain-of-agents setting to assign three agents with complementary roles of Planner, Critic, and Solver and progressively decompose, judge, refine, and solve the problem; (ii) Mixture Style, where a mixture of domain-specialized agents (Math, Code, Science) reasons over the input problem in parallel, and their outputs are aggregated by a Summarizer agent to form the final answer; (iii) Distillation Style, where a larger, more capable Expert agent is paired with a smaller, faster Learner agent to distill expert knowledge while retaining higher generation efficiency; and (iv) Deliberation Style, where an inner-thinking Reflector is paired with a Tool-Caller that can invoke external tools (e.g., Python or search APIs). The agents iteratively exchange, critique, and refine candidate solutions until reaching a shared consensus, after which the Tool-Caller produces the final answer.

##### 3. Building a Recursive Multi-Agent System

We introduce RecursiveMAS, an end-to-end recursive framework that links heterogeneous LLM agents together to scale the entire system through efficient and seamless latent collaboration. In the following, we will first elaborate the detailed architectural design of RecursiveMAS, and then present the corresponding recursive learning algorithm. We also interleave theoretical analyses throughout the method pipeline to support underlying design principles.

###### 3.1. A Lightweight RecursiveLink

###### RecursiveLink

![image 21](<2026-zou-recursive-multi-agent-systems_images/imageFile21.png>)

A language model’s last-layer hidden states provide a natural representation of its generated semantics. The RecursiveLink R is designed to preserve and transmit this information from one embedding space to another. In RecursiveMAS, the transition arises in two cases: (i) Denseto-Shallow Transition, where the previous step’s last-layer embeddings are fed back as the next-step input embeddings during latent thoughts generation; and (ii) CrossModel Transition, where one model’s newly generated latent representations are passed as conditioning inputs to another model. As illustrated in Figure 3, we bridge these two transitions through the inner and outer links.

Last-layer Emb

- Agent Ai Emb
- Agent Aj Emb


Linear

Linear

Linear

GELU

GELU

Linear

Linear

Residual Connection

Residual

Connection

+

+

Input-layer Emb

Inner Outer

(Same Agent)

Figure 3 | Illustration on the inner and outer RecursiveLink Design.

Inner Link. Each LLM agent 𝐴𝑖 ∈ A is paired with an inner RecursiveLink Rin during auto-regressive generation. Given any new last-layer embedding vector ℎ, Rin transforms it as:

Rin(ℎ) = ℎ + 𝑊2 𝜎(𝑊1ℎ), (3)

where 𝑊1 and 𝑊2 are two standard linear layers, 𝜎(·) is the GELU activation, and the residual connection preserves the original latent semantics. The transformed embedding is then used as input to the next forward pass of agent 𝐴𝑖.

Outer Link. An outer RecursiveLink Rout connects heterogeneous agents with different hidden dimensions. To support this, an additional linear layer 𝑊3 is introduced in the residual branch to map the source embedding from agent 𝐴𝑖 into the target embedding space of agent 𝐴𝑗, i.e.,

Rout(ℎ) = 𝑊3ℎ + 𝑊2 𝜎(𝑊1ℎ). (4)

###### Why Residual Connection?

The residual branch largely preserves the original semantics of the input, allowing the RecursiveLink network to focus on aligning distributional differences rather than learning the full projection from scratch. This leads to more stable and efficient training. We also explore other alternatives and empirically validate our proposed design in Section 5.

###### 3.2. Chain All Agents Together as a Loop

In recursive language models (RLMs), Transformer layers are connected through hidden states, and the residual stream loops across these layers to increase reasoning depth. Under this view, we cast each agent in RecursiveMAS as an RLM layer, with information flowing and recurring within and across agents as the hidden stream of the system. As shown in Figure 2, each agent contributes by reasoning and interacting with others in the latent space, together forming a recursive loop.

Latent Thoughts Generation inside Agents. We start by describing how each agent unfolds reasoning through the auto-regressive generation of latent thoughts. Specifically, given input contexts’ embeddings 𝐸𝐴1 = [𝑒1, 𝑒2, . . . , 𝑒𝑡] for the question and the agent-specific instructions, the first agent 𝐴1 passes 𝐸𝐴1 through the Transformer and computes the last-layer hidden representation ℎ𝑡 at step 𝑡. Then, we insert ℎ𝑡 into the inner link Rin to map the distribution back into the input embedding space for the next step, yielding 𝑒𝑡+1 = Rin(ℎ𝑡). Agent 𝐴1 repeats this process auto-regressively for 𝑚 forward steps, generating a new continuous sequence of latent thoughts 𝐻𝐴1 = [ℎ𝑡, ℎ𝑡+1, . . . , ℎ𝑡+𝑚].

Interaction across Heterogeneous Agents. Once agent 𝐴1 completes latent reasoning, its latent thoughts 𝐻𝐴1 are sent to the next agent 𝐴2 for cross-agent interaction. To achieve seamless information transmission across different types of agents, we first pass 𝐻𝐴1 through the outer link Rout to transform it into input embeddings aligned with agent 𝐴2. Next, agent 𝐴2 starts latent thoughts generation conditioned on both its own input contexts and transferred information from 𝐴1 (i.e., 𝐸𝐴2 ⊕Rout(𝐻𝐴1)). We continue this interaction process across all consecutive agents in RecursiveMAS. In particular, after the last agent 𝐴𝑁 completes latent thoughts generation, its latent outputs (representing the system’s latent answer to the input question) are passed back to the first agent 𝐴1 through the inner-outer RecursiveLink, thereby closing the recursive loop. This recurrent connection allows each new recursion round to condition on information produced in previous rounds, so that each agent can iteratively reflect on earlier system outputs and refine their current generation. Throughout intermediate recursion rounds, all agents collaborate entirely in the latent space. Only after the final recursion round, the agent 𝐴𝑁 decodes the textual output as the system’s final answer to the question.

Preliminary Inner-Loop Training (Each Agent)

Parallelly Inner-train A1, A2, …, AN

Agent A1 Inner-Training

![image 22](<2026-zou-recursive-multi-agent-systems_images/imageFile22.png>)

###### After Inner-Training

Connect Train & Optimize

![image 23](<2026-zou-recursive-multi-agent-systems_images/imageFile23.png>)

![image 24](<2026-zou-recursive-multi-agent-systems_images/imageFile24.png>)

![image 25](<2026-zou-recursive-multi-agent-systems_images/imageFile25.png>)

![image 26](<2026-zou-recursive-multi-agent-systems_images/imageFile26.png>)

![image 27](<2026-zou-recursive-multi-agent-systems_images/imageFile27.png>)

Support Latent Reasoning Refine Latent Thoughts Ready to Start Recursion

![image 28](<2026-zou-recursive-multi-agent-systems_images/imageFile28.png>)

![image 29](<2026-zou-recursive-multi-agent-systems_images/imageFile29.png>)

Regression Loss

![image 30](<2026-zou-recursive-multi-agent-systems_images/imageFile30.png>)

Agent A1

![image 31](<2026-zou-recursive-multi-agent-systems_images/imageFile31.png>)

![image 32](<2026-zou-recursive-multi-agent-systems_images/imageFile32.png>)

![image 33](<2026-zou-recursive-multi-agent-systems_images/imageFile33.png>)

Agent A1

![image 34](<2026-zou-recursive-multi-agent-systems_images/imageFile34.png>)

![image 35](<2026-zou-recursive-multi-agent-systems_images/imageFile35.png>)

![image 36](<2026-zou-recursive-multi-agent-systems_images/imageFile36.png>)

![image 37](<2026-zou-recursive-multi-agent-systems_images/imageFile37.png>)

![image 38](<2026-zou-recursive-multi-agent-systems_images/imageFile38.png>)

![image 39](<2026-zou-recursive-multi-agent-systems_images/imageFile39.png>)

Ground-Truth Distribution

Predicted Latent Thoughts

![image 40](<2026-zou-recursive-multi-agent-systems_images/imageFile40.png>)

Inner Link of A1

x N

###### Recursive Outer-Loop Training (Entire MAS)

Forward Pass Backward Propagation

- Recursion Round 1 Outer-Training
- Recursion Round 2 Outer-Training


![image 41](<2026-zou-recursive-multi-agent-systems_images/imageFile41.png>)

![image 42](<2026-zou-recursive-multi-agent-systems_images/imageFile42.png>)

![image 43](<2026-zou-recursive-multi-agent-systems_images/imageFile43.png>)

Connect

![image 44](<2026-zou-recursive-multi-agent-systems_images/imageFile44.png>)

![image 45](<2026-zou-recursive-multi-agent-systems_images/imageFile45.png>)

![image 46](<2026-zou-recursive-multi-agent-systems_images/imageFile46.png>)

![image 47](<2026-zou-recursive-multi-agent-systems_images/imageFile47.png>)

![image 48](<2026-zou-recursive-multi-agent-systems_images/imageFile48.png>)

![image 49](<2026-zou-recursive-multi-agent-systems_images/imageFile49.png>)

![image 50](<2026-zou-recursive-multi-agent-systems_images/imageFile50.png>)

![image 51](<2026-zou-recursive-multi-agent-systems_images/imageFile51.png>)

![image 52](<2026-zou-recursive-multi-agent-systems_images/imageFile52.png>)

#### …

Input Contexts

Input Contexts

![image 53](<2026-zou-recursive-multi-agent-systems_images/imageFile53.png>)

![image 54](<2026-zou-recursive-multi-agent-systems_images/imageFile54.png>)

![image 55](<2026-zou-recursive-multi-agent-systems_images/imageFile55.png>)

![image 56](<2026-zou-recursive-multi-agent-systems_images/imageFile56.png>)

![image 57](<2026-zou-recursive-multi-agent-systems_images/imageFile57.png>)

![image 58](<2026-zou-recursive-multi-agent-systems_images/imageFile58.png>)

![image 59](<2026-zou-recursive-multi-agent-systems_images/imageFile59.png>)

![image 60](<2026-zou-recursive-multi-agent-systems_images/imageFile60.png>)

![image 61](<2026-zou-recursive-multi-agent-systems_images/imageFile61.png>)

![image 62](<2026-zou-recursive-multi-agent-systems_images/imageFile62.png>)

Agent A1

Agent A2

![image 63](<2026-zou-recursive-multi-agent-systems_images/imageFile63.png>)

![image 64](<2026-zou-recursive-multi-agent-systems_images/imageFile64.png>)

![image 65](<2026-zou-recursive-multi-agent-systems_images/imageFile65.png>)

Agent AN

![image 66](<2026-zou-recursive-multi-agent-systems_images/imageFile66.png>)

![image 67](<2026-zou-recursive-multi-agent-systems_images/imageFile67.png>)

![image 68](<2026-zou-recursive-multi-agent-systems_images/imageFile68.png>)

![image 69](<2026-zou-recursive-multi-agent-systems_images/imageFile69.png>)

![image 70](<2026-zou-recursive-multi-agent-systems_images/imageFile70.png>)

![image 71](<2026-zou-recursive-multi-agent-systems_images/imageFile71.png>)

![image 72](<2026-zou-recursive-multi-agent-systems_images/imageFile72.png>)

![image 73](<2026-zou-recursive-multi-agent-systems_images/imageFile73.png>)

![image 74](<2026-zou-recursive-multi-agent-systems_images/imageFile74.png>)

![image 75](<2026-zou-recursive-multi-agent-systems_images/imageFile75.png>)

![image 76](<2026-zou-recursive-multi-agent-systems_images/imageFile76.png>)

![image 77](<2026-zou-recursive-multi-agent-systems_images/imageFile77.png>)

![image 78](<2026-zou-recursive-multi-agent-systems_images/imageFile78.png>)

![image 79](<2026-zou-recursive-multi-agent-systems_images/imageFile79.png>)

! !

![image 80](<2026-zou-recursive-multi-agent-systems_images/imageFile80.png>)

![image 81](<2026-zou-recursive-multi-agent-systems_images/imageFile81.png>)

![image 82](<2026-zou-recursive-multi-agent-systems_images/imageFile82.png>)

![image 83](<2026-zou-recursive-multi-agent-systems_images/imageFile83.png>)

![image 84](<2026-zou-recursive-multi-agent-systems_images/imageFile84.png>)

Outer Link of A1,A2

Outer Link of AN,A1

Outer Link of A2,A3

Latent Outputs

![image 85](<2026-zou-recursive-multi-agent-systems_images/imageFile85.png>)

![image 86](<2026-zou-recursive-multi-agent-systems_images/imageFile86.png>)

![image 87](<2026-zou-recursive-multi-agent-systems_images/imageFile87.png>)

![image 88](<2026-zou-recursive-multi-agent-systems_images/imageFile88.png>)

![image 89](<2026-zou-recursive-multi-agent-systems_images/imageFile89.png>)

![image 90](<2026-zou-recursive-multi-agent-systems_images/imageFile90.png>)

![image 91](<2026-zou-recursive-multi-agent-systems_images/imageFile91.png>)

![image 92](<2026-zou-recursive-multi-agent-systems_images/imageFile92.png>)

![image 93](<2026-zou-recursive-multi-agent-systems_images/imageFile93.png>)

![image 94](<2026-zou-recursive-multi-agent-systems_images/imageFile94.png>)

![image 95](<2026-zou-recursive-multi-agent-systems_images/imageFile95.png>)

![image 96](<2026-zou-recursive-multi-agent-systems_images/imageFile96.png>)

#### …

![image 97](<2026-zou-recursive-multi-agent-systems_images/imageFile97.png>)

Input

![image 98](<2026-zou-recursive-multi-agent-systems_images/imageFile98.png>)

![image 99](<2026-zou-recursive-multi-agent-systems_images/imageFile99.png>)

![image 100](<2026-zou-recursive-multi-agent-systems_images/imageFile100.png>)

![image 101](<2026-zou-recursive-multi-agent-systems_images/imageFile101.png>)

![image 102](<2026-zou-recursive-multi-agent-systems_images/imageFile102.png>)

![image 103](<2026-zou-recursive-multi-agent-systems_images/imageFile103.png>)

![image 104](<2026-zou-recursive-multi-agent-systems_images/imageFile104.png>)

![image 105](<2026-zou-recursive-multi-agent-systems_images/imageFile105.png>)

![image 106](<2026-zou-recursive-multi-agent-systems_images/imageFile106.png>)

Agent A1

Agent A2

![image 107](<2026-zou-recursive-multi-agent-systems_images/imageFile107.png>)

![image 108](<2026-zou-recursive-multi-agent-systems_images/imageFile108.png>)

![image 109](<2026-zou-recursive-multi-agent-systems_images/imageFile109.png>)

Contexts +

Agent AN

![image 110](<2026-zou-recursive-multi-agent-systems_images/imageFile110.png>)

![image 111](<2026-zou-recursive-multi-agent-systems_images/imageFile111.png>)

![image 112](<2026-zou-recursive-multi-agent-systems_images/imageFile112.png>)

![image 113](<2026-zou-recursive-multi-agent-systems_images/imageFile113.png>)

![image 114](<2026-zou-recursive-multi-agent-systems_images/imageFile114.png>)

![image 115](<2026-zou-recursive-multi-agent-systems_images/imageFile115.png>)

![image 116](<2026-zou-recursive-multi-agent-systems_images/imageFile116.png>)

![image 117](<2026-zou-recursive-multi-agent-systems_images/imageFile117.png>)

![image 118](<2026-zou-recursive-multi-agent-systems_images/imageFile118.png>)

![image 119](<2026-zou-recursive-multi-agent-systems_images/imageFile119.png>)

![image 120](<2026-zou-recursive-multi-agent-systems_images/imageFile120.png>)

! "

![image 121](<2026-zou-recursive-multi-agent-systems_images/imageFile121.png>)

![image 122](<2026-zou-recursive-multi-agent-systems_images/imageFile122.png>)

![image 123](<2026-zou-recursive-multi-agent-systems_images/imageFile123.png>)

![image 124](<2026-zou-recursive-multi-agent-systems_images/imageFile124.png>)

![image 125](<2026-zou-recursive-multi-agent-systems_images/imageFile125.png>)

![image 126](<2026-zou-recursive-multi-agent-systems_images/imageFile126.png>)

![image 127](<2026-zou-recursive-multi-agent-systems_images/imageFile127.png>)

![image 128](<2026-zou-recursive-multi-agent-systems_images/imageFile128.png>)

Outer Link of A1,A2

Outer Link of AN,A1

Outer Link of A2,A3

…

Latent Outputs

Recursion Round n Outer-Training

![image 129](<2026-zou-recursive-multi-agent-systems_images/imageFile129.png>)

![image 130](<2026-zou-recursive-multi-agent-systems_images/imageFile130.png>)

CE Loss

![image 131](<2026-zou-recursive-multi-agent-systems_images/imageFile131.png>)

![image 132](<2026-zou-recursive-multi-agent-systems_images/imageFile132.png>)

![image 133](<2026-zou-recursive-multi-agent-systems_images/imageFile133.png>)

![image 134](<2026-zou-recursive-multi-agent-systems_images/imageFile134.png>)

![image 135](<2026-zou-recursive-multi-agent-systems_images/imageFile135.png>)

![image 136](<2026-zou-recursive-multi-agent-systems_images/imageFile136.png>)

+ … Agent AN

![image 137](<2026-zou-recursive-multi-agent-systems_images/imageFile137.png>)

Input Contexts

![image 138](<2026-zou-recursive-multi-agent-systems_images/imageFile138.png>)

![image 139](<2026-zou-recursive-multi-agent-systems_images/imageFile139.png>)

![image 140](<2026-zou-recursive-multi-agent-systems_images/imageFile140.png>)

![image 141](<2026-zou-recursive-multi-agent-systems_images/imageFile141.png>)

![image 142](<2026-zou-recursive-multi-agent-systems_images/imageFile142.png>)

![image 143](<2026-zou-recursive-multi-agent-systems_images/imageFile143.png>)

![image 144](<2026-zou-recursive-multi-agent-systems_images/imageFile144.png>)

![image 145](<2026-zou-recursive-multi-agent-systems_images/imageFile145.png>)

![image 146](<2026-zou-recursive-multi-agent-systems_images/imageFile146.png>)

Agent A1

Agent A2

![image 147](<2026-zou-recursive-multi-agent-systems_images/imageFile147.png>)

![image 148](<2026-zou-recursive-multi-agent-systems_images/imageFile148.png>)

![image 149](<2026-zou-recursive-multi-agent-systems_images/imageFile149.png>)

![image 150](<2026-zou-recursive-multi-agent-systems_images/imageFile150.png>)

![image 151](<2026-zou-recursive-multi-agent-systems_images/imageFile151.png>)

![image 152](<2026-zou-recursive-multi-agent-systems_images/imageFile152.png>)

![image 153](<2026-zou-recursive-multi-agent-systems_images/imageFile153.png>)

![image 154](<2026-zou-recursive-multi-agent-systems_images/imageFile154.png>)

![image 155](<2026-zou-recursive-multi-agent-systems_images/imageFile155.png>)

![image 156](<2026-zou-recursive-multi-agent-systems_images/imageFile156.png>)

![image 157](<2026-zou-recursive-multi-agent-systems_images/imageFile157.png>)

![image 158](<2026-zou-recursive-multi-agent-systems_images/imageFile158.png>)

! #

![image 159](<2026-zou-recursive-multi-agent-systems_images/imageFile159.png>)

![image 160](<2026-zou-recursive-multi-agent-systems_images/imageFile160.png>)

LM Head of AN

Outer Link of A1,A2

Outer Link of A2,A3

Final Text Outputs

- Figure 4 | Two-Stage Training Pipeline of RecursiveMAS. We first perform inner-loop training for each agent in parallel to warm up the inner RecursiveLink for latent thoughts generation, and then conduct outer-loop training to recursively optimize the outer RecursiveLink over the entire system.


End-to-End Complexity Analyses. To characterize the architectural efficiency of the full RecursiveMAS pipeline, we next analyze its end-to-end runtime complexity with RecursiveLink integrated throughout the system. The following proposition compares RecursiveMAS with a text-based recursive MAS, in which agents follow the same multi-round recursive collaboration structure but communicate through an explicit text medium rather than RecursiveLink-enabled latent interaction.

Proposition 3.1 (RecursiveMAS Runtime Complexity). Without RecursiveLink, a text-based Recursive MAS with the same collaboration structure requires runtime complexity of Θ(𝑁(𝑚|𝑉|𝑑ℎ + (𝑡 +𝑚)𝑑ℎ2 + (𝑡 +𝑚)2𝑑ℎ)); In contrast, with RecursiveLink-enabled collaboration, RecursiveMAS achieves an end-to-end runtime complexity of Θ(𝑁(𝑚𝑑ℎ2 + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ)).

Remark 3.2. Since 𝑑ℎ ≪ |𝑉| in practice, RecursiveMAS replaces the expensive per-step vocabularyspace decoding cost 𝑚|𝑉|𝑑ℎ with a much more efficient latent-space transformation 𝑚𝑑ℎ2.

Proposition 3.1 shows the end-to-end runtime advantage of RecursiveMAS. The full proof is provided in Appendix A.1. We also empirically analyze the efficiency advantage of our method in Section 5.

##### 4. Learning to Recur as a Whole

With the framework in place, we next present the recursive learning algorithm, which only needs to train on the RecursiveLink to enable co-optimization of the entire system loop. As illustrated in Figure 4, the learning procedure consists of two stages: (i) a preliminary inner-loop to equip each agent with stronger latent thoughts generation capabilities; and (ii) an iterative outer-loop to progressively optimize the system as one unified entity over recursion rounds.

Model-Level Inner-Loop Training. For practical deployment of RecursiveMAS, we directly adopt off-the-shelf text-generation models as agents. To adapt these agents to the latent thoughts generation pattern, we first warm-start them through the inner RecursiveLink Rin. Specifically, given each agent 𝐴𝑖 ∈ A with parameters 𝜃𝑖 and the training example (𝑥, 𝑦) ∈ Dtrain, we construct the target latent thoughts distribution by passing the ground-truth text 𝑦 through the standard input embedding layer Emb𝜃

of agent 𝐴𝑖. The objective of training the inner link Rin corresponding to 𝐴𝑖 then formulates as:

𝑖

𝑖(𝑦) , (5) where 𝐻 denotes the last-layer latent thoughts generated by agent 𝐴𝑖, and cos(·, ·) denotes the standard cosine similarity. The regression objective here encourages each agent to leverage its inner link Rin to align latent thoughts with the semantic distribution from the input embedding layer, while eliminating the process of explicit decoding and re-encoding.

Lin = 1 − cos Rin(𝐻), Emb𝜃

System-Level Outer-Loop Training. Next, we iteratively co-optimize the entire system through the outer RecursiveLink Rout. Let S(𝑟) denote the system state at recursion round 𝑟 = 1, . . . , 𝑛. During outer-loop training, the system is first unrolled along its looped structure for 𝑛 forward rounds. After the final textual prediction is produced in the last recursion round, we jointly optimize all outer links that connect the system with the following cross-entropy (CE) objective:

Lout = CE S(𝑛) S(𝑛−1)(· · · S(1)(𝑥)) , 𝑦 . (6)

Throughout training, the computation graph is preserved along the full recursive paths. Gradient backpropagation assigns each outer link a shared credit signal according to its global contribution to the final prediction, thereby enabling information flow to be iteratively optimized as a whole.

Learning Advantage of RecursiveMAS. To better understand why latent collaboration of agents in the inner-outer loop training confers a stronger learning advantage, we provide a detailed theoretical analysis below of the gradient propagation process throughout recursive training of RecursiveMAS.

Theorem 4.1 (Gradient Stability). Under the Realistic Assumptions (stated in Appendix A.2), if tokens are confident with entropy ≤ 𝜖, where typically 𝜖 ≪ 1: directly applying text-based SFT (denoted by Rtext(ℎ)) during recursion suffers from gradient vanishing (i.e., gradient norm close to 0); while RecursiveMAS with the RecursiveLink R maintains stable and near constant gradients (i.e., gradient norm close to 1) during looped backpropagation process. Formally, with probability ≥ 1 − 𝛿,

√︄ 1

1

𝜕R(ℎ) 𝜕ℎ 2 ≥ Ω 1 −

𝜕Rtext(ℎ) 𝜕ℎ 2 ≤ 𝑂(𝜖) ≪ 1,

log

. (7)

𝑑ℎ

𝛿

The full proof is provided in Appendix A.3. Theorem 4.1 demonstrates the learning advantage of RecursiveMAS, by allowing gradients to remain informative across recursion rounds. Together, theoretical justifications in Proposition 3.1 and Theorem 4.1 motivate our design of latent-based interaction among agents rather than text mediation, as it makes the whole-system co-optimization of RecursiveMAS easier and more effective. During inference, RecursiveMAS performs recursive generation by following the same 𝑛 recursion rounds as in the outer-loop training.

- Table 1 | Agent configurations for different collaboration patterns in RecursiveMAS. We select off-the-shelf models from diverse model families to form heterogeneous agent compositions with complementary strengths. Each assignment is chosen to match the role-specific needs of the corresponding collaboration pattern while preserving both practical efficiency and scalability.


Collaboration Pattern Role Model Size & Version

Planner Qwen3-1.7B (Yang et al., 2025)

Sequential Style (Light)

Critic Llama3.2-1B-Instruct (Grattafiori et al., 2024)

- Solver Qwen2.5-Math-1.5B-Instruct (Qwen et al., 2025)

Sequential Style (Scaled)

Planner Gemma3-4B-it (Team et al., 2025)

Critic Llama3.2-3B-Instruct (Grattafiori et al., 2024)

- Solver Qwen3.5-4B (Yang et al., 2025)


Code Specialist Qwen2.5-Coder-3B-Instruct (Hui et al., 2024)

Science Specialist BioMistral-7B (Labrak et al., 2024)

Mixture Style

Math Specialist DeepSeek-R1-Distill-Qwen-1.5B (Qwen et al., 2025)

Summarizer Qwen3.5-2B (Yang et al., 2025)

Learner Qwen3.5-4B (Yang et al., 2025) Expert Qwen3.5-9B (Yang et al., 2025)

Distillation Style

Reflector Qwen3.5-4B (Yang et al., 2025)

Deliberation Style

Tool-Caller Qwen3.5-4B (with Tool-Integration) (Yang et al., 2025)

##### 5. Empirical Evaluations

Tasks and Datasets. We conduct comprehensive evaluations of RecursiveMAS on nine benchmarks across various domains: (i) Mathematical Reasoning, including MATH500 (HuggingFaceH4, 2023), AIME2025 (math ai, 2025), and AIME2026 (MathArena, 2026); (ii) Scientific and Medical Tasks, including GPQA-Diamond (Rein et al., 2023) and MedQA (Yang et al., 2024a); (iii) Code Generation, including LiveCodeBench-v6 (Jain et al., 2025) and MBPP Plus (Liu et al., 2023); and (iv) Search QA, including HotpotQA (Yang et al., 2018) and Bamboogle (Press et al., 2023). We adopt the standard evaluation metric for each dataset. For AIME2025/2026, we report Pass@10 accuracy for testing robustness. Additional benchmark and metrics details are in Appendix B.1.

Models and Baselines. We instantiate RecursiveMAS with diverse agent collaboration patterns, including (i) Sequential Style, (ii) Mixture Style, (iii) Distillation Style, and (iv) Deliberation Style, following the setups described in Section 2. For each collaboration style, we use off-the-shelf LLMs from diverse model families, covering Qwen (Qwen et al., 2025; Yang et al., 2025), Llama (Grattafiori et al., 2024), Gemma (Team et al., 2025), and Mistral (Jiang et al., 2024), to construct heterogeneous agent compositions. Detailed model configurations and their assigned roles are provided in Table 1.

For baseline comparisons, we evaluate RecursiveMAS against (i) Single Advanced Agents, where individual LLM agents from each collaboration pattern are isolated as standalone models to solve problems, such as the final agent in Sequential Style and each domain specialist in Mixture Style. For fair comparison, we provide full supervised and LoRA fine-tuning (Schulman and Lab, 2025) for single models on the same training set. (ii) Recursion-based Methods, including single recursive language models, LoopLM (Zhu et al., 2025), and Recursive-TextMAS, where agents collaborate in the same way as RecursiveMAS but interact through text instead of latent thoughts; and (iii) additional Representative Multi-Agent Frameworks, including TextGrad (Yuksekgonul et al., 2025) and

- Table 2 | Main results of RecursiveMAS over Different Recursion Rounds. We report the accuracy (%, “Acc.”), end-to-end runtime (s, “Time”), and overall token usage (“Token”) across domains. For Code Gen., we evaluate the Light and Scaled settings on MBPP+ and LiveCodeBench, respectively. The average standard deviation of RecursiveMAS across 5 runs is ±0.0041 for accuracy, ±26 for runtime, and ±33 for tokens. We compare with all methods under the same MAS framework structure and recursion budgets. The performance and efficiency advantages of RecursiveMAS become increasingly significant as the recursion round 𝑟 increases, with improvements highlighted.


Math500 AIME2025 AIME2026 GPQA-D MedQA Code Gen.

Method Metric

Improve Light Scaled Light Scaled Light Scaled Light Scaled Light Scaled Light Scaled

- Recursive Round r=1

|Recursive-TextMAS<br><br>|Acc. Time Token|71.9 84.2 24.0 71.3 16.7 76.7 1368 2401 2380 8462 2216 9376 1185 1471 2993 9397 2754 8854<br><br>|28.1 61.5 29.0 76.1 1056 2190 1555 1522 2084 3693 2382 1427|30.7 38.5 976 8867<br><br>1146 3154|Base Base Base<br><br>|
|---|---|---|---|---|---|
|RecursiveMAS|Acc. Time Token<br><br>|75.8 86.3 30.7 80.0 17.3 82.7 825 1701 1829 7784 1788 8134 523 816 1622 6338 1576 7021<br><br>|30.3 63.1 30.3 78.2 586 1965 1194 1348 829 2675 1369 964<br><br>|35.1 40.1 449 7908 577 2198<br><br>|↑ 3.4 ×1.2 ↓ 34.6%<br><br>|


- Recursive Round r=2

|Recursive-TextMAS<br><br>|Acc. Time Token|72.5 84.4 23.3 70.7 10.0 77.3<br><br>2204 3958 4247 14380 3960 14110 2117 2794 5318 16372 4982 16213<br><br>|28.7 59.1 28.3 76.1 1825 4207 3097 2745 3708 6128 4436 2609<br><br>|30.0 38.0 1847 14792 1998 5369|Base Base Base<br><br>|
|---|---|---|---|---|---|
|RecursiveMAS|Acc. Time Token<br><br>|76.6 87.1 33.3 86.0 18.7 84.0 1096 1974 2367 8178 2263 8965<br><br>495 953 1614 5314 1552 6657<br><br>|32.3 64.6 31.2 78.3 752 2342 1427 1664 813 2521 1383 1008<br><br>|36.9 41.3 627 8329 531 2020<br><br>|↑ 6.0 ×1.9 ↓ 65.5%<br><br>|


- Recursive Round r=3


|Recursive-TextMAS|Acc. Time Token<br><br>|69.1 85.8 18.0 73.3 16.7 74.7 2952 6010 6183 19304 5907 19678 3059 4100 8645 23651 7813 22915|28.7 58.6 28.5 77.1 3322 7537 4684 3922 5820 8091 6307 3731<br><br>|29.3 36.5 2310 22036 2676 7078|Base Base Base<br><br>|
|---|---|---|---|---|---|
|RecursiveMAS|Acc. Time Token<br><br>|77.8 88.2 34.0 86.7 20.0 86.0 1360 2320 2727 8981 2629 9623<br><br>519 893 1586 5342 1537 6860<br><br>|32.6 66.2 31.7 79.3 861 2638 1704 1912 786 2524 1378 1056<br><br>|37.4 42.8 805 10186 595 2247<br><br>|↑ 7.2 ×2.4 ↓ 75.6%<br><br>|


Mixture-of-Agents (MoA) (Wang et al., 2025b) for more holistic structure-wide evaluations. Detailed baseline implementations are provided in Appendix B.2.

Training and Implementation Details. For inner-outer loop training, we freeze all LLM agent parameters and update only the inner/outer RecursiveLink. We curate a diverse training set spanning multiple domains, sourced from s1K (Muennighoff et al., 2025) for mathematical problem solving, m1k (Huang et al., 2025) for medical and scientific tasks, OpenCodeReasoning (Ahmad et al., 2025) for code generation, and ARPO-SFT (Dong et al., 2025) for agentic tool-augmentation (Python Code/Search-API) settings. We use AdamW with a learning rate of 5e-4, a cosine learning rate scheduler, and a batch size of 4. During inference, we set top-p to 0.95 and use a temperature of 0.6 for most reasoning tasks and 0.2 for code generation, as suggested in each model’s official report. The maximum output length is adjusted for each task based on its relative difficulty. We perform hyperparameter tuning and report the mean performance over five independent runs. More training/inference details and hyperparameter setups are provided in Appendix B.3.

###### 5.1. Scaling Performance via Recursion

We begin by evaluating how RecursiveMAS performs across different recursion depths 𝑟 = 1, 2, 3. As shown in Table 2, we analyze agent collaboration behavior from three complementary perspectives: (i) accuracy, (ii) end-to-end runtime, and (iii) overall system token throughput. We also include a text-based recursive baseline for reference. Across seven math, science, and code generation tasks, both light and scaled versions of RecursiveMAS exhibit a consistent upward trend as recursion depth

###### Table 3 | Comparison of RecursiveMAS with Other Methods. We evaluate RecursiveMAS at recursion round 𝑟 = 3. Under the same training budget and model setups, RecursiveMAS consistently outperforms advanced single-agent methods, alternative MAS frameworks, and recursive computation baselines.

###### Method MATH500 AIME2025 AIME2026 GPQA-D LiveCodeBench MedQA

Single Agent (w/ LoRA) 83.1 70.0 73.3 62.0 37.4 76.1 Single Agent (w/ Full-SFT) 83.2 73.3 76.7 62.8 38.6 77.0

Mixture-of-Agents (MoA) 79.8 60.0 63.3 47.6 27.0 57.5 TextGrad 84.9 73.3 76.7 62.5 39.8 77.2

LoopLM 84.6 66.7 63.3 48.1 24.9 56.4 Recursive-TextMAS 85.8 73.3 73.3 61.6 38.7 77.0

RecursiveMAS 88.0 86.7 86.7 66.2 42.9 79.3

increases. When compared with the text-based recursion, RecursiveMAS consistently improves over the baseline by an average of 8.1% at 𝑟 = 1, 19.6% at 𝑟 = 2, and 20.2% at 𝑟 = 3, with performance advantage more pronounced as the recursion deepens. Additionally, under identical MAS architectures, RecursiveMAS delivers steadily increasing efficiency gains across recursion rounds, accelerating end-toend inference time from 1.2× to 2.4× while reducing output tokens from 34.6% to 75.6%. Additional case studies on the running pipeline of RecursiveMAS across domains are provided in Appendix G.

Scaling Law on RecursiveMAS (Training v.s. Inference). We further examine the scaling behavior of recursion in RecursiveMAS by jointly varying the training-time and inference-time recursion rounds. Figure 1 (Up) illustrates the performance landscape of RecursiveMAS under different training and inference settings. Increasing inference depth continues to improve systems trained with fewer rounds, while deeper training shifts the entire performance frontier upward, with the strongest results consistently appearing in the upper-right region where both are large. This trend suggests a complementary training-inference scaling effect in RecursiveMAS: training recursion progressively teaches the system to form refinement-ready latent states, and subsequent inference recursion translates this learned recursive structure into additional test-time gains.

###### 5.2. Broader Comparison with Alternative Architectures and Training Frameworks

Table 3 compares RecursiveMAS at the whole-system level against a broader set of baselines, including single fine-tuned agents, representative multi-agent frameworks, and alternative recursive methods. To ensure fair comparison, all methods are instantiated with identical backbone models and comparable training budgets (e.g., matched trainable parameter counts, recursion depth, training set).

Overall, RecursiveMAS delivers a consistent whole-system advantage, achieving an average performance improvement of 8.3% over the strongest baseline on each benchmark. With the same training data, fine-tuning individual agents strengthens performance relative to their off-the-shelf versions, while RecursiveMAS delivers further gains by optimizing cross-agent collaboration at the system level. In addition, RecursiveMAS remains the performance advantage compared to advanced architectures such as TextGrad and LoopLM, especially on reasoning-intensive tasks (e.g., accuracy gains of 18.1% on AIME2025, 13.0% on AIME2026, and 5.4% on GPQA-Diamond).

###### 5.3. Can RecursiveMAS Generalize across Diverse Collaboration Patterns?

Beyond the sequential setting, we further instantiate RecursiveMAS under three additional MAS collaboration patterns in Table 1 to assess whether our method is agnostic to any specific system architecture and generalizes across diverse usage scenarios. As shown in Figure 1 (Down), we compare

![image 161](<2026-zou-recursive-multi-agent-systems_images/imageFile161.png>)

Avg. 34.6% Fewer Token Usage

Avg. 75.6% Fewer Token Usage

Avg. 65.5% Fewer Token Usage

![image 162](<2026-zou-recursive-multi-agent-systems_images/imageFile162.png>)

![image 163](<2026-zou-recursive-multi-agent-systems_images/imageFile163.png>)

Recursive Multi-Agent Systems

![image 164](<2026-zou-recursive-multi-agent-systems_images/imageFile164.png>)

![image 165](<2026-zou-recursive-multi-agent-systems_images/imageFile165.png>)

![image 166](<2026-zou-recursive-multi-agent-systems_images/imageFile166.png>)

Avg. 1.2x Inference Speedup

Avg. 1.9x Inference Speedup

Avg. 2.4x Inference Speedup

###### Figure 5 | Inference Time Speedup of RecursiveMAS across Three Recursion Rounds. RecursiveMAS exhibits increasing inference speedup as the recursion depth increases.

Avg. 65.5% Fewer Token Usage

Avg. 75.6% Fewer Token Usage

![image 167](<2026-zou-recursive-multi-agent-systems_images/imageFile167.png>)

![image 168](<2026-zou-recursive-multi-agent-systems_images/imageFile168.png>)

![image 169](<2026-zou-recursive-multi-agent-systems_images/imageFile169.png>)

Avg. 34.6% Fewer Token Usage

###### Figure 6 | Token Reduction of RecursiveMAS across Three Recursion Rounds. As recursion deepens, RecursiveMAS reduces substantially more tokens than Recursive-TextMAS.

the accuracy of RecursiveMAS against strong standalone agents within each collaboration pattern.

In Mixture-style, RecursiveMAS achieves an average improvement of 6.2% over the strongest domain specialist on each benchmark, suggesting that recursive interaction enables non-trivial cross-domain composition beyond what can be attained by selecting one individual specialist alone. In Deliberationstyle, we evaluate tool use on both mathematical and search-intensive tasks. RecursiveMAS improves the original tool-calling agent by 4.8%, showing that recursive latent coordination remains effective in tool-calling settings through iterative interaction with the Reflector. Finally, in Distillation-style, RecursiveMAS improves the learner by 8.0% while retaining 1.5× end-to-end speed advantage over the expert. In this way, RecursiveMAS distills much of the expert’s capability into a more efficient system. We leave detailed reports of Figure 1 (Down) in Appendix D.1.

###### 5.4. Efficiency Analyses on Latent-space Recursion

Inference Time Speedup. We analyze the efficiency of RecursiveMAS to empirically support our complexity advantage in Proposition 3.1. We first compare RecursiveMAS against Recursive-TextMAS to study how our advantage on end-to-end inference time scales with recursion depth. As shown in Figure 5, although deeper recursion rounds introduce cost, we find that RecursiveMAS consistently exhibits efficiency gain, and the advantage further increases as recursion deepens. For example, at recursion round 𝑟 = 1, RecursiveMAS already achieves a 1.2× speedup on average, and this advantage grows to 1.9× and 2.4× at larger recursion rounds of 𝑟 = 2/3. This trend aligns well with our method design, where RecursiveMAS achieves a favorable scaling behavior by conducting recursive collaboration directly in latent space and avoiding repeated intermediate text generation.

Overall Token Usage Reduction. We next demonstrate the substantial token usage reduction of RecursiveMAS in Figure 6. Within the comparison, we find that the baseline method suffers from rapidly growing token overhead as recursion round increases, while RecursiveMAS reduces the token usage by 34.6% for the first recursion round, and the reduction scales to 75.6% at 𝑟 = 3. This is because Recursive-TextMAS repeatedly decode the intermediate text at every recursion round, whereas

RecursiveMAS performs most recursive interaction directly in latent space. Overall, RecursiveMAS enables a much more efficient system-level scaling behavior, and the resulting efficiency gain is amplified as the number of recursion rounds increases.

##### 6. In-depth Analyses on RecursiveMAS

RecursiveLink Design. To validate the effectiveness of RecursiveLink, we compare our 2-layer residual design against three alternatives: (i) a 1-layer network, (ii) a 1-layer network with the residual connection, and (iii) a 2-layer network without the residual connection. We conduct experiments using the scaled sequential-style RecursiveMAS and adapt the same architecture for both Rin and Rout.

As shown in Table 4, our 2-layer residual design performs best across all three benchmarks, and the residual connection delivers additional improvements across different backbone models. For example, on GPQA-Diamond, equipping a single-layer design with a residual branch improves the performance from 63.2% to 65.3%, which is even higher than the plain 2-layer design (64.5%). These results align with our design intuition in Section 3.1: by preserving latent semantics while learning only the distributional shift, RecursiveLink achieves stable training and stronger inference performance.

Table 4 | Efficacy on RecursiveLink Design. We compare accuracy across alternative architectural designs.

RecursiveLink Design Math500 GPQA-D LiveCodeBench

- 1-Layer 84.4 63.2 40.1

- Res+1-Layer 86.7 65.3 41.4

2-Layer 85.6 64.5 40.5

- Res+2-Layer (ours) 88.0 66.2 42.9




Semantic Representations in Recursion. We analyze how the semantic distribution of RecursiveMAS changes across different recursion rounds. Under the scaled sequential setting of RecursiveMAS, we randomly sample 500 question-answer pairs spanning all downstream domains. We then use the solver agent’s input embedding layer to map each ground-truth answer string into embedding representations, which serves as the reference semantic distribution. We run RecursiveMAS at recursion rounds 𝑟 = 1, 2, 3 to generate final answers for all these 500 questions, map the generated answers into embeddings using the same input embedding layer, and visualize both the ground-truth reference ("purple") and newly generated distributions ("orange") via PCA projection.

![image 170](<2026-zou-recursive-multi-agent-systems_images/imageFile170.png>)

- Figure 7 | Semantic Representations of RecursiveMAS across Differnt Recursion Rounds. We visualize the semantic distribution of the final answers generated by RecursiveMAS and the corresponding ground-truth across 500 questions. Increasing recursion rounds progressively aligns the generated distribution of RecursiveMAS with the ground truth distribution.


In Figure 7, the generated answers at 𝑟 = 1 remain visibly shifted from the ground-truth distribution, but this discrepancy progressively narrows as depth increases, with the two distributions becoming largely aligned by 𝑟 = 3. This aligning trend suggests that RecursiveMAS iteratively refines the latent embeddings and corresponding answers through recursion. We further take a closer look to examine

- Table 5 | Cost analysis on RecursiveMAS. We report the peak GPU memory usage (GB), number of trainable parameters, estimated cost, and average accuracy (%) across all downstream tasks.


###### Methods GPU Mem. Trainable Param. Cost Avg. Acc.

LoRA Training 21.67 15.92M (0.37%) $6.64 66.9 Full-SFT 41.40 4.21B (100%) $9.67 68.6 RecursiveMAS 15.29 13.12M (0.31%) $4.27 74.9

individual test instances and provide detailed case studies in Appendix F. Our case studies reveal a common pattern in which RecursiveMAS may produce an incorrect answer at an early stage, while deeper recursion successfully corrects it through iterative refinement. Together, these analyses provide further evidence that latent thoughts capture semantically meaningful representations, and that deeper recursion improves alignment toward correct final outputs.

Optimal Length of Latent Thoughts Generation. We next study and ablate the latent thoughts length 𝑚 to examine how much of each agent’s internal reasoning is sufficient to support effective collaboration. Under the scaled sequential-style of RecursiveMAS, we evaluate a broad range of 𝑚. As illustrated in Figure 8, increasing 𝑚 improves performance in the early regime. Once 𝑚 reaches a moderate scale (around 𝑚 = 80), performance is stabilized across all benchmarks. The ablation suggests that RecursiveMAS enables effective agent reasoning and interaction with only a modest latent-thought budget, in sharp contrast to text-based collaboration that typically requires longer CoT and costly token generation.

![image 171](<2026-zou-recursive-multi-agent-systems_images/imageFile171.png>)

Figure 8 | Effectiveness of RecursiveMAS’s latent thoughts with different step lengths.

Training Cost Analysis We further analyze the training cost of RecursiveMAS under the scaled sequential-style MAS setting. We compare RecursiveMAS with direct training methods, including LoRA and full supervised fine-tuning with the same training data and backbone setup. For cost estimation, we follow prior methods (Liu et al., 2025; Lu et al., 2023) to measure the cost based on GPU usage. As shown in Table 5, RecursiveMAS utilizes the lowest per-agent GPU memory, trainable parameter count, and estimated cost among all compared training strategies. Meanwhile, RecursiveMAS achieves the highest accuracy across all downstream tasks, suggesting that optimizing the lightweight RecursiveLink provides a better cost-performance trade-off than other training methods.

##### 7. Related Works

LLM-based Multi-Agent Systems. Current LLMs achieve strong performance on general tasks, but they often exhibit bottlenecks when facing diverse reasoning patterns (Maheswaran et al., 2026; Mirzadeh et al., 2025; Valmeekam et al., 2023) or domain-specific challenges (Chen et al., 2025). To overcome these limitations, Multi-agent systems extend the single LLM paradigm to a collaborative setting (Su et al., 2025; Tran et al., 2025; Wu et al., 2024; Yang et al., 2024b) by organizing a set of agents with distinct roles that jointly address the problem. A standard multi-agent system topology involves a sequential configuration (Li et al., 2023; Qian et al., 2024), where agents are assigned in a linear pipeline to decompose and resolve problems in order. Beyond sequential settings, other

works also explore mixture-style settings (Wang et al., 2025b; Ye et al., 2025b; Yun et al., 2026), where multiple agents with domain expertise reason in parallel, and their outputs are aggregated into a final decision. Another line of work seeks to improve MAS through textual feedback signals. For example, related optimization methods (Shen et al., 2025; Yuksekgonul et al., 2025) leverage an LLM to generate natural language feedback to refine contextual inputs and instructions of each agent. Additionally, another study (Motwani et al., 2024) improves MAS by separately training each agent with role-specific responses. Rather than separate training each individual agent or only leveraging textual feedback, RecursiveMAS treats MAS as a unified whole, and scales the system performance via recursively refining the latent information flow.

Scaling Reasoning via Recursion. Recent studies explore recursion as an alternative scaling axis for LLMs (Bae et al., 2025; Geiping et al., 2025; Li et al., 2026; Tang et al., 2026), where the same computation blocks are reused through multiple recurrent rounds (i.e., loops) to increase reasoning depth and iteratively refine hidden representations. One line of work studies recursive language models that apply shared layers to scale latent reasoning. For instance, LoopLM (Zhu et al., 2025) introduces pre-trained looped language models with iterative latent computation. Besides, other work explores other recursive architectures (Jolicoeur-Martineau, 2025; Wang et al., 2025a; Zhang et al.,

- 2025a), including tiny recursive networks and recursive self-calling schemes for long-context inference. While existing methods in agentic AI primarily focus on recursion inside a single language model, RecursiveMAS exhibits the first attempt to extend the recursive scaling paradigm to system-level. Additional related works are provided in Appendix C.


##### 8. Conclusion

We introduce RecursiveMAS, a recursive multi-agent framework that scales agent collaboration through system-level recursion. RecursiveMAS first supports latent-thoughts generation within each agent through inner RecursiveLink, then connects heterogeneous agents through outer RecursiveLink, and optimizes the whole system with an inner-outer loop training paradigm. Theoretically, our framework leads to more stable training dynamics and improves efficiency compared to text-based baselines. Our empirical results across mathematical and scientific reasoning, code generation, and search benchmarks show that RecursiveMAS consistently improves accuracy while substantially reducing inference time and token usage. Overall, RecursiveMAS provides a scalable and efficient framework for multi-agent systems to recursively collaborate, refine, and evolve in latent space.

##### References

W. U. Ahmad, S. Narenthiran, S. Majumdar, A. Ficek, S. Jain, J. Huang, V. Noroozi, and B. Ginsburg. Opencodereasoning: Advancing data distillation for competitive coding, 2025. URL https:// arxiv.org/abs/2504.01943.

H. Babu, P. Schillinger, and T. Asfour. Adaptive domain modeling with language models: A multi-agent approach to task planning. In 2025 IEEE 21st International Conference on Automation Science and Engineering (CASE), pages 1701–1708. IEEE, 2025.

- S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, et al. Mixture-of-recursions: Learning dynamic recursive depths for adaptive token-level computation. arXiv preprint arXiv:2507.10524, 2025.


H. Chen, Z. Fang, Y. Singla, and M. Dredze. Benchmarking large language models on answering and explaining challenging medical questions. In Proceedings of the 2025 Conference of the Nations of

the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 3563–3599, 2025.

- G. Dong, H. Mao, K. Ma, L. Bao, Y. Chen, Z. Wang, Z. Chen, J. Du, H. Wang, F. Zhang, et al. Agentic reinforced policy optimization. arXiv preprint arXiv:2507.19849, 2025.

Z. Du, R. Wang, H. Bai, Z. Cao, X. Zhu, Y. Cheng, B. Zheng, W. Chen, and H. Ying. Enabling agents to communicate entirely in latent space. arXiv preprint arXiv:2511.09149, 2025.

- H. Face. Transformers documentation. https://huggingface.co/docs/transformers/en/ index, 2025.


- T. Fu, Z. Min, H. Zhang, J. Yan, G. Dai, W. Ouyang, and Y. Wang. Cache-to-cache: Direct semantic communication between large language models. arXiv preprint arXiv:2510.03215, 2025.


J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein. Scaling up test-time compute with latent reasoning: A recurrent depth approach. arXiv preprint arXiv:2502.05171, 2025.

A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten,

- A. Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.

- W. Gu, J. Han, H. Wang, X. Li, and B. Cheng. Explain-analyze-generate: A sequential multi-agent collaboration method for complex reasoning. In Proceedings of the 31st International Conference on Computational Linguistics, pages 7127–7140, 2025.

- M. Hu, Y. Zhou, W. Fan, Y. Nie, B. Xia, T. Sun, Z. Ye, Z. Jin, Y. Li, Q. Chen, et al. Owl: Optimized workforce learning for general multi-agent assistance in real-world task automation. arXiv preprint arXiv:2505.23885, 2025.

X. Huang, J. Wu, H. Liu, X. Tang, and Y. Zhou. m1: Unleash the potential of test-time scaling for medical reasoning with large language models, 2025. URL https://arxiv.org/abs/2504.00869.

HuggingFaceH4. Math-500 dataset. https://huggingface.co/datasets/HuggingFaceH4/ MATH-500, 2023.

B. Hui, J. Yang, Z. Cui, J. Yang, D. Liu, L. Zhang, T. Liu, J. Zhang, B. Yu, K. Lu, et al. Qwen2. 5-coder technical report. arXiv preprint arXiv:2409.12186, 2024.

- N. Jain, K. Han, A. Gu, W.-D. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. In The Thirteenth International Conference on Learning Representations, 2025.


- Y. Labrak, A. Bazoge, E. Morin, P.-A. Gourraud, M. Rouvier, and R. Dufour. Biomistral: A collection of open-source pretrained large language models for medical domains. In Findings of the association for computational linguistics: acl 2024, pages 5848–5864, 2024.




A. Q. Jiang, A. Sablayrolles, A. Roux, A. Mensch, B. Savary, C. Bamford, D. S. Chaplot, D. d. l. Casas, E. B. Hanna, F. Bressand, et al. Mixtral of experts. arXiv preprint arXiv:2401.04088, 2024.

A. Jolicoeur-Martineau. Less is more: Recursive reasoning with tiny networks. arXiv preprint arXiv:2510.04871, 2025.

- W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. Gonzalez, H. Zhang, and I. Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the 29th symposium on operating systems principles, pages 611–626, 2023.


- G. Li, H. A. Al Kader Hammoud, H. Itani, D. Khizbullin, and B. Ghanem. Camel: communicative agents for "mind" exploration of large language model society. In Proceedings of the 37th International Conference on Neural Information Processing Systems, NIPS ’23, Red Hook, NY, USA, 2023. Curran Associates Inc.


- Y. Li, J. Chen, F. Wu, J. Yu, H. Qi, W. Xuan, H. Zhao, P. Nie, D. Jin, and X. Tang. Learning multi-step reasoning via persistent latent state propagation. In Workshop on Latent {\&} Implicit Thinking {\textendash} Going Beyond CoT Reasoning, 2026.
- Z. Li, H. Zhang, S. Han, S. Liu, J. Xie, Y. Zhang, Y. Choi, J. Zou, and P. Lu. In-the-flow agentic system optimization for effective planning and tool use. arXiv preprint arXiv:2510.05592, 2025a.


- Z.-Z. Li, D. Zhang, M.-L. Zhang, J. Zhang, Z. Liu, Y. Yao, H. Xu, J. Zheng, P.-J. Wang, X. Chen, et al. From system 1 to system 2: A survey of reasoning large language models. arXiv preprint arXiv:2502.17419, 2025b.


- A. Liu, A. Mei, B. Lin, B. Xue, B. Wang, B. Xu, B. Wu, B. Zhang, C. Lin, C. Dong, et al. Deepseek-v3. 2: Pushing the frontier of open large language models. arXiv preprint arXiv:2512.02556, 2025.


- J. Liu, C. S. Xia, Y. Wang, and L. Zhang. Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation. Advances in Neural Information Processing Systems, 36:21558–21572, 2023.


Y. Lu, C. Li, H. Liu, J. Yang, J. Gao, and Y. Shen. An empirical study of scaling instruct-tuned large multimodal models. arXiv preprint arXiv:2309.09958, 2023.

- M. Maheswaran, L. Lakhani, Z. Zhou, S. Yang, J. Wang, C. Hooper, Y. Hu, R. Tiwari, J. Wang, H. Singh, et al. Squeeze evolve: Unified multi-model orchestration for verifier-free evolution. arXiv preprint arXiv:2604.07725, 2026.

math ai. AIME 2025 dataset. https://huggingface.co/datasets/math-ai/aime25, 2025. MathArena. Aime 2026 dataset. https://huggingface.co/datasets/MathArena/aime_

2026, 2026.

S. I. Mirzadeh, K. Alizadeh, H. Shahrokhi, O. Tuzel, S. Bengio, and M. Farajtabar. Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models. In The Thirteenth International Conference on Learning Representations, 2025.

S. R. Motwani, C. Smith, R. J. Das, R. Rafailov, I. Laptev, P. H. Torr, F. Pizzati, R. Clark, and C. S. de Witt. Malt: Improving reasoning with multi-agent llm training. arXiv preprint arXiv:2412.01928, 2024.

- N. Muennighoff, Z. Yang, W. Shi, X. L. Li, L. Fei-Fei, H. Hajishirzi, L. Zettlemoyer, P. Liang, E. Candès, and T. Hashimoto. s1: Simple test-time scaling. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 20275–20321. Association for Computational Linguistics, Nov. 2025.
- O. Press, M. Zhang, S. Min, L. Schmidt, N. A. Smith, and M. Lewis. Measuring and narrowing the compositionality gap in language models. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 5687–5711, 2023.


- C. Qian, W. Liu, H. Liu, N. Chen, Y. Dang, J. Li, C. Yang, W. Chen, Y. Su, X. Cong, et al. Chatdev: Communicative agents for software development. In Proceedings of the 62nd annual meeting of the association for computational linguistics (volume 1: Long papers), pages 15174–15186, 2024.


C. Qian, Z. Xie, Y. Wang, W. Liu, K. Zhu, H. Xia, Y. Dang, Z. Du, W. Chen, C. Yang, et al. Scaling large language model-based multi-agent collaboration. In The Thirteenth International Conference on Learning Representations, 2025.

Qwen, :, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, et al.

Qwen2.5 technical report, 2025. URL https://arxiv.org/abs/2412.15115. Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URL https://qwen. ai/blog?id=qwen3.5.

- D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman. Gpqa: A graduate-level google-proof q&a benchmark, 2023. URL https://arxiv.org/abs/ 2311.12022.


- J. Schulman and T. M. Lab. Lora without regret. Thinking Machines Lab: Connectionism, 2025. doi: 10.64434/tml.20250929. https://thinkingmachines.ai/blog/lora/.

M. Shen, R. Shu, A. Pratik, J. Gung, Y. Ge, M. Sunkara, and Y. Zhang. Optimizing llm-based multi-agent system with textual feedback: A case study on software development. arXiv preprint arXiv:2505.16086, 2025.

P. Shojaee, I. Mirzadeh, K. Alizadeh, M. Horton, S. Bengio, and M. Farajtabar. The illusion of thinking: Understanding the strengths and limitations of reasoning models via the lens of problem complexity. SuperIntelligence-Robotics-Safety & Alignment, 2(6), 2025.

- P. Song, P. Han, and N. Goodman. Large language model reasoning failures. arXiv preprint arXiv:2602.06176, 2026.


H. Su, S. Diao, X. Lu, M. Liu, J. Xu, X. Dong, Y. Fu, P. Belcak, H. Ye, H. Yin, Y. Dong, E. Bakhturina, T. Yu, Y. Choi, J. Kautz, and P. Molchanov. Toolorchestra: Elevating intelligence via efficient model and tool orchestration, 2025. URL https://arxiv.org/abs/2511.21689.

- V. Subramaniam, Y. Du, J. B. Tenenbaum, A. Torralba, S. Li, and I. Mordatch. Multiagent finetuning: Self improvement with diverse reasoning chains. arXiv preprint arXiv:2501.05707, 2025.


- G. Tang, S. Jiang, H. Chang, N. Chen, Y. Li, H. Fan, J. Li, M. Liu, and B. Qin. Looprpt: Reinforcement pre-training for looped language models. arXiv preprint arXiv:2603.19714, 2026.


Tavily. Tavily search api. https://www.tavily.com, 2026.

- G. Team, A. Kamath, J. Ferret, S. Pathak, N. Vieillard, R. Merhej, S. Perrin, T. Matejovicova, A. Ramé, et al. Gemma 3 technical report, 2025. URL https://arxiv.org/abs/2503.19786.


- K.-T. Tran, D. Dao, M.-D. Nguyen, Q.-V. Pham, B. O’Sullivan, and H. D. Nguyen. Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint arXiv:2501.06322, 2025.


- K. Valmeekam, M. Marquez, A. Olmo, S. Sreedharan, and S. Kambhampati. Planbench: An extensible benchmark for evaluating large language models on planning and reasoning about change. Advances in Neural Information Processing Systems, 36:38975–38987, 2023.


- A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. u. Kaiser, and I. Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 30. Curran Associates, Inc., 2017.


- G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori. Hierarchical reasoning model. arXiv preprint arXiv:2506.21734, 2025a.

J. Wang, W. Jue, B. Athiwaratkun, C. Zhang, and J. Zou. Mixture-of-agents enhances large language model capabilities. In The Thirteenth International Conference on Learning Representations, 2025b.

Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, et al. Autogen: Enabling next-gen llm applications via multi-agent conversations. In First Conference on Language Modeling, 2024.

B. Xu, C. Li, W. Wang, W. Fan, T. Zheng, H. Shi, T. Fan, Y. Song, and Q. Yang. Towards multi-agent reasoning systems for collaborative expertise delegation: An exploratory design study. arXiv preprint arXiv:2505.07313, 2025.

- A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.


- H. Yang, H. Chen, H. Guo, Y. Chen, C.-S. Lin, S. Hu, J. Hu, X. Wu, and X. Wang. Llm-medqa: Enhancing medical question answering through case studies in large language models. arXiv preprint arXiv:2501.05464, 2024a.


- Y. Yang, Q. Peng, J. Wang, Y. Wen, and W. Zhang. Llm-based multi-agent systems: Techniques and business perspectives. arXiv preprint arXiv:2411.14033, 2024b.
- Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. Cohen, R. Salakhutdinov, and C. D. Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 conference on empirical methods in natural language processing, pages 2369–2380, 2018.


- H. Ye, Z. Gao, M. Ma, Q. Wang, Y. Fu, M.-Y. Chung, Y. Lin, Z. Liu, J. Zhang, D. Zhuo, et al. Kvcomm: Online cross-context kv-cache communication for efficient llm-based multi-agent systems. arXiv preprint arXiv:2510.12872, 2025a.


- R. Ye, X. Liu, Q. Wu, X. Pang, Z. Yin, L. Bai, and S. Chen. X-mas: Towards building multi-agent systems with heterogeneous llms. arXiv preprint arXiv:2505.16997, 2025b.

X. Yu, Z. Chen, Y. He, T. Fu, C. Yang, C. Xu, Y. Ma, X. Hu, Z. Cao, J. Xu, et al. The latent space: Foundation, evolution, mechanism, ability, and outlook. arXiv preprint arXiv:2604.02029, 2026.

M. Yuksekgonul, F. Bianchi, J. Boen, S. Liu, P. Lu, Z. Huang, C. Guestrin, and J. Zou. Optimizing generative ai by backpropagating language model feedback. Nature, 639(8055):609–616, 2025.

- S. Yun, J. Peng, P. Li, W. Fan, J. Chen, J. Zou, G. Li, and T. Chen. Graph-of-agents: A graph-based framework for multi-agent llm collaboration. In The Fourteenth International Conference on Learning Representations, 2026.


- A. L. Zhang, T. Kraska, and O. Khattab. Recursive language models. arXiv preprint arXiv:2512.24601, 2025a.


- Q. Zhang, C. Hu, S. Upasani, B. Ma, F. Hong, V. Kamanuru, J. Rainton, C. Wu, M. Ji, H. Li, et al. Agentic context engineering: Evolving contexts for self-improving language models. arXiv preprint arXiv:2510.04618, 2025b.


- W. Zhao, M. Yuksekgonul, S. Wu, and J. Zou. Sirius: Self-improving multi-agent systems via bootstrapped reasoning. arXiv preprint arXiv:2502.04780, 2025.


- Y. Zheng, Z. Zhao, Z. Li, Y. Xie, M. Gao, L. Zhang, and K. Zhang. Thought communication in multiagent collaboration. arXiv preprint arXiv:2510.20733, 2025.


- H. Zhou, X. Wan, R. Sun, H. Palangi, S. Iqbal, I. Vulić, A. Korhonen, and S. Ö. Arık. Multi-agent design: Optimizing agents with better prompts and topologies. arXiv preprint arXiv:2502.02533, 2025.


- R.-J. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, et al. Scaling latent reasoning via looped language models. arXiv preprint arXiv:2510.25741, 2025.


J. Zou, X. Yang, R. Qiu, G. Li, K. Tieu, P. Lu, K. Shen, H. Tong, Y. Choi, J. He, J. Zou, M. Wang, and L. Yang. Latent collaboration in multi-agent systems, 2025. URL https://arxiv.org/abs/ 2511.20639.

### Table of Contents

- A Theoretical Analysis 21

- A.1 Running Complexity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- A.2 Realistic Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- A.3 Learning Advantage Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


- B Experiment Setups 23

- B.1 Evaluation Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- B.2 Compared Baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- B.3 Additional Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


- C Additional Related Work 26
- D Additional Experiments 26

- D.1 Results on Different Collaboration Patterns . . . . . . . . . . . . . . . . . . . . . . . . 26
- D.2 Ablations on Latent Thoughts Lengths . . . . . . . . . . . . . . . . . . . . . . . . . . 27


- E Prompt Template for RecursiveMAS 28
- F Case Study on Different Recursion Rounds 30
- G Examples of RecursiveMAS Across Different Downstream Tasks 33


### Appendix

##### A. Theoretical Analysis

###### A.1. Running Complexity Analysis

Proposition A.1 (Restate of Proposition 3.1). Without RecursiveLink, a text-based Recursive MAS with the same collaboration structure requires runtime complexity of Θ(𝑁(𝑚|𝑉|𝑑ℎ + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ)); In contrast, with RecursiveLink-enabled collaboration, RecursiveMAS achieves an end-to-end runtime complexity of Θ(𝑁(𝑚𝑑ℎ2 + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ)).

Proof of Proposition 3.1. We analyze the runtime complexity for each agent and then extend the result to the full multi-agent system. For each single agent, given the context length is at most 𝑡, and the generation length is at most 𝑚, the Transformer processes a sequence of length at most 𝑡+𝑚, requiring Θ((𝑡 + 𝑚)𝑑ℎ2) time for the feed-forward layers and Θ((𝑡 + 𝑚)2𝑑ℎ) time for self-attention. This standard Transformer computation is shared by both RecursiveMAS and text-based Recursive MAS.

The computational difference comes from how RecursiveMAS process the generated embeddings. In RecursiveMAS, each of the 𝑚 latent embeddings is transformed by RecursiveLink, which incurs an additional cost of Θ(𝑚𝑑ℎ2). In text-based Recursive MAS, each embedding must be decoded into an explicit token by projecting it to the vocabulary space and computing logits over |𝑉| tokens, resulting in an additional cost of Θ(𝑚|𝑉|𝑑ℎ).

Adding all terms together, our proposed RecursiveMAS needs Θ(𝑚𝑑ℎ2 + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ) time for each agent, while text-based Recursive MAS needs Θ(𝑚|𝑉|𝑑ℎ + (𝑡+𝑚)𝑑ℎ2 + (𝑡+𝑚)2𝑑ℎ) time. Since there are 𝑁 agents in the system, our proposed RecursiveMAS needs Θ(𝑁(𝑚𝑑ℎ2 + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ)) time, and text-based Recursive MAS needs Θ(𝑁(𝑚|𝑉|𝑑ℎ + (𝑡 + 𝑚)𝑑ℎ2 + (𝑡 + 𝑚)2𝑑ℎ)) time in total. □

###### A.2. Realistic Assumptions

Assumption A.1. Text-based SFT can be regarded as using Rtext(ℎ) = 𝑊in softmax(𝑊outℎ) as the recursive link, where 𝑊in is the token-to-embedding matrix, and 𝑊out denotes the embedding-to-logits matrix. We also assume ∥𝑊in∥2 ≤ 𝑂(1) and ∥𝑊out∥2 ≤ 𝑂(1). For RecursiveLink R(ℎ), we assume that 𝑊1,𝑊2 follow Kaiming normal initialization, and we only analyze the case where 𝑊3 = 𝐼.

###### A.3. Learning Advantage Analysis

Theorem A.2 (Restate of Theorem 4.1). Under the Realistic Assumptions (stated in Appendix A.2), if tokens are confident with entropy ≤ 𝜖, where typically 𝜖 ≪ 1: directly applying text-based SFT (denoted by Rtext(ℎ)) during recursion suffers from gradient vanishing (i.e., gradient norm close to 0); while RecursiveMAS with the RecursiveLink R maintains stable and near constant gradients (i.e., gradient norm close to 1) during looped backpropagation process. Formally, with probability ≥ 1 − 𝛿,

√︄ 1

1

𝜕R(ℎ) 𝜕ℎ 2 ≥ Ω 1 −

𝜕Rtext(ℎ) 𝜕ℎ 2 ≤ 𝑂(𝜖) ≪ 1,

log

. (8)

𝑑ℎ

𝛿

Proof of Theorem 4.1. We first analyze the gradient behavior of text-based recursive interaction. By

applying the chain rule to Rtext(ℎ), the gradient matrix is:

𝜕Rtext(ℎ) 𝜕ℎ

= 𝑊in𝑆𝑊out, 𝑆 = diag(𝑝) − 𝑝𝑝𝑇,

𝐽text =

where 𝑝 = softmax(𝑊outℎ) is the next token distribution. Then, by the sub-multiplicativity of the spectral norm,

∥𝐽text∥2 ≤ ∥𝑊in∥2∥𝑆∥2∥𝑊out∥2 ≤ 𝑂(1) · ∥𝑆∥2 · 𝑂(1) = 𝑂(∥𝑆∥2).

Because 𝑆 represents the covariance matrix of a categorical distribution, it is symmetric and positive semi-definite. Thus, its spectral norm is upper-bounded by its trace:

∑︁|𝑉|

∑︁|𝑉|

###### ∑︁|𝑉|

(𝑝𝑖 − 𝑝2𝑖 ) =

𝑝2𝑖 = 1 − ∥𝑝∥22.

∥𝑆∥2 ≤ Tr(𝑆) =

𝑝𝑖 −

𝑖=1

𝑖=1

𝑖=1

Using the logarithm inequality ln 𝑧 ≤ 𝑧 − 1 (for all 𝑧 > 0), we can lower-bound the entropy:

∑︁|𝑉|

###### ∑︁|𝑉|

𝑝𝑖(1 − 𝑝𝑖) = 1 − ∥𝑝∥22.

𝑝𝑖(−ln 𝑝𝑖) ≥

𝜖 ≥

𝑖=1

𝑖=1

Substituting this inequality back into the norm bound yields:

∥𝑆∥2 ≤ 1 − ∥𝑝∥22 ≤ 𝜖. Therefore, combining the constants, we have:

𝜕Rtext(ℎ)

= ∥𝐽text∥2 ≤ 𝑂(𝜖).

𝜕ℎ 2

We next analyze the gradient behavior of RecursiveMAS. Applying the chain rule to R(ℎ), the gradient matrix is:

𝜕R(ℎ) 𝜕ℎ

= 𝐼 + 𝑊2Σ′𝑊1,

𝐽 =

where Σ′ = diag(𝜎′(𝑊1ℎ)). By the triangle inequality for the matrix norm,

###### ∥𝐽∥2 − 1 = ∥𝐽∥2 − ∥𝐼∥2 ≤ ∥𝐽 − 𝐼∥2 = ∥𝑊2Σ′𝑊1∥2.

Since 𝑊1,𝑊2 follow Kaiming initialization, and the GELU function 𝜎 has |𝜎′| ≤ 𝑂(1), then by the subgaussian matrix concentration inequality, ∥𝑊2Σ′𝑊1∥2 ≤ 𝑂  √︃

1 𝑑ℎ log 1𝛿 + 1 with probability ≥ 1 − 𝛿.

It follows that:

√︄ 1

1

∥𝐽∥2 ≥ Ω 1 −

log

.

𝑑ℎ

𝛿

###### □

##### B. Experiment Setups

- B.1. Evaluation Datasets We introduce all datasets used in our experiments as follows: Mathematical Reasoning.


- • MATH500 (HuggingFaceH4, 2023) is a widely used subset of the MATH benchmark, containing mathematical problems across algebra, geometry, number theory, probability, and combinatorics.
- • AIME2025 (math ai, 2025) contains 30 challenging problems from the 2025 American Invitational Mathematics Examination. These problems require olympiad-style derivations and precise numerical answers, providing a compact but difficult benchmark for mathematical reasoning.
- • AIME2026 (MathArena, 2026) follows the same AIME-style questions with 30 challenging competitionlevel math problems. We use it to further test performance and generalization on difficult mathematical reasoning tasks.


###### Scientific and Medical Tasks.

- • GPQA-Diamond (Rein et al., 2023) is the most difficult split of GPQA, consisting of graduatelevel multiple-choice questions in biology, physics, and chemistry. It requires specialized scientific knowledge and careful multi-step reasoning beyond shallow factual recall.
- • MedQA (Yang et al., 2024a) contains medical licensing-style questions that assess biomedical knowledge, clinical reasoning, and diagnostic decision-making. The benchmark requires integrating domain-specific evidence from patient scenarios and selecting the most appropriate answer.


###### Code Generation.

- • LiveCodeBench-v6 (Jain et al., 2025) is a contamination-resistant code generation benchmark built from recent programming problems. It evaluates whether models can synthesize functionally correct programs under realistic problem specifications and hidden test cases.
- • MBPP Plus (Liu et al., 2023) extends the original MBPP benchmark with more comprehensive test cases for Python program synthesis. The stricter execution-based evaluation provides a more reliable measure of functional correctness.


###### Search-based Question Answering.

- • HotpotQA (Yang et al., 2018) is a multi-hop question answering benchmark based on Wikipedia. It requires models to gather and combine evidence from multiple supporting facts, making it suitable for evaluating search-based reasoning.
- • Bamboogle (Press et al., 2023) is a compact but challenging benchmark for search-intensive multi-hop reasoning. Its questions often require decomposition and intermediate retrieval steps before composing the final answer.


###### B.2. Compared Baselines We compare our method against the following baselines: Single-Agent Fine-tuning Baselines.

- • Single Agent (w/ LoRA) uses the final agent from the corresponding collaboration pattern and trains it with LoRA adapters using the same training data as RecursiveMAS.
- • Single Agent (w/ Full-SFT) further fine-tunes all parameters of the same single-agent backbone using fully supervised fine-tuning.


###### Representative Multi-Agent Frameworks.

- • Mixture-of-Agents (MoA) (Wang et al., 2025b) organizes multiple LLM agents into a layered multi-agent system, where agents in each layer aggregate responses from the previous layer to produce refined outputs as the final answer.
- • TextGrad (Yuksekgonul et al., 2025) optimizes multi-agent systems by propagating naturallanguage feedback as textual gradients. We use TextGrad as a baseline method for text-mediated system optimization.


###### Recursion-based Methods.

- • LoopLM (Zhu et al., 2025) is a looped language model that performs recursive computation with shared transformations in latent space. In our evaluation, we mainly adopt the Ouro-2.6B model.
- • Recursive-TextMAS uses the same recursive multi-agent collaboration structure as RecursiveMAS, but agents communicate through explicit text rather than latent representations.


###### B.3. Additional Implementation Details

Training Data Curation. To optimize RecursiveMAS under our inner-outer training pipeline, we construct role-specific supervision targets for each agent across all collaboration patterns. We start by collecting question-answer pairs as raw training samples from four domains, including s1K (Muennighoff et al., 2025), m1K (Huang et al., 2025), OpenCodeReasoning (Ahmad et al., 2025), and ARPO-SFT (Dong et al., 2025). For each training sample, we rewrite the original answer into agent-level targets according to the role assignments of each collaboration pattern, as follows:

- • For Sequential-Style, we use Qwen3.5-397B-A17B to rewrite the answers into an initial step-by-step plan and a refined critic-guided plan. During training, the initial plan is used as the supervision target for the Planner, the critic-guided plan is used for the Critic, and the original answer is retained for the Solver.
- • For Mixture-Style, each specialist in the MAS first generates responses for questions from its specialized domain, and these responses are then used to supervise the corresponding specialist. The ground truth answers are used as targets for the Summarizer.
- • For Distillation-Style, the Expert first generates guidance-style responses for each training sample, which are then used as supervision targets for the Expert. The Learner is supervised directly by the ground-truth answers.
- • For Deliberation-Style, we use the ground truth answers as the supervision targets for both the Reflector and Tool-Caller agent.


After the role-specific data construction, each agent is assigned its own training pairs, where the input consists of the original question, and the output is the corresponding role-based response. These agent-level pairs are then used as the supervision data for subsequent training.

Implementation Details. During training, all base LLMs’ parameters are frozen, and we only update the inner and outer RecursiveLink using AdamW with a batch size of 4 and a maximum sequence

length of 4096 tokens. During inference, the maximum generation length is set for 2000 tokens for MATH500, 4000 tokens for MedQA, GPQA-Diamond, LiveCodeBench, and MBPP Plus, and 16000 tokens for AIME2025/2026. For all Qwen models, we enables the official Instruct mode (Qwen Team,

- 2026) for more efficient and controllable answer generation. For the Deliberation-Style MAS, we provide a standard Python environment and a Tavily (Tavily, 2026) search API as external tools. We implement RecursiveMAS and baselines with both HuggingFace Transformer (Face, 2025) and vLLM backend (Kwon et al., 2023). All experiments are conducted on H100 and A100 GPUs.


Evaluation Protocol. Across all non-code generation tasks, we first normalize the extracted answer by removing extra whitespace, stripping punctuation, and converting text to lowercase before applying task-specific correctness checks.

- • For numerical problems (MATH500, AIME2025, AIME2026), we compare the numerical value of the extracted answer with the ground truth. The answer is considered correct if the two values are mathematically equivalent.
- • For multiple-choice questions (GPQA-Diamond MedQA), we directly compare the predicted choice with the ground truth letter, where an exact option match is counted as correct.
- • For code generation tasks (LiveCodeBench and MBPP Plus), we first extract the generated code block and then execute it with provided test cases in a sandboxed python environment. Each individual test case is assigned a timeout of 10 seconds to prevent non-terminating programs.
- • For search-based tasks (HotpotQA, Bamboogle), we follow the standard LLM-as-a-judge evaluation method (Li et al., 2025a) and use the Qwen3.5-397B-A17B model as a binary judge to determine whether the generated answer is correct with respect to the ground truth answer.


When an output reaches the maximum generation length without producing an extractable answer, we follow standard early-stopping evaluation methods (Muennighoff et al., 2025; Yang et al., 2025) by appending “Final Answer:” to the model output to elicit a final response.

###### Table 6 | Comparison of RecursiveMAS in Distillation-Style Multi-agent System. RecursiveMAS improves the Learner agent by 8.0% via distilling knowledge from the Expert agent while retaining a 1.5× end-to-end speed advantage over the Expert agent.

Method (Distillation-Style) Metric AIME2026 GPQA-D LiveCodeBench MBPP+ MedQA

Acc. 90.0 72.7 46.2 73.4 86.0 Time 9473 2558 9352 2342 2124

Expert Model

Acc. 76.7 61.4 38.4 67.5 77.9 Time 4495 1289 5396 1171 1183

Learner Model

Acc. 83.3 70.0 40.1 71.9 83.0 Time 5967 1671 6863 1516 1436

RecursiveMAS

- C. Additional Related Work

Latent-Space Collaboration. Beyond text-based interaction, recent studies have explored leveraging the latent space as an alternative medium for LLM communication. One line of work studies transferring hidden embeddings for cross-model communication (Du et al., 2025; Yu et al., 2026), while other works investigate reusing internal states to share information across LLMs (Fu et al., 2025; Ye et al., 2025a). Recent studies extend this scheme to agentic settings, where latent interfaces are used to support coordination among multiple agents (Zheng et al., 2025; Zou et al., 2025). Different from these studies, RecursiveMAS treats latent information as part of a system-level recursive information flow, enabling heterogeneous agents to recursively collaborate and improve as a unified MAS.

- D. Additional Experiments


- D.1. Results on Different Collaboration Patterns


###### Table 7 | Comparison of RecursiveMAS in Mixture-Style Multi-agent System.

Method (Mixture-Style) AIME2026 GPQA-Diamond LiveCodeBench MedQA

Math Specialist 43.3 37.4 18.9 29.0 Code Specialist 13.3 26.2 21.5 43.3 Science Specialist 10.0 27.0 7.6 48.1

RecursiveMAS 46.7 43.0 23.8 61.7

###### Table 8 | Comparison of RecursiveMAS in Deliberation-Style Multi-agent System.

###### Method (Deliberation-Style) AIME2026 GPQA-Diamond HotpotQA Bamboogle

Reflector 76.7 61.2 27.5 40.9 Tool-Caller 86.7 63.1 39.6 49.8

RecursiveMAS 90.0 65.0 41.4 53.7

###### We report the detailed results of RecursiveMAS under three additional collaboration patterns in Tables 7, 6, and 8, corresponding to the summarized results in Figure 1 (Down). In both Mixture and

Deliberation settings, RecursiveMAS achieves consistent accuracy gains over the strongest individual agent in each setting. In Distillation Style, RecursiveMAS improves performance over the Learner while requiring substantially less inference time than the Expert. Overall, these results show that RecursiveMAS provides both performance gains and efficiency benefits across diverse MAS collaboration patterns, further demonstrating the generality of our method.

###### D.2. Ablations on Latent Thoughts Lengths

- Table 9 | Ablation Study on Length of Latent Thoughts 𝑚 transferred across agents on RecursiveMAS.


###### Latent Steps 0 16 32 48 64 80 96 112 128 Math500 83.3 84.9 85.2 85.6 86.8 86.8 86.5 86.9 86.7 GPQA-D 61.4 62.0 62.8 63.6 64.1 64.2 64.5 64.3 64.4 LiveCodeBench 38.1 40.3 40.7 41.4 42.0 42.5 42.2 42.6 42.6

We provide detailed ablation results on the length of latent thoughts 𝑚 in Table 9, corresponding to the plot in Figure 8. As 𝑚 increases, RecursiveMAS consistently improves across all benchmarks, and the performance gradually saturates around 𝑚 = 80, suggesting that a moderate latent thought budget is sufficient for effective latent collaboration.

##### E. Prompt Template for RecursiveMAS

###### Prompt Template for Sequential-Style RecursiveMAS

System Prompt for All Agents: You are a helpful assistant.

User Prompt for Planner Agent:

You are a planner agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings}. Given the latent information, you should output a step-by-step plan to solve the question: {Question}

###### User Prompt for Critic Agent:

You are a critic agent in a recursive multi-agent system. Here is the latent information from previous agent: {Latent Thought Embeddings}. Given the latent information, you should critique the initial plan and output an improved plan to solve the question: {Question}

User Prompt for Solver Agent: You are a solver agent in a recursive multi-agent system. Here is the latent information from previous agent: {Latent Thought Embeddings} Given the latent information, you should solve the question and provide the final answer: {Question} Solve the question and put the final answer inside \boxed{}.

###### Prompt Template for Mixture-Style RecursiveMAS

System Prompt for All Agents: You are a helpful assistant.

User Prompt for Math Specialist Agent:

You are a math specialist agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings} Given the latent information, you should provide a domain-specific answer for the question: {Question}

###### User Prompt for Science Specialist Agent:

You are a science specialist agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings} Given the latent information, you should provide a domain-specific answer for the question: {Question}

###### User Prompt for Code Specialist Agent:

You are a code specialist agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings} Given the latent information, you should provide a domain-specific answer for the question: {Question}

User Prompt for Summarizer Agent: You are a summarizer agent in a recursive multi-agent system. Here is the latent information from the math specialist: {Math Specialist Latent Thought Embeddings}. Here is the latent information from the code specialist: {Code Specialist Latent Thought Embeddings}. Here is the latent information from the science specialist: {Science Specialist Latent Thought Embeddings}. Given the latent information from all previous specialists, you should aggregate their reasoning and provide the final answer to the question: {Question} Put the final answer inside \boxed{}.

###### Prompt Template for Distillation-Style RecursiveMAS

System Prompt for All Agents: You are a helpful assistant.

User Prompt for Expert Agent:

You are an expert agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings}. Given the latent information, you should provide expert-level guidance to solve the question: {Question}

User Prompt for Learner Agent: You are a learner agent in a recursive multi-agent system. Here is the latent information from previous agent: {Latent Thought Embeddings}. Given the latent information, you should use the expert guidance to solve the question and provide the final answer: {Question} Put the final answer inside \boxed{}.

###### Prompt Template for Deliberation-Style RecursiveMAS

###### System Prompt for All Agents (with Tool-Calling Instructions):

You are a helpful assistant that can solve the given question with the help of external tools, including a web search tool and a Python interpreter. For each question, you should reason carefully and use tools when they are necessary. You can invoke the web search tool to retrieve factual information, and use the Python interpreter to perform calculations or execute code. The search query and search result should be enclosed within <search> </search> and <result> </result> tags respectively. The Python code and execution result should be enclosed within <python> </python> and <result> </result> tags respectively.

###### User Prompt for Reflector Agent:

You are a reflector agent in a recursive multi-agent system. Here is the latent information from previous round: {Latent Thought Embeddings}. Given the latent information, you should reflect on the current solution and provide an improved solution to the question: {Question}

User Prompt for Tool-Caller Agent: You are a tool-caller agent in a recursive multi-agent system. Here is the latent information from the Reflector agent: {Latent Thought Embeddings}. Given the latent information, you should solve the question: {Question} Put the final answer inside \boxed{}.

##### F. Case Study on Different Recursion Rounds

###### Output of RecursiveMAS in Recursion Round 1 (On MATH500)

Question: For how many positive integers 𝑛 > 1 is it true that 224 is a perfect 𝑛th power?

Final Answer of RecursiveMAS: First, let’s express 𝑘 in terms of its prime factorization. Since 224 is a power of 2, 𝑘 must also be a power of 2. Let 𝑘 = 2𝑚 for some integer 𝑚. Then we have:

224 = (2𝑚)𝑛 = 2𝑚𝑛

This equation tells us that 24 = 𝑚𝑛. We need to find all pairs of positive integers (𝑚, 𝑛) such that 𝑚𝑛 = 24 and 𝑛 > 1. Let’s list the factor pairs of 24:

(1, 24), (2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2), (24, 1)

We discard the pairs where 𝑛 = 1 because we are looking for 𝑛 > 1. The remaining pairs are:

(2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2)

Each pair (𝑚, 𝑛) corresponds to a valid 𝑛 greater than 1. Therefore, the possible values of 𝑛 are 2, 3, 4, 6, 8, and 12. Counting these values, we find there are 6 possible values for 𝑛. Thus, the number of positive integers 𝑛 > 1 for which 224 is a perfect 𝑛-th power is

. Incorrect Answer ✗

|6|
|---|


###### Output of RecursiveMAS in Recursion Round 2 (On MATH500)

Question: For how many positive integers 𝑛 > 1 is it true that 224 is a perfect 𝑛th power?

Final Answer of RecursiveMAS: First, let’s express 224 in terms of its prime factorization: 224 For 224 to be a perfect 𝑛th power, 𝑛 must be a divisor of 24. This is because if 224 = 𝑘𝑛, then 𝑘 must be a power of 2, say 𝑘 = 2𝑚. Therefore, we have:

224 = (2𝑚)𝑛 = 2𝑚𝑛 Equating the exponents, we get:

24 = 𝑚𝑛 We need to find all pairs (𝑚, 𝑛) such that 𝑚𝑛 = 24 and 𝑛 > 1. Let’s list the divisors of 24:

- 1, 2, 3, 4, 6, 8, 12, 24

Since 𝑛 > 1, we exclude 1 from the list of divisors. The remaining divisors are:

- 2, 3, 4, 6, 8, 12, 24


Thus, the number of positive integers 𝑛 > 1 for which 224 is a perfect 𝑛th power is:

Correct Answer ✓

|7|
|---|


###### Output of RecursiveMAS in Recursion Round 3 (On MATH500)

Question: For how many positive integers 𝑛 > 1 is it true that 224 is a perfect 𝑛th power?

Final Answer of RecursiveMAS: First, let’s express 224 in terms of its prime factorization: For 224 to be a perfect 𝑛-th power, 𝑛 must be a divisor of 24. This is because if 224 = 𝑘𝑛, then 𝑘 must be of the form 2𝑚 for some integer 𝑚, and thus we have (2𝑚)𝑛 = 2𝑚𝑛 = 224, this implies:

𝑚𝑛 = 24 We need to find all positive divisors of 24. The divisors of 24 are:

- 1, 2, 3, 4, 6, 8, 12, 24

Since we are looking for 𝑛 > 1, we exclude 1 from the list. The remaining divisors are:

- 2, 3, 4, 6, 8, 12, 24


Thus, the number of positive integers 𝑛 > 1 for which 224 is a perfect 𝑛-th power is:

Correct Answer ✓

|7|
|---|


###### Output of TextMAS (On MATH500)

Question: For how many positive integers 𝑛 > 1 is it true that 224 is a perfect 𝑛th power?

Output of Planner Agent: Ok, I need to provide a step-by-step plan to solve the problem.

- • Step 1: Determine the prime factorization of 224.
- • Step 2: Recognize that 224 can be expressed as a perfect 𝑛th power if the exponent 24 is divisible by 𝑛.
- • Step 3: Find all positive integers 𝑛 > 1 such that 24 is divisible by 𝑛.
- • Step 4: Count the number of such integers 𝑛.
- • Step 5: Conclude that the number of positive integers 𝑛 > 1 for which 224 is a perfect 𝑛th power is equal to the number of divisors of 24 that are greater than 1.
- • Step 6: List the divisors of 24 greater than 1 and count them.
- • Step 7: The final answer is the count of such divisors.


Output of Critic Agent: Here is a detailed plan for the problem:

- Step 1: Analyze the problem We are asked to find how many positive integers 𝑛 > 1 satisfy the condition that 224 is a perfect 𝑛th power.
- Step 2: Recall the definition of a perfect 𝑛th power A number 𝑥 is a perfect 𝑛th power if there exists an integer 𝑘 such that 𝑥 = 𝑘𝑛.
- Step 3: Express 224 as a power of some base We can write 224 = (2𝑚)𝑛, where 𝑚 and 𝑛 are positive integers.
- Step 4: Find the possible values of 𝑛 For 224 to be a perfect 𝑛th power, 𝑛 must be a divisor of 24 (since 224 = (2𝑚)𝑛 implies 𝑛 divides 24).
- Step 5: Count the number of valid divisors Find the total number of positive divisors of 24, and then subtract 1 to account for the restriction that 𝑛 > 1.


Output of Solver Agent: To determine for how many positive integers 𝑛 > 1 the number 224 is a perfect 𝑛-th power, we need to find all the divisors of 24, since 224 can be written as

(2𝑘)𝑛

, where 𝑘𝑛 = 24. First, we list all the divisors of 24. The divisors of 24 are: 1, 2, 3, 4, 6, 8, 12, 24

Each divisor 𝑑 of 24 corresponds to a possible value of 𝑛 such that 224 is a perfect 𝑛-th power. Specifically, if 𝑑 is a divisor of 24, then 𝑛 = 24𝑑 will be an integer and 224 = (2𝑑)24/𝑑. Let’s list the corresponding 𝑛 values for each divisor 𝑑: - If 𝑑 = 1, then 𝑛 = 241 = 24 - If 𝑑 = 2, then 𝑛 = 242 = 12 - If 𝑑 = 3, then 𝑛 = 243 = 8 - If 𝑑 = 4, then 𝑛 = 244 = 6 - If 𝑑 = 6, then 𝑛 = 246 = 4 - If 𝑑 = 8, then 𝑛 = 248 = 3 - If 𝑑 = 12, then 𝑛 = 2412 = 2 - If 𝑑 = 24, then 𝑛 = 2424 = 1 (but since 𝑛 > 1, we exclude this case) Thus, the possible values of 𝑛 are 2, 3, 4, 6, 8, 12, 24. There are 7 such values. Therefore, the number of positive integers 𝑛 > 1 for which 224 is a perfect 𝑛-th power is:

Correct Answer ✓

|7|
|---|


##### G. Examples of RecursiveMAS Across Different Downstream Tasks

###### Case Study of RecursiveMAS on Mathematical Reasoning Questions (AIME2026)

###### Question:

A plane contains points 𝐴 and 𝐵 with 𝐴𝐵 = 1. Point 𝐴 is rotated in the plane counterclockwise through an acute angle 𝜃 around point 𝐵 to point 𝐴′. Then 𝐵 is rotated in the plane clockwise through angle 𝜃 around point 𝐴′ to point 𝐵′. Suppose that 𝐴𝐵′ = 43. The value of cos𝜃 can be written as 𝑚𝑛 , where 𝑚 and 𝑛 are relatively prime positive integers. Find 𝑚+𝑛.

- Recursion Round 1 (in latent space): Planner → Critic → Solver →

- Recursion Round 2 (in latent space): Planner → Critic → Solver →

- Recursion Round 3 (with final output): Planner → Critic → Solver: To solve the problem, we need to analyze the geometric transformations and use the given distances to find the value of cos𝜃.


- 1. Initial Setup: Points 𝐴 and 𝐵 are in the plane with 𝐴𝐵 = 1. Point 𝐴 is rotated counterclockwise through an acute angle 𝜃 around point 𝐵 to point 𝐴′. Point 𝐵 is then rotated clockwise through the same angle 𝜃 around point 𝐴′ to point 𝐵′. We are given that 𝐴𝐵′ = 43.

- 2. Coordinate System: Place point 𝐵 at the origin (0, 0) and point 𝐴 at (1, 0).
- 3. Rotation of Point 𝐴: When point 𝐴 is rotated counterclockwise by angle 𝜃 around point 𝐵, its new coordinates 𝐴′ are: 𝐴′ = (1cos𝜃, 1sin𝜃) = (cos𝜃, sin𝜃).
- 4. Rotation of Point 𝐵: Point 𝐵 is rotated clockwise by angle 𝜃 around point 𝐴′. The coordinates of 𝐵′ after this rotation can be found using:

𝐵′ = 𝐴′ + 𝑅−𝜃(𝐵 − 𝐴′), where 𝑅−𝜃 is the rotation matrix for clockwise rotation by 𝜃:

𝑅−𝜃 =

cos𝜃 sin𝜃 −sin𝜃 cos𝜃

.

The coordinates of 𝐵 − 𝐴′ are 𝐵 − 𝐴′ = (0 − cos𝜃, 0 − sin𝜃) = (−cos𝜃, −sin𝜃). Applying the rotation matrix:

𝑅−𝜃(𝐵 − 𝐴′) =

cos𝜃 sin𝜃 −sin𝜃 cos𝜃

−cos𝜃 −sin𝜃

= −cos2 𝜃 − sin2 𝜃

cos𝜃sin𝜃 − sin𝜃cos𝜃

= −1

0

.

Therefore, the coordinates of 𝐵′ are: 𝐵′ = (cos𝜃, sin𝜃) + (−1, 0) = (cos𝜃 − 1, sin𝜃).

- 5. Distance 𝐴𝐵′: The distance 𝐴𝐵′ is given by:

𝐴𝐵′ = √︁(cos𝜃 − 1 − 1)2 + (sin𝜃 − 0)2 = √︃

(cos𝜃 − 2)2 + sin2 𝜃. Simplifying inside the square root:

𝐴𝐵′ = √︁cos2 𝜃 − 4cos𝜃 + 4 + sin2 𝜃 =

√1 − 4cos𝜃 + 4 =

√5 − 4cos𝜃.

We are given that 𝐴𝐵′ = 43, so √5 − 4cos𝜃 = 43. Squaring both sides gives 5 − 4cos𝜃 = 169 . Solving for cos𝜃: 5 −

16 9

= 4cos𝜃 =⇒

45 9 −

16 9

= 4cos𝜃 =⇒

29 9

= 4cos𝜃 =⇒ cos𝜃 =

29 36

.

- 6. Final Answer: The value of cos𝜃 is 3629. The sum of the numerator and the denominator is 𝑚 + 𝑛 = 29 + 36 = 65.


. Correct Answer ✓

Thus, the final answer is

|65|
|---|


###### Case Study of RecursiveMAS on Scientific and Medical Questions (AIME2026)

###### Question:

A 45-year-old mechanic presents to the emergency department complaining of acute-onset shortness of breath while repairing a plowing tractor for his neighbor. The patient denies having any history of asthma or respiratory symptoms, and does not smoke. His temperature is 99.8°F (37.7°C), pulse is 65/min, blood pressure is 126/86 mmHg, and respirations are 20/min. His oxygen saturation is 97%. On exam, he is pale and diaphoretic. His pupils are contracted. Diffuse wheezes are noted in all lung fields. What is the best treatment for his condition?

- A. Succinylcholine
- B. Inhaled ipratropium and oxygen
- C. Atropine and pralidoxime
- D. Inhaled albuterol and oxygen


- Recursion Round 1 (in latent space): Planner → Critic → Solver →

- Recursion Round 2 (in latent space): Planner → Critic → Solver →

- Recursion Round 3 (with final output): Planner → Critic → Solver: The clinical presentation is highly suggestive of organophosphate poisoning. Clinical Signs:


- • Dizziness/Shortness of breath: Suggests respiratory distress.
- • Pupils are contracted (Miosis): This is a classic sign of cholinergic excess (SLUDGE mnemonic: Salivation, Lacrimation, Urination, Defecation, GI upset, Emesis).
- • Diffuse wheezes: Caused by bronchorrhea and bronchospasm due to overstimulation in the lungs.
- • Pale and diaphoretic: Diaphoresis is a key sign of cholinergic crisis.
- • Vitals: The patient is tachypneic (20/min is borderline but in context of distress, this is significant) and hypoxic (implied by distress, though 97% is maintained, the saturation will drop quickly without treatment).


Analysis of Options:

- • A. Succinylcholine: Depolarizing neuromuscular blocker. Exacerbates or prolongs paralysis due to high endogenous acetylcholine; does not resolve the underlying cholinergic crisis.
- • B. Inhaled ipratropium and oxygen: Anticholinergic. Relieves local respiratory symptoms but fails to address the root cause and systemic cholinergic toxicity.
- • C. Atropine and pralidoxime: Correct treatment. Atropine (muscarinic antagonist) is life-saving, reversing severe secretions and bronchospasm. Pralidoxime reactivates acetylcholinesterase to resolve nicotinic effects.
- • D. Inhaled albuterol and oxygen: Beta-2 agonist. May help bronchospasm but ineffective against massive bronchorrhea and systemic poisoning.


Conclusion: The patient is suffering from organophosphate poisoning (cholinergic crisis). The standard of care involves the administration of atropine to reverse muscarinic effects (especially respiratory secretions and bronchospasm) and pralidoxime to regenerate acetylcholinesterase. So the final answer is:

Correct Answer ✓

|𝐶|
|---|


###### Case Study of RecursiveMAS on Code Generation Tasks (MBPP Plus)

Question: Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.

- Recursion Round 1 (in latent space): Planner → Critic → Solver →

- Recursion Round 2 (in latent space): Planner → Critic → Solver →

- Recursion Round 3 (with final output): Planner → Critic → Solver: To solve this problem, we need to write a function that takes two tuples as input and checks if each element of the second tuple is smaller than its corresponding element in the first tuple. If all elements satisfy this condition, the function should return True; otherwise, it should return False. Here is the code logic:


- 1. Define the function ‘check_smaller‘ that takes two tuples as input.
- 2. Check if the lengths of the two tuples are equal. If they are not, return False.
- 3. Iterate over the elements of the tuples and check if each element of the second tuple is smaller than its corresponding element in the first tuple.
- 4. If all elements satisfy the condition, return True; otherwise, return False. Here is the Python code for the solution: def check_smaller(tuple1, tuple2):


# Check if the lengths of the tuples are equal if len(tuple1) != len(tuple2):

return False

# Iterate over the elements of the tuples for i in range(len(tuple1)):

if tuple1[i] <= tuple2[i]: return False

# If all elements satisfy the condition, return True return True

Correct Answer ✓

###### Case Study of RecursiveMAS on Search Based Tasks (Bamboogle)

Question: Who was president of the United States in the year that Citibank was founded?

- Recursion Round 1 (in latent space): Planner → Critic → Solver →

- Recursion Round 2 (in latent space): Planner → Critic → Solver →

- Recursion Round 3 (with final output): Planner → Critic → Solver: To answer this question, I need to find out the year Citibank was founded and then identify the President of the United States in that year. First, I will search for the founding year of Citibank. <search>When was Citibank founded?</search> <result>


- [1] Citigroup - Wikipedia Citibank was chartered by the State of New York on June 16, 1812, with $2 million of capital. · · ·
- [2] What is Brief History of Citi Company? - Matrix BCG The genesis of Citi, originally named the City Bank of New York, dates back to June 16, 1812, when it received its charter in New York City. The bank commenced operations on September 14, 1812. · · ·
- [3] Citibank - Students | Britannica Kids | Homework Help Second largest bank in U.S., with about 270 branch banks in New York City area. Present name since 1976. · · ·
- [4] A bank with history and tradition - Citi.com Citibank opened for business in 1812 in New York under its original name City Bank of New York. Since then, Citi has been a major player in some of the world’s most innovative breakthroughs in banking. · · · </result>


Based on the search results, Citibank (originally City Bank of New York) was founded in 1812. Specifically, it was chartered on June 16, 1812, and opened for business on September 14, 1812. Now I need to find out who was the President of the United States in 1812.

<search>President of the United States 1812</search> <result>

- [1] The Election of 1812 | American Battlefield Trust On October 14, 1812, incumbent president, James Madison, wrote to his friend and former president, · · ·
- [2] The War of 1812: The Nation Braces for War James Madison (1751-1836) James Madison, the Father of the Constitution and the Bill of Rights, was President of the United States during the War of 1812. · · ·
- [3] Key American Personalities | 1812 Virtual Exhibition As secretary of state under President Thomas Jefferson, future president James Madison had been deeply involved in the events leading to the war. · · ·
- [4] James Madison - Wikipedia Madison was elected president in 1808. Motivated by a desire to acquire land held by Britain, Spain, and Native Americans, Madison led the United States into the War of 1812. · · · </result>


The search results indicate that James Madison was the President of the United States in 1812. So, the answer is Correct Answer ✓

|𝐽𝑎𝑚𝑒𝑠 𝑀𝑎𝑑𝑖𝑠𝑜𝑛|
|---|


