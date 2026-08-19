import pytest

from physex.dynamics import (
    centripetal_force,
    force,
    friction_force,
    gravitational_force,
    momentum,
    weight,
)


def test_force():
    assert force(3.0, 4.0) == pytest.approx(12.0)


def test_momentum():
    assert momentum(2.0, 10.0) == pytest.approx(20.0)


def test_weight_default_gravity():
    # m=1 кг → ~9.80665 Н
    assert weight(1.0) == pytest.approx(9.80665)
    assert weight(5.0, g=10.0) == pytest.approx(50.0)


def test_gravitational_force():
    # Земля ~5.972e24 кг, тело 1 кг на R=6.371e6 м
    G = 6.67430e-11
    f = gravitational_force(5.972e24, 1.0, 6.371e6, g=G)
    assert f == pytest.approx(9.8, rel=0.02)


def test_gravitational_force_zero_distance():
    with pytest.raises(ZeroDivisionError):
        gravitational_force(1.0, 1.0, 0.0)


def test_friction_force():
    assert friction_force(50.0, 0.3) == pytest.approx(15.0)


def test_centripetal_force():
    # 2 кг, 3 м/с, радиус 1 м → F = 18 Н
    assert centripetal_force(2.0, 3.0, 1.0) == pytest.approx(18.0)


def test_centripetal_force_zero_radius():
    with pytest.raises(ZeroDivisionError):
        centripetal_force(1.0, 1.0, 0.0)
