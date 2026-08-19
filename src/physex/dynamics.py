"""Динамика: сила, импульс, гравитация, трения и центробежные силы."""

from __future__ import annotations

from .constants import gravitational_constant, standard_gravity

__all__ = [
    "force",
    "momentum",
    "weight",
    "gravitational_force",
    "friction_force",
    "centripetal_force",
    "newton_gravitation",
]


def force(mass: float, acceleration: float) -> float:
    """Второй закон Ньютона: F = m·a."""
    return mass * acceleration


def momentum(mass: float, velocity: float) -> float:
    """Импульс тела: p = m·v."""
    return mass * velocity


def weight(mass: float, g: float | None = None) -> float:
    """Сила тяжести: F = m·g. По умолчанию g = 9.80665 м/с²."""
    if g is None:
        g = standard_gravity.value
    return mass * g


def gravitational_force(m1: float, m2: float, distance: float,
                        g: float | None = None) -> float:
    """Закон всемирного тяготения: F = G·m1·m2/r²."""
    if distance == 0:
        raise ZeroDivisionError("Расстояние не может быть нулевым")
    if g is None:
        g = gravitational_constant.value
    return g * m1 * m2 / (distance * distance)


def friction_force(normal_force: float, coefficient: float) -> float:
    """Сила трения скольжения: F = μ·N."""
    return coefficient * normal_force


def centripetal_force(mass: float, velocity: float, radius: float) -> float:
    """Центростремительная сила: F = m·v²/r."""
    if radius == 0:
        raise ZeroDivisionError("Радиус не может быть нулевым")
    return mass * velocity * velocity / radius


# Алиас для единообразного именования.
newton_gravitation = gravitational_force
