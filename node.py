"""Shared Node class for the linked-list stack and queue."""


class Node:
    """A single node of a singly linked list."""

    def __init__(self, value):
        self.value = value   # data stored in the node
        self.next = None     # reference to the next node (None = end)
