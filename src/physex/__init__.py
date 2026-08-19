"""PhysEX — библиотека для физических расчётов.

Модули:
    constants       — фундаментальные физические константы
    units           — работа с размерными величинами
    kinematics      — кинематика прямолинейного движения
    dynamics        — динамика, сила и импульс
    energy          — энергия, работа, мощность
    thermodynamics  — термодинамика идеального газа
    electrodynamics — электростатика и электрические цепи
"""

from . import constants, dynamics, electrodynamics, energy, kinematics, thermodynamics, units
from .constants import (
    avogadro,
    boltzmann,
    elementary_charge,
    gas_constant,
    gravitational_constant,
    planck,
    speed_of_light,
    standard_gravity,
)

__version__ = "0.1.0"

__all__ = [
    "constants",
    "units",
    "kinematics",
    "dynamics",
    "energy",
    "thermodynamics",
    "electrodynamics",
    "avogadro",
    "boltzmann",
    "elementary_charge",
    "gas_constant",
    "gravitational_constant",
    "planck",
    "speed_of_light",
    "standard_gravity",
    "__version__",
]
