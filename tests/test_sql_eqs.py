import math

import pytest

from sqr_eqs import (
    almost_equal,
    solve
)


def test_no_roots():
    """Проверить случай, когда нет корней."""
    assert solve(1, 0, 1) == {}


def test_two_roots():
    """Проверить случай, когда корней два."""
    solution = solve(1, 0, -1)
    assert solution == [1, -1] or solution == [-1, 1]


def test_one_root():
    """Проверить случай когда есть единственный корень.

    В тесте подбираются корни близкие по значению, чтобы функция solve решила, что у уравнения есть только 1 корень.
    """
    precision = 1e-100
    delta = 1e-101
    root_1 = 2
    root_2 = 2 + delta

    # подсчитаем коэфициенты b и c
    # (x - root_1) * (x - root_2) == 0
    # x*x - x*root_2 - x*root_1 + root_1*root_2 == 0
    # x*x + x*(-(root_1 + root_2)) + root_1*root_2 == 0
    b = -(root_1 + root_2)
    c = root_1 * root_2

    # Убеждаемся, что только один корень
    [actual_root] = solve(1, b, c, precision)

    assert almost_equal(actual_root, root_1, precision)
    assert almost_equal(actual_root, root_2, precision)


def test_non_zero_square():
    """Проверить поведение, когда коэфиент `a` равен нулю."""
    with pytest.raises(ValueError, match="Argument 'a' shouldn't be a zero."):
        solve(1e-101, 0, 0, precision=1e-100)


@pytest.mark.parametrize(
    'a, b, c',
    (
        (math.nan, 1.0, 1.0),
        (1.0, math.nan, 1.0),
        (1.0, 1.0, math.nan),
    ),
)
def test_nan(a, b, c):
    """Проверить поведение, когда передается NaN одним из аргументов."""
    with pytest.raises(ValueError, match="Got NaN in args"):
        solve(a, b, c)
