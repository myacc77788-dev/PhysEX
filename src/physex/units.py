"""Простые операции с размерными величинами в единицах СИ.

Класс :class:`Quantity` хранит численное значение и название единицы,
позволяя выполнять арифметику и контролировать размерность ключевых операций.
"""

from __future__ import annotations

from typing import Union

__all__ = ["Quantity", "dimension"]


Number = Union[int, float]


class Quantity:
    """Размерная величина: численное значение + единица измерения."""

    __slots__ = ("value", "unit")

    def __init__(self, value: Number, unit: str = ""):
        if isinstance(value, Quantity):
            raise TypeError("Нельзя обернуть Quantity в Quantity: используйте value.value")
        self.value = float(value)
        self.unit = unit or ""

    # --- отображение -----------------------------------------------------------
    def __repr__(self) -> str:  # pragma: no cover
        return f"Quantity({self.value:g}, {self.unit!r})"

    def __str__(self) -> str:
        return f"{self.value:g} {self.unit}".strip()

    # --- арифметика ------------------------------------------------------------
    def __add__(self, other: "Quantity") -> "Quantity":
        other = self._coerce(other)
        if other.unit != self.unit:
            raise ValueError(f"Несовместимые единицы: {self.unit!r} и {other.unit!r}")
        return Quantity(self.value + other.value, self.unit)

    def __sub__(self, other: "Quantity") -> "Quantity":
        other = self._coerce(other)
        if other.unit != self.unit:
            raise ValueError(f"Несовместимые единицы: {self.unit!r} и {other.unit!r}")
        return Quantity(self.value - other.value, self.unit)

    def __mul__(self, other: "Quantity") -> "Quantity":
        if isinstance(other, Quantity):
            return Quantity(self.value * other.value, _join_units(self.unit, other.unit, "*"))
        if isinstance(other, (int, float)):
            return Quantity(self.value * other, self.unit)
        return NotImplemented

    def __rmul__(self, other: Number) -> "Quantity":
        if isinstance(other, (int, float)):
            return Quantity(self.value * other, self.unit)
        return NotImplemented

    def __truediv__(self, other: "Quantity") -> "Quantity":
        if isinstance(other, Quantity):
            return Quantity(self.value / other.value, _join_units(self.unit, other.unit, "/"))
        if isinstance(other, (int, float)):
            return Quantity(self.value / other, self.unit)
        return NotImplemented

    def __pow__(self, power: int) -> "Quantity":
        if not isinstance(power, (int, float)):
            return NotImplemented
        return Quantity(self.value ** power, f"({self.unit})^{power}" if self.unit else "")

    def __eq__(self, other: object) -> bool:
        try:
            other = self._coerce(other)  # type: ignore[assignment]
        except (TypeError, ValueError):
            return False
        return self.unit == other.unit and abs(self.value - other.value) < 1e-12

    # --- вспомогательное --------------------------------------------------------
    @staticmethod
    def _coerce(other: object) -> "Quantity":
        if isinstance(other, Quantity):
            return other
        if isinstance(other, (int, float)):
            return Quantity(other)
        raise TypeError(f"Нельзя смешивать Quantity с {type(other).__name__}")

    def to_base(self, factor: float) -> "Quantity":
        """Перевести в базовые единицы: умножить значение на factor."""
        return Quantity(self.value * factor, self.unit)


def _join_units(a: str, b: str, op: str) -> str:
    """Объединить строки единиц для операций умножения/деления."""
    if not a:
        return b
    if not b:
        return a
    if op == "*":
        return f"{a}·{b}"
    return f"{a}/{b}"


def dimension(q: Quantity) -> str:
    """Вернуть размерность величины в виде строки (заглушка для отладки)."""
    return q.unit if q.unit else "безразмерная"
