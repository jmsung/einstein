"""Tests for the prompt_tone factor (prereg §4) — the verbatim preamble registry
and the length-match confound guard (§7)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import prompt_tone as pt  # noqa: E402


def test_neutral_default_preamble_is_empty():
    # NEUTRAL maps to "" so build_prompt(neutral) stays byte-identical to the
    # pre-tone prompt (regression-safe default; the §4 freeze may swap in the
    # length-matched filler).
    assert pt.PREAMBLES[pt.PromptTone.NEUTRAL] == ""


def test_encouraging_preamble_is_the_frozen_human_phrasing():
    s = pt.PREAMBLES[pt.PromptTone.ENCOURAGING]
    assert "Never give up" in s
    assert "rank 1" in s.lower()


def test_every_tone_has_a_registry_entry():
    assert set(pt.PREAMBLES) == set(pt.PromptTone)


def test_length_matched_neutral_is_within_tolerance_of_encouraging():
    # §7 token-count confound guard: the length-matched control must be ~the same
    # character length as the encouraging preamble (else "encouraging" also buys
    # raw tokens).
    pt.assert_length_matched(pt.NEUTRAL_LENGTH_MATCHED, pt.PREAMBLES[pt.PromptTone.ENCOURAGING])


def test_assert_length_matched_rejects_mismatch():
    with pytest.raises(AssertionError):
        pt.assert_length_matched("short", "a" * 500)


def test_length_matched_neutral_carries_no_motivational_content():
    # The control must be content-free: same length, no "never give up" semantics.
    low = pt.NEUTRAL_LENGTH_MATCHED.lower()
    assert "never give up" not in low
    assert "rank 1" not in low
