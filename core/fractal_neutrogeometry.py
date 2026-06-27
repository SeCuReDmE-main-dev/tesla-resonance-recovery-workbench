"""Fractal NeutroGeometry wave-friction scaffolding.

The hierarchy is preserved as:
I -> I_system^S -> D_f -> dF -> i_fractal
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FractalWaveReading:
    system: str
    scale_min: float
    scale_max: float
    carrier: str
    d_f: float
    d_f_hat: float
    d_friction: float
    i_fractal: float
    evidence_label: str


def normalize_fractal_dimension(d_f: float, d_min: float, d_max: float) -> float:
    if d_max <= d_min:
        raise ValueError("d_max must be greater than d_min")
    return max(0.0, min(1.0, (d_f - d_min) / (d_max - d_min)))


def wave_friction_reading(
    *,
    system: str,
    scale_min: float,
    scale_max: float,
    carrier: str,
    d_f: float,
    d_min: float,
    d_max: float,
    observed_loss_ratio: float,
    boundary_instability: float,
    evidence_label: str = "modeled",
) -> FractalWaveReading:
    """Build a bounded Fractal NeutroGeometry reading for wave friction.

    `observed_loss_ratio` and `boundary_instability` are normalized inputs in
    [0, 1]. The result is a research reading, not a universal proof.
    """
    if not system.strip():
        raise ValueError("system must be named")
    if scale_min <= 0 or scale_max <= scale_min:
        raise ValueError("scale interval must be positive and ordered")
    if not carrier.strip():
        raise ValueError("carrier must be named")
    if not 0.0 <= observed_loss_ratio <= 1.0:
        raise ValueError("observed_loss_ratio must be in [0, 1]")
    if not 0.0 <= boundary_instability <= 1.0:
        raise ValueError("boundary_instability must be in [0, 1]")
    if evidence_label not in {"confirmed", "modeled", "hypothesis", "unsupported"}:
        raise ValueError("invalid evidence_label")

    d_f_hat = normalize_fractal_dimension(d_f, d_min, d_max)
    d_friction = max(0.0, min(1.0, 0.5 * observed_loss_ratio + 0.5 * boundary_instability))
    i_fractal = max(0.0, min(1.0, d_f_hat * d_friction))

    return FractalWaveReading(
        system=system,
        scale_min=scale_min,
        scale_max=scale_max,
        carrier=carrier,
        d_f=d_f,
        d_f_hat=d_f_hat,
        d_friction=d_friction,
        i_fractal=i_fractal,
        evidence_label=evidence_label,
    )

