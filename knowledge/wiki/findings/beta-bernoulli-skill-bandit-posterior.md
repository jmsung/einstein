---
type: finding
author: agent
drafted: 2026-05-27
question_origin: branch-js-feat-skill-bandit
status: answered
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - ../../source/2019-slivkins-introduction-multi-armed-bandits.md
  - ../../source/2019-feng-intrinsic-robustness-stochastic-bandits.md
  - ../../agent/skill-library.md
---

# Beta-Bernoulli is the right posterior for the skill bandit (G0)

## Question

The skill bandit must pick *which technique to try* per problem category from
`docs/agent/skill-library.md`. Which bandit policy fits — Thompson sampling
(Beta-Bernoulli), UCB, or ε-greedy — given the library's counts and our
warm-restart / sparse-reward setting?

## Answer: Thompson sampling with `Beta(α=top3+1, β=tried−top3+1)`

Three properties of *our* setting pin the choice:

1. **The reward is Bernoulli, so the conjugate prior is Beta.** Each
   skill-library row records `tried` (arm pulls) and `top3` (successes) for a
   `(category, technique)` arm. The latent "P(this technique reaches top-3 on
   this category)" is a single Bernoulli parameter θ. Beta is the conjugate
   prior to Bernoulli: after `s` successes in `n` pulls the posterior is
   `Beta(s+1, n−s+1)` from a uniform `Beta(1,1)` prior. So
   `Beta(top3+1, tried−top3+1)` *is* the exact posterior the counts already
   encode — no modeling assumption beyond "did it land top-3?", which is the
   column the library was built to track.

2. **Warm-restart is free with Thompson; awkward with the others.** The
   library's counts are HISTORICAL (pre-refactor episodes, see its "Bootstrap
   entries"). Thompson seeds each arm's posterior directly from those counts —
   a `5/3` arm starts at `Beta(4,3)` (informative), an unseen arm at `Beta(1,1)`
   (uniform → samples ~U(0,1), maximal exploration). UCB needs a pull-count
   schedule and a tuned confidence constant; ε-greedy throws away the count
   structure entirely and explores uniformly. Thompson's exploration is
   *automatically* proportional to posterior variance, which is exactly what
   sparse, unequal historical counts call for.

3. **Sparse rewards favor posterior sampling over confidence bounds.** With
   many arms at `tried < 3` (the library's own "watchlist" threshold), UCB's
   bonus term is dominated by the count denominator and degenerates toward
   round-robin; Thompson keeps sampling informative even at n=1 because the
   Beta posterior is still proper. Slivkins frames Thompson as "Bayesian
   posterior matching" and places stochastic K-armed regret at the optimal
   `Θ(√KT)` minimax with a logarithmic instance-dependent floor — the same
   landscape UCB achieves, but without a tuning constant
   (`source/2019-slivkins-introduction-multi-armed-bandits.md`). Feng et al.
   survey UCB, ε-greedy, and Thompson side by side as the three canonical
   stochastic policies (`source/2019-feng-intrinsic-robustness-stochastic-bandits.md`).

## The connection the wiki already flagged

Slivkins' own "why it matters here" note anticipated this branch verbatim:
*"Could UCB-style allocation rule the loop's compute router — treat techniques
in `skill-library.md` as arms with regret = wasted GPU-hours, exploit by
success rate?"* This finding answers the variant: yes, but with **Thompson over
Beta-Bernoulli**, not UCB, because our reward is binary (top-3 or not) and our
counts are sparse + warm-started — the regime where posterior sampling beats a
confidence bound.

## What this fixes for the build

- The sampler arm for `(category, technique)` is `Beta(top3+1, tried−top3+1)`;
  posterior mean `(top3+1)/(tried+2)` is the Laplace-smoothed hit-rate, so the
  bandit degrades gracefully to "rank by hit-rate" in the high-data limit while
  exploring correctly when data is thin.
- Unseen `(category, technique)` → `Beta(1,1)` = uniform prior (the
  empty-history fallback the sampler tests in G1).
- Per-category masking (don't sample autocorrelation arms for a kissing
  problem) is orthogonal to the posterior — it restricts the arm set before
  sampling.

## What this rules out

- **UCB** — needs a tuned exploration constant and degenerates to round-robin
  under sparse counts; revisit only if a future audit shows Thompson
  over-exploiting a stale high-count arm.
- **ε-greedy** — discards the Beta structure the library already carries; strictly
  dominated here.

See also: `docs/agent/skill-library.md` (the arm table), the swap-surface finding
`meta-loop-swap-surface.md` (where `thompson-bandit-v0` plugs in).
