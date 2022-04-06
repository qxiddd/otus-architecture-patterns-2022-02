import enum
import math


class CompareResult(enum.Enum):
    lower = -1
    equal = 0
    greater = 1


def compare(
    x: float,
    y: float,
    precision: float = 1e-7,
) -> CompareResult:
    """Сравнит что числа `x` и `y` c точностью `precision`.

    Args:
        x: первое сравнимое
        y: первое сравнимое
        precision: точность сравнения.

    Returns:
        `True`, если `x` почти равен `y`, иначе `False`.
    """
    if abs(x - y) < precision:
        return CompareResult.equal
    if x < y:
        return CompareResult.lower
    return CompareResult.greater


def solve(
    a: float,
    b: float,
    c: float,
    precision: float = 1e-7,
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

    if compare(a, 0, precision) == CompareResult.equal:
        raise ValueError("Argument 'a' shouldn't be a zero.")

    discriminant = b**2 - (4 * a * c)
    if compare(discriminant, 0, precision) == CompareResult.lower:
        return {}
    if compare(discriminant, 0, precision) == CompareResult.equal:
        return [-b / (2 * a)]
    return [
        (-b + math.sqrt(discriminant)) / (2 * a),
        (-b - math.sqrt(discriminant)) / (2 * a),
    ]
