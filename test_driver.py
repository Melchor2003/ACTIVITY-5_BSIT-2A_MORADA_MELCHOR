"""Non-interactive test driver. Demonstrates every operation, error handling
(underflow / overflow), circular wrap-around, and both applications.

Run:  python test_driver.py
"""

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, simulate_print_queue


def expect_error(label, func, exc_type):
    """Run func and confirm it raises exc_type; print the message."""
    try:
        func()
    except exc_type as err:
        print(f"  {label}: caught {exc_type.__name__} -> {err}")
    else:
        raise AssertionError(f"{label}: expected {exc_type.__name__}")


def test_stack(stack, name):
    print(f"\n--- {name} ---")
    expect_error("pop on empty", stack.pop, IndexError)
    expect_error("peek on empty", stack.peek, IndexError)
    assert stack.is_empty()
    for item in ["A", "B", "C"]:
        stack.push(item)
        print(f"  push {item}: {stack}")
    assert stack.peek() == "C"
    assert stack.pop() == "C"
    assert stack.peek() == "B"
    print(f"  after pop (C) and peek (B): {stack}")
    assert stack.pop() == "B" and stack.pop() == "A"   # LIFO order
    assert stack.is_empty()
    print("  LIFO order verified")


def test_array_stack_overflow():
    print("\n--- ArrayStack overflow ---")
    s = ArrayStack(2)
    s.push(1)
    s.push(2)
    assert s.is_full()
    expect_error("push on full", lambda: s.push(3), OverflowError)


def test_queue(queue, name):
    print(f"\n--- {name} ---")
    expect_error("dequeue on empty", queue.dequeue, IndexError)
    expect_error("peek_front on empty", queue.peek_front, IndexError)
    assert queue.is_empty()
    for item in ["A", "B", "C"]:
        queue.enqueue(item)
        print(f"  enqueue {item}: {queue}")
    assert queue.peek_front() == "A"
    assert queue.dequeue() == "A"
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"                       # FIFO order
    assert queue.is_empty()
    print("  FIFO order verified")


def test_circular_wraparound():
    print("\n--- ArrayQueue circular wrap-around (capacity 4) ---")
    q = ArrayQueue(4)
    for x in [1, 2, 3, 4]:
        q.enqueue(x)
    print(f"  full: {q}")
    expect_error("enqueue on full", lambda: q.enqueue(5), OverflowError)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    print(f"  after 2 dequeues: {q}")
    q.enqueue(5)   # goes into physical index 0
    q.enqueue(6)   # goes into physical index 1
    print(f"  after enqueue 5, 6 (wrapped past the end): {q}")
    assert q.is_full()
    assert [q.dequeue() for _ in range(4)] == [3, 4, 5, 6]
    print("  order after wrap-around verified: [3, 4, 5, 6]")


def test_linked_queue_reset():
    print("\n--- LinkedQueue rear reset when emptied ---")
    q = LinkedQueue()
    q.enqueue("x")
    q.dequeue()
    assert q.front is None and q.rear is None
    q.enqueue("y")                      # would break if rear were stale
    assert q.dequeue() == "y"
    print("  front and rear both None after emptying; later enqueue works")


def test_applications():
    print("\n--- Balanced parentheses ---")
    cases = {"([]{})": True, "(]": False, "((": False, "())": False,
             "{[()]}": True, "": True, "a(b[c]d)e": True}
    for text, expected in cases.items():
        result = is_balanced(text)
        assert result == expected, text
        print(f"  '{text}' -> {'balanced' if result else 'NOT balanced'}")

    print("\n--- Print queue simulation ---")
    report = simulate_print_queue([("J1", 5), ("J2", 2), ("J3", 10)])
    assert [r[1] for r in report] == ["J1", "J2", "J3"]   # FIFO


if __name__ == "__main__":
    test_stack(ArrayStack(5), "ArrayStack")
    test_stack(LinkedStack(), "LinkedStack")
    test_array_stack_overflow()
    test_queue(ArrayQueue(5), "ArrayQueue")
    test_queue(LinkedQueue(), "LinkedQueue")
    test_circular_wraparound()
    test_linked_queue_reset()
    test_applications()
    print("\nAll tests passed.")
