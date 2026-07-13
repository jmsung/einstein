<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: A Self-Driving Lab for Nano- and Advanced Materials Synthesis
authors: [Mohammad Zaki, Carsten Prinz, Bastian Ruehle]
year: 2025
doi: 10.1021/acsnano.4c17504
source_url: https://doi.org/10.1021/acsnano.4c17504
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# A Self-Driving Lab for Nano- and Advanced Materials Synthesis

## TL;DR
MINERVA is a modular, robot-arm-centered self-driving lab (SDL) that fully automates synthesis, purification, and in-line characterization of seven nano-/advanced materials spanning five material classes, with batch-to-batch size variation below ~5%; all hardware designs and the orchestrating software (MINERVA-OS) are released open-source.

## Key findings
- **Versatility across chemistries:** One platform reproducibly made seven materials from five classes via five distinct reaction mechanisms — Au NPs (citrate reduction), silica + mesoporous silica (sol–gel/Stöber), ZIF-8 MOF (coordination chemistry), CuO (coprecipitation), and Au@SiO₂ / CuO@SiO₂ core–shell (seed-mediated growth). Reaction scales ranged from sub-10 mL to a few hundred mL.
- **Reproducibility (3 batches each):**
  - AuNP: DLS Z-average 19.1 ± 0.9 nm; TEM 16.2 ± 0.4 nm (auto-seg) vs 16.5 ± 0.4 nm (manual); SPR peak at 518 nm across all batches; batch variation <5%.
  - SiNP: Z-average 115.2 ± 1.6 nm; TEM 94.0 ± 0.5 nm (auto) vs 95.3 ± 2.5 nm (manual); zeta −55.4 ± 2.3 mV; variation <3%.
  - MSN: Z-average 208.6 ± 6 nm; TEM 89.1 ± 3.6 nm; zeta −40.7 ± 3 mV; broader distribution (known for MSN), variation ~5%.
  - ZIF-8: Z-average 648.1 ± 19.7 nm; SEM 351.1 ± 14.7 nm; XRD confirmed sodalite phase (COD 4118891), peaks at 2θ = 7.3°, 10.38°, 12.74°, 14.88°, 16.65°, 18.2°.
  - CuO: dn 54.2 ± 3.6 nm; intensity-based values diverged due to clustering (TEM dn ~48.5 ± 6.6 nm).
  - Core–shell: Au@SiO₂ 101.7 ± 8.7 nm; CuO@SiO₂ 91.9 ± 15.6 nm.
- **Robot-arm-centric (not flow-based):** A 6-DOF xArm6 arm (700 mm reach, ±0.1 mm repeatability, 5 kg payload, open Python API) moves vessels between stationary stations — closer to traditional bench work, easing adaptation of literature batch protocols and rescaling, avoiding the upscaling difficulty of microfluidic SDLs.
- **MINERVA-OS software:** High-level chemist-friendly commands (add, heat, sonicate, centrifuge) sit atop abstract-base-class hardware drivers. A producer-consumer **task scheduler** on a priority queue parallelizes multithreaded tasks, prevents race conditions/deadlocks, and locks/unlocks hardware while keeping same-reaction steps sequential. The backend auto-looks up densities/molar masses from Wikidata/PubChem, converts units, applies heuristics for unspecified params, and logs everything to an OpenBIS ELN-LIMS.
- **Characterization-hardware workarounds:** Where no API existed, the team automated DLS/Zeta (Zetasizer Ultra) via emulated keyboard/mouse input + pixel-reading sanity checks, and reverse-engineered the plate-reader's proprietary protocol-file format to generate acquisition parameters in Python — both enabling closed-loop use.
- **AI-assisted analysis:** A CNN segmentation model measured >1000 particles in minutes (1–2 orders of magnitude faster than manual), with auto and manual means agreeing closely — removing a characterization bottleneck.
- **Batch mixing:** High homogeneity let them pool multiple AuNP/CuO batches as cores for core–shell synthesis, sidestepping scale-up.

## Methods (brief)
Custom multi-vendor hardware (xArm6 arm, OT-2 pipettor, syringe pumps + selector valves, IKA hot plates, automatable centrifuge, probe/bath sonicators) plus 3D-printed Arduino-controlled custom parts (capper, clamps, valve actuators). Characterization by DLS/ELS, UV-Vis absorbance, TEM, SEM/tSEM, and XRD. Three parallel batches per material assessed for size-distribution reproducibility.

## Limitations
Demonstrates **reproducibility, not yet closed-loop ML optimization** (flagged as future work alongside a GUI and solid dosing). Current scope is ambient-atmosphere/pressure liquid handling only — inert-atmosphere, high-pressure/solvothermal, and rigorous O₂/H₂O exclusion would require a glovebox. The emulated-input DLS automation is brittle to popups and proprietary file-format changes. n = 3 batches per material.

## Citations of interest
- Abolhasani & Kumacheva, *Nat. Synth.* 2023 — review framing the rise of self-driving labs.
- Burger et al., *Nature* 2020 — mobile robotic chemist (the elaborate end of the SDL spectrum).
- Steiner et al., *Science* 2019 (Cronin) — modular robotic system / chemical programming language; basis for the custom valve actuators.
- Dembski et al., *Sci. Rep.* 2023 — robot platform for automated silica nanoparticle production (closest prior batch-NP SDL).
- Rühle et al., *Sci. Rep.* 2021 — CNN-based EM particle segmentation workflow reused here for sizing.
- Barillari et al. / Bauch et al. — openBIS ELN-LIMS, used for experiment/metadata logging.
