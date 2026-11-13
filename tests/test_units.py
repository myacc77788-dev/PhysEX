import operator

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


def test_subtract_same_units_without_mutating_operands():
    left = Quantity(5.0, "м")
    right = Quantity(2.0, "м")
    result = left - right
    assert result.value == pytest.approx(3.0)
    assert result.unit == "м"
    assert left.value == 5.0
    assert right.value == 2.0


@pytest.mark.parametrize("other", [Quantity(1.0, "с"), 1.0])
def test_subtract_incompatible_units(other):
    with pytest.raises(ValueError, match="Несовместимые единицы"):
        Quantity(2.0, "м") - other


@pytest.mark.parametrize("operation", [operator.add, operator.sub])
def test_dimensionless_arithmetic_accepts_scalars(operation):
    result = operation(Quantity(4.0), 2)
    assert result.value == pytest.approx(operation(4.0, 2))
    assert result.unit == ""


@pytest.mark.parametrize(
    "operation",
    [operator.add, operator.sub, operator.mul, operator.truediv, operator.pow],
)
@pytest.mark.parametrize("other", ["2", None])
def test_arithmetic_rejects_non_numeric_operands(operation, other):
    with pytest.raises(TypeError):
        operation(Quantity(4.0, "м"), other)


def test_reflected_multiply_rejects_non_numeric_operand():
    with pytest.raises(TypeError):
        "2" * Quantity(4.0, "м")


@pytest.mark.parametrize("divisor", [0, 0.0, Quantity(0.0, "с")])
def test_division_by_zero(divisor):
    with pytest.raises(ZeroDivisionError):
        Quantity(4.0, "м") / divisor


@pytest.mark.parametrize("value, error", [("invalid", ValueError), (None, TypeError)])
def test_constructor_rejects_non_numeric_values(value, error):
    with pytest.raises(error):
        Quantity(value, "м")


@pytest.mark.parametrize("other", ["1", None, object()])
def test_equality_with_unsupported_values_is_false(other):
    assert not (Quantity(1.0) == other)


def test_to_base_scales_value_without_mutating_original():
    original = Quantity(2.5, "м")
    converted = original.to_base(1000)
    assert converted.value == pytest.approx(2500)
    assert converted.unit == "м"
    assert original.value == 2.5
    assert original.unit == "м"
