# Remove Element

**Platform:** LeetCode

**Problem Number:** 27

---

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place and return the number of remaining elements.

The order of the elements may be changed. Return the number of elements that are not equal to `val`.

---

## Example

**Input:**

```text
nums = [3,2,2,3]
val = 3
```

**Output:**

```text
2
```

**Explanation:**

After removing all occurrences of `3`, the array becomes:

```text
[2,2]
```

The number of remaining elements is `2`.

---

## Approach 1: Brute Force

Create a new array.

Traverse the original array.

- If the current element is not equal to `val`, add it to the new array.
- Copy the new array back if required.

This approach is simple but uses extra memory.

---

## Algorithm

1. Create an empty array.
2. Traverse the given array.
3. Add elements that are not equal to `val`.
4. Return the length of the new array.

---

## Python Code (Brute Force)

```python
class Solution:
    def removeElement(self, nums, val):
        result = []

        for num in nums:
            if num != val:
                result.append(num)

        nums[:len(result)] = result
        return len(result)
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

## Approach 2: Optimized (Two Pointers)

Use two pointers.

- One pointer (`j`) traverses the array.
- Another pointer (`i`) keeps track of where the next valid element should be placed.
- Whenever an element is not equal to `val`, place it at index `i` and move `i` forward.

This removes the elements in-place without using extra memory.

---

## Algorithm

1. Initialize `i = 0`.
2. Traverse the array using `j`.
3. If `nums[j] != val`, copy it to `nums[i]`.
4. Increment `i`.
5. Return `i`.

---

## Python Code (Optimized)

```python
class Solution:
    def removeElement(self, nums, val):
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Takeaway

Using two pointers allows us to remove elements in-place without creating another array.

---

## What I Learned

- How the Fast & Slow Pointer technique works.
- How to modify an array in-place.
- How to reduce space complexity from **O(n)** to **O(1)**.
