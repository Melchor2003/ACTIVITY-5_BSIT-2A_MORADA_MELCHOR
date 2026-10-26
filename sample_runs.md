# Sample Runs

## 1. Test driver (`python test_driver.py`)

Shows normal operation, underflow and overflow errors, circular wrap-around, and both applications.

```

--- ArrayStack ---
  pop on empty: caught IndexError -> Stack underflow: cannot pop from an empty stack
  peek on empty: caught IndexError -> Stack is empty: nothing to peek
  push A: ArrayStack (bottom -> top): ['A']  [size=1/5]
  push B: ArrayStack (bottom -> top): ['A', 'B']  [size=2/5]
  push C: ArrayStack (bottom -> top): ['A', 'B', 'C']  [size=3/5]
  after pop (C) and peek (B): ArrayStack (bottom -> top): ['A', 'B']  [size=2/5]
  LIFO order verified

--- LinkedStack ---
  pop on empty: caught IndexError -> Stack underflow: cannot pop from an empty stack
  peek on empty: caught IndexError -> Stack is empty: nothing to peek
  push A: LinkedStack (bottom -> top): ['A']  [size=1]
  push B: LinkedStack (bottom -> top): ['A', 'B']  [size=2]
  push C: LinkedStack (bottom -> top): ['A', 'B', 'C']  [size=3]
  after pop (C) and peek (B): LinkedStack (bottom -> top): ['A', 'B']  [size=2]
  LIFO order verified

--- ArrayStack overflow ---
  push on full: caught OverflowError -> Stack overflow: cannot push onto a full stack

--- ArrayQueue ---
  dequeue on empty: caught IndexError -> Queue underflow: cannot dequeue from an empty queue
  peek_front on empty: caught IndexError -> Queue is empty: nothing to peek
  enqueue A: ArrayQueue (front -> rear): ['A']  [size=1/5, front index=0, raw array=['A', None, None, None, None]]
  enqueue B: ArrayQueue (front -> rear): ['A', 'B']  [size=2/5, front index=0, raw array=['A', 'B', None, None, None]]
  enqueue C: ArrayQueue (front -> rear): ['A', 'B', 'C']  [size=3/5, front index=0, raw array=['A', 'B', 'C', None, None]]
  FIFO order verified

--- LinkedQueue ---
  dequeue on empty: caught IndexError -> Queue underflow: cannot dequeue from an empty queue
  peek_front on empty: caught IndexError -> Queue is empty: nothing to peek
  enqueue A: LinkedQueue (front -> rear): ['A']  [size=1]
  enqueue B: LinkedQueue (front -> rear): ['A', 'B']  [size=2]
  enqueue C: LinkedQueue (front -> rear): ['A', 'B', 'C']  [size=3]
  FIFO order verified

--- ArrayQueue circular wrap-around (capacity 4) ---
  full: ArrayQueue (front -> rear): [1, 2, 3, 4]  [size=4/4, front index=0, raw array=[1, 2, 3, 4]]
  enqueue on full: caught OverflowError -> Queue overflow: cannot enqueue into a full queue
  after 2 dequeues: ArrayQueue (front -> rear): [3, 4]  [size=2/4, front index=2, raw array=[None, None, 3, 4]]
  after enqueue 5, 6 (wrapped past the end): ArrayQueue (front -> rear): [3, 4, 5, 6]  [size=4/4, front index=2, raw array=[5, 6, 3, 4]]
  order after wrap-around verified: [3, 4, 5, 6]

--- LinkedQueue rear reset when emptied ---
  front and rear both None after emptying; later enqueue works

--- Balanced parentheses ---
  '([]{})' -> balanced
  '(]' -> NOT balanced
  '((' -> NOT balanced
  '())' -> NOT balanced
  '{[()]}' -> balanced
  '' -> balanced
  'a(b[c]d)e' -> balanced

--- Print queue simulation ---
  Submitted job J1 (5 pages)
  Submitted job J2 (2 pages)
  Submitted job J3 (10 pages)

  Printing in FIFO order:
  #1: printing job J1 (5 pages) - waited for 0 pages ahead of it
  #2: printing job J2 (2 pages) - waited for 5 pages ahead of it
  #3: printing job J3 (10 pages) - waited for 7 pages ahead of it

  Total pages printed: 17

All tests passed.
```

## 2. Menu program error handling (`python main.py`)

ArrayStack with capacity 2: push x, push y, push z (overflow), pop, pop, pop (underflow).

```

===== Stacks and Queues Lab =====
1) ArrayStack
2) LinkedStack
3) ArrayQueue (circular)
4) LinkedQueue
5) Application: balanced parentheses (stack)
6) Application: print queue simulation (queue)
0) Exit
Choose: Capacity (positive integer): 
=== ArrayStack ===

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   Value to push:   Pushed.
  State -> ArrayStack (bottom -> top): ['x']  [size=1/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   Value to push:   Pushed.
  State -> ArrayStack (bottom -> top): ['x', 'y']  [size=2/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   Value to push:   ERROR: Stack overflow: cannot push onto a full stack
  State -> ArrayStack (bottom -> top): ['x', 'y']  [size=2/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   Popped: y
  State -> ArrayStack (bottom -> top): ['x']  [size=1/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   Popped: x
  State -> ArrayStack (bottom -> top): []  [size=0/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose:   ERROR: Stack underflow: cannot pop from an empty stack
  State -> ArrayStack (bottom -> top): []  [size=0/2]

1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back
Choose: 
===== Stacks and Queues Lab =====
1) ArrayStack
2) LinkedStack
3) ArrayQueue (circular)
4) LinkedQueue
5) Application: balanced parentheses (stack)
6) Application: print queue simulation (queue)
0) Exit
Choose: Goodbye!
```
