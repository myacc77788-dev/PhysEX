import math

import pytest

from physex.energy import (
    elastic_potential_energy,
    kinetic_energy,
    potential_energy,
    power,
    work,
)


def test_kinetic_energy():
    assert kinetic_energy(2.0, 3.0) == pytest.approx(9.0)  # 0.5*2*9


def test_potential_energy():
    assert potential_energy(10.0, 2.0, g=9.8) == pytest.approx(196.0)


def test_elastic_potential_energy():
    assert elastic_potential_energy(100.0, 0.1) == pytest.approx(0.5)


def test_work_parallel():
    # F=10 Н, s=5 м, θ=0 → A=50 Дж
    assert work(10.0, 5.0, 0.0) == pytest.approx(50.0)


def test_work_angle():
    # F=10, s=5, θ=60° → A=50*cos60=25
    assert work(10.0, 5.0, 60.0) == pytest.approx(25.0, rel=1e-9)


def test_power():
    assert power(100.0, 10.0) == pytest.approx(10.0)


def test_power_zero_time():
    with pytest.raises(ZeroDivisionError):
        power(1.0, 0.0)
