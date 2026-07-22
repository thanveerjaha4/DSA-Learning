# Search Insert Position

**Platform:** LeetCode

**Problem Number:** 35

---

## Problem

Given a sorted array of distinct integers `nums` and an integer `target`, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

### Example 1

**Input**

```text
nums = [1,3,5,6]
target = 5
```

**Output**

```text
2
```

**Explanation**

The target `5` already exists at index `2`.

---

### Example 2

**Input**

```text
nums = [1,3,5,6]
target = 2
```

**Output**

```text
1
```

**Explanation**

The target `2` should be inserted between `1` and `3`.

Therefore, the correct index is `1`.

---

### Example 3

**Input**

```text
nums = [1,3,5,6]
target = 7
```

**Output**

```text
4
```

**Explanation**

The target `7` is greater than all elements in the array.

Therefore, it should be inserted at the end of the array, which is index `4`.

---

# Approach 1: Brute Force (Linear Search)

Traverse the array from left to right.

For every element, check whether it is greater than or equal to the target.

If `nums[i] >= target`, return `i`.

If the target is greater than every element, return `len(nums)`.

---

## Algorithm

1. Traverse the array from left to right.
2. Check if `nums[i] >= target`.
3. If true, return `i`.
4. If the loop finishes, return `len(nums)`.

---

## Python Code (Brute Force)

```python
class Solution:
    def searchInsert(self, nums, target):

        for i in range(len(nums)):

            if nums[i] >= target:
                return i

        return len(nums)
```

---

## Time Complexity

**O(n)**

Reason:

In the worst case, we may have to traverse the entire array.

---

## Space Complexity

**O(1)**

No extra data structure is used.

---

# Approach 2: Optimized (Binary Search)

Since the array is **sorted**, we can use Binary Search.

We search for the position where the target exists or should be inserted.

There are three cases:

- If `nums[mid] == target`, return `mid`.
- If `nums[mid] < target`, search the right half.
- If `nums[mid] > target`, search the left half.

When the loop ends, `left` will contain the correct insertion position.

---

## Algorithm

1. Set `left = 0`.
2. Set `right = len(nums) - 1`.
3. Find the middle index.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`, move `left` to `mid + 1`.
6. If `nums[mid] > target`, move `right` to `mid - 1`.
7. Continue until `left > right`.
8. Return `left`.

---

## Python Code (Optimized)

```python
class Solution:
    def searchInsert(self, nums, target):

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

        return left
```

---

## Time Complexity

**O(log n)**

Reason:

Binary Search eliminates half of the search space after every comparison.

---

## Space Complexity

**O(1)**

Only `left`, `right`, and `mid` variables are used.

---

# Dry Run

### Input

```text
nums = [1,3,5,6]
target = 2
```

---

### Step 1

```text
left = 0
right = 3
```

Calculate:

```text
mid = 0 + (3 - 0) // 2
mid = 1
```

The middle element is:

```text
nums[mid] = 3
```

Since:

```text
3 > 2
```

The target should be on the left side.

Update:

```text
right = mid - 1
right = 0
```

---

### Step 2

```text
left = 0
right = 0
```

Calculate:

```text
mid = 0 + (0 - 0) // 2
mid = 0
```

The middle element is:

```text
nums[mid] = 1
```

Since:

```text
1 < 2
```

The target should be on the right side.

Update:

```text
left = mid + 1
left = 1
```

---

### Step 3

Now:

```text
left = 1
right = 0
```

The condition:

```text
left <= right
```

is false.

The loop ends.

Return:

```text
left = 1
```

Therefore, the target `2` should be inserted at index `1`.

---

# Key Takeaway

This problem is a variation of **Binary Search**.

We are not only searching for the target.

We also need to find the position where the target should be inserted if it does not exist.

The important idea is:

```text
If target is found:
    return mid

If target is not found:
    return left
```

At the end of Binary Search, `left` points to the correct insertion position.

---

# What I Learned

- How to find the insertion position using Binary Search.
- How to search for a target in a sorted array.
- How to return the target index when it exists.
- How to return the correct position when the target does not exist.
- Why the final value of `left` gives the insertion position.
- How Binary Search reduces the time complexity from **O(n)** to **O(log n)**.
- How to use the same Binary Search pattern for different problems.
