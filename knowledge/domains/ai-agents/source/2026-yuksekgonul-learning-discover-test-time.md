---
type: source
kind: paper
title: Learning to Discover at Test Time
authors: Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2601.16175
source_local: ../raw/2026-yuksekgonul-learning-discover-test-time.pdf
topic: general-knowledge
cites:
---

# Learning to Discover at Test Time

**Authors:** Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2601.16175

## One-line
Continue training (RL fine-tune) an open LLM at test time on a single hard problem, using an entropic max-favoring objective and PUCT-style state reuse, to discover new state-of-the-art constructions.

## Key claim
TTT-Discover with gpt-oss-120b sets new SOTA on Erdős' minimum overlap ($c \leq 0.380876$, vs AlphaEvolve's $0.380924$ and Haugland's human $0.380927$), first autocorrelation inequality ($C_1 \leq 1.50287$, vs AlphaEvolve V2 $1.50317$), a GPUMode TriMul kernel competition (up to 2× faster than best human), AtCoder Heuristic Contest 39 ($567{,}062$ vs human $566{,}997$), and single-cell denoising (MSE $0.71$ vs MAGIC $0.64$) — at ~$500/run on Tinker.

## Method
Frame each problem as an MDP where state $s$ is a candidate solution (step function, kernel code, algorithm code), action $a$ is LLM-generated code+thinking, transition executes the code, reward $R(s)$ is the certified bound or inverse runtime. Train via the **entropic objective** $J_\beta(\theta)=\mathbb{E}_s \log \mathbb{E}_{a\sim\pi_\theta}[e^{\beta(s)R(s,a)}]$ with per-state adaptive $\beta$ (KL-constrained), advantage $A(a;s)=w_{\beta(s)}(a)-1-\lambda\log(\pi_\theta/\pi_{\theta_0})$ — heavily upweighting near-max rewards rather than mean. Reuse heuristic is **PUCT** with $Q(s)=\max$ child reward (not mean) plus rank-based prior and visit-count exploration bonus; runs 50 steps × 512 rollouts on gpt-oss-120b via LoRA rank-32.

## Result
- Erdős min overlap: 600-piece **asymmetric** step function gives $c \leq 0.380876$ — improvement 16× larger than AlphaEvolve's gain over Haugland; uses FFT-accelerated gradient descent + random hill climbing + simulated annealing with feasibility projection ($f\in[0,1]$, $\int f=1$).
- AC1: 30000-piece step function gives $C_1 \leq 1.50287$, starting from scratch (not refining AlphaEvolve V2). Key trick: LP restricted to top-$K$ near-tight convolution positions; gradients aggregated from all near-maximum positions.
- AC2: $0.959$ — fell short of AlphaEvolve V2's $0.961$.
- Best-of-25600 baseline with same budget also beats AlphaEvolve on Erdős — surprising; shows much of the win comes from the open-model sampling distribution, with TTT-Discover adding the rest.

## Why it matters here
Direct upgrade path for the autonomous-loop agent: the same problems (Erdős min overlap, autocorrelation inequalities) are in the Einstein-Arena-style mathematics suite, and the **entropic-objective + PUCT-with-max** recipe is a concrete alternative to vanilla best-of-N or evolutionary search currently informing `compute-router` / council-dispatch choices. Confirms that for discovery (max, not mean), max-favoring objectives matter — relevant to how the agent ranks/keeps constructions in its own buffer.

## Open questions / connections
- Can the entropic-$J_\beta$ + PUCT recipe be replicated without an RL fine-tuning loop (prompt-only) and still beat plain best-of-N? Best-of-25600 already beat AlphaEvolve here.
- AC2 regression: why does TTT-Discover lose to AlphaEvolve V2's 50000-piece construction on $C_2$ but win on $C_1$? Construction-size scaling vs optimizer choice.
- Extends AlphaEvolve / ShinkaEvolve / ThetaEvolve / EvoTune / MiGrATe line — leaves open whether learning vs search advantage holds on geometry problems (e.g., circle packing was attempted but not reported as SOTA).
- The 600-piece **asymmetric** Erdős construction breaks the symmetric-density prior — invites re-examining the Swinnerton-Dyer density framework for other partition-overlap-style problems.

## Key terms
test-time training, reinforcement learning, entropic objective, PUCT, evolutionary search, AlphaEvolve, Erdős minimum overlap, autocorrelation inequality, step function construction, LP restricted active set, best-of-N, gpt-oss-120b, Swinnerton-Dyer density, LoRA, discovery problem
