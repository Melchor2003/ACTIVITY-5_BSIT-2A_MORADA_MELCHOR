"""ArrayQueue: a fixed-capacity circular queue backed by a Python list.

The array is treated as a ring using the modulo operator, so slots freed
at the front by dequeue are reused by later enqueues. A `size` counter is
used (not front == rear) to tell an empty queue from a full one.
"""


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.data = [None] * capacity
        self.front = 0    # index of the front element
        self.size = 0     # number of stored elements

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        """Insert value at the rear. O(1)."""
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue")
        rear = (self.front + self.size) % len(self.data)   # wrap around
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        """Remove and return the front value. O(1)."""
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)     # wrap around
        self.size = self.size - 1
        return value

    def peek_front(self):
        """Return the front value without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.data[self.front]

    def __str__(self):
        items = [self.data[(self.front + i) % len(self.data)] for i in range(self.size)]
        return (f"ArrayQueue (front -> rear): {items}  "
                f"[size={self.size}/{len(self.data)}, front index={self.front}, raw array={self.data}]")
