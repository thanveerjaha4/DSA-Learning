# Two Sum

**Platform:** LeetCode

**Problem Number:** 1

---

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

---

## Example

**Input:**

```text
nums = [2, 7, 11, 15]
target = 9
```

**Output:**

```text
[0, 1]
```

**Explanation:**

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Approach 1: Brute Force

The simplest way is to check every possible pair.

- Pick the first element.
- Compare it with every remaining element.
- If their sum equals the target, return their indices.
- Otherwise, continue checking.

This approach is easy to understand but becomes slow for larger arrays because it checks many unnecessary pairs.

---

## Algorithm

1. Traverse the array using the first loop.
2. For each element, traverse the remaining elements using the second loop.
3. Check if their sum equals the target.
4. If yes, return the indices.
5. Otherwise, continue until the answer is found.

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

Reason: Two nested loops are used.

---

## Space Complexity

**O(1)**

Reason: No extra data structure is used.

---

## Approach 2: Optimized (Hash Map)

Instead of checking every pair, store the numbers you've already seen in a dictionary.

For each number:

- Find the required value (`target - current number`).
- Check if it already exists in the dictionary.
- If yes, return both indices.
- Otherwise, store the current number and continue.

This avoids checking the same elements repeatedly.

---

## Algorithm

1. Create an empty dictionary.
2. Traverse the array.
3. Calculate the required value.
4. If it exists in the dictionary, return the answer.
5. Otherwise, store the current number and its index.
6. Continue until the pair is found.

---

## Python Code (Optimized)

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            required = target - num

            if required in seen:
                return [seen[required], i]

            seen[num] = i
```

---

## Time Complexity

**O(n)**

Reason: The array is traversed only once.

---

## Space Complexity

**O(n)**

Reason: The dictionary stores previously visited elements.

---

## Key Takeaway

- The brute force approach is easy to understand but slow.
- Using a **Hash Map (Dictionary)** allows us to find the required number in constant time.
- This improves the time complexity from **O(n²)** to **O(n)**.
