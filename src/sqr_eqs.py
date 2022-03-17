import math


def almost_equal(
    x: float,
    y: float,
    precision: float = 1e-100,
) -> bool:
    """Сравнит что числа `x` и `y` различаются не больше чем на `precision`.

    Args:
        x: первое сравнимое
        y: первое сравнимое
        precision: точность сравнения.

    Returns:
        `True`, если `x` почти равен `y`, иначе `False`.
    """
    return abs(x - y) < precision


def solve(
    a: float,
    b: float,
    c: float,
    precision: float = 1e-100,
) -> list[float]:
    """Решает квадратные уравнения.

    Args:
        a: коэфициент a
        b: коэфициент b
        c: коэфициент c
        precision: точность для сравнения с нулем.

    Raises:
        ValueError: если NaN в аргументах
        ValueError: если коэфициент `a` близок к нулю.

    Returns:
        Список корней. Если корней нет, список пустой.
    """
    if any([
        math.isnan(arg)
        for arg in (a, b, c)
    ]):
        raise ValueError("Got NaN in args")

    if almost_equal(a, 0, precision):
        raise ValueError("Argument 'a' shouldn't be a zero.")

    discriminant = b**2 - (4 * a * c)
    if discriminant < 0:
        return {}
    if almost_equal(discriminant, 0, precision):
        return [-b / (2 * a)]
    return [
        (-b + math.sqrt(discriminant)) / (2 * a),
        (-b - math.sqrt(discriminant)) / (2 * a),
    ]
