from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Вычисляет n-е число Фибоначчи с мемоизацией.

    Временная сложность: O(n).
    Память (кэш): O(n).
    Рекурсивный стек: O(n).
    """
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def count_recursive_calls_naive(n: int) -> int:
    """Точно считает число вызовов для наивной fib_naive.

    Модель вызовов: C(0)=1, C(1)=1, C(n)=C(n-1)+C(n-2)+1
    (где +1 — сам вызов текущей функции).

    Реализация использует динамическое программирование за O(n) времени и O(n) памяти.

    Возвращает:
        int: число вызовов функции fib_naive при вычислении fib_naive(n).
    """
    if n <= 1:
        return 1
    c: List[int] = [0] * (n + 1)
    c[0] = 1
    c[1] = 1
    for i in range(2, n + 1):  # O(n)
        c[i] = c[i - 1] + c[i - 2] + 1
    return c[n]
