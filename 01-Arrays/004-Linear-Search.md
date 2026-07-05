# Linear Search

**Platform:** GeeksforGeeks

**Problem:** Linear Search

---

## Problem

Given an array and a target element, find the index of the target element. If the element is not found, return -1.

---

## Example

**Input:**

```text
arr = [10, 20, 30, 40, 50]
target = 30
```

**Output:**

```text
2
```

**Explanation:**

The element `30` is present at index `2`.

---

## Approach

Linear Search checks each element one by one from the beginning of the array.

- Start from the first element.
- Compare it with the target.
- If both are equal, return the index.
- Otherwise, move to the next element.
- If the entire array is checked and the target is not found, return `-1`.

This approach works for both **sorted** and **unsorted** arrays.

---

## Algorithm

1. Traverse the array from the first element.
2. Compare the current element with the target.
3. If they are equal, return the current index.
4. If the loop ends without finding the target, return `-1`.

---

## Python Code

```python
class Solution:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
```

---

## Optimized Python Code

```python
class Solution:
    def linearSearch(self, arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1
```

---

## Time Complexity

**O(n)**

**Reason:** In the worst case, we may have to check every element in the array.

---

## Space Complexity

**O(1)**

**Reason:** No extra memory is used.

---

## Key Takeaway

- Linear Search is the simplest searching algorithm.
- It works on both sorted and unsorted arrays.
- It is easy to implement but becomes slow for large arrays.
- If the array is sorted, **Binary Search** is a much faster option.

---

## What I Learned

- How to traverse an array.
- How to compare each element with a target.
- When to use Linear Search.
- Why Binary Search is preferred for sorted arrays.
