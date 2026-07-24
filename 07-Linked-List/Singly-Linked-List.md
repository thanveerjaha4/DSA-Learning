# Singly Linked List

A **Singly Linked List** is a linear data structure where each node contains two parts:

1. **Data** – Stores the value.
2. **Next** – Stores a reference to the next node.

Each node points only to the next node in the sequence.

---

## Basic Structure

A singly linked list looks like:

```text
Head
 ↓
[10 | Next] → [20 | Next] → [30 | Next] → None
```

Here:

- `10` is the first node.
- `20` is the second node.
- `30` is the last node.
- `Head` points to the first node.
- `None` indicates the end of the linked list.

---

# Node Structure in Python

We can create a node using a class.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Here:

- `val` stores the value.
- `next` stores the reference to the next node.

---

# Creating Nodes

Create three nodes:

```python
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
```

Initially:

```text
10 → None

20 → None

30 → None
```

Now connect them:

```python
node1.next = node2
node2.next = node3
```

The linked list becomes:

```text
10 → 20 → 30 → None
```

Set the head:

```python
head = node1
```

Complete structure:

```text
Head
 ↓
10 → 20 → 30 → None
```

---

# Traversing a Singly Linked List

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
2. Store the current node.
3. Process the current node.
4. Move to the next node using `current.next`.
5. Continue until `current` becomes `None`.

---

# Searching in a Singly Linked List

To find a value, traverse the linked list.

```python
def search(head, target):

    current = head

    while current:

        if current.val == target:
            return True

        current = current.next

    return False
```

Example:

```text
Head
 ↓
10 → 20 → 30 → None
```

Search:

```text
target = 20
```

The function returns:

```text
True
```

---

# Accessing a Node

Unlike arrays, a singly linked list does not support direct index access.

In an array:

```python
arr[2]
```

takes:

```text
O(1)
```

But in a linked list, we must start from the head and move node by node.

```text
Head
 ↓
10 → 20 → 30
          ↑
       Index 2
```

Therefore, accessing a node takes:

```text
O(n)
```

---

# Reversing a Singly Linked List

A common operation is reversing the direction of all links.

Before:

```text
10 → 20 → 30 → None
```

After:

```text
None ← 10 ← 20 ← 30
```

The new head is `30`.

To reverse a linked list, we commonly use three pointers:

```text
prev
current
next
```

---

## Python Code

```python
def reverseList(head):

    prev = None
    current = head

    while current:

        next_node = current.next

        current.next = prev

        prev = current

        current = next_node

    return prev
```

---

## Time Complexity

**O(n)**

Every node is visited once.

---

## Space Complexity

**O(1)**

Only a few pointer variables are used.

---

# Advantages

- Dynamic size.
- Efficient insertion and deletion at the beginning.
- Does not require contiguous memory.
- Simple structure.
- Useful for implementing stacks and queues.

---

# Disadvantages

- No direct random access.
- Searching takes O(n).
- Extra memory is needed for the `next` reference.
- Cannot traverse backwards directly.

---

# Time Complexity

| Operation | Time Complexity |
|---|---|
| Access by Index | O(n) |
| Search | O(n) |
| Insert at Beginning | O(1) |
| Delete at Beginning | O(1) |
| Insert at End | O(n) |
| Delete at End | O(n) |
| Traverse | O(n) |
| Reverse | O(n) |

---

# Key Takeaway

A **Singly Linked List** is made up of nodes where each node points to the next node.

The basic structure is:

```text
Head → Node → Node → Node → None
```

Each node contains:

```text
Data + Next
```

The most important operations are:

- Traversal
- Searching
- Insertion
- Deletion
- Reversal

The most important pointer technique for reversing a linked list is:

```text
prev
current
next
```

---

# What I Learned

- How a Singly Linked List works.
- How to create nodes using Python.
- How to connect nodes using `next`.
- How the `head` points to the first node.
- How to traverse a linked list.
- How to search for an element.
- Why linked lists do not support direct index access.
- How to reverse a linked list using three pointers.
- The time and space complexity of common operations.
