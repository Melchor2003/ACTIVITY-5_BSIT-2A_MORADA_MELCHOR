"""LinkedQueue: a queue built on a singly linked list.

Keeps references to both the head (front, for dequeue) and the tail
(rear, for enqueue), so both operations are O(1).
"""

from node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None   # dequeue from the head
        self.rear = None    # enqueue at the tail
        self.size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, value):
        """Insert value at the rear. O(1)."""
        node = Node(value)
        if self.is_empty():
            self.front = node        # first element is both front and rear
        else:
            self.rear.next = node    # link after the old tail
        self.rear = node             # new node becomes the rear
        self.size += 1

    def dequeue(self):
        """Remove and return the front value. O(1)."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:       # queue became empty -> reset rear too
            self.rear = None
        self.size -= 1
        return value

    def peek_front(self):
        """Return the front value without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.front.value

    def __str__(self):
        items = []
        cur = self.front
        while cur is not None:
            items.append(cur.value)
            cur = cur.next
        return f"LinkedQueue (front -> rear): {items}  [size={self.size}]"
