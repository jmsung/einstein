"""Projected-Hessian floor certificate (Phase-8 promotion of the P10 finding)."""

import json
from pathlib import Path

import numpy as np

from einstein.thomson.hessian_certificate import certify_local_min

SEED = Path("scripts/thomson/seeds/best.json")


def test_wales_seed_certifies_strict_local_min():
    pts = np.asarray(json.load(open(SEED))["vectors"], dtype=np.float64)
    cert = certify_local_min(pts)
    assert cert.is_strict_local_min
    assert cert.n_negative_modes == 0
    assert cert.n_zero_modes == 3  # SO(3) rotational gauge
    assert cert.lambda_min_nonzero > 1.0  # large spectral gap (≈3.41)
    assert cert.max_tangential_gradient < 1e-5  # a critical point


def test_perturbed_config_is_not_certified():
    """A random perturbation off the minimum must not certify (negative modes
    or a positive tangential gradient)."""
    rng = np.random.default_rng(0)
    pts = json.load(open(SEED))["vectors"]
    pts = np.asarray(pts, dtype=np.float64)
    pts = pts + 0.05 * rng.standard_normal(pts.shape)  # kick off the basin floor
    cert = certify_local_min(pts)
    assert not cert.is_strict_local_min
