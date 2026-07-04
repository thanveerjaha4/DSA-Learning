# Reverse an Array

**Platform:** GeeksforGeeks (Basic Array Problem)

**Problem Number:** N/A

---

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

We use the Two Pointer technique.

- One pointer starts from the beginning.
- Another pointer starts from the end.
- Swap both elements.
- Move the pointers towards each other.
- Continue until they meet.

---

## Algorithm

1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Swap `arr[left]` and `arr[right]`.
3. Move `left` forward and `right` backward.
4. Repeat until `left >= right`.

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

---

## Space Complexity

O(1)

---

## Key Takeaway

Two pointers allow us to reverse an array efficiently without using extra space.
