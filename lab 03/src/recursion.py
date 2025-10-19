from typing import Dict, Optional

PC_INFO: str = (
    "Характеристики ПК для тестирования:\n"
    "- CPU: (заполните)\n"
    "- RAM: (заполните)\n"
    "- ОС: (заполните)\n"
    "- Python: (заполните)\n"
)


def factorial(n: int) -> int:
    """Вычисляет факториал n рекурсивно.

    Базовый случай: factorial(0) == 1.
    Временная сложность: O(n) — выполняется n рекурсивных вызовов.
    Пространственная сложность (стек): O(n) — глубина рекурсии n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:  # O(1) — базовый случай
        return 1  # O(1)
    return n * factorial(n - 1)  # рекурсивный шаг: O(1) * O(n-1) => O(n)


def fib_naive(n: int) -> int:
    """Наивный рекурсивный расчёт n-го числа Фибоначчи.

    Определение:
        fib(0) = 0, fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2) для n >= 2

    Временная сложность: O(phi^n) — экспоненциальная (примерно O(1.618^n)).
    Пространственная сложность (стек): O(n) — глубина рекурсии равна n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:  # O(1) — базовый случай
        return n  # O(1)
    # два рекурсивных вызова
    return fib_naive(n - 1) + fib_naive(n - 2)  # экспоненциальное количество вызовов


def fast_pow(a: float, n: int) -> float:
    """Быстрое возведение a в степень n (exponentiation by squaring).

    Временная сложность: O(log n) — число рекурсивных вызовов ~ log2(n).
    Пространственная сложность: O(log n) — глубина стека рекурсии.
    """
    if n < 0:
        return 1.0 / fast_pow(a, -n)  # обработка отрицательной степени
    if n == 0:
        return 1.0
    if n % 2 == 0:
        half = fast_pow(a, n // 2)  # один рекурсивный вызов
        return half * half
    # n нечетное
    return a * fast_pow(a, n - 1)


if __name__ == "__main__":
    print(PC_INFO)
    print("factorial(5) =", factorial(5))  # 120
    print("fib_naive(10) =", fib_naive(10))  # 55
    print("fast_pow(2, 10) =", fast_pow(2, 10))  # 1024
