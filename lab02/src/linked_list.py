"""Реализация односвязного списка (ЛР-02)."""
from __future__ import annotations
from typing import Any, Optional


class Node:
    """Узел связного списка."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional[Node] = None


class LinkedList:
    """Односвязный список."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  # Для O(1) вставки в конец

    def insert_at_start(self, data: Any) -> None:
        """Вставка элемента в начало. Сложность O(1)."""
        new_node = Node(data)  # O(1)
        new_node.next = self.head  # O(1)
        self.head = new_node  # O(1)
        if self.tail is None:  # O(1)
            self.tail = new_node  # O(1)

    def insert_at_end(self, data: Any) -> None:
        """Вставка элемента в конец. Сложность O(1) при наличии tail."""
        new_node = Node(data)  # O(1)
        if self.tail:  # O(1)
            self.tail.next = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:
            self.head = self.tail = new_node  # O(1)

    def delete_from_start(self) -> Optional[Any]:
        """Удаление элемента из начала. Сложность O(1)."""
        if self.head is None:  # O(1)
            return None
        removed_data = self.head.data  # O(1)
        self.head = self.head.next  # O(1)
        if self.head is None:  # O(1)
            self.tail = None  # O(1)
        return removed_data  # O(1)

    def traversal(self) -> list[Any]:
        """Возвращает список элементов. Сложность O(n)."""
        elements: list[Any] = []  # O(1)
        current = self.head  # O(1)
        while current:  # O(n)
            elements.append(current.data)  # O(1)
            current = current.next  # O(1)
        return elements  # O(1)
