<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Efficient inference for agent-based models of real-world phenomena
authors: [Andreas Christ Sølvsten Jørgensen, Atiyo Ghosh, Marc Sturrock, Vahid Shahrezaei]
year: 2021
doi: 10.1101/2021.10.04.462980
source_url: https://doi.org/10.1101/2021.10.04.462980
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Efficient inference for agent-based models of real-world phenomena

## TL;DR
Machine-learning emulators and "direct inference machines" can recover the parameters of computationally heavy stochastic agent-based models (ABMs) orders of magnitude faster than classical simulation-based inference, but no single algorithm wins across problems — method choice is problem-dependent and must be benchmarked per application.

## Key findings
- Two ML strategies compared on two real-world ABMs (a glioblastoma cellular-automata "CA" model, 4 params; a SIRDS epidemic lattice model, 5 params): (1) **emulators** (surrogate simulators feeding rejection-ABC or MCMC) and (2) **direct inference machines** that map observations → parameters directly, skipping Bayesian sampling.
- Three emulators tested: deep **neural network (NN)** with MC-dropout (an approximate Bayesian/Gaussian-process formulation, Gal & Ghahramani loss), **mixture density network (MDN)**, **Gaussian process (GP)**.
- **No one-size-fits-all**: NN was best emulator for the cancer CA model (closely recovers mean/median/width, lowest Wasserstein distance); **MDN beat NN for the epidemic SIRDS model** at large training sets. GP was consistently worst (distributions too broad) and could not handle the kernel matrix at the largest grid (10⁵).
- **Direct inference machines performed as well or better than emulation-based inference, even with small training sets** — some metrics did not improve with more data. This is the paper's headline practical recommendation.
- **MCMC robustness problem**: the stochastic emulator output inflates autocorrelation lengths. Using individual emulator predictions in the likelihood (case a) gave median autocorrelation lengths of 383–412 (CA-NN) vs 1889–1953 (CA-GP) and 2118–2179 (SIRDS-NN) — GP yields far fewer effective samples, noisy/disconnected posterior contours. Switching to **global distribution properties in the likelihood (case b)** cut autocorrelation to 163–174 (CA) and 194–266 (SIRDS) (Table 1).
- **Rejection ABC did NOT suffer the MCMC noise pathology** for either ABM, reliably reconstructing mean/median even when its distance measure uses individual emulator predictions.
- **CPU cost** (Fig 5): the simulations dominate total time; emulator/inference-machine training costs orders of magnitude less. Methods minimizing required simulations win — direct inference machines need new sims only at training, whereas MCMC needs fresh sims per observation set.
- All methods struggled with the same (non-identifiable) parameters and succeeded on the same others — a consistency sanity-check across methods.

## Methods (brief)
Synthetic "mock observations" generated from each ABM (250 parameter sets × 250 repeats); training grids of 10²–10⁵ unique-parameter simulations built via Sobol sequences over uniform priors. Emulators built in TensorFlow (NN: 3×100-neuron hidden layers, 20% dropout, early stopping; MDN: 3-component multivariate-normal mixture) and scikit-learn (GP: RBF + white-noise kernel). Inference via rejection ABC (elfi, keep best 10⁴ of 10⁷) and ensemble MCMC (emcee). Emulator quality scored by error in mean/median, σ-ratio, Wasserstein distance; inference scored by residuals, posterior σ, and −log q(θ₀) attributed to the truth.

## Limitations
Both ABMs are deliberately simplistic toy-realistic models; conclusions about which algorithm wins may not generalize. Sequential inference techniques (which can cut simulation counts further) were excluded because the 250-test-case design negates their per-observation retraining advantage. HMC was inapplicable (no reliable gradients). Mock observations assumed multivariate-Gaussian, diagonal-covariance data — a simplification the authors note real data may violate.

## Citations of interest
- Lueckmann et al. 2021 (arXiv:2101.04653) — benchmarking simulation-based inference; the no-one-size-fits-all finding aligns with this work.
- Gal & Ghahramani 2015 (arXiv:1506.02142) — dropout as Bayesian approximation; basis for the NN's stochastic/uncertainty-aware predictions.
- Cranmer, Brehmer & Louppe — review of the frontier of simulation-based inference (likelihood/posterior density estimation).
- Bishop 1994; Davis et al. 2019 — mixture density networks and their use in emulating epidemiological individual-based models.
- Foreman-Mackey et al. 2013 (emcee) / Goodman & Weare 2010 — the ensemble MCMC sampler and affine-invariance method used.
- Bellinger et al. 2016 — Sobol-sequence grid sampling and the observation-error sampling scheme for direct inference machines.
