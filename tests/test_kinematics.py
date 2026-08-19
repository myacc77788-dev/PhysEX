import math

import pytest

from physex.kinematics import (
    acceleration_needed,
    average_velocity,
    displacement,
    final_velocity,
    free_fall_time,
    velocity_after_displacement,
)


def test_final_velocity():
    assert final_velocity(0.0, 2.0, 5.0) == pytest.approx(10.0)
    assert final_velocity(5.0, -1.0, 2.0) == pytest.approx(3.0)


def test_displacement_uniform():
    assert displacement(10.0, 3.0) == pytest.approx(30.0)


def test_displacement_accelerated():
    assert displacement(0.0, 4.0, 2.0) == pytest.approx(16.0)
    assert displacement(2.0, 3.0, 4.0) == pytest.approx(2 * 3 + 0.5 * 4 * 9)


def test_acceleration_needed():
    assert acceleration_needed(0.0, 20.0, 100.0) == pytest.approx(2.0)


def test_acceleration_needed_zero_path():
    with pytest.raises(ZeroDivisionError):
        acceleration_needed(1.0, 2.0, 0.0)


def test_velocity_after_displacement():
    assert velocity_after_displacement(0.0, 2.0, 4.0) == pytest.approx(4.0)


def test_velocity_after_displacement_no_solution():
    with pytest.raises(ValueError):
        velocity_after_displacement(1.0, -5.0, 1.0)


def test_average_velocity():
    assert average_velocity(0.0, 10.0) == pytest.approx(5.0)


def test_free_fall_time():
    # t = sqrt(2h/g); для h=4.9 м и g=9.8 с → t≈1.0 с
    assert free_fall_time(4.9, 9.8) == pytest.approx(1.0, rel=1e-6)
    assert free_fall_time(0.0) == pytest.approx(0.0)


def test_free_fall_time_negative():
    with pytest.raises(ValueError):
        free_fall_time(-1.0)
