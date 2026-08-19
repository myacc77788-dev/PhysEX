import pytest

import physex
from physex import constants


def test_well_known_values():
    assert constants.speed_of_light.value == pytest.approx(2.99792458e8)
    assert constants.planck.value == pytest.approx(6.62607015e-34)
    assert constants.elementary_charge.value == pytest.approx(1.602176634e-19)
    assert constants.avogadro.value == pytest.approx(6.02214076e23)


def test_gas_constant_relation():
    # R = k_B * N_A
    R = constants.gas_constant.value
    kB = constants.boltzmann.value
    NA = constants.avogadro.value
    assert R == pytest.approx(kB * NA, rel=1e-6)


def test_reduced_planck():
    import math

    h = constants.planck.value
    assert constants.reduced_planck.value == pytest.approx(h / (2 * math.pi))


def test_all_constants_units():
    for c in constants.all_constants():
        assert isinstance(c.name, str)
        assert c.unit != "" or c.name == "постоянная тонкой структуры"


def test_exports_from_package():
    assert physex.speed_of_light.value == pytest.approx(2.99792458e8)
    assert physex.__version__ == "0.1.0"
