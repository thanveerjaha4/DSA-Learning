# Reverse an Array

## Problem

Given an array, reverse its elements.

---

## Example

Input:

arr = [1, 2, 3, 4, 5]

Output:

[5, 4, 3, 2, 1]

---

## Approach

We use two pointers:

- One pointer starts from the beginning.
- Another pointer starts from the end.
- Swap both elements.
- Move the left pointer forward and the right pointer backward.
- Repeat until both pointers meet.

---

## Algorithm

1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Swap `arr[left]` and `arr[right]`.
3. Increment `left` and decrement `right`.
4. Continue until `left >= right`.

---

## Python Code

```python
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
```

---

## Time Complexity

O(n)

The array is traversed only once.

---

## Space Complexity

O(1)

No extra memory is used.

---

## Key Takeaway

Two pointers help solve this problem efficiently without using an extra array.
