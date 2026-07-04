# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers whose sum equals the target.

---

## Example

Input:

nums = [2, 7, 11, 15]

target = 9

Output:

[0, 1]

Explanation:

nums[0] + nums[1] = 2 + 7 = 9

---

## Approach (Brute Force)

The simplest way is to check every possible pair of numbers.

- Take the first number and add it with every number after it.
- If the sum equals the target, return their indices.
- If not, continue checking until the pair is found.

This method is easy to understand but becomes slow for large arrays because it checks many unnecessary pairs.

---

## Algorithm

1. Start with the first element.
2. Compare it with every remaining element.
3. If their sum equals the target, return both indices.
4. Otherwise, continue checking.
5. Repeat until the answer is found.

---

## Python Code

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

O(n²)

Reason:
Two nested loops are used to check every possible pair.

---

## Space Complexity

O(1)

Reason:
No extra data structure is used.

---

## Key Takeaway

This is the easiest approach to understand and is a good starting point.

However, it checks many pairs repeatedly, making it inefficient for large inputs.

In the next approach, we'll use a **Hash Map** to reduce the time complexity from **O(n²)** to **O(n)**.
