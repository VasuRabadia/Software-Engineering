import pytest
from adder import add


def test_add_integers():
    assert add(0, 0) == 0
    assert add(1, 1) == 2
    assert add(7, 5) == 12
    assert add(-7, -5) == -12
    assert add(-3, 5) == 2
    assert add(3, -5) == -2


def test_add_floats():
    assert add(0.0, 0.0) == 0.0
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -4.0
    assert add(-3.25, 5.25) == 2.0
    assert add(3.25, 5.25) == 8.5
    assert add(0.1234, 0.1234) == 0.2468


def test_add_mixed_types():
    assert add(1, 1.5) == 2.5
    assert add(3.2, 2) == 5.2
    assert add(-5, 2.7) == -2.3
    assert add(7.9, -3) == 4.9


def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
    assert add(-1_000_000, 2_000_000) == 1_000_000
    assert add(1e9, 1e9) == 2e9


def test_add_edge_cases():
    assert add(float("inf"), 1) == float("inf")
    assert add(float("-inf"), -1) == float("-inf")
    assert add(float("inf"), float("-inf")) != float("inf")  # Should result in NaN


def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("string", 2)
    with pytest.raises(TypeError):
        add(None, 1)
    with pytest.raises(TypeError):
        add([1, 2, 3], 4)
    with pytest.raises(TypeError):
        add({"a": 1}, 5)
