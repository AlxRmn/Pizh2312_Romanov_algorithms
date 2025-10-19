from typing import Union


def factorial(n: int) -> int:
    """Вычисляет факториал n рекурсивно.

    Базовый случай: n <= 1 -> 1.
    Временная сложность: O(n).
    Память (рекурсивный стек): O(n).
    """
    if n <= 1:  # O(1)
        return 1
    # O(1) * n рекурсивных вызовов => O(n)
    return n * factorial(n - 1)


def fib_naive(n: int) -> int:
    """Наивный рекурсивный вычислитель чисел Фибоначчи.

    Определение:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2) для n >= 2

    Временная сложность: O(2^n) (экспоненциальная).
    Память (рекурсивный стек): O(n) — глубина рекурсии.
    Замечание: для больших n этот вариант крайне неэффективен.
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fast_pow(a: Union[int, float], n: int) -> Union[int, float]:
    """Возведение a в степень n рекурсивно (деление степени пополам).

    Алгоритм: бинарное возведение в степень (exponentiation by squaring).
    Временная сложность: O(log n).
    Память (рекурсивный стек): O(log n).
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_pow(a, n // 2)  # рекурсивный вызов для n/2
        return half * half
    # если n нечётно
    return a * fast_pow(a, n - 1)
