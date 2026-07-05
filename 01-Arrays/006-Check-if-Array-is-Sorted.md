# Check if Array is Sorted

**Platform:** GeeksforGeeks

**Problem:** Check if an Array is Sorted

---

## Problem

Given an array of integers, check whether the array is sorted in non-decreasing order. Return `True` if it is sorted; otherwise, return `False`.

---

## Example

**Input:**

```text
arr = [1, 2, 3, 4, 5]
```

**Output:**

```text
True
```

**Example 2**

**Input:**

```text
arr = [1, 4, 3, 5]
```

**Output:**

```text
False
```

**Explanation:**

The element `4` is greater than `3`, so the array is not sorted.

---

## Approach 1: Brute Force

Compare every element with all the elements after it.

If any previous element is greater than a later element, the array is not sorted.

---

## Algorithm

1. Traverse the array.
2. Compare each element with every element after it.
3. If any element is greater than a later element, return `False`.
4. Otherwise, return `True`.

---

## Python Code (Brute Force)

```python
class Solution:
    def isSorted(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    return False

        return True
```

---

## Time Complexity

**O(n²)**

---

## Space Complexity

**O(1)**

---

## Approach 2: Optimized

A sorted array always satisfies:

Current Element ≤ Next Element

Traverse the array once and compare adjacent elements.

If any element is greater than the next one, return `False`.

Otherwise, return `True`.

---

## Algorithm

1. Traverse the array from index `0` to `n-2`.
2. Compare `arr[i]` and `arr[i+1]`.
3. If `arr[i] > arr[i+1]`, return `False`.
4. Return `True` after completing the loop.

---

## Python Code (Optimized)

```python
class Solution:
    def isSorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False

        return True
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Takeaway

Checking only adjacent elements is enough to determine whether an array is sorted.

---

## What I Learned

- How to compare adjacent elements.
- How to check if an array is sorted using one traversal.
- Why a single-pass solution is more efficient.
