# Two Sum

**Platform:** LeetCode

**Problem Number:** 1

---

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

## Example

### Example 1

**Input**

```text
nums = [2,7,11,15]
target = 9
```

**Output**

```text
[0,1]
```

**Explanation**

```
nums[0] + nums[1] = 2 + 7 = 9
```

---

### Example 2

**Input**

```text
nums = [3,2,4]
target = 6
```

**Output**

```text
[1,2]
```

---

### Example 3

**Input**

```text
nums = [3,3]
target = 6
```

**Output**

```text
[0,1]
```

---

# Approach 1: Brute Force

Compare every pair of elements.

If their sum equals the target, return their indices.

---

## Algorithm

1. Traverse the array using the first loop.
2. Traverse the remaining elements using the second loop.
3. Check if their sum equals the target.
4. If yes, return their indices.

---

## Python Code (Brute Force)

```python
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## Time Complexity

**O(n²)**

Reason:

Each element is compared with every other element.

---

## Space Complexity

**O(1)**

No extra space is used.

---

# Approach 2: Optimized (Using Hash Map)

Store each number and its index in a Hash Map.

For every number:

- Find its complement.

```text
complement = target - current_number
```

If the complement already exists in the Hash Map, we have found the answer.

Otherwise, store the current number and its index.

---

## Algorithm

1. Create an empty Hash Map.
2. Traverse the array.
3. Find the complement.
4. If the complement exists in the Hash Map, return both indices.
5. Otherwise, store the current number and its index.
6. Continue until the answer is found.

---

## Python Code (Optimized)

```python
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i
```

---

## Time Complexity

**O(n)**

Reason:

We traverse the array only once.

Hash Map lookup and insertion take **O(1)** average time.

---

## Space Complexity

**O(n)**

Reason:

The Hash Map stores the array elements and their indices.

---

# Key Takeaway

A **Hash Map** allows us to find the required complement in constant time.

Instead of checking every pair of numbers, we store previously seen numbers and their indices. This reduces the time complexity from **O(n²)** to **O(n)**.

---

# What I Learned

- How to use a **Hash Map (Dictionary)** in Python.
- How to solve the Two Sum problem in one pass.
- How the **complement technique** works.
- Why Hash Maps are useful for fast searching.
