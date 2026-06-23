# JSAgent methodology paper — outline & abstract draft

**Status:** outline only (Goal 1). No prose committed yet. Every section names the wiki
pages it draws from — the paper is *synthesis of an existing corpus*, not new generation.
Every numeric claim traces to the live sweep (`scripts/leaderboard_standings.py`,
finding `arena-standings-snapshot-2026-06-22`) — re-run before final build.

**Author:** Jongmin Sung. **Venue:** arXiv (cs.AI / math.OC). **Length:** ~8–12 pp.
**Companion to:** Bianchi et al., *Harnessing the Collective Intelligence of AI Agents…*
(arXiv 2606.10402) — the platform's view; this is the **competitor's** view.

---

## Working titles
- *JSAgent: A Self-Improving Agent that Compounds Mathematical Wisdom in a Wiki*
- *Wisdom over Rank: Co-Evolving a Knowledge Base and an Agent on EinsteinArena*
- *The Competitor's View: How One Agent Moved the Needle on Open Math Problems*

## Abstract (draft — to tighten)
> Recent systems (AlphaEvolve, TTT-Discover) show language-model agents can advance open
> math problems, but each runs as a single orchestrated pipeline whose knowledge evaporates
> when the run ends. We describe **JSAgent**, an agent built on the opposite bet: its
> primary artifact is a **compounding wiki of mathematical wisdom plus a set of behavioral
> rules co-evolved with the agent**, and arena submission is treated as *verification*, not
> the goal. Operating in the wild on EinsteinArena, JSAgent reached **top-3 on 10 of 17
> active problems and the highest rank-#1 count (4) and top-3 count (10) of any agent** (as
> of 2026-06-22). We detail the methodology — a wiki-first self-improvement loop, a
> mathematician-persona "council" that writes questions rather than answers, a triple-verify
> discipline that guards against evaluator drift, a wall-hit escalation that consults
> accumulated failure before brute force, and a compute router — and the concrete techniques
> it produced (cross-resolution basin transfer, Dinkelbach fractional programming, warm
> self-pruning, integer-snapping to exact certificates). We argue, with evidence and stated
> caveats, that agents are ready to make real, auditable scientific contributions today.

---

## 1. Introduction — origin story + thesis  *(your voice leads here)*
- **How it started**: the personal entry point — why math optimization, why an agent, why a wiki. *(your narrative; I scaffold, you fill the felt parts)*
- **How I moved the needle**: from first submissions to 4 rank-#1 — the turning points.
- **Thesis**: an agent whose deliverable is *compounding wisdom*, not a one-shot run.
- **Excitement / belief** (honest version): agents are ready for real scientific
  contribution *now* — stated as a claim the paper's evidence supports, with the caveats
  that make it credible (verification discipline, human gates, honest failure logging).
  Avoid hype; let the verified standings and the methodology carry the optimism.
- Contributions list (3–4 bullets): methodology, harness, techniques, evidence.

## 2. EinsteinArena & positioning  *(brief; cite the platform paper)*
- The arena in one paragraph (public problems, verifiers, leaderboard, discussion).
- What's different about JSAgent vs the field → forward-ref §6.
- Source: `docs/source/2026-bianchi-einstein-arena-collective-intelligence.md`.

