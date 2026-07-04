# Remove Duplicates from Sorted Array

**Platform:** LeetCode

**Problem Number:** 26

---

## Problem

Given a sorted array, remove the duplicate elements in-place and return the number of unique elements.

---

## Example

Input:

nums = [1,1,2]

Output:

2

Updated array:

[1,2,_]

---

## Approach

Since the array is already sorted, duplicate elements appear next to each other.

We use two pointers:

- `i` keeps track of the last unique element.
- `j` scans the array.
- Whenever a new unique element is found, place it after the last unique element.

---

## Algorithm

1. If the array is empty, return 0.
2. Initialize `i = 0`.
3. Traverse the array using `j`.
4. If `nums[j]` is different from `nums[i]`, increment `i` and copy the value.
5. Return `i + 1`.

---

## Python Code

```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

---

## Time Complexity

O(n)

---

## Space Complexity

O(1)

---

## Key Takeaway

A sorted array makes it easy to identify duplicates, and the Two Pointer technique removes them without using extra memory.
