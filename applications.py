"""Application exercises (pair work).

a) balanced_parentheses: use a stack to check ()[]{} balance.
b) simulate_print_queue: FIFO print queue with job IDs and page counts.
"""

from linked_stack import LinkedStack
from linked_queue import LinkedQueue


def is_balanced(text):
    """Return True if every (, [, { in text is closed correctly and in order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)                      # remember the opener
        elif ch in ")]}":
            if stack.is_empty():                # closer with no opener
                return False
            if stack.pop() != pairs[ch]:        # wrong type of opener
                return False
    return stack.is_empty()                     # leftover openers => unbalanced


def simulate_print_queue(jobs):
    """Enqueue (job_id, pages) tuples, then print them in FIFO order.

    Returns a list of (wait_order, job_id, pages, pages_printed_before).
    """
    queue = LinkedQueue()
    for job in jobs:
        queue.enqueue(job)
        print(f"  Submitted job {job[0]} ({job[1]} pages)")

    print("\n  Printing in FIFO order:")
    report = []
    order = 1
    pages_before = 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print(f"  #{order}: printing job {job_id} ({pages} pages) "
              f"- waited for {pages_before} pages ahead of it")
        report.append((order, job_id, pages, pages_before))
        pages_before += pages
        order += 1
    print(f"\n  Total pages printed: {pages_before}")
    return report


def run_parentheses_demo():
    print("\n--- Balanced parentheses checker ---")
    while True:
        text = input("Enter a string (blank to go back): ")
        if text == "":
            break
        result = "BALANCED" if is_balanced(text) else "NOT balanced"
        print(f"  '{text}' -> {result}")


def run_print_queue_demo():
    print("\n--- Print queue simulation ---")
    jobs = []
    while True:
        job_id = input("Job ID (blank to finish): ").strip()
        if job_id == "":
            break
        try:
            pages = int(input("  Page count: "))
            if pages <= 0:
                raise ValueError
        except ValueError:
            print("  Page count must be a positive whole number. Job skipped.")
            continue
        jobs.append((job_id, pages))
    if not jobs:
        print("  No jobs submitted.")
        return
    print()
    simulate_print_queue(jobs)
