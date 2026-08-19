"""Фундаментальные физические константы в единицах СИ.

Значения взяты из CODATA 2018 (согласованные значения).
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "Constant",
    "speed_of_light",
    "planck",
    "reduced_planck",
    "boltzmann",
    "avogadro",
    "gas_constant",
    "elementary_charge",
    "electron_mass",
    "proton_mass",
    "neutron_mass",
    "atomic_mass_unit",
    "gravitational_constant",
    "standard_gravity",
    "vacuum_permittivity",
    "vacuum_permeability",
    "fine_structure_constant",
    "stefan_boltzmann",
]


@dataclass(frozen=True)
class Constant:
    """Физическая константа с именем, значением и размерностью."""

    name: str
    symbol: str
    value: float
    unit: str

    def __repr__(self) -> str:  # pragma: no cover - отладочный вывод
        return f"{self.symbol} = {self.value:g} {self.unit}"


# --- Фундаментальные константы -------------------------------------------------
speed_of_light = Constant("скорость света в вакууме", "c", 2.99792458e8, "м/с")
planck = Constant("постоянная Планка", "h", 6.62607015e-34, "Дж·с")
reduced_planck = Constant("постоянная Планка (h-bar)", "ħ", planck.value / (2.0 * 3.141592653589793), "Дж·с")
boltzmann = Constant("постоянная Больцмана", "k_B", 1.380649e-23, "Дж/К")
avogadro = Constant("число Авогадро", "N_A", 6.02214076e23, "моль⁻¹")
gas_constant = Constant("универсальная газовая постоянная", "R", 8.31446261815324, "Дж/(моль·К)")

# --- Электричество и атомная физика -------------------------------------------
elementary_charge = Constant("элементарный заряд", "e", 1.602176634e-19, "Кл")
electron_mass = Constant("масса электрона", "m_e", 9.1093837015e-31, "кг")
proton_mass = Constant("масса протона", "m_p", 1.67262192369e-27, "кг")
neutron_mass = Constant("масса нейтрона", "m_n", 1.67492749804e-27, "кг")
atomic_mass_unit = Constant("атомная единица массы", "u", 1.66053906660e-27, "кг")
fine_structure_constant = Constant(
    "постоянная тонкой структуры", "α", 7.2973525693e-3, "безразмерная"
)

# --- Механика и гравитация -----------------------------------------------------
gravitational_constant = Constant("гравитационная постоянная", "G", 6.67430e-11, "м³/(кг·с²)")
standard_gravity = Constant("стандартное ускорение свободного падения", "g", 9.80665, "м/с²")

# --- Электродинамика ------------------------------------------------------------
vacuum_permittivity = Constant(
    "электрическая постоянная", "ε₀", 8.8541878128e-12, "Ф/м"
)
vacuum_permeability = Constant(
    "магнитная постоянная", "μ₀", 1.25663706212e-6, "Н/А²"
)

# --- Тепловое излучение ---------------------------------------------------------
stefan_boltzmann = Constant(
    "постоянная Стефана — Больцмана",
    "σ",
    5.670374419e-8,
    "Вт/(м²·К⁴)",
)


def all_constants() -> list[Constant]:
    """Вернуть список всех констант модуля (порядок не гарантирован)."""
    return [
        obj
        for name, obj in globals().items()
        if isinstance(obj, Constant)
    ]
