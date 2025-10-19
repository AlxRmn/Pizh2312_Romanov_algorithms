"""Практические задачи из ЛР-02."""
from collections import deque


def is_balanced_brackets(s: str) -> bool:
    """Проверка сбалансированности скобок. Сложность O(n)."""
    stack: list[str] = []  # O(1)
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in s:  # O(n)
        if char in brackets.values():
            stack.append(char)  # O(1)
        elif char in brackets:  # O(1)
            if not stack or stack.pop() != brackets[char]:  # O(1)
                return False
    return not stack  # O(1)


def print_queue_simulation(jobs: list[str]) -> None:
    """Симуляция обработки очереди печати. Сложность O(n)."""
    queue = deque(jobs)  # O(n)
    while queue:  # O(n)
        job = queue.popleft()  # O(1)
        print(f"Печатается: {job}")  # O(1)


def is_palindrome(seq: str) -> bool:
    """Проверка палиндрома через deque. Сложность O(n)."""
    d = deque(seq.lower())  # O(n)
    while len(d) > 1:  # O(n/2)
        if d.popleft() != d.pop():  # O(1)
            return False
    return True
