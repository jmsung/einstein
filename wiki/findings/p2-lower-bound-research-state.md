---
type: finding
author: agent
drafted: 2026-05-02
question_origin: research/p2-lower-bound (Goal 2 reframed)
status: answered
related_problems: [P2]
related_concepts: [autocorrelation-inequality.md, lp-duality.md, sidon-sets.md]
cites:
  - ../../source/papers/2017-cloninger-autoconvolution-sidon.md
  - ../../source/papers/2010-matolcsi-autoconvolution.md
  - ../../source/papers/2010-vinuesa-sidon-thesis.md
---

# Why P2 lower bounds aren't advancing past 1.28

## Question

The published lower bound for the first-autocorrelation constant has been stuck at $C_1 \ge 1.28$ since Cloninger–Steinerberger 2017, while the construction-side upper bound has dropped from 1.5097 (2010) to 1.50286 (2026, TTT-Discover). The conjectured continuous infimum is $C_1 \approx 3/2$ (Matolcsi–Vinuesa 2010). What blocks lower-bound progress, and what avenue is structurally new?

## Answer

Four proof techniques cover the published literature. Three are exhausted; one is untried.

| Technique | Best bound | Why it stops |
|---|---:|---|
| Sidon-set transfer (Cilleruelo–Ruzsa–Trujillo, Green, Martin–O'Bryant) | 1.183 | Combinatorial slack — continuous limit loses the integer structure |
| Fourier-kernel + Selberg majorant (Yu, Martin–O'Bryant, Matolcsi–Vinuesa) | **1.2748** | **Theoretical ceiling at ~1.276** — proven by Matolcsi–Vinuesa 2010, §4 |
| Spatial-decomposition LP relaxation (Cloninger–Steinerberger) | **1.28** | **Compute-bound** — $\sim 2 \times 10^4$ CPU hours for $n \le 24$, $m=50$ rationals; scales exponentially in $n$ |
| **SOS / Lasserre hierarchy** | — | **Never published for $C_1$** — open avenue |

### Two distinct walls

The three exhausted techniques fail in two qualitatively different ways:

- **Theoretical wall (Fourier-kernel)**: the Fourier-kernel framework with kernels of the form $K = \beta * \beta$ has a theoretical ceiling at $\approx 1.276$ (Matolcsi–Vinuesa 2010 §4). Tightening the kernel within the framework returns diminishing fractions of the gap to 1.276 and never crosses it; an entirely different kernel class would be needed to break through.

- **Compute wall (Cloninger–Steinerberger)**: their proof has *no* theoretical ceiling — they explicitly state the method "should be able to prove lower bounds arbitrarily close to the sharp result" — but the case enumeration grows exponentially in the discretization parameter $n$. To push from 1.28 ($n \le 24$) to ~1.30 needs $n \approx 30+$, estimated $\sim 10^6$ CPU hours under their published scaling. This is reachable in principle (a few months of cloud compute) but no group has published the run.

The unpublished claim of 1.2802 (Xinyuan Xie, Grok-assisted, Jan 2026) is within the C-S framework and consistent with this picture — squeezing a few units in the third decimal at the same compute scale, not a structural advance.

### What's structurally untried

Lasserre / SOS hierarchies have not been published for the autoconvolution lower-bound problem. The setup is well-posed:

$$
C_1 = \inf \big\{ \|f \star f\|_\infty \;:\; f \ge 0,\; \mathrm{supp}\, f \subseteq [-\tfrac{1}{4}, \tfrac{1}{4}],\; \int f = 1 \big\}
$$

Discretizing $f$ on $n$ cells turns the constraint $\|f \star f\|_\infty \le \tau$ into a system of polynomial inequalities of degree 2 in the cell heights, which fits the Lasserre framework. The level-$d$ relaxation upper-bounds $C_1$ from below with a semidefinite program of size $O(n^{2d})$. For modest $n$ (say $n \le 50$, $d=2$) the SDP is solvable on a workstation; the question is whether the SDP's optimum tracks the C-S branch-and-bound bound or beats it.

This is a structurally different argument: the C-S relaxation is a *finite* LP per case, with branch-and-bound chasing tight enumeration; the Lasserre relaxation is a *single* SDP per level, with the hierarchy converging to the true value as $d \to \infty$ (Lasserre's positivstellensatz). The two methods could combine — Lasserre as an outer SDP, C-S as an inner case-elimination — producing a hybrid that neither has on its own.

## What this rules out (or does not)

- Rules out: pursuing the Fourier-kernel direction without a structural change. The 1.276 ceiling is a theorem.
- Does not rule out: extending the C-S enumeration with more compute. A $\sim 10^6$ CPU-hour run pushing to $n \approx 30$ would tighten the bound by an estimated $0.01$–$0.02$ (small but published-bound territory).
- Identifies as new: SOS/Lasserre hierarchy as the only published-literature gap.

## What might still work

1. **Lasserre level-2 SDP at $n \in [20, 40]$** — small enough to solve, large enough to maybe beat 1.28. Single-SDP feasibility test before committing to compute.
2. **Hybrid SDP + branch-and-bound** — use the Lasserre dual to eliminate sub-cases in the C-S enumeration, reducing the branch-and-bound exponent.
3. **Replicate C-S at $n=25$** as a calibration run on our compute. Cost-estimate before launching, but if cheap it lets us put a number on "what would it take to push to 1.29."

## Confidence

- Survey of techniques: high confidence — sourced from `lower-bounds-first.md` (curated by prior cycles) and the four primary papers.
- "SOS untried" claim: high confidence — `lower-bounds-first.md` states "nothing in the literature surveys a Lasserre or SDP hierarchy for this problem"; not refuted by the 2025–2026 arena-side activity (TTT-Discover, AlphaEvolve, ThetaEvolve are all upper-bound constructions).
- Compute estimates: rough order-of-magnitude. C-S 2017 reports ~20K CPU hours for $n \le 24$; the exponential-in-$n$ scaling is their own claim, not a fitted curve from multiple data points.

## See also

- Concept: [autocorrelation-inequality](../concepts/autocorrelation-inequality.md)
- Concept: [lp-duality](../concepts/lp-duality.md) (LP-side framing)
- Concept: [sidon-sets](../concepts/sidon-sets.md) (Sidon-set transfer baseline)
- Open question: [2026-05-02-p2-sos-lasserre-feasibility](../questions/2026-05-02-p2-sos-lasserre-feasibility.md)
- Source: [2017-cloninger-autoconvolution-sidon](../../source/papers/2017-cloninger-autoconvolution-sidon.md)
- Source: [2010-matolcsi-autoconvolution](../../source/papers/2010-matolcsi-autoconvolution.md)
- Tracking: `mb/tracking/problem-2-first-autocorrelation/lower-bounds.md`
- Tracking (full survey): `mb/tracking/problem-3-autocorrelation/lower-bounds-first.md`
