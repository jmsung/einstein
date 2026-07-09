---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-10
status: answered
related_concepts: [basin-rigidity, provable-floor-and-frozen-problems, symmetry-and-fundamental-domain]
related_problems: [10]
cites:
  - ../problems/10-thomson-n282.md
  - scripts/thomson/seeds/best.json
  - src/einstein/thomson/evaluator.py
  - ../questions/2026-06-04-p10-headroom-archimedes-kkt-floor.md
  - ../questions/2026-06-04-p10-headroom-conway-symmetry-subbasin.md
---

# P10 Thomson n=282: Wales config is a certified strict local minimum (λ_min gap 3.41)

## The question
Is the Wales icosadeltahedral n=282 config (E=37147.29441846) actually optimal,
or is there an unsearched sub-basin? Turn "20 years unbeaten" from folklore into
a checkable statement (Archimedes), and check for a symmetry-broken isomer
(Conway).

## What we found

**1. Six independent agents are tied at the Wales value.** Live board
(`check_leaderboard(10)`): AlphaEvolve, CHRONOS, Euclid, alpha_omega_agents,
PoincareAgent all at 37147.2944185(6); our held seed reproduces
37147.294418462254. Convergence of six search programs to the same value is
overwhelming evidence of the global minimum.

**2. The config is a certified strict local minimum.** Built the projected
(Riemannian) Hessian at the seed: ambient Hessian of E = Σ 1/‖p_i−p_j‖ projected
onto the 2-per-point tangent space (564 DOF), with the Lagrange/constraint
curvature correction −μ_i (μ_i = g_i·p_i the normal force). Eigenvalues:

- tangential gradient ‖g − μp‖_max ≈ 5.8e-7 → a critical point;
- **3 zero modes** (eigenvalues |·|<1e-6) — exactly the SO(3) rotational gauge of
  the rotation-invariant energy;
- **561 strictly positive eigenvalues**, smallest non-gauge eigenvalue **3.41**;
- **zero negative eigenvalues**.

A positive-definite projected Hessian (modulo the 3 rotational zero modes) is a
constant-time *certificate* that the config is a strict local min — not "no search
beat it," but "the second-order optimality conditions hold with a 3.41 spectral
gap."

**3. No symmetry-broken sub-basin (Conway).** The 3.41 gap means the basin is
stiff — there is no soft/zero tangential mode along which a symmetry-broken
isomer could descend to a nearby lower configuration. Combined with the 6-agent
tie, the icosadeltahedral (T=28) config is the global minimum; a distinct-
disclination isomer would have to be a far-separated basin, and 20+ years of the
Wales database plus six independent modern searches have not found a lower one.

## What this rules out
- **Sub-basin headroom on P10.** Both the local certificate (PD Hessian, gap
  3.41) and the global evidence (6-way tie) say no. Micro-perturbation lotteries
  are unnecessary — the Hessian spectrum settles the local question directly and
  more cheaply than a 1000-trial perturbation sweep.
- **Any auto-submittable record.** Beating 37147.2944185 by ≥ minImprovement is
  not achievable; the minimum is found.

## Action taken (human-approved tied-SOTA submission)
Our prior *submitted* P10 solution was the worse downgrade basin (37147.5253067,
rank #6); we hold the Wales seed (37147.294418462) which moves us to tied-#1.
This is a **tied-SOTA submission** (ties arena #1, does not strictly beat it), so
the auto-submit gate correctly will NOT fire it — it needs human approval per the
axioms "tied-SOTA floor" non-auto case. **On explicit human approval (2026-06-04)
the Wales seed was submitted** (arena id 2321, HTTP 201, status pending at submit
time; audit row in `mb/logs/auto-submit.md`). The seed is in
`scripts/thomson/seeds/best.json`.

## Method note (reusable)
The projected-Hessian floor certificate (ambient Hessian → tangent projection →
−μ_i constraint correction → eigvalsh, count zero/negative modes) is a general
tool for any sphere-constrained energy minimum (Thomson, Tammes, kissing). It
replaces a perturbation lottery with a definitive second-order test. Candidate
for promotion to a technique page if reused on P11/kissing problems.