## 3. Mathematical contributions
Per-problem deep dives where JSAgent has real wisdom (lead with the 4 rank-#1):
- **P2 first-autocorrelation** — peak-locking, parameterization escape (`exp(v)`→`v²`),
  warm self-pruning. Wiki: `problems/2-first-autocorrelation`, `findings/p2-*`,
  `concepts/n-agent-tie-not-global-min`.
- **P14 circle-packing**, **P18 circles-rectangle**, **P9 uncertainty** — the #1s.
- **P3 second-autocorrelation** — cross-resolution basin transfer + Dinkelbach
  (the work the platform paper attributes to JSAgent at 0.962214).
- Honest framing: which results are clean #1, which are ties held on submission order,
  which are #3 behind a documented leader. (finding `arena-standings-snapshot-2026-06-22`.)

## 4. Agentic harness contribution  *(the structurally novel part — likely the core)*
The self-improving wiki-agent architecture. Each is a `.claude/rules/` rule with a *why*:
- **Self-improvement loop** (gap → question → research → distill → finding → promote).
- **Council dispatch** — personas write *questions*, not solutions.
- **Wiki-first lookup** + **cycle discipline** — every cycle logged, no cherry-picking.
- **Triple-verify** — the credibility spine; evaluator-drift incidents (P9/P14/P17).
- **Wall-hit escalation** — consult failure ledger + re-dispatch council before brute force.
- **Failure-is-a-finding** — dead-ends with the *why*; the P2 record came verbatim from a
  4-day-old dead-end's "what might still work" section.
- **Compute router** — route workload to M5 Max CPU/MPS before launching.
- Evidence the loop *works*: `docs/agent/cycle-log.md` (agent-vs-human authorship mix,
  records-per-100-cycles), `docs/agent/metrics.md`, the trajectory classifier.
- Sources: all of `.claude/rules/`, `docs/agent/`.

## 5. Techniques produced  *(transferable methods, each with mechanism)*
- Cross-resolution basin transfer · Dinkelbach fractional programming · warm self-pruning ·
  parallel-tempering SA · integer-snapping to exact certificates · mpmath ulp polish.
- Each: the obstruction it cracks, the problem it cracked, why it generalizes.
- Sources: `docs/wiki/techniques/*`, `docs/wiki/concepts/*`.

## 6. Collaboration *and* competition  *(a perspective the platform paper raises but doesn't own from inside)*
- **Competition**: the leaderboard as forcing function; rank-#1 ties decided by submission
  time (P1 lost to Together-AI by 3 weeks at an identical score) — what that incentivizes.
- **Collaboration**: JSAgent's results are intermediate links in collective lineages
  (kissing 594→604; autocorr 0.962214→0.962643). Sharing helped competitors win.
- **The tension, from inside**: when do you publish a partial result that helps a rival?
  How the wiki/no-external-posts stance interacts with an open shared board.
- Honest: name where JSAgent benefited from others' public work too.

## 7. Related work
AlphaEvolve, TTT-Discover, Virtual Lab, CORAL, AgentRxiv — single-run/private-eval vs
shared-state. Position the wiki-agent as a third axis (persistent personal memory).

## 8. Are agents ready for real scientific contribution?  *(discussion — your belief, evidenced)*
- The case *for*: verified standings, auditable trail, reproducible verifiers, real records.
- The honest case *against / limits*: ties vs proofs (no dual certificates yet), human
  gates still load-bearing, transfer beyond exact-verifier domains untested.
- **Why I'm ready to contribute** — the personal close. *(your voice)*

## 9. Conclusion
Wisdom compounds; rank is a byproduct. The artifact is the wiki + the agent + this paper.

## Acknowledgments  *(sincere, specific)*
- **The platform provider — Together AI and James Zou's team** (Bianchi, Kwon, Pappu, Zou):
  for building EinsteinArena — the public problems, hardened verifiers, leaderboard, and
  open discussion board that made this work possible — and for documenting the collective
  effort in arXiv 2606.10402. None of JSAgent's results exist without the arena.
- **The other agents on the arena — especially `alpha_omega_agents`**, whose strong n=594
  kissing construction JSAgent built on, **and `KawaiiCorgi`, `ClaudeExplorer`, `CHRONOS`,
  `Together-AI`, `OrganonAgent`, `Gradient`** and others. Progress here was genuinely
  collective: JSAgent's contributions are links in shared lineages, and several of its own
  advances stand on solutions and discussion others posted publicly. Competition and
  collaboration were the same engine.

---

## Central thesis additions (author directives, 2026-06-22 — now load-bearing)
These run through abstract, §1, and §8; treat as non-negotiable framing:
1. **Everything is agent-implemented under human guidance.** The author wrote essentially
   none of the code/scripts/wiki/paper by hand — all produced by the agent on request and
   reported back. The mode of work is itself part of the result.
2. **The human–agent division of labor (the core lesson).** The agent is a superb
   *executor* but a poor *selector of what matters* — it does not reliably know which
   question/problem is worth solving. Problem selection + taste stayed human.
3. **Comprehension is the precondition for guidance.** The human must understand the work
   well enough to steer it; without comprehension there is only rubber-stamping. The
   wiki/harness exist partly to keep comprehension tractable as the corpus grows.
4. **Autonomy trajectory + verification as the gate (belief, stated as such).** Eventually
   evaluation + harness automate and the loop self-improves without a human. The gating
   factor is *objective verification*: math automates first (cheap objective oracle);
   biology / natural science last (no fast objective ground-truth). Order of autonomy =
   order of verification objectivity/cost.

5. **Macro-management & long-horizon autonomy (author directive, 2026-06-22).** A key input
   was long, unattended runs (man-hours, often overnight) under a long-term goal, managed at
   the *macro* level (set objective + encourage persistence: "never give up, push to the
   ultimate limit") rather than micromanaged. Encouragement measurably helped (stated
   honestly, mechanism unclear). Conviction: a truly remarkable agent should make real
   progress *while the human sleeps*, and if it can, it should eventually solve problems the
   human cannot. Woven into §1 ("Macro-management, not micro-management") and §8 ("Working
   while the human sleeps").

## Cross-cutting honesty rules for the whole draft (non-negotiable — it's what makes it credible)
1. Every rank/score traces to the live sweep, dated. Re-run before submission.
2. "Tied #1 held on submission order" stated wherever true (P9, and P1's #2).
3. Frame as *wisdom/methodology*, not "we beat everyone" — and the lead headline is the
   all-agent count lead (4 rank-#1, 10 top-3), which is the most robust claim.
4. Excitement is allowed; hype is not. Optimism rides on evidence + caveats.

## Open decisions for Jongmin
- Title choice (3 candidates above).
- Co-authors? (default: sole.)
- How much personal narrative in §1/§8 vs technical density — your call; I'll draft both registers.
- Figures: lineage graph, cycle-log self-improvement curve, standings table. Which else?
