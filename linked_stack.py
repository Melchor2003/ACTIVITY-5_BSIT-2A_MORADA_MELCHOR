"""LinkedStack: a stack built on a singly linked list (no fixed capacity).

Push and pop both happen at the HEAD of the list, so both are O(1).
Popping from the tail of a singly linked list would be O(n).
"""

from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None   # head of the list = top of the stack
        self.size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity; it only runs out of memory.
        return False

    def push(self, value):
        """Insert value at the top. O(1)."""
        node = Node(value)
        node.next = self.top   # new node points to the old top
        self.top = node        # new node becomes the top
        self.size += 1

    def pop(self):
        """Remove and return the top value. O(1)."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next   # move top down the chain
        self.size -= 1
        return value

    def peek(self):
        """Return the top value without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def __str__(self):
        items = []
        cur = self.top
        while cur is not None:
            items.append(cur.value)
            cur = cur.next
        items.reverse()   # show bottom -> top, same as ArrayStack
        return f"LinkedStack (bottom -> top): {items}  [size={self.size}]"
