# Binary Search

**Platform:** LeetCode

**Problem Number:** 704

---

## Problem

Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array.

If `target` does not exist in the array, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

### Example 1

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output**

```text
4
```

**Explanation**

The target `9` exists at index `4`.

---

## Python Code

```python
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
```

---

## Time Complexity

**O(log n)**

---

## Space Complexity

**O(1)**

---

# Key Takeaway

Binary Search works on a **sorted array**.

It checks the middle element and eliminates half of the search space in every step.

This makes Binary Search much faster than Linear Search for large sorted arrays.

---

# What I Learned

- How Binary Search works.
- How to use `left`, `right`, and `mid`.
- How to eliminate half of the search space.
- Why Binary Search has **O(log n)** time complexity.
