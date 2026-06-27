"""Source-grounded resonance primitives.

These functions are intentionally general physics primitives. They do not model
transmitter targeting, ionospheric operations, weather control, or weapon effects.
"""

from __future__ import annotations

import math


def lc_resonance_hz(inductance_h: float, capacitance_f: float) -> float:
    """Return ideal LC resonant frequency in hertz."""
    if inductance_h <= 0 or capacitance_f <= 0:
        raise ValueError("inductance_h and capacitance_f must be positive")
    return 1.0 / (2.0 * math.pi * math.sqrt(inductance_h * capacitance_f))


def damped_response_amplitude(
    drive_frequency_hz: float,
    natural_frequency_hz: float,
    damping_ratio: float,
) -> float:
    """Return relative amplitude for a normalized damped driven oscillator."""
    if drive_frequency_hz <= 0 or natural_frequency_hz <= 0:
        raise ValueError("frequencies must be positive")
    if damping_ratio <= 0:
        raise ValueError("damping_ratio must be positive")
    ratio = drive_frequency_hz / natural_frequency_hz
    return 1.0 / math.sqrt((1.0 - ratio * ratio) ** 2 + (2.0 * damping_ratio * ratio) ** 2)


def standing_wave_nodes(length_m: float, wavelength_m: float) -> list[float]:
    """Return node positions for a one-dimensional ideal standing wave cavity."""
    if length_m <= 0 or wavelength_m <= 0:
        raise ValueError("length_m and wavelength_m must be positive")
    spacing = wavelength_m / 2.0
    node_count = int(math.floor(length_m / spacing))
    return [round(index * spacing, 12) for index in range(node_count + 1)]


def plasma_frequency_hz(electron_density_m3: float) -> float:
    """Return electron plasma frequency for transparent validation cases."""
    if electron_density_m3 <= 0:
        raise ValueError("electron_density_m3 must be positive")
    electron_charge_c = 1.602176634e-19
    vacuum_permittivity_f_m = 8.8541878128e-12
    electron_mass_kg = 9.1093837015e-31
    omega = math.sqrt(
        electron_density_m3
        * electron_charge_c
        * electron_charge_c
        / (vacuum_permittivity_f_m * electron_mass_kg)
    )
    return omega / (2.0 * math.pi)

