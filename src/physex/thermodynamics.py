"""Термодинамика: идеальный газ, теплота, теплопередача."""

from __future__ import annotations

from .constants import gas_constant

__all__ = [
    "ideal_gas_pressure",
    "heat_required",
    "heat_capacity_constant_pressure",
    "heat_capacity_constant_volume",
    "boltzmann_energy",
    "efficiency",
    "adiabatic_ratio",
]


def ideal_gas_pressure(moles: float, temperature: float, volume: float,
                       r: float | None = None) -> float:
    """Уравнение Менделеева–Клапейрона: p·V = ν·R·T → p = ν·R·T/V.

    Args:
        moles: количество вещества ν, моль.
        temperature: абсолютная температура T, К.
        volume: объём V, м³.
        r: газовая постоянная (по умолчанию R = 8.314).
    """
    if volume == 0:
        raise ZeroDivisionError("Объём не может быть нулевым")
    if r is None:
        r = gas_constant.value
    return moles * r * temperature / volume


def heat_required(mass: float, specific_heat: float, delta_t: float) -> float:
    """Количество теплоты: Q = c·m·ΔT.

    Args:
        mass: масса, кг.
        specific_heat: удельная теплоёмкость, Дж/(кг·К).
        delta_t: изменение температуры, К.
    """
    return specific_heat * mass * delta_t


def heat_capacity_constant_pressure(moles: float, cv: float) -> float:
    """Теплоёмкость при постоянном давлении для идеального газа:
    C_p = C_v + ν·R. Принимает молярную теплоёмкость C_v на моль.
    """
    return (cv + gas_constant.value) * moles


def heat_capacity_constant_volume(moles: float, cv: float) -> float:
    """Теплоёмкость при постоянном объёме: C_v = cv·ν."""
    return cv * moles


def boltzmann_energy(temperature: float, k_b: float | None = None) -> float:
    """Характерная энергия теплового движения: E = k_B·T.

    Args:
        temperature: температура, К.
        k_b: постоянная Больцмана (по умолчанию 1.380649e-23 Дж/К).
    """
    if k_b is None:
        from .constants import boltzmann

        k_b = boltzmann.value
    return k_b * temperature


def efficiency(useful_work: float, heat_input: float) -> float:
    """Термический КПД тепловой машины: η = A_полезн/Q_подвед."""
    if heat_input == 0:
        raise ZeroDivisionError("Подведённая теплота не может быть нулевой")
    return useful_work / heat_input


def adiabatic_ratio(cp: float, cv: float) -> float:
    """Показатель адиабаты: γ = C_p/C_v."""
    if cv == 0:
        raise ZeroDivisionError("C_v не может быть нулевой")
    return cp / cv
