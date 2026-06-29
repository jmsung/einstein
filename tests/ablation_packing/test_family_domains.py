"""Tests for the non-geometric ablation families (Tammes sphere, autocorrelation 1D).

Validates the generalized Family adapter contract: each family self-registers, its
cold_init produces a config its own parser accepts, its score is finite on that config,
and its triple_verify agrees three ways on a valid config and rejects a degenerate one.
"""

import numpy as np
import pytest

from einstein.ablation_packing import families as fam
from einstein.ablation_packing import family_domains as fd


@pytest.mark.parametrize("name", ["tammes_sphere", "autocorrelation_seq"])
def test_family_registered_and_resolvable(name):
    f = fam.get_family(name)
    assert f.name == name
    assert callable(f.score) and callable(f.triple_verify) and callable(f.cold_init)
    assert f.answer_key in {"vectors", "values"}


@pytest.mark.parametrize(
    "name,n",
    [("tammes_sphere", 50), ("autocorrelation_seq", 32)],
)
def test_cold_init_roundtrips_through_parse_and_scores(name, n):
    f = fam.get_family(name)
    init = f.cold_init(n, seed=1)
    # cold_init is deterministic given the seed
    assert np.allclose(init, f.cold_init(n, seed=1))
    # the family's own parser accepts its own prompt-formatted start config
    parsed = f.parse(f.format_init(init), n)
    assert parsed is not None and parsed.shape == init.shape
    # score is finite on a valid config
    assert np.isfinite(f.score(init))
    # config_space description mentions the size
    assert str(n) in f.config_space(n)


@pytest.mark.parametrize("name,n", [("tammes_sphere", 12), ("autocorrelation_seq", 16)])
def test_triple_verify_agrees_three_ways(name, n):
    f = fam.get_family(name)
    init = f.cold_init(n, seed=3)
    tv = f.triple_verify(init)
    assert tv.feasible and tv.passed and tv.reason == "ok"
    assert tv.fast == pytest.approx(tv.exact, abs=1e-9)
    assert tv.fast == pytest.approx(tv.cross, abs=1e-9)
    # the triple-verify fast value matches the family's score on a feasible config
    assert tv.fast == pytest.approx(f.score(init), abs=1e-9)


def test_tammes_rejects_degenerate():
    tv = fd.tammes_triple_verify(np.zeros((5, 3)))
    assert tv.feasible is False and tv.passed is False
    assert fd.tammes_score(np.zeros((1, 3))) == float("-inf")


def test_autocorr_rejects_negative_sequence():
    tv = fd.autocorr_triple_verify(np.array([1.0, -0.5, 0.3]))
    assert tv.feasible is False and tv.passed is False
    assert fd.autocorr_score(np.array([-1.0, 2.0])) == float("-inf")


def test_parse_rejects_wrong_shape():
    tam = fam.get_family("tammes_sphere")
    assert tam.parse([[0.0, 1.0]] * 5, 5) is None  # 2D not 3D
    assert tam.parse("nope", 5) is None
    seq = fam.get_family("autocorrelation_seq")
    assert seq.parse([[1.0, 2.0]], 1) is None  # nested, not flat
    assert seq.parse([1.0, 2.0, 3.0], 5) is None  # wrong length
