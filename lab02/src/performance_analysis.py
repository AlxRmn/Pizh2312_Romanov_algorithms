"""Сравнение производительности list, LinkedList и deque (ЛР-02)."""
import timeit
from collections import deque
import matplotlib.pyplot as plt
from lab02.src.linked_list import LinkedList


def measure_time(func, *args, number: int = 1000) -> float:
    """Замер времени выполнения функции (среднее, мс)."""
    return timeit.timeit(lambda: func(*args), number=number) * 1000 / number


def compare_insert_start(sizes: list[int]) -> tuple[list[float], list[float]]:
    """Сравнение вставки в начало: list vs LinkedList."""
    list_times, linked_times = [], []
    for n in sizes:
        lst = []
        t_list = timeit.timeit(lambda: lst.insert(0, 1), number=n) * 1000 / n
        list_times.append(t_list)

        ll = LinkedList()
        t_ll = timeit.timeit(lambda: ll.insert_at_start(1), number=n) * 1000 / n
        linked_times.append(t_ll)
    return list_times, linked_times


def compare_queue(sizes: list[int]) -> tuple[list[float], list[float]]:
    """Сравнение удаления из начала: list vs deque."""
    deque_times, list_pop_times = [], []
    for n in sizes:
        d = deque(range(n))
        lst_q = list(range(n))
        t_deque = timeit.timeit(lambda: d.popleft(), number=n) * 1000 / n
        t_list_pop0 = timeit.timeit(lambda: lst_q.pop(0), number=n) * 1000 / n
        deque_times.append(t_deque)
        list_pop_times.append(t_list_pop0)
    return deque_times, list_pop_times


def plot_insert_graph(sizes: list[int], list_times: list[float],
                      linked_times: list[float]) -> None:
    """График сравнения вставки."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_times, "r-o", label="list.insert(0, x)")
    plt.plot(sizes, linked_times, "g-o", label="LinkedList.insert_at_start")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Время одной операции (мс)")
    plt.title("Вставка в начало: list vs LinkedList")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("insert_comparison.png", dpi=300, bbox_inches="tight")


def plot_queue_graph(sizes: list[int], deque_times: list[float],
                     list_pop_times: list[float]) -> None:
    """График сравнения очередей."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_pop_times, "r-o", label="list.pop(0)")
    plt.plot(sizes, deque_times, "b-o", label="deque.popleft()")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Время одной операции (мс)")
    plt.title("Удаление из начала: list vs deque")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("queue_comparison.png", dpi=300, bbox_inches="tight")


def main() -> None:
    """Основной запуск: замеры + графики."""
    sizes = [100, 500, 1000, 5000, 10000]
    list_times, linked_times = compare_insert_start(sizes)
    deque_times, list_pop_times = compare_queue(sizes)

    plot_insert_graph(sizes, list_times, linked_times)
    plot_queue_graph(sizes, deque_times, list_pop_times)

    pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-10210U @ 1.60GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 10
- Python: 3.13.2
"""
    print(pc_info)


if __name__ == "__main__":
    main()
