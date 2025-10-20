import time
from functools import lru_cache
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt


# Глобальные счётчики вызовов
call_count_naive: int = 0
call_count_memo: int = 0


# Временная сложность: O(phi^n) — экспоненциальная (phi ≈ 1.618...)
# Пространственная сложность (стек рекурсии): O(n)
def fibonacci_naive(n: int) -> int:
    """
    Наивная рекурсивная реализация Фибоначчи.

    Сложность: время O(phi^n), память (стек) O(n).
    """
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# Временная сложность: O(n) — каждое значение 0..n вычисляется один раз благодаря кешу
# Пространственная сложность: O(n) — кеш + глубина рекурсии
@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """
    Рекурсивная реализация Фибоначчи с мемоизацией (LRU-кеш).

    Сложность: время O(n), память O(n) (кеш + стек).
    """
    global call_count_memo
    call_count_memo += 1
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


# Замер времени: сложность вызова зависит от func(n);
# накладные расходы измерения — O(1) (start/stop таймер, вызов func).
def measure_time(func: Callable[[int], int], n: int, runs: int = 1) -> float:
    """
    Возвращает среднее время выполнения func(n) в секундах.

    Очистка кеша (если есть) выполняется перед запуском.
    """
    cache_clear = getattr(func, "cache_clear", None)
    if callable(cache_clear):
        cache_clear()

    times: List[float] = []
    for _ in range(max(1, runs)):
        t0 = time.perf_counter()
        func(n)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return sum(times) / len(times)


def save_time_plot(ns: List[int], naive_times: List[float], memo_times: List[float], fname: str) -> None:
    """Строит и сохраняет график времени (сек)."""
    plt.figure(figsize=(8, 5))
    plt.plot(ns, naive_times, marker="o", label="Наивная рекурсия")
    plt.plot(ns, memo_times, marker="s", label="Мемоизация (lru_cache)")
    plt.title("Сравнение времени вычисления чисел Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig(fname, dpi=300, bbox_inches="tight")
    plt.show()    
    plt.close()


def main() -> None:
    """Запускает эксперимент и сохраняет результаты."""
    ns: List[int] = list(range(5, 36, 5))
    naive_times: List[float] = []
    memo_times: List[float] = []
    naive_calls: List[int] = []
    memo_calls: List[int] = []

    for n in ns:
        # Сбрасываем счётчики
        global call_count_naive, call_count_memo
        call_count_naive = 0
        call_count_memo = 0

        # Наивная версия (внимание: для n > ~30 долго)
        t_naive = measure_time(fibonacci_naive, n, runs=1)
        naive_times.append(t_naive)
        naive_calls.append(call_count_naive)

        # Мемоизированная версия (несколько прогонов для устойчивости)
        t_memo = measure_time(fibonacci_memo, n, runs=3)
        memo_times.append(t_memo)
        memo_calls.append(call_count_memo)

    # Печать результатов
    print(f"{'n':>3} | {'naive(s)':>10} | {'naive_calls':>11} | {'memo(s)':>10} | {'memo_calls':>10}")
    print("-" * 60)
    for i, n in enumerate(ns):
        print(
            f"{n:3d} | {naive_times[i]:10.6f} | {naive_calls[i]:11d} | "
            f"{memo_times[i]:10.6f} | {memo_calls[i]:10d}"
        )

    # Сохранение графика времени
    save_time_plot(ns, naive_times, memo_times, fname="fib_time_comparison.png")


if __name__ == "__main__":
    main()
