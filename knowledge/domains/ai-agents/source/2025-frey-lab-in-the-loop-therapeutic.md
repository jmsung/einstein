<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Lab-in-the-loop therapeutic antibody design with deep learning
authors: [Nathan C. Frey, Isidro Hötzel, Samuel D. Stanton, Ryan Kelly, Robert G. Alberstein, Emily K. Makowski, Karolis Martinkus, Daniel Berenberg, Jack Bevers, Tim Bryson, Pamela Chan, Yan Chen, Alicja Czubaty, Tamica D'Souza, Hayley Dwyer, Anna Dziewulska, James W. Fairman, Allen Goodman, Jens Hofmann, Henri Isaacson, Aya Ismail, Samuel James, Tomas Joren, Simon Kelow, James R. Kiefer, Matthieu Kirchmeyer, Joseph Kleinhenz, James T. Koerber, Julien Lafrance-Vanasse, Andrew Leaver-Fay, Jae Hyeon Lee, Edith Lee, Donghyeon Lee, Wenzhao Liang, Jae Yoon Lin, Sidney Lisanza, Andreas Loukas, Jan Ludwiczak, Sai Pooja Mahajan, Omar Mahmood, Hamed Mohammadi-Peyhani, Santrupti Nerli, Ji Won Park, Jisun Park, Stephen Ra, Sarah Robinson, Saeed Saremi, Franziska Seeger, Indrani Sinha, Anna M. Sokol, Nataša Tagasovska, Hung To, Edward Wagstaff, Allen Wang, Andrew M. Watkins, Brian Wilson, Shuai Wu, Karolina Zadorozhny, John Marioni, Aviv Regev, Yan Wu, Kyunghyun Cho, Richard Bonneau, Vladimir Gligorijević]
year: 2025
doi: 10.1101/2025.02.19.639050
source_url: https://www.biorxiv.org/content/10.1101/2025.02.19.639050v1
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Lab-in-the-loop therapeutic antibody design with deep learning

## TL;DR
A semi-autonomous "lab-in-the-loop" pipeline couples generative ML, multi-task property predictors, and active-learning selection with iterative in vitro testing, yielding 3–100× affinity improvements for 10/11 seed antibodies across four clinical antigen targets, with the best binders exceeding 100 pM affinity.

## Key findings
- **Closed-loop architecture.** The system orchestrates five components in an iterative optimization loop: (1) repertoire-mining methods to source candidate sequences, (2) generative ML models to propose antibody variants, (3) multi-task property predictors, (4) active-learning ranking/selection of which designs to assay, and (5) in vitro experimentation whose data is re-ingested to update models each round. The key claim is *end-to-end* automation of the design→predict→select→assay→ingest cycle.
- **Scope of the campaign.** Applied to **11 seed antibodies** obtained via animal immunization against **four clinically relevant antigen targets — EGFR, IL-6, HER2, and OSM** (oncostatin M).
- **Throughput.** Over **1,800 unique antibody variants** were experimentally tested across **four rounds** of iterative optimization.
- **Outcome.** Identified **3–100× better-binding variants for all four targets and for 10 of 11 seeds**; the best binders exceeded **100 pM affinity**. The single seed not improved is noted as the lone failure case.
- **Significance for ML-driven discovery.** Demonstrates that multi-property antibody optimization — historically a slow, expert-driven affinity-maturation problem — can be driven by an automated ML+lab loop, framing antibody engineering as an active-learning problem where each experimental round sharpens the predictors and the generative proposal distribution.
- **Motivation context.** Antibodies are a dominant therapeutic modality (58 new FDA-approved antibody therapeutics 2019–2023); discovery/engineering cost is the bottleneck this method targets.

## Methods (brief)
Seed antibodies were raised by animal immunization. The computational loop combines repertoire mining, generative sequence/structure models, and multi-task predictors trained to forecast binding and developability properties, with an active-learning acquisition step selecting a batch of designs per round. Designs were expressed and characterized in vitro (binding affinity), and measured data fed back to retrain/rerank over four rounds. (Detailed model architectures and assay protocols are in the full preprint; the paperclip extraction here captured the abstract and introduction only.)

## Limitations
N is modest at the seed level (11 seeds, 4 targets) and the loop improved 10/11, so generality of the failure mode is unclear; results are an unreviewed bioRxiv preprint, and the captured extraction lacked the Results/Discussion detail (ablations, per-component contribution, developability outcomes), so the relative value of each pipeline component cannot be assessed from this distillation. Reported affinities (>100 pM) are binding metrics, not validated therapeutic efficacy.

## Citations of interest
- FDA antibody-approval landscape 2019–2023 (cited [3]) — establishes the 58-approval demand context motivating the work.
- Foundational immunology of antibody diversification ([1], [2]) — basis for treating antibodies as a near-universal recognition modality.
- (Full reference list not retained in the paperclip extraction; primary preprint at DOI 10.1101/2025.02.19.639050 for generative-model and active-learning method citations.)
