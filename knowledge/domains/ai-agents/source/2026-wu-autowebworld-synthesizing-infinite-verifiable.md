<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines
authors: [Yifan Wu, Yiran Peng, Yiyu Chen, Jianhao Ruan, Zijie Zhuang, Cheng Yang, Jiayi Zhang, Man Chen, Yenchi Tseng, Zhaoyang Yu, Liang Chen, Yuyao Zhai, Bang Liu, Chenglin Wu, Yuyu Luo]
year: 2026
source_url: https://arxiv.org/abs/2602.14296
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines

**Authors:** Yifan Wu, Yiran Peng, Yiyu Chen, Jianhao Ruan, Zijie Zhuang, Cheng Yang, Jiayi Zhang, Man Chen, Yenchi Tseng, Zhaoyang Yu, Liang Chen, Yuyao Zhai, Bang Liu, Chenglin Wu, Yuyu Luo  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2602.14296

## One-line
Synthesizes verifiable training environments for web GUI agents by specifying each site as a finite state machine, then having a coding agent render a runnable front-end whose state transitions match the FSM exactly.

## Key claim
Training a 7B Qwen2.5-VL agent on 11,663 FSM-verified synthetic trajectories (generated at $0.04/trajectory across 29 synthetic websites, total cost $447.37) yields 27.42% success rate on WebVoyager within 15 steps, beating baselines trained on orders-of-magnitude larger datasets, with a clean scaling law in trajectory volume vs benchmark performance.

## Method
FSM-as-environment: a multi-agent pipeline (FSM Proposer / Validator / Improver) drafts an FSM from a web-theme name; a coding agent then synthesizes a Vue front-end whose components correspond to FSM states. Trajectories are produced by BFS over the FSM transition graph (only expanding actions whose preconditions hold), then replayed in the synthesized site to filter UI-mismatch failures. The policy is trained with GRPO using a composite reward $R = R_{\text{act}} + R_{\text{coord}} + R_{\text{fmt}}$ (action-type match, bounding-box containment of predicted click coordinates, and tag-format regex match).

## Result
29 synthetic sites across commerce / productivity / health / media / communication; 11,663 verified trajectories; total pipeline cost $447.37 (Thinking dominates at $272.17, FSM $57.10, Web $52.26, Queries $65.84). Trained 7B agent reaches 27.42% on WebVoyager ≤15 steps (SOTA in that regime); monotonic improvement on WebVoyager and Online-Mind2Web as synthetic data volume grows.

## Key terms
finite state machine, FSM, web GUI agent, synthetic environment, verifiable trajectory, BFS trajectory synthesis, GRPO, Qwen2.5-VL, WebVoyager, Online-Mind2Web, coding agent, verifier bottleneck, scaling law, multi-agent pipeline
