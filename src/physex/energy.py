"""Энергия, работа и мощность."""

from __future__ import annotations

__all__ = [
    "kinetic_energy",
    "potential_energy",
    "elastic_potential_energy",
    "work",
    "power",
    "gravitational_potential_energy",
]


def kinetic_energy(mass: float, velocity: float) -> float:
    """Кинетическая энергия: E_k = ½·m·v²."""
    return 0.5 * mass * velocity * velocity


def potential_energy(mass: float, height: float, g: float = 9.80665) -> float:
    """Потенциальная энергия в поле тяжести: E_p = m·g·h."""
    return mass * g * height


def elastic_potential_energy(stiffness: float, displacement: float) -> float:
    """Потенциальная энергия упругой деформации: E = ½·k·x².

    Args:
        stiffness: жёсткость пружины k, Н/м.
        displacement: деформация x, м.
    """
    return 0.5 * stiffness * displacement * displacement


def work(force_mag: float, displacement_mag: float, angle_deg: float = 0.0) -> float:
    """Механическая работа: A = F·s·cos(θ), угол в градусах."""
    import math

    return force_mag * displacement_mag * math.cos(math.radians(angle_deg))


def power(work_value: float, time: float) -> float:
    """Мощность: P = A/t."""
    if time == 0:
        raise ZeroDivisionError("Время не может быть нулевым")
    return work_value / time


# Алиас для наглядности в физике.
gravitational_potential_energy = potential_energy
