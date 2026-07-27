# Middle of the Linked List

**Platform:** LeetCode

**Problem Number:** 876

**Difficulty:** Easy

---

## Problem

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second middle node**.

---

## Example

### Example 1

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[3,4,5]
```

**Explanation**

The linked list is:

```text
1 → 2 → 3 → 4 → 5 → None
```

The middle node is:

```text
3
```

So we return:

```text
3 → 4 → 5 → None
```

---

### Example 2

**Input**

```text
head = [1,2,3,4,5,6]
```

**Output**

```text
[4,5,6]
```

**Explanation**

The linked list is:

```text
1 → 2 → 3 → 4 → 5 → 6 → None
```

There are two middle nodes:

```text
3 and 4
```

According to the problem, we return the **second middle node**.

So the answer is:

```text
4 → 5 → 6 → None
```

---

# Approach 1: Brute Force (Using Array)

We can first traverse the linked list and store all the nodes in an array.

Then we can find the middle node using the index:

```text
len(nodes) // 2
```

For example:

```text
1 → 2 → 3 → 4 → 5
```

Store the nodes:

```text
[1, 2, 3, 4, 5]
```

The length is:

```text
5
```

Middle index:

```text
5 // 2 = 2
```

So:

```text
nodes[2] = 3
```

Therefore, the middle node is `3`.

For an even-length list:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Middle index:

```text
6 // 2 = 3
```

So:

```text
nodes[3] = 4
```

This correctly returns the second middle node.

---

## Algorithm

1. Create an empty array called `nodes`.
2. Traverse the linked list.
3. Store every node in the array.
4. Find the middle index using `len(nodes) // 2`.
5. Return the node at the middle index.

---

## Python Code (Brute Force)

```python
class Solution:
    def middleNode(self, head):

        nodes = []

        current = head

        while current:
            nodes.append(current)
            current = current.next

        middle = len(nodes) // 2

        return nodes[middle]
```

---

## Time Complexity

**O(n)**

Reason:

We traverse all nodes once to store them in the array.

---

## Space Complexity

**O(n)**

Reason:

We store all the nodes in an array.

---

# Approach 2: Optimized (Slow and Fast Pointers)

We can solve this problem efficiently using the **Slow and Fast Pointer Technique**.

We use two pointers:

```text
slow
fast
```

The `slow` pointer moves **one step** at a time.

The `fast` pointer moves **two steps** at a time.

```text
slow → 1 step

fast → 2 steps
```

When `fast` reaches the end of the linked list, `slow` will be at the middle.

---

## Example

Consider:

```text
1 → 2 → 3 → 4 → 5 → None
```

Initially:

```text
slow = 1
fast = 1
```

---

### Step 1

Move `slow` one step:

```text
slow = 2
```

Move `fast` two steps:

```text
fast = 3
```

Now:

```text
1 → 2 → 3 → 4 → 5
     ↑    ↑
    slow fast
```

---

### Step 2

Move `slow` one step:

```text
slow = 3
```

Move `fast` two steps:

```text
fast = 5
```

Now:

```text
1 → 2 → 3 → 4 → 5
          ↑       ↑
         slow    fast
```

---

### Step 3

Move `slow` one step:

```text
slow = 4
```

Move `fast` two steps:

```text
fast = None
```

Now the loop stops.

But for the standard implementation:

```python
while fast and fast.next:
```

At this point, `slow` is the middle node.

For the list:

```text
1 → 2 → 3 → 4 → 5
```

The middle is:

```text
3
```

---

## Algorithm

1. Initialize `slow = head`.
2. Initialize `fast = head`.
3. While `fast` and `fast.next` exist:
   - Move `slow` one step.
   - Move `fast` two steps.
4. When the loop ends, `slow` points to the middle node.
5. Return `slow`.

---

## Python Code (Optimized)

```python
class Solution:
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        return slow
```

---

## Time Complexity

**O(n)**

Reason:

The `fast` pointer moves through the linked list, and every node is visited at most once.

---

## Space Complexity

**O(1)**

Reason:

We only use two pointer variables:

```text
slow
fast
```

No extra array is used.

---

# Dry Run

### Input

```text
1 → 2 → 3 → 4 → 5 → None
```

---

### Initial State

```text
slow = 1
fast = 1
```

---

### Step 1

Move `slow` one step:

```text
slow = 2
```

Move `fast` two steps:

```text
fast = 3
```

State:

```text
1 → 2 → 3 → 4 → 5
     ↑    ↑
    slow fast
```

---

### Step 2

Move `slow` one step:

```text
slow = 3
```

Move `fast` two steps:

```text
fast = 5
```

State:

```text
1 → 2 → 3 → 4 → 5
          ↑       ↑
         slow    fast
```

---

### Step 3

Move `slow` one step:

```text
slow = 4
```

Move `fast` two steps:

```text
fast = None
```

The loop stops when `fast` becomes `None`.

The middle node is:

```text
3
```

The returned linked list is:

```text
3 → 4 → 5 → None
```

---

# Dry Run for Even Length

### Input

```text
1 → 2 → 3 → 4 → 5 → 6 → None
```

Initially:

```text
slow = 1
fast = 1
```

---

### Step 1

```text
slow = 2
fast = 3
```

---

### Step 2

```text
slow = 3
fast = 5
```

---

### Step 3

```text
slow = 4
fast = None
```

The loop stops.

The returned node is:

```text
4
```

The result is:

```text
4 → 5 → 6 → None
```

This is the **second middle node**, as required by the problem.

---

# Key Takeaway

The most important technique in this problem is the **Slow and Fast Pointer Technique**.

We use:

```text
slow → moves 1 step

fast → moves 2 steps
```

When the `fast` pointer reaches the end of the linked list, the `slow` pointer will be at the middle.

The important code is:

```python
while fast and fast.next:

    slow = slow.next

    fast = fast.next.next
```

Finally:

```python
return slow
```

This technique allows us to find the middle of a linked list in:

```text
O(n) Time
O(1) Space
```

For an even-length linked list, this implementation automatically returns the **second middle node**.

---

# What I Learned

- How to find the middle node of a linked list.
- How to use the Slow and Fast Pointer technique.
- The `slow` pointer moves one step at a time.
- The `fast` pointer moves two steps at a time.
- How to handle both odd and even-length linked lists.
- How to return the second middle node for an even-length list.
- How to solve the problem using O(n) time.
- How to optimize the space complexity from O(n) to O(1).
- Why the Slow and Fast Pointer technique is important in Linked List problems.
