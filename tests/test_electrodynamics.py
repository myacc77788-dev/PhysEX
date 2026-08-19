import pytest

from physex.electrodynamics import (
    capacitance,
    capacitor_energy,
    coulomb_force,
    current,
    electric_field,
    electric_potential,
    electric_power,
    ohm_law_voltage,
    resistance,
)


def test_coulomb_force():
    # два заряда по 1 мкКл на 1 см → F≈90 Н
    q = 1e-6
    f = coulomb_force(q, q, 0.01)
    assert f == pytest.approx(89.875, rel=1e-2)


def test_coulomb_force_zero_distance():
    with pytest.raises(ZeroDivisionError):
        coulomb_force(1.0, 1.0, 0.0)


def test_electric_field():
    e = electric_field(1e-9, 1.0)
    # E = k*q/r² ≈ 8.99 В/м
    assert e == pytest.approx(8.99, rel=1e-2)


def test_electric_potential():
    phi = electric_potential(1e-9, 1.0)
    assert phi == pytest.approx(8.99, rel=1e-2)


def test_current():
    assert current(5.0, 2.0) == pytest.approx(2.5)


def test_current_zero_time():
    with pytest.raises(ZeroDivisionError):
        current(1.0, 0.0)


def test_resistance():
    assert resistance(12.0, 2.0) == pytest.approx(6.0)


def test_resistance_zero_current():
    with pytest.raises(ZeroDivisionError):
        resistance(1.0, 0.0)


def test_ohm_law_voltage():
    assert ohm_law_voltage(3.0, 4.0) == pytest.approx(12.0)


def test_electric_power():
    assert electric_power(12.0, 2.0) == pytest.approx(24.0)


def test_capacitance():
    assert capacitance(1e-6, 2.0) == pytest.approx(0.5e-6)


def test_capacitance_zero_voltage():
    with pytest.raises(ZeroDivisionError):
        capacitance(1.0, 0.0)


def test_capacitor_energy():
    # C=10 мкФ, U=100 В → W=0.5*10e-6*10000=0.05 Дж
    assert capacitor_energy(10e-6, 100.0) == pytest.approx(0.05)
