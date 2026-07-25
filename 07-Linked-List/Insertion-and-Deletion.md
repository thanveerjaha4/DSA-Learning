# Insertion and Deletion in Linked List

Insertion and deletion are two important operations performed on a Linked List.

Unlike arrays, linked lists can insert and delete nodes by changing the connections between nodes.

The main idea is to update the `next` references correctly.

---

# Node Structure

A node contains:

```text
Data + Next
```

In Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

# Insertion in Linked List

A new node can be inserted in different positions:

1. At the beginning.
2. At the end.
3. At a specific position.

---

# 1. Insert at the Beginning

Suppose the linked list is:

```text
10 → 20 → 30 → None
```

We want to insert `5`.

Create a new node:

```python
new_node = ListNode(5)
```

Connect the new node to the current head:

```python
new_node.next = head
```

Update the head:

```python
head = new_node
```

The new linked list becomes:

```text
5 → 10 → 20 → 30 → None
```

---

## Python Code

```python
def insertAtBeginning(head, value):

    new_node = ListNode(value)

    new_node.next = head

    head = new_node

    return head
```

---

## Time Complexity

**O(1)**

Only a few pointer changes are required.

---

# 2. Insert at the End

Suppose the linked list is:

```text
10 → 20 → 30 → None
```

We want to insert `40`.

Create a new node:

```python
new_node = ListNode(40)
```

Traverse to the last node:

```text
10 → 20 → 30
             ↑
          Last Node
```

Connect the last node to the new node:

```text
10 → 20 → 30 → 40 → None
```

---

## Python Code

```python
def insertAtEnd(head, value):

    new_node = ListNode(value)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head
```

---

## Time Complexity

**O(n)**

We may need to traverse the entire linked list to reach the last node.

> If a `tail` pointer is maintained, insertion at the end can be **O(1)**.

---

# 3. Insert at a Specific Position

Suppose the linked list is:

```text
10 → 20 → 30 → None
```

We want to insert `15` between `10` and `20`.

Create a new node:

```python
new_node = ListNode(15)
```

Before insertion:

```text
10 → 20 → 30
```

Connect the new node to `20`:

```python
new_node.next = current.next
```

Connect `10` to the new node:

```python
current.next = new_node
```

After insertion:

```text
10 → 15 → 20 → 30 → None
```

---

## Python Code

```python
def insertAtPosition(head, value, position):

    new_node = ListNode(value)

    if position == 0:
        new_node.next = head
        return new_node

    current = head

    for _ in range(position - 1):

        if current is None:
            return head

        current = current.next

    if current is None:
        return head

    new_node.next = current.next

    current.next = new_node

    return head
```

---

## Time Complexity

**O(n)**

We may need to traverse the list to reach the required position.

---

# Deletion in Linked List

A node can be deleted from different positions:

1. Delete the first node.
2. Delete the last node.
3. Delete a node with a specific value.
4. Delete a node at a specific position.

---

# 1. Delete the First Node

Suppose:

```text
10 → 20 → 30 → None
```

We want to delete `10`.

Move the head to the next node:

```python
head = head.next
```

The linked list becomes:

```text
20 → 30 → None
```

---

## Python Code

```python
def deleteFirst(head):

    if head is None:
        return None

    return head.next
```

---

## Time Complexity

**O(1)**

Only the head reference needs to be changed.

---

# 2. Delete the Last Node

Suppose:

```text
10 → 20 → 30 → None
```

We want to delete `30`.

We need to reach the second-last node:

```text
10 → 20 → 30
      ↑
 Second Last
```

Then set:

```python
current.next = None
```

The linked list becomes:

```text
10 → 20 → None
```

---

## Python Code

```python
def deleteLast(head):

    if head is None:
        return None

    if head.next is None:
        return None

    current = head

    while current.next.next:
        current = current.next

    current.next = None

    return head
```

---

## Time Complexity

**O(n)**

We may need to traverse the entire linked list.

---

# 3. Delete a Node by Value

Suppose:

```text
10 → 20 → 30 → None
```

We want to delete:

```text
20
```

We need to find the node before `20`.

```text
10 → 20 → 30
 ↑     ↑
prev  current
```

Then change:

```python
prev.next = current.next
```

The linked list becomes:

```text
10 → 30 → None
```

---

## Python Code

```python
def deleteValue(head, value):

    if head is None:
        return None

    if head.val == value:
        return head.next

    current = head

    while current.next:

        if current.next.val == value:

            current.next = current.next.next

            return head

        current = current.next

    return head
```

---

## Time Complexity

**O(n)**

In the worst case, we need to search the entire linked list.

---

# 4. Delete a Node at a Specific Position

Suppose:

```text
10 → 20 → 30 → 40 → None
```

We want to delete the node at position `2`.

The node is:

```text
30
```

Before:

```text
10 → 20 → 30 → 40
      ↑     ↑
     prev current
```

Change:

```python
prev.next = current.next
```

After:

```text
10 → 20 → 40 → None
```

---

## Python Code

```python
def deleteAtPosition(head, position):

    if head is None:
        return None

    if position == 0:
        return head.next

    current = head

    for _ in range(position - 1):

        if current.next is None:
            return head

        current = current.next

    if current.next is not None:
        current.next = current.next.next

    return head
```

---

## Time Complexity

**O(n)**

We may need to traverse the linked list to reach the required position.

---

# Important Pointer Concept

The most important idea in Linked List insertion and deletion is changing the `next` reference.

For insertion:

```text
Before:

10 → 20

Insert 15

After:

10 → 15 → 20
```

We perform:

```python
new_node.next = current.next
current.next = new_node
```

For deletion:

```text
Before:

10 → 20 → 30

Delete 20

After:

10 → 30
```

We perform:

```python
current.next = current.next.next
```

---

# Dummy Node

A **Dummy Node** is an extra node placed before the actual head.

Example:

```text
Dummy → Head → Node → Node
```

It is useful when the head itself may be deleted or modified.

Example:

```python
dummy = ListNode(0)
dummy.next = head
```

Now:

```text
Dummy → 10 → 20 → 30 → None
```

Using a dummy node can make insertion and deletion logic simpler because every actual node has a previous node.

---

# Time Complexity

| Operation | Time Complexity |
|---|---|
| Insert at Beginning | O(1) |
| Insert at End | O(n) |
| Insert at Position | O(n) |
| Delete First Node | O(1) |
| Delete Last Node | O(n) |
| Delete by Value | O(n) |
| Delete at Position | O(n) |

> With a `tail` pointer, insertion at the end can be **O(1)**.

---

# Key Takeaway

Insertion and deletion in a Linked List are performed by changing the `next` references between nodes.

For insertion:

```text
new_node.next = current.next
current.next = new_node
```

For deletion:

```text
current.next = current.next.next
```

The most important thing is to make sure that the links between the remaining nodes are not lost.

A **Dummy Node** is also a useful technique when the head of the linked list may need to be modified.

---

# What I Learned

- How to insert a node at the beginning.
- How to insert a node at the end.
- How to insert a node at a specific position.
- How to delete the first node.
- How to delete the last node.
- How to delete a node by its value.
- How to delete a node at a specific position.
- How to update `next` references during insertion.
- How to update `next` references during deletion.
- How and why Dummy Nodes are used.
- The time complexity of Linked List insertion and deletion operations.
