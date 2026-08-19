"""Электродинамика: закон Кулона, ток, сопротивление, мощность."""

from __future__ import annotations

from .constants import vacuum_permittivity

__all__ = [
    "coulomb_force",
    "electric_field",
    "electric_potential",
    "current",
    "resistance",
    "electric_power",
    "ohm_law_voltage",
    "capacitance",
    "capacitor_energy",
]


def coulomb_force(q1: float, q2: float, distance: float,
                  k: float | None = None) -> float:
    """Закон Кулона: F = k·|q1·q2|/r² (сила по модулю).

    Args:
        q1, q2: заряды, Кл.
        distance: расстояние, м.
        k: коэффициент (по умолчанию 1/(4πε₀) ≈ 8.9875e9 Н·м²/Кл²).
    """
    if distance == 0:
        raise ZeroDivisionError("Расстояние не может быть нулевым")
    if k is None:
        k = 1.0 / (4.0 * 3.141592653589793 * vacuum_permittivity.value)
    return k * abs(q1 * q2) / (distance * distance)


def electric_field(charge: float, distance: float,
                   k: float | None = None) -> float:
    """Напряжённость поля точечного заряда: E = k·|q|/r²."""
    if distance == 0:
        raise ZeroDivisionError("Расстояние не может быть нулевым")
    if k is None:
        k = 1.0 / (4.0 * 3.141592653589793 * vacuum_permittivity.value)
    return k * abs(charge) / (distance * distance)


def electric_potential(charge: float, distance: float,
                       k: float | None = None) -> float:
    """Потенциал поля точечного заряда: φ = k·q/r."""
    if distance == 0:
        raise ZeroDivisionError("Расстояние не может быть нулевым")
    if k is None:
        k = 1.0 / (4.0 * 3.141592653589793 * vacuum_permittivity.value)
    return k * charge / distance


def current(charge: float, time: float) -> float:
    """Сила тока: I = q/t."""
    if time == 0:
        raise ZeroDivisionError("Время не может быть нулевым")
    return charge / time


def resistance(voltage: float, current_value: float) -> float:
    """Сопротивление по закону Ома: R = U/I."""
    if current_value == 0:
        raise ZeroDivisionError("Ток не может быть нулевым")
    return voltage / current_value


def ohm_law_voltage(current_value: float, resistance_value: float) -> float:
    """Напряжение по закону Ома: U = I·R."""
    return current_value * resistance_value


def electric_power(voltage: float, current_value: float) -> float:
    """Электрическая мощность: P = U·I."""
    return voltage * current_value


def capacitance(charge: float, voltage: float) -> float:
    """Ёмкость конденсатора: C = q/U."""
    if voltage == 0:
        raise ZeroDivisionError("Напряжение не может быть нулевым")
    return charge / voltage


def capacitor_energy(capacitance_value: float, voltage: float) -> float:
    """Энергия заряженного конденсатора: W = ½·C·U²."""
    return 0.5 * capacitance_value * voltage * voltage
