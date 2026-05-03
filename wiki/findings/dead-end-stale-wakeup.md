---
type: finding
author: hybrid
drafted: 2026-05-02
question_origin: cross-problem
status: answered
related_concepts: []
related_techniques: []
related_findings: [cross-pollination-not-compute.md]
related_personas: []
cites:
  - ../../.claude/rules/cycle-discipline.md
---

# Dead end: stale ScheduleWakeup callbacks (and how to prevent them)

## TL;DR

When the agent schedules a `ScheduleWakeup` callback to handle long-running background work and then completes that work *earlier than expected*, the wakeup still fires at the originally-scheduled time, **with a prompt that re-asks the agent to do the work that's already been done**. The user reads a "this is already complete" reply on a wasted turn. The fix: **always cancel scheduled wakeups when the work that prompted them finishes before the deadline.** Don't just let them fire and discover the work is done.

## What we observed

In this session (2026-05-02), I scheduled two `ScheduleWakeup` callbacks for long-running background commands:

1. **wakeup #1** — waiting for `tools/wiki_graph.py` v3 gap-detector run (~3 min for ~80 qmd queries). Scheduled 200s ahead. The bg task actually finished closer to 150s, and the next user prompt arrived mid-run; I checked the file, computed the diff, and surfaced to the user. The wakeup fired ~30s after the user's reply, asking me to do work I had already done.

2. **wakeup #2** — same pattern with v4 gap-detector. Scheduled 258s ahead; work completed; wakeup still fired with stale instructions.

Both times I responded with "this is already complete," consuming a user turn for no value.

## Why it failed (the obstruction)

ScheduleWakeup is fire-and-forget from the agent's perspective: there's no built-in "cancel if done early" hook. The agent must explicitly decide *not* to use it (or to cancel it) when the work-that-prompted-it finishes early.

In practice, I did the natural thing: schedule a callback as a defensive measure for "in case the bg run takes the full 3 min and the user doesn't ping me," then continue the conversation organically. When the user *did* ping me before the deadline, I forgot the wakeup was still scheduled.

The structural pattern: **ScheduleWakeup is a deadline-style construct, not a polling-style one.** It's correct for "I genuinely have nothing to do until time T" but wrong for "I'm waiting on a task that *might* be ready before T."

## What this rules out

- Treating `ScheduleWakeup` as a free safety net "just in case." It's not free; it costs a turn at the user's end if the work completes early.
- Scheduling a wakeup *and* responding to the user in the same turn — the response itself signals the user is engaged, so the wakeup will fire on stale state.

## What works instead

Three correct patterns:

1. **No wakeup, lean on the user**. If the bg task takes 2-5 min and there's a reasonable chance the user will ping me before then, just say "background running, will respond when it's done or when you ping" and don't schedule. The user's natural cadence handles the case.

2. **Inline polling loop with bounded wait**. For sub-5-min bg tasks, a `for i in 1..N: sleep 30; check` loop in the same turn is cheaper than a wakeup-and-resume. Burns my own context, not the user's.

3. **Wakeup ONLY if the agent has nothing to do for the duration**. If the bg task is 30+ min and I genuinely cannot proceed without it, schedule the wakeup. If I can do *anything* in the interim (write a finding, prep next branch), prefer to use the time and skip the wakeup.

## The cancellation that's missing

Ideally `ScheduleWakeup` would have a `Cancel` companion. Without it, the agent's mental model needs to be: **schedule a wakeup only when no other path exists**. The default should be "don't schedule" — the same way the default for cite hygiene is "don't cite if you can't verify."

This connects to the broader cycle-discipline pattern (`.claude/rules/cycle-discipline.md`): every commitment the agent makes (a wakeup, a cite, a submission, a file modification) creates state that may need to be cleaned up. Default to *not making the commitment* unless it's load-bearing.

## How to apply

When tempted to use `ScheduleWakeup`:

1. Ask: *can the user reasonably ping me before this fires?* If yes → don't schedule.
2. Ask: *can I do anything else useful in the interim?* If yes → don't schedule; do the other thing.
3. Ask: *is the wait genuinely longer than 5 min AND I have no other moves?* Only here is `ScheduleWakeup` correct.
4. If you do schedule and the work completes early, document in your reply that the wakeup is now pending-but-stale, so the user doesn't read the future fire as a fresh request.

## Triggering moment

User noticed the pattern (2026-05-02): two of my scheduled wakeups in one session both fired on already-completed work. The user observed it and asked whether to file it as a wiki finding to encode the lesson. Author: hybrid (user pattern recognition + agent codification).

## See also

- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — same family of meta-discipline findings about *how the agent should work*, not what it should think
- [`.claude/rules/cycle-discipline.md`](../../.claude/rules/cycle-discipline.md) — broader workflow discipline this connects to

*Last updated: 2026-05-02*
