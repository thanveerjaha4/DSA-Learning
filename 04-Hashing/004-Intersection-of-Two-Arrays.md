# Intersection of Two Arrays

**Platform:** LeetCode

**Problem Number:** 349

---

## Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must be **unique**, and you may return the result in any order.

---

## Example

### Example 1

**Input**

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

**Output**

```text
[2]
```

**Explanation**

The common element between both arrays is `2`.

---

### Example 2

**Input**

```text
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
```

**Output**

```text
[9,4]
```

or

```text
[4,9]
```

Both answers are correct because the order does not matter.

---

# Approach 1: Brute Force

Compare every element of the first array with every element of the second array.

If both elements are equal and not already present in the answer, add them.

---

## Algorithm

1. Create an empty list `result`.
2. Traverse `nums1`.
3. Traverse `nums2`.
4. If both elements are equal and not already in `result`, add it.
5. Return `result`.

---

## Python Code (Brute Force)

```python
class Solution:
    def intersection(self, nums1, nums2):
        result = []

        for i in nums1:
            for j in nums2:
                if i == j and i not in result:
                    result.append(i)

        return result
```

---

## Time Complexity

**O(n × m)**

Reason:

Every element of the first array is compared with every element of the second array.

---

## Space Complexity

**O(k)**

Where **k** is the number of unique common elements.

---

# Approach 2: Optimized (Using Hash Set)

A set stores only unique elements.

Convert both arrays into sets and find their common elements.

---

## Algorithm

1. Convert `nums1` into a set.
2. Convert `nums2` into a set.
3. Find the common elements using the `&` operator.
4. Convert the result back to a list.
5. Return the list.

---

## Python Code (Optimized)

```python
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
```

---

## Alternative Optimized Code

```python
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = []

        for num in set(nums2):
            if num in set1:
                result.append(num)

        return result
```

---

## Time Complexity

**O(n + m)**

Reason:

- Creating the two sets takes **O(n + m)**.
- Finding the intersection takes **O(min(n, m))** on average.

Overall complexity is **O(n + m)**.

---

## Space Complexity

**O(n + m)**

Reason:

Two sets are created to store the unique elements.

---

# Key Takeaway

A **Hash Set** automatically removes duplicate values.

Instead of comparing every pair of elements, we convert the arrays into sets and directly find the common unique elements.

This reduces the time complexity from **O(n × m)** to **O(n + m)**.

---

# What I Learned

- How to use a **Hash Set** in Python.
- How to remove duplicate elements using `set()`.
- How to find the intersection of two sets.
- Why set operations make array problems much faster.
