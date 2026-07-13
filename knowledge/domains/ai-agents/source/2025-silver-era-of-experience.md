<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Welcome to the Era of Experience"
authors: [David Silver, Richard S. Sutton]
year: 2025
source_url: https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
drive_file_id: 1s7lUx-6g1Nj47qw_Z7RV0VEeMbI6Lm3k
text_source: pdf
ingested_by: agent
---
# Welcome to the Era of Experience

**Authors:** David Silver, Richard S. Sutton  ·  **Year:** 2025  ·  **Source:** https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf (preprint chapter for *Designing an Intelligence*, MIT Press)

## One-line
AI is transitioning from an "era of human data" (imitation/fine-tuning on human-generated text) to an "era of experience," where superhuman agents learn predominantly from their own grounded interaction with the world.

## Key claim
Training on human-generated data is approaching a limit — high-quality data sources are being exhausted and the approach cannot surface knowledge (new theorems, technologies, discoveries) that lies beyond existing human understanding. The next leap to superhuman intelligence requires agents that learn continually from streams of self-generated experience, with actions/observations richly grounded in the environment, rewards grounded in real-world signals rather than human prejudgement, and reasoning that goes beyond human language/thought patterns.

## Method
This is a position essay (not an empirical study). It argues via four proposed dimensions distinguishing "experiential" agents from human-data agents: (1) agents inhabit long streams of experience rather than short isolated episodes; (2) actions/observations are richly grounded in real/digital environments (APIs, tool use, computer control) rather than mediated solely through human dialogue; (3) rewards are grounded in environmental/real-world signals (e.g., health metrics, exam results, sales, sensor data) rather than human-judged preferences; (4) agents plan and reason using flexible, possibly non-human representations of thought, not solely human language chains-of-thought. It illustrates each dimension with examples (health/wellness agents, education agents, science agents) and grounds the argument historically via a "sketch chronology" figure spanning the era of simulation (AlphaGo/AlphaZero), era of human data (GPT-3/ChatGPT), and emerging era of experience (Computer Use, AlphaProof).

## Result
The authors contend today's algorithms and technology already provide a sufficient foundation for this transition, citing AlphaProof (IMO medal via RL on self-generated proofs) and DeepSeek's RL-driven reasoning gains as early evidence experiential learning already surpasses human-centric approaches in narrow domains. They propose reward functions can be adapted in a user-guided way (e.g., a neural network combining grounded signals, tuned via human feedback as a bi-level optimization) to preserve steerability without reintroducing a human-judgement ceiling. They argue that grounding in real-world feedback is necessary to escape inherited human biases/fallacies in reasoning, and that world models offer one path to plan directly in terms of actions and their real-world consequences. Overall, they predict imminent, rapid progress toward broadly capable, superhuman agents as the field shifts investment toward RL-style experiential learning.

## Key terms
reinforcement learning, streams of experience, grounded rewards, human-centric AI, AlphaProof, AlphaZero, world model, chain of thought, autonomous agents, reward function, self-play, superhuman intelligence
