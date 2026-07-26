# Reverse Linked List

**Platform:** LeetCode

**Problem Number:** 206

**Difficulty:** Easy

---

## Problem

Given the head of a singly linked list, reverse the linked list and return the reversed linked list.

---

## Example

### Example 1

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[5,4,3,2,1]
```

**Explanation**

The original linked list is:

```text
1 → 2 → 3 → 4 → 5 → None
```

After reversing:

```text
5 → 4 → 3 → 2 → 1 → None
```

---

### Example 2

**Input**

```text
head = [1,2]
```

**Output**

```text
[2,1]
```

**Explanation**

The original linked list is:

```text
1 → 2 → None
```

After reversing:

```text
2 → 1 → None
```

---

### Example 3

**Input**

```text
head = []
```

**Output**

```text
[]
```

**Explanation**

The linked list is empty, so the result is also an empty linked list.

---

# Approach 1: Brute Force (Using Extra Array)

We can first store all the values of the linked list in an array.

Then reverse the array and create a new linked list.

Example:

Original linked list:

```text
1 → 2 → 3 → None
```

Store the values:

```text
[1, 2, 3]
```

Reverse the array:

```text
[3, 2, 1]
```

Create the reversed linked list:

```text
3 → 2 → 1 → None
```

This approach is simple but uses extra space.

---

## Algorithm

1. Create an empty array called `values`.
2. Traverse the linked list.
3. Store each node's value in the array.
4. Reverse the array.
5. Create a new linked list using the reversed values.
6. Return the new head.

---

## Python Code (Brute Force)

```python
class Solution:
    def reverseList(self, head):

        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        values.reverse()

        dummy = ListNode(0)
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
```

---

## Time Complexity

**O(n)**

Reason:

We traverse the linked list once to store the values and once to create the new linked list.

---

## Space Complexity

**O(n)**

Reason:

We store all node values in an array and create new nodes.

---

# Approach 2: Optimized (Iterative Pointer Method)

Instead of creating a new linked list, we can reverse the existing linked list by changing the direction of the `next` pointers.

We use three pointers:

- `prev`
- `current`
- `next_node`

Initially:

```text
prev = None
current = head
```

For example:

```text
1 → 2 → 3 → None
↑
current
```

---

## Algorithm

1. Initialize `prev = None`.
2. Initialize `current = head`.
3. While `current` is not `None`:
   - Store the next node in `next_node`.
   - Reverse the current node's pointer.
   - Move `prev` to `current`.
   - Move `current` to `next_node`.
4. Return `prev`.

---

## Python Code (Optimized)

```python
class Solution:
    def reverseList(self, head):

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

Reason:

Every node is visited exactly once.

---

## Space Complexity

**O(1)**

Reason:

We only use three pointer variables:

```text
prev
current
next_node
```

No extra array or linked list is created.

---

# Dry Run

### Input

```text
1 → 2 → 3 → None
```

---

### Initial State

```text
prev = None
current = 1
```

Linked list:

```text
1 → 2 → 3 → None
↑
current
```

---

### Step 1

Save the next node:

```text
next_node = 2
```

Reverse the pointer:

```text
1 → None
```

Move the pointers:

```text
prev = 1
current = 2
```

Now:

```text
None ← 1    2 → 3 → None
       ↑    ↑
      prev current
```

---

### Step 2

Save the next node:

```text
next_node = 3
```

Reverse the pointer:

```text
2 → 1 → None
```

Move the pointers:

```text
prev = 2
current = 3
```

Now:

```text
None ← 1 ← 2    3 → None
            ↑    ↑
           prev current
```

---

### Step 3

Save the next node:

```text
next_node = None
```

Reverse the pointer:

```text
3 → 2 → 1 → None
```

Move the pointers:

```text
prev = 3
current = None
```

The loop stops because `current` is `None`.

Return:

```text
prev
```

Final result:

```text
3 → 2 → 1 → None
```

---

# Key Takeaway

The most important technique in this problem is reversing the direction of the `next` pointer of every node.

We use three pointers:

```text
prev
current
next_node
```

The main operations are:

```python
next_node = current.next
current.next = prev
prev = current
current = next_node
```

The order of these operations is very important.

We must save `current.next` before changing `current.next`. Otherwise, we may lose access to the remaining part of the linked list.

At the end, `prev` becomes the new head of the reversed linked list.

---

# What I Learned

- How to reverse a singly linked list.
- How to use `prev`, `current`, and `next_node` pointers.
- How to reverse a linked list in-place.
- Why we must save the next node before changing the current pointer.
- How pointer manipulation works in linked lists.
- How to reverse a linked list in O(n) time.
- How to reverse a linked list using O(1) extra space.
- The importance of the three-pointer technique in Linked List problems.
