# Linked List

A **Linked List** is a linear data structure where elements are stored in separate objects called **nodes**.

Unlike arrays, linked list elements are not stored in contiguous memory locations.

Each node contains:

1. **Data** – The value stored in the node.
2. **Next** – A reference or pointer to the next node.

---

## Basic Structure

A singly linked list looks like:

```text
[10 | Next] → [20 | Next] → [30 | Next] → None
```

Here:

- `10` is the first node.
- `20` is the second node.
- `30` is the third node.
- `None` indicates the end of the linked list.

The first node is called the **Head**.

---

## Node Structure in Python

A node can be created using a class.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Here:

- `val` stores the data.
- `next` stores the reference to the next node.

---

## Creating a Linked List

```python
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3
```

The linked list becomes:

```text
10 → 20 → 30 → None
```

The head is:

```python
head = node1
```

---

# Traversing a Linked List

To visit every node, start from the `head` and follow the `next` reference.

```python
current = head

while current:
    print(current.val)
    current = current.next
```

Output:

```text
10
20
30
```

---

## Traversal Algorithm

1. Start from the `head`.
2. Store the current node in a variable.
3. Process the current node.
4. Move to the next node using `current.next`.
5. Continue until `current` becomes `None`.

---

# Types of Linked Lists

## 1. Singly Linked List

Each node contains:

```text
Data + Next
```

Example:

```text
10 → 20 → 30 → None
```

Each node points only to the next node.

---

## 2. Doubly Linked List

Each node contains:

```text
Previous + Data + Next
```

Example:

```text
None ← 10 ⇄ 20 ⇄ 30 → None
```

Each node has two references:

- `prev` → Previous node
- `next` → Next node

This allows traversal in both directions.

---

## 3. Circular Linked List

In a circular linked list, the last node points back to the first node.

Example:

```text
10 → 20 → 30
↑         ↓
└─────────┘
```

There is no `None` at the end.

---

# Linked List Operations

Common operations performed on linked lists are:

- Traversal
- Insertion
- Deletion
- Searching
- Reversal

---

## Insertion

A new node can be inserted:

1. At the beginning.
2. At the end.
3. At a specific position.

Example:

Before:

```text
10 → 20 → 30
```

Insert `5` at the beginning:

```text
5 → 10 → 20 → 30
```

---

## Deletion

A node can be deleted from:

1. The beginning.
2. The end.
3. A specific position.

Example:

Before:

```text
10 → 20 → 30
```

Delete `20`:

```text
10 → 30
```

---

# Linked List vs Array

| Feature | Array | Linked List |
|---|---|---|
| Memory | Contiguous | Non-contiguous |
| Access by Index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at Beginning | O(n) | O(1) |
| Delete at Beginning | O(n) | O(1) |
| Dynamic Size | Limited / Resizing | Dynamic |
| Extra Memory | Less | More due to pointers |

---

# Time Complexity

| Operation | Singly Linked List |
|---|---|
| Access by Index | O(n) |
| Search | O(n) |
| Insert at Beginning | O(1) |
| Insert at End | O(n) |
| Delete at Beginning | O(1) |
| Delete at End | O(n) |
| Reverse | O(n) |

> If we maintain a `tail` pointer, insertion at the end can be **O(1)**.

---

# Advantages

- Dynamic size.
- Efficient insertion and deletion at the beginning.
- No need for contiguous memory.
- Useful for implementing stacks and queues.

---

# Disadvantages

- No direct random access.
- Searching takes O(n).
- Extra memory is required for storing pointers.
- Traversal is slower compared to arrays for indexed access.

---

# Important Linked List Patterns

While solving Linked List problems, commonly used techniques include:

### 1. Two Pointers

Use two pointers such as:

```text
slow
fast
```

Useful for:

- Finding the middle of a linked list.
- Detecting cycles.

---

### 2. Fast and Slow Pointer

The slow pointer moves one step at a time.

The fast pointer moves two steps at a time.

```text
slow → 1 step
fast → 2 steps
```

This technique is commonly used to find the middle node and detect cycles.

---

### 3. Reversing a Linked List

Use three pointers:

```text
prev
current
next
```

Basic idea:

```text
prev ← current → next
```

Reverse the direction of the links one by one.

---

### 4. Dummy Node

A dummy node is an extra node placed before the actual head.

```text
Dummy → Head → Node → Node
```

It simplifies problems involving:

- Insertion.
- Deletion.
- Merging linked lists.

---

# Common Problems

The following problems will be solved in this section:

- Reverse Linked List — LeetCode 206
- Middle of the Linked List — LeetCode 876
- Merge Two Sorted Lists — LeetCode 21
- Linked List Cycle — LeetCode 141
- Remove Linked List Elements — LeetCode 203

---

# Key Takeaway

A **Linked List** is a linear data structure made up of nodes.

Each node stores data and a reference to another node.

The most important concept is:

```text
Head → Node → Node → Node → None
```

Unlike arrays, linked lists do not provide direct access using an index.

However, linked lists are useful when frequent insertion and deletion operations are required.

The most important techniques to learn are:

- Traversal
- Insertion
- Deletion
- Reversal
- Two Pointers
- Fast and Slow Pointers
- Dummy Nodes

---

# What I Learned

- What a Linked List is.
- What a Node contains.
- How the `head` points to the first node.
- How nodes are connected using `next`.
- How to traverse a linked list.
- The difference between Singly, Doubly, and Circular Linked Lists.
- How insertion and deletion work.
- The difference between Arrays and Linked Lists.
- The time complexity of common Linked List operations.
- How Two Pointer and Fast-Slow Pointer techniques are used in Linked List problems.
