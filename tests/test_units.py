import pytest

from physex.units import Quantity, dimension


def test_create_and_str():
    q = Quantity(10.0, "м")
    assert q.value == 10.0
    assert q.unit == "м"


def test_add_same_units():
    q = Quantity(2.0, "кг") + Quantity(3.0, "кг")
    assert q.value == pytest.approx(5.0)
    assert q.unit == "кг"


def test_add_incompatible():
    with pytest.raises(ValueError):
        Quantity(1.0, "м") + Quantity(1.0, "с")


def test_mul_scalar():
    q = Quantity(4.0, "Н") * 2
    assert q.value == pytest.approx(8.0)
    assert q.unit == "Н"


def test_rmul_scalar():
    q = 2 * Quantity(4.0, "Н")
    assert q.value == pytest.approx(8.0)


def test_mul_quantities():
    q = Quantity(2.0, "м") * Quantity(3.0, "с")
    assert q.value == pytest.approx(6.0)
    assert "м" in q.unit and "с" in q.unit


def test_div():
    q = Quantity(10.0, "м") / Quantity(2.0, "с")
    assert q.value == pytest.approx(5.0)


def test_div_scalar():
    assert (Quantity(10.0, "м") / 2).value == pytest.approx(5.0)


def test_pow():
    q = Quantity(3.0, "м") ** 2
    assert q.value == pytest.approx(9.0)


def test_equality():
    assert Quantity(1.0, "м") == Quantity(1.0, "м")
    assert Quantity(1.0, "м") != Quantity(2.0, "м")
    assert Quantity(1.0, "м") != Quantity(1.0, "с")


def test_wrap_quantity_forbidden():
    with pytest.raises(TypeError):
        Quantity(Quantity(1.0), "")


def test_mixed_with_int_raises():
    # скаляр + размерная величина = несовместимые единицы
    with pytest.raises(ValueError):
        Quantity(1.0, "м") + 5


def test_scalar_plus_scalar():
    assert (Quantity(1.0) + Quantity(2.0)).value == pytest.approx(3.0)


def test_dimension():
    assert dimension(Quantity(1.0, "м")) == "м"
    assert dimension(Quantity(1.0)) == "безразмерная"
