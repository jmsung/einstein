---
type: source
kind: paper
title: "Reinforcement Learning for Combinatorial Optimization: A Survey"
authors: Nina Mazyavkina, S. Sviridov, S. Ivanov, Evgeny Burnaev
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.03600
source_local: ../raw/2020-mazyavkina-reinforcement-learning-combinatorial-optimiz.pdf
topic: general-knowledge
cites:
---

# Reinforcement Learning for Combinatorial Optimization: A Survey

**Authors:** Nina Mazyavkina, S. Sviridov, S. Ivanov, Evgeny Burnaev  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.03600

## One-line
Survey of reinforcement-learning approaches that replace hand-crafted heuristics for NP-hard combinatorial optimization (TSP, Max-Cut, MIS, MVC, BPP, VRP) by training an agent to construct or iteratively improve solutions.

## Key claim
RL-based solvers — particularly attention-encoder + REINFORCE/A2C methods of Kool et al. (2019), Bello et al. (2017), and the iterative learner of Lu et al. (2020) — match or beat OR-Tools and approach LKH-3 on TSP/CVRP at $N \in \{20, 50, 100\}$ (e.g., TSP tour lengths $\approx 3.8 / 5.7 / 7.9$ vs LKH-3's $3.8 / 5.7 / 7.8$), while running an order of magnitude faster than classical heuristics; quality degrades on larger $N$ ($\geq 250$).

## Method
Frames CO as an MDP where states are partial/complete solutions, actions extend or rewire them, rewards reflect objective change, and a learned policy $\pi_\theta(a|s)$ or value $Q(s,a)$ replaces the heuristic. State encoders are RNN/LSTM, pointer networks, attention/Transformer, or GNNs (GCN, GAT, GIN, Structure2Vec). Training uses model-free policy-gradient (REINFORCE, A2C/A3C, PPO, Sinkhorn-PG), value-based DQN-style Q-learning, or model-based MCTS (AlphaZero/MuZero variants); methods split into *constructive* (build solution step-by-step) vs *joint/iterative* (start from feasible solution and improve).

## Result
On Erdős–Rényi TSP: Kool et al. attention + REINFORCE reaches $5.7$ at $N{=}50$ matching LKH-3; on CVRP, Lu et al.'s iterative rewriter ties or beats LKH-3 across all reported capacities (e.g., $10.4$ at $N{=}50$/Cap.30). On Max-Cut, MIS, MVC, BPP the picture is more fragmented — most works test only a few configurations and only against weak baselines. Empirical pattern: RL ≈ baseline up to $N{\approx}100$, falls behind for $N \geq 250$, and consistently beats classical heuristics on wall-clock time.

## Why it matters here
General background; no direct arena tie. None of the surveyed problems (TSP, Max-Cut, MIS, MVC, BPP, VRP) are Einstein Arena problems, but the MDP framing — "constructive vs iterative-improvement" agent loops, encoder choice (GNN/attention) for structured states, and policy-gradient vs MCTS trade-offs — is the closest established literature for the autonomous-loop agent's own design, particularly any future RL-driven move-generator for discrete-combinatorics problems.

## Open questions / connections
- Generalization across problem instances/sizes/distributions remains weak — most learners overfit to the training $N$; how to transfer learned policies across CO families is open.
- Joint+constructive hybrids are unexplored for BPP; joint methods absent for MVC — fertile gaps the survey itself flags.
- How to fuse learned heuristics with branch-and-bound / cutting-plane solvers (cf. Tang et al. 2020 "learning to cut"; imitation learning à la Hester et al. 2018) for provable bounds.
- Whether MCTS-style planners (AlphaZero/MuZero) outperform policy-gradient methods on graph CO at scale is still empirically unsettled (Abe et al. 2019).

## Key terms
reinforcement learning, combinatorial optimization, Markov decision process, policy gradient, REINFORCE, Q-learning, actor-critic, Monte-Carlo tree search, AlphaZero, pointer network, attention encoder, graph neural network, Structure2Vec, Travelling Salesman Problem, Max-Cut, Maximum Independent Set, Minimum Vertex Cover, Bin Packing, Vehicle Routing Problem, LKH-3, OR-Tools, constructive vs iterative heuristics
