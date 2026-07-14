# Merge Sorted Array

**Platform:** LeetCode

**Problem Number:** 88

---

## Problem

You are given two sorted arrays, `nums1` and `nums2`.

Merge `nums2` into `nums1` as one sorted array.

The final sorted array should be stored inside `nums1`.

---

## Example

**Input:**

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

**Output:**

```text
[1,2,2,3,5,6]
```

---

## Approach 1: Brute Force

Copy all elements of `nums2` into the empty positions of `nums1`.

Sort the combined array.

This works but sorting takes extra time.

---

## Algorithm

1. Copy all elements of `nums2` into `nums1`.
2. Sort `nums1`.
3. Return.

---

## Python Code (Brute Force)

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
```

---

## Time Complexity

**O((m+n) log(m+n))**

---

## Space Complexity

**O(1)**

---

## Approach 2: Optimized (Two Pointers)

Since both arrays are already sorted, compare elements from the **end**.

- `i` points to the last valid element of `nums1`.
- `j` points to the last element of `nums2`.
- `k` points to the last position of `nums1`.

Place the larger element at the end and move the corresponding pointer.

This avoids sorting again.

---

## Algorithm

1. Set `i = m-1`, `j = n-1`, `k = m+n-1`.
2. Compare `nums1[i]` and `nums2[j]`.
3. Place the larger element at `nums1[k]`.
4. Move the corresponding pointer.
5. Copy any remaining elements from `nums2`.

---

## Python Code (Optimized)

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Time Complexity

**O(m + n)**

---

## Space Complexity

**O(1)**

---

## Key Takeaway

When two arrays are already sorted, start merging from the **end**. This avoids shifting elements and gives an efficient in-place solution.

---

## What I Learned

- How to merge two sorted arrays without using extra space.
- How opposite-direction pointers work.
- Why comparing from the end is more efficient than sorting again.
