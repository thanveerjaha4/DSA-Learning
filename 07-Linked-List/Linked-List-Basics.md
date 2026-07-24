# Linked List Basics

A **Linked List** is a linear data structure made up of a sequence of nodes.

Unlike an array, the elements of a linked list are not stored in contiguous memory locations.

Each node contains:

1. **Data** – The value stored in the node.
2. **Next** – A reference to the next node.

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
- `None` represents the end of the linked list.

The first node is called the **Head**.

---

# Node Structure

In Python, we can create a node using a class.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Here:

- `val` stores the value of the node.
- `next` stores the reference to the next node.

---

# Creating a Node

We can create a node like this:

```python
node1 = ListNode(10)
```

The node looks like:

```text
10 → None
```

Create another node:

```python
node2 = ListNode(20)
```

Now connect the first node to the second node:

```python
node1.next = node2
```

The linked list becomes:

```text
10 → 20 → None
```

---

# Creating a Complete Linked List

```python
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

head = node1
```

The linked list is:

```text
head
 ↓
10 → 20 → 30 → None
```

The `head` points to the first node.

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

## Traversal Explanation

Initially:

```text
current = head
```

So:

```text
current → 10
```

Print:

```text
10
```

Move to the next node:

```python
current = current.next
```

Now:

```text
current → 20
```

Print:

```text
20
```

Move again:

```text
current → 30
```

Print:

```text
30
```

Move again:

```text
current → None
```

The loop stops.

---

# Traversal Algorithm

1. Start from the `head`.
2. Store the current node in a variable.
3. Process the current node.
4. Move to the next node using `current.next`.
5. Continue until `current` becomes `None`.

---

# Complete Example

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

head = node1

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

# Accessing a Specific Node

Unlike arrays, linked lists do not support direct access using an index.

For example, in an array:

```python
arr[2]
```

takes **O(1)** time.

But in a linked list, to reach the third node, we must start from the head and move through the previous nodes.

```text
Head
 ↓
10 → 20 → 30
          ↑
       Third Node
```

Therefore, accessing a node by position takes:

```text
O(n)
```

---

# Searching in a Linked List

To search for a value, traverse the linked list.

Example:

```python
def search(head, target):

    current = head

    while current:

        if current.val == target:
            return True

        current = current.next

    return False
```

If the target is found, return `True`.

Otherwise, return `False`.

---

# Inserting at the Beginning

Suppose we have:

```text
10 → 20 → 30 → None
```

We want to insert `5` at the beginning.

First create a new node:

```python
new_node = ListNode(5)
```

Connect it to the current head:

```python
new_node.next = head
```

Move the head to the new node:

```python
head = new_node
```

The linked list becomes:

```text
5 → 10 → 20 → 30 → None
```

Insertion at the beginning takes:

```text
O(1)
```

---

# Deleting the First Node

Suppose we have:

```text
10 → 20 → 30 → None
```

To delete the first node, move the head to the second node.

```python
head = head.next
```

The linked list becomes:

```text
20 → 30 → None
```

Deletion from the beginning takes:

```text
O(1)
```

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

# Linked List vs Array

| Feature | Array | Linked List |
|---|---|---|
| Memory | Contiguous | Non-contiguous |
| Access by Index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at Beginning | O(n) | O(1) |
| Delete at Beginning | O(n) | O(1) |
| Dynamic Size | Resizing required | Dynamic |
| Extra Memory | Less | More due to pointers |

---

# Time Complexity

| Operation | Time Complexity |
|---|---|
| Access by Index | O(n) |
| Search | O(n) |
| Insert at Beginning | O(1) |
| Delete at Beginning | O(1) |
| Traverse | O(n) |
| Reverse | O(n) |

> If a `tail` pointer is maintained, insertion at the end can be **O(1)**.

---

# Important Terms

### Node

An individual element of a linked list.

```text
[Data | Next]
```

---

### Head

The first node of the linked list.

```text
Head → 10 → 20 → 30 → None
```

---

### Tail

The last node of the linked list.

```text
10 → 20 → 30 → None
          ↑
         Tail
```

The `next` of the last node is usually `None`.

---

### Next

A reference that points to the next node.

```text
10 → 20
```

The `next` of node `10` points to node `20`.

---

### None

Indicates that there is no next node.

```text
10 → 20 → 30 → None
```

---

# Advantages

- Dynamic size.
- Efficient insertion and deletion at the beginning.
- Does not require contiguous memory.
- Useful for implementing stacks and queues.

---

# Disadvantages

- No direct random access.
- Searching takes O(n).
- Extra memory is required for storing references.
- Accessing elements is slower than arrays.

---

# Key Takeaway

A **Linked List** is a collection of nodes connected using references.

The basic structure is:

```text
Head → Node → Node → Node → None
```

Each node contains:

```text
Data + Next
```

The most important concepts to remember are:

- `Node`
- `Head`
- `Tail`
- `Next`
- `None`
- Traversal
- Insertion
- Deletion

Unlike arrays, linked lists do not provide direct access using an index.

However, they are useful when we need efficient insertion and deletion operations.

---

# What I Learned

- What a Linked List is.
- What a Node is.
- How to create a Node in Python.
- How nodes are connected using `next`.
- How the `head` points to the first node.
- How to traverse a linked list.
- How to search for an element.
- How to insert a node at the beginning.
- How to delete the first node.
- The difference between Singly, Doubly, and Circular Linked Lists.
- The difference between Arrays and Linked Lists.
- The time complexity of common Linked List operations.
