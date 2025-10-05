# sum_analysis.py
import random  # Стандартная библиотека
import timeit  # Стандартная библиотека
from typing import List  # Стандартная библиотека

import matplotlib.pyplot as plt  # Сторонняя библиотека


def calculate_sum_from_file(filename: str) -> None:
    """Считывает два целых числа из файла и выводит их сумму.

    Общая сложность: O(1), так как количество операций не зависит от размера входных данных.
    """
    # O(1) — открытие файла
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()  # O(1), т.к. в файле фиксированное количество чисел (2 строки)

    print("Содержимое файла:")
    for line in lines:  # O(1), цикл фиксированной длины (2 строки)
        print(f"→ {line.strip()} (считано число из файла)")

    # O(1) — преобразование строк в числа
    a: int = int(lines[0].strip())
    b: int = int(lines[1].strip())

    # O(1) — вычисление суммы
    result: int = a + b

    # O(1) — вывод результата
    print(f"Сумма чисел {a} и {b} равна {result}")

    # Общая сложность: O(1)


def sum_array(arr: List[int]) -> int:
    """Возвращает сумму всех элементов массива.

    Сложность: O(N), где N — длина массива.
    """
    total: int = 0  # O(1).
    for num in arr:  # O(N).
        total += num  # O(1).
    return total  # O(1).
    # Общая сложность: O(N).


def measure_time(func, data: List[int]) -> float:
    """Измеряет время выполнения функции в миллисекундах."""
    start_time: float = timeit.default_timer()
    func(data)
    end_time: float = timeit.default_timer()
    return (end_time - start_time) * 1000  # В миллисекундах.


def run_experiments() -> None:
    """Проводит замеры времени выполнения и строит график."""
    pc_info: str = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-10210U @ 1.60GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 10
- Python: 3.13.2
"""
    print(pc_info)

    sizes: List[int] = [1000, 5000, 10000, 50000, 100000, 500000]
    times: List[float] = []

    print('Замеры времени выполнения для алгоритма суммирования массива:')
    print('{:>10} {:>12} {:>15}'.format('Размер (N)', 'Время (мс)', 'Время/N (мкс)'))

    for size in sizes:
        data: List[int] = [random.randint(1, 1000) for _ in range(size)]

        execution_time: float = (
            timeit.timeit(lambda: sum_array(data), number=10) * 1000 / 10
        )
        times.append(execution_time)
        time_per_element: float = (
            (execution_time * 1000) / size if size > 0 else 0
        )

        print(
            '{:>10} {:>12.4f} {:>15.4f}'.format(
                size, execution_time, time_per_element
            )
        )

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', label='Измеренное время')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время выполнения (мс)')
    plt.title('Зависимость времени выполнения от размера массива\nСложность: O(N)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('time_complexity_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

    print('\nАнализ результатов:')
    print('1. Теоретическая сложность алгоритма: O(N).')
    print('2. Практические замеры показывают линейную зависимость времени от N.')
    print(
        f'3. Время на один элемент примерно постоянно '
        f'(~{time_per_element:.4f} мкс).'
    )


if __name__ == '__main__':
    calculate_sum_from_file("input.txt")  
    run_experiments()
