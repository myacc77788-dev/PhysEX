import pytest

from physex.thermodynamics import (
    adiabatic_ratio,
    boltzmann_energy,
    efficiency,
    heat_capacity_constant_pressure,
    heat_capacity_constant_volume,
    heat_required,
    ideal_gas_pressure,
)


def test_ideal_gas_pressure():
    # 1 моль, T=273.15 К, V=0.022414 м³ → p≈101325 Па (1 атм)
    p = ideal_gas_pressure(1.0, 273.15, 0.022414)
    assert p == pytest.approx(101325.0, rel=1e-3)


def test_ideal_gas_pressure_zero_volume():
    with pytest.raises(ZeroDivisionError):
        ideal_gas_pressure(1.0, 300.0, 0.0)


def test_heat_required():
    # 2 кг воды, c=4186 Дж/(кг·К), ΔT=10 К → Q=83720 Дж
    assert heat_required(2.0, 4186.0, 10.0) == pytest.approx(83720.0)


def test_heat_capacity():
    # моноатомный газ C_v=1.5R, ν=2 → C_p=(1.5R+R)*2
    R = 8.31446261815324
    cv_per_mole = 1.5 * R
    cp = heat_capacity_constant_pressure(2.0, cv_per_mole)
    assert cp == pytest.approx((1.5 * R + R) * 2.0)
    cv = heat_capacity_constant_volume(2.0, cv_per_mole)
    assert cv == pytest.approx(1.5 * R * 2.0)


def test_boltzmann_energy():
    # T=300 К → E=1.380649e-23*300
    assert boltzmann_energy(300.0) == pytest.approx(1.380649e-23 * 300)


def test_efficiency():
    assert efficiency(30.0, 100.0) == pytest.approx(0.3)


def test_efficiency_zero_input():
    with pytest.raises(ZeroDivisionError):
        efficiency(1.0, 0.0)


def test_adiabatic_ratio():
    # одноатомный газ: γ=5/3
    R = 8.31446261815324
    assert adiabatic_ratio(2.5 * R, 1.5 * R) == pytest.approx(5.0 / 3.0)
