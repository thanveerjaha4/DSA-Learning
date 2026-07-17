# Contains Duplicate

**Platform:** LeetCode

**Problem Number:** 217

---

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Example

### Example 1

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
true
```

Explanation:

The number **1** appears twice.

---

### Example 2

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
false
```

Explanation:

All elements are unique.

---

### Example 3

**Input**

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

**Output**

```text
true
```

---

# Approach 1: Brute Force

Compare every element with every other element.

If two elements are the same, return `True`.

Otherwise, return `False`.

---

## Algorithm

1. Traverse the array.
2. Compare the current element with every remaining element.
3. If a duplicate is found, return `True`.
4. If no duplicate exists, return `False`.

---

## Python Code (Brute Force)

```python
class Solution:
    def containsDuplicate(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
```

---

## Time Complexity

**O(n²)**

Reason:

Every element is compared with every other element.

---

## Space Complexity

**O(1)**

No extra space is used.

---

# Approach 2: Optimized (Using Hash Set)

A **Hash Set** stores only unique elements.

As we traverse the array:

- If the element is already in the set, it is a duplicate.
- Otherwise, add it to the set.

---

## Algorithm

1. Create an empty set.
2. Traverse the array.
3. If the current element is already present in the set, return `True`.
4. Otherwise, add the element to the set.
5. If the loop finishes, return `False`.

---

## Python Code (Optimized)

```python
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

---

## Time Complexity

**O(n)**

Reason:

Each element is visited only once.

Checking and inserting into a set takes **O(1)** average time.

---

## Space Complexity

**O(n)**

Reason:

In the worst case, all elements are unique and are stored in the set.

---

# Key Takeaway

A **Hash Set** is useful when you only need to check whether an element has already been seen.

Instead of comparing every pair of elements, we store visited elements in a set and check for duplicates in constant time.

This reduces the time complexity from **O(n²)** to **O(n)**.

---

# What I Learned

- How to use a **Hash Set** in Python.
- How to check duplicates efficiently.
- The difference between the brute force and optimized approaches.
- Why hashing is one of the most important techniques in DSA.
