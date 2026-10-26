# Stacks and Queues: Array vs. Linked List

A Python lab that builds a stack and a queue from first principles, each in two ways: with a fixed-size array and with a singly linked list. A menu-driven program lets you try every operation and see the structure's state after each one.

No built-in list shortcuts such as `insert(0, x)` or `pop(0)` are used as stack/queue operations.

## Files

| File | Description |
|---|---|
| `node.py` | `Node` class shared by the linked stack and linked queue |
| `array_stack.py` | `ArrayStack`: fixed capacity, `top` index starting at `-1` |
| `linked_stack.py` | `LinkedStack`: push/pop at the head, no fixed capacity |
| `array_queue.py` | `ArrayQueue`: circular buffer using `front` + `size` and modulo wrap-around |
| `linked_queue.py` | `LinkedQueue`: head (`front`) and tail (`rear`) references |
| `applications.py` | Balanced-parentheses checker (stack) and print-queue simulation (queue) |
| `main.py` | Menu-driven program (choose implementation and operation) |
| `test_driver.py` | Non-interactive tests, including underflow, overflow and wrap-around |
| `sample_runs.md` | Captured output showing normal use and error handling |
| `analysis.md` | Written answer to the analysis question |

## Requirements

Python 3.8 or newer. No external packages.

## How to run

Run all commands from the folder containing the files.

**Menu program (interactive):**

```
python main.py
```

Choose an option:

1. `ArrayStack` (asks for a capacity)
2. `LinkedStack`
3. `ArrayQueue` (circular, asks for a capacity)
4. `LinkedQueue`
5. Balanced parentheses checker
6. Print queue simulation

Inside a structure's menu you can push/pop/peek (stacks) or enqueue/dequeue/peek_front (queues), check `is_empty` / `is_full`, or show the state. The state is printed after every operation. Errors (underflow/overflow) are reported with a descriptive message instead of crashing.

**Test driver (non-interactive):**

```
python test_driver.py
```

Runs every check and prints `All tests passed.` at the end.

## Operations and complexity

| Structure | Operations | Time |
|---|---|---|
| Stack (array or linked) | `push`, `pop`, `peek`, `is_empty`, `is_full` | O(1) each |
| Queue (array or linked) | `enqueue`, `dequeue`, `peek_front`, `is_empty`, `is_full` | O(1) each |

## Error handling

| Condition | Exception raised |
|---|---|
| `pop()` / `peek()` on an empty stack | `IndexError` ("Stack underflow..." / "Stack is empty...") |
| `push()` on a full `ArrayStack` | `OverflowError` ("Stack overflow...") |
| `dequeue()` / `peek_front()` on an empty queue | `IndexError` ("Queue underflow..." / "Queue is empty...") |
| `enqueue()` on a full `ArrayQueue` | `OverflowError` ("Queue overflow...") |

The linked versions have no fixed capacity, so `is_full()` always returns `False` and they never overflow.

## Design notes

- `ArrayStack` starts with `top = -1`. `push` increments `top` and then stores; `pop` reads the value and then decrements `top`.
- `LinkedStack` works only at the head so every operation is O(1).
- `ArrayQueue` uses a `size` counter rather than comparing `front` and `rear`, which avoids the empty-vs-full ambiguity.
- `LinkedQueue` resets `rear` to `None` when the queue becomes empty so later enqueues work correctly.

## Application exercises

- **Balanced parentheses:** `is_balanced(text)` uses a stack to check `()`, `[]`, `{}`.
- **Print queue:** `simulate_print_queue(jobs)` enqueues `(job_id, pages)` jobs and prints them in FIFO order, reporting the wait order and how many pages were ahead of each job.

## Author

Replace this line with your name, section and course.
