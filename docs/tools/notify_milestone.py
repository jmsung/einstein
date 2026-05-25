#!/usr/bin/env python3
"""notify_milestone.py — macOS native notification on autonomous-loop milestones.

Goal 7.8c. When `auto_submit` accepts a new arena record (`submitted=True`),
the orchestrator fires a desktop notification so the human knows to check
the leaderboard. Zero-dep — calls `osascript display notification` and that's
it. No Slack, no external posts (axiom A2). No Linux fallback for now;
non-macOS becomes a silent no-op.

Test seam: pass `runner=...` to `notify(...)` to mock the subprocess.
"""

from __future__ import annotations

import logging
import platform
import shlex
import subprocess
from typing import Callable

log = logging.getLogger("notify_milestone")


DEFAULT_TIMEOUT_S = 5


def _escape_for_applescript(text: str) -> str:
    """Escape backslashes + double quotes so the value can sit inside the
    AppleScript string literal `"<text>"`. Newlines become spaces because
    AppleScript notifications collapse them anyway.
    """
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").replace("\r", " ")


def build_osascript_cmd(*, title: str, message: str, subtitle: str | None = None) -> list[str]:
    """Compose the `osascript -e 'display notification …'` argv.

    Exposed for tests + manual dogfooding. The returned list can be passed
    straight to `subprocess.run`.
    """
    body = f'display notification "{_escape_for_applescript(message)}"'
    body += f' with title "{_escape_for_applescript(title)}"'
    if subtitle:
        body += f' subtitle "{_escape_for_applescript(subtitle)}"'
    return ["osascript", "-e", body]


def is_supported() -> bool:
    """True on macOS where `osascript` exists. Other platforms get a no-op."""
    return platform.system() == "Darwin"


def notify(
    *,
    title: str,
    message: str,
    subtitle: str | None = None,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    runner: Callable[..., object] | None = None,
) -> bool:
    """Fire a macOS notification. Returns True iff osascript exited 0.

    Best-effort — never raises. On any failure (non-macOS, osascript missing,
    timeout, non-zero exit), logs at WARNING and returns False.

    The autonomous loop should not branch on the return; the notification is
    a UX nicety, not a load-bearing signal.
    """
    if not is_supported() and runner is None:
        log.debug("notify skipped — non-macOS (system=%s)", platform.system())
        return False

    cmd = build_osascript_cmd(title=title, message=message, subtitle=subtitle)
    log.debug("notify: %s", shlex.join(cmd))

    real_runner = runner or subprocess.run
    try:
        proc = real_runner(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        log.warning("notify failed: %s", e)
        return False
    except Exception as e:
        log.warning("notify failed unexpectedly: %s", e)
        return False

    rc = getattr(proc, "returncode", 1)
    if rc != 0:
        log.warning("osascript exit %d (%s)", rc, (getattr(proc, "stderr", "") or "").strip())
        return False
    return True


def notify_arena_record(
    *, problem_id: int, score: float, runner: Callable[..., object] | None = None
) -> bool:
    """Convenience wrapper — the milestone the autonomous loop cares about
    today is `auto_submit` accepting a new arena record. One-liner so the
    orchestrator call site stays clean.
    """
    return notify(
        title=f"Einstein Arena — P{problem_id} submission accepted",
        message=f"New record: {score:.10g}",
        subtitle="autonomous loop",
        runner=runner,
    )
