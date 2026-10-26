"""ArrayStack: a fixed-capacity stack backed by a Python list.

`top` is the index of the current top element; -1 means the stack is empty.
"""


class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.data = [None] * capacity   # fixed-size storage
        self.top = -1                   # -1 => empty stack

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        """Insert value at the top. O(1)."""
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack")
        self.top = self.top + 1         # move top up first...
        self.data[self.top] = value     # ...then store

    def pop(self):
        """Remove and return the top value. O(1)."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]     # read the top value first...
        self.data[self.top] = None      # (clear slot for clarity)
        self.top = self.top - 1         # ...then move top down
        return value

    def peek(self):
        """Return the top value without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.data[self.top]

    def __str__(self):
        items = self.data[: self.top + 1]
        return f"ArrayStack (bottom -> top): {items}  [size={self.top + 1}/{len(self.data)}]"
