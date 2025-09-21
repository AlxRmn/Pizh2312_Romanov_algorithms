# search_comparison.py
import random  # Импорты из стандартной библиотеки
import timeit
from typing import List, Optional

import matplotlib.pyplot as plt  # Импорты из сторонних библиотек


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Линейный поиск элемента в массиве.

    Сложность: O(n), где n — длина массива.
    """
    for i, value in enumerate(arr):  # O(n) — цикл по массиву
        if value == target:  # O(1) — сравнение
            return i  # O(1) — возврат индекса
    return None  # O(1) — возврат None
    # Общая сложность: O(n)

пш