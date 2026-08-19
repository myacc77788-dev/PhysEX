"""Кинематика: прямолинейное движение с постоянным ускорением.

Все функции работают с числами в единицах СИ
(метры, секунды, метры в секунду, м/с²).
"""

from __future__ import annotations

__all__ = [
    "final_velocity",
    "displacement",
    "acceleration_needed",
    "velocity_after_displacement",
    "average_velocity",
    "free_fall_time",
]


def final_velocity(v0: float, a: float, t: float) -> float:
    """Скорость через время t: v = v0 + a·t.

    Args:
        v0: начальная скорость, м/с.
        a: ускорение, м/с².
        t: время, с.

    Returns:
        Скорость, м/с.
    """
    return v0 + a * t


def displacement(v0: float, t: float, a: float = 0.0) -> float:
    """Перемещение: s = v0·t + ½·a·t².

    Args:
        v0: начальная скорость, м/с.
        t: время, с.
        a: ускорение, м/с² (по умолчанию 0 — равномерное движение).

    Returns:
        Перемещение, м.
    """
    return v0 * t + 0.5 * a * t * t


def acceleration_needed(v0: float, v: float, s: float) -> float:
    """Ускорение для разгона от v0 до v на пути s: a = (v² − v0²)/(2·s).

    Args:
        v0: начальная скорость, м/с.
        v: конечная скорость, м/с.
        s: путь, м.

    Returns:
        Ускорение, м/с².
    """
    if s == 0:
        raise ZeroDivisionError("Путь s не может быть равен нулю")
    return (v * v - v0 * v0) / (2.0 * s)


def velocity_after_displacement(v0: float, a: float, s: float) -> float:
    """Скорость после пути s при ускорении a: v = √(v0² + 2·a·s).

    Args:
        v0: начальная скорость, м/с.
        a: ускорение, м/с².
        s: путь, м.

    Returns:
        Скорость, м/с.
    """
    vsq = v0 * v0 + 2.0 * a * s
    if vsq < 0:
        raise ValueError("Подкоренное выражение отрицательно: нет вещественного решения")
    return vsq ** 0.5


def average_velocity(v0: float, v1: float) -> float:
    """Средняя скорость при равноускоренном движении: (v0 + v1)/2."""
    return 0.5 * (v0 + v1)


def free_fall_time(height: float, g: float = 9.80665) -> float:
    """Время свободного падения с высоты height (начальная скорость 0).

    Args:
        height: высота, м.
        g: ускорение свободного падения, м/с² (по умолчанию 9.80665).

    Returns:
        Время падения, с.
    """
    if height < 0:
        raise ValueError("Высота не может быть отрицательной")
    return (2.0 * height / g) ** 0.5
