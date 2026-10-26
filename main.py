"""Menu-driven program: choose an implementation, run any operation,
and see the structure's state after each operation.

Run:  python main.py
"""

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import run_parentheses_demo, run_print_queue_demo


def ask_capacity():
    while True:
        try:
            cap = int(input("Capacity (positive integer): "))
            if cap > 0:
                return cap
        except ValueError:
            pass
        print("  Please enter a positive whole number.")


def stack_menu(stack, name):
    print(f"\n=== {name} ===")
    while True:
        print("\n1) push  2) pop  3) peek  4) is_empty  5) is_full  6) show  0) back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                stack.push(input("  Value to push: "))
                print("  Pushed.")
            elif choice == "2":
                print(f"  Popped: {stack.pop()}")
            elif choice == "3":
                print(f"  Top: {stack.peek()}")
            elif choice == "4":
                print(f"  is_empty: {stack.is_empty()}")
            elif choice == "5":
                print(f"  is_full: {stack.is_full()}")
            elif choice == "6":
                pass
            elif choice == "0":
                return
            else:
                print("  Invalid choice.")
                continue
        except (IndexError, OverflowError) as err:
            print(f"  ERROR: {err}")
        print(f"  State -> {stack}")


def queue_menu(queue, name):
    print(f"\n=== {name} ===")
    while True:
        print("\n1) enqueue  2) dequeue  3) peek_front  4) is_empty  5) is_full  6) show  0) back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                queue.enqueue(input("  Value to enqueue: "))
                print("  Enqueued.")
            elif choice == "2":
                print(f"  Dequeued: {queue.dequeue()}")
            elif choice == "3":
                print(f"  Front: {queue.peek_front()}")
            elif choice == "4":
                print(f"  is_empty: {queue.is_empty()}")
            elif choice == "5":
                print(f"  is_full: {queue.is_full()}")
            elif choice == "6":
                pass
            elif choice == "0":
                return
            else:
                print("  Invalid choice.")
                continue
        except (IndexError, OverflowError) as err:
            print(f"  ERROR: {err}")
        print(f"  State -> {queue}")


def main():
    while True:
        print("\n===== Stacks and Queues Lab =====")
        print("1) ArrayStack")
        print("2) LinkedStack")
        print("3) ArrayQueue (circular)")
        print("4) LinkedQueue")
        print("5) Application: balanced parentheses (stack)")
        print("6) Application: print queue simulation (queue)")
        print("0) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            stack_menu(ArrayStack(ask_capacity()), "ArrayStack")
        elif choice == "2":
            stack_menu(LinkedStack(), "LinkedStack")
        elif choice == "3":
            queue_menu(ArrayQueue(ask_capacity()), "ArrayQueue")
        elif choice == "4":
            queue_menu(LinkedQueue(), "LinkedQueue")
        elif choice == "5":
            run_parentheses_demo()
        elif choice == "6":
            run_print_queue_demo()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
