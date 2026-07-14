# Move Zeroes

**Platform:** LeetCode

**Problem Number:** 283

---

## Problem

Given an integer array `nums`, move all the `0`s to the end of the array while maintaining the relative order of the non-zero elements.

You must do this **in-place** without making a copy of the array.

---

## Example

**Input:**

```text
nums = [0,1,0,3,12]
```

**Output:**

```text
[1,3,12,0,0]
```

**Explanation:**

All non-zero elements remain in the same order, and all zeroes are moved to the end.

---

## Approach 1: Brute Force

Create a new array.

- Traverse the array and store all non-zero elements.
- Count the number of zeroes.
- Append the zeroes at the end.
- Copy the result back to the original array.

This approach is simple but uses extra memory.

---

## Algorithm

1. Create an empty list.
2. Traverse the array.
3. Store all non-zero elements.
4. Add the required number of zeroes at the end.
5. Copy the result back to the original array.

---

## Python Code (Brute Force)

```python
class Solution:
    def moveZeroes(self, nums):
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        while len(result) < len(nums):
            result.append(0)

        nums[:] = result
```

---

## Time Complexity

**O(n)**

Reason: The array is traversed once.

---

## Space Complexity

**O(n)**

Reason: An extra list is used.

---

## Approach 2: Optimized (Two Pointers)

Use two pointers.

- `i` points to the position where the next non-zero element should be placed.
- `j` traverses the array.
- Whenever a non-zero element is found, swap it with the element at `i`.
- Move `i` forward.

This keeps all non-zero elements at the beginning and pushes zeroes to the end.

---

## Algorithm

1. Initialize `i = 0`.
2. Traverse the array using `j`.
3. If `nums[j]` is not zero:
   - Swap `nums[i]` and `nums[j]`.
   - Increment `i`.
4. Continue until the end of the array.

---

## Python Code (Optimized)

```python
class Solution:
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

---

## Time Complexity

**O(n)**

Reason: The array is traversed only once.

---

## Space Complexity

**O(1)**

Reason: No extra data structure is used.

---

## Key Takeaway

The Fast & Slow Pointer technique allows us to move all non-zero elements to the front while maintaining their order, without using extra space.

---

## What I Learned

- How to solve problems in-place.
- How the Fast & Slow Pointer technique works.
- How swapping helps avoid using an extra array.
- Why this approach is more efficient than creating a new list.
