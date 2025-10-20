import os
from typing import List, Optional, Tuple


def recursive_binary_search(arr: List[int], target: int, left: int, right: int) -> Optional[int]:
    """Рекурсивный бинарный поиск в отсортированном массиве arr[left:right+1].

    Временная сложность: O(log n)
    Пространственная сложность (стек): O(log n)
    """
    if left > right:  # O(1) — базовый случай, элемент не найден
        return None
    mid = (left + right) // 2  # O(1)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    return recursive_binary_search(arr, target, left, mid - 1)


def hanoi_moves(n: int, src: str, aux: str, dst: str, moves: Optional[List[Tuple[str, str]]] = None) -> List[Tuple[str, str]]:
    """Генерирует последовательность перемещений для задачи Ханойских башен.

    Возвращает список кортежей (откуда, куда).

    Временная сложность: O(2^n) (количество перемещений = 2^n - 1).
    Пространственная сложность: O(n) (глубина рекурсии).
    """
    if moves is None:
        moves = []
    if n <= 0:
        return moves
    if n == 1:
        moves.append((src, dst))
        return moves
    # Переместить n-1 дисков src -> aux
    hanoi_moves(n - 1, src, dst, aux, moves)
    # Переместить самый большой диск src -> dst
    moves.append((src, dst))
    # Переместить n-1 дисков aux -> dst
    hanoi_moves(n - 1, aux, src, dst, moves)
    return moves


def walk_directory(path: str, depth: int = 0, max_depth: Optional[int] = None) -> List[str]:
    """Рекурсивный обход директории: возвращает список строк с отступами, представляющими дерево.

    depth: текущий уровень (используется для отступов).
    max_depth: если задан, ограничивает глубину обхода.

    Временная сложность: O(number_of_files + number_of_dirs)
    Пространственная сложность: O(depth)
    """
    entries: List[str] = []
    try:
        with os.scandir(path) as it:
            for entry in it:
                entries.append("  " * depth + entry.name)
                if entry.is_dir(follow_symlinks=False):
                    if max_depth is None or depth + 1 <= max_depth:
                        entries.extend(walk_directory(entry.path, depth + 1, max_depth))
    except PermissionError:
        entries.append("  " * depth + "[PermissionError]")
    except FileNotFoundError:
        entries.append("  " * depth + "[NotFound]")
    return entries


def max_depth_walk(path: str) -> int:
    """Измеряет максимальную глубину вложенности в файловой системе начиная с path.

    Возвращает максимальное значение depth.
    """
    max_d = 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_dir(follow_symlinks=False):
                    child_depth = max_depth_walk(entry.path)
                    if child_depth + 1 > max_d:
                        max_d = child_depth + 1
    except PermissionError:
        return 0
    except FileNotFoundError:
        return 0
    return max_d


# Примеры работы
if __name__ == "__main__":
    # Рекурсивный бинарный поиск
    arr_example = list(range(0, 100, 2))
    idx = recursive_binary_search(arr_example, 42, 0, len(arr_example) - 1)
    print("Index of 42 in even array:", idx)

    # Ханойские башни (пример n=3)
    moves_example = hanoi_moves(3, "A", "B", "C")
    print("Hanoi moves for n=3:")
    for m in moves_example:
        print(f"{m[0]} -> {m[1]}")

    # Обход текущей директории (ограничим глубину, чтобы не идти слишком глубоко)
    tree = walk_directory(".", max_depth=2)
    print("Directory tree (depth <=2):")
    for line in tree[:50]:
        print(line)

    # Максимальная глубина текущей папки
    print("Max directory depth (this dir):", max_depth_walk("."))
