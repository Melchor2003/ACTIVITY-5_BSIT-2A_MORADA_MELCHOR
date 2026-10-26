# Analysis

**Why does the linked-list stack push at the head instead of the tail?**
In a singly linked list, each node only points forward, so removing the last node requires walking the whole list to find the second-to-last node, which makes `pop` O(n). At the head, both inserting and removing only change one reference (`top`), so `push`, `pop`, and `peek` are all O(1). Since a stack only ever touches one end, the head is the natural choice.

**Why must the array queue be circular?**
In a plain array queue, `dequeue` either moves `front` forward and permanently wastes the freed slots at the start, or shifts every element left, which costs O(n). Making the array circular with the modulo operator lets `front` and the rear position wrap back to index 0, so freed slots are reused and both `enqueue` and `dequeue` stay O(1) with no wasted space. A `size` counter is used to tell a full queue from an empty one.
