# Contains Duplicate II

**Platform:** LeetCode

**Problem Number:** 219

---

## Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` such that:

- `nums[i] == nums[j]`
- `abs(i - j) <= k`

Otherwise, return `false`.

---

## Example

### Example 1

**Input**

```text
nums = [1,2,3,1]
k = 3
```

**Output**

```text
true
```

**Explanation**

The duplicate value is `1`.

Indices:

```text
nums[0] = 1
nums[3] = 1
```

Distance:

```text
|3 - 0| = 3
```

Since `3 <= k`, return `true`.

---

### Example 2

**Input**

```text
nums = [1,0,1,1]
k = 1
```

**Output**

```text
true
```

**Explanation**

The last two `1`s are adjacent.

```text
|3 - 2| = 1
```

---

### Example 3

**Input**

```text
nums = [1,2,3,1,2,3]
k = 2
```

**Output**

```text
false
```

**Explanation**

Although duplicates exist, their index difference is greater than `2`.

---

# Approach 1: Brute Force

Compare every pair of elements.

If the values are equal and their index difference is less than or equal to `k`, return `True`.

---

## Algorithm

1. Traverse the array.
2. Compare each element with every remaining element.
3. If duplicate is found,
   - Check the index difference.
4. If difference ≤ `k`, return `True`.
5. Otherwise, return `False`.

---

## Python Code (Brute Force)

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False
```

---

## Time Complexity

**O(n²)**

Reason:

Every pair is compared.

---

## Space Complexity

**O(1)**

---

# Approach 2: Optimized (Hash Map)

Store each number with its latest index.

Whenever we see the same number again:

- Check the difference between the current index and the previous index.

If the difference is less than or equal to `k`, return `True`.

Otherwise, update the index.

---

## Algorithm

1. Create an empty dictionary.
2. Traverse the array.
3. If the number already exists,
   - Check the index difference.
4. If difference ≤ `k`, return `True`.
5. Update the latest index.
6. Return `False`.

---

## Python Code (Optimized)

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i - hashmap[nums[i]] <= k:
                    return True

            hashmap[nums[i]] = i

        return False
```

---

## Time Complexity

**O(n)**

Reason:

Each element is visited once.

Dictionary lookup takes **O(1)** on average.

---

## Space Complexity

**O(n)**

Reason:

The dictionary stores the latest index of each unique element.

---

# Sliding Window Approach (Using Hash Set)

Instead of storing all indices, maintain a window of size `k`.

As the window slides:

- Remove elements that move out of the window.
- Check whether the current element already exists in the window.

If yes, return `True`.

---

## Algorithm

1. Create an empty set.
2. Traverse the array.
3. If the current element exists in the set, return `True`.
4. Add the current element.
5. If the window size becomes greater than `k`, remove the leftmost element.
6. Continue until the end.

---

## Python Code (Sliding Window)

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False
```

---

## Time Complexity

**O(n)**

Reason:

Each element is added and removed at most once.

---

## Space Complexity

**O(k)**

Reason:

The sliding window stores at most `k` elements.

---

# Key Takeaway

There are two efficient ways to solve this problem:

- **Hash Map** stores the latest index of each number and checks the distance directly.
- **Sliding Window + Hash Set** keeps only the last `k` elements in memory, making it ideal when you only care about nearby duplicates.

Both approaches improve the time complexity from **O(n²)** to **O(n)**.

---

# What I Learned

- How to use a **Hash Map** to track the latest occurrence of an element.
- How to apply a **Sliding Window** with a **Hash Set**.
- The difference between checking all duplicates and checking only nearby duplicates.
- How combining **Hashing** and **Sliding Window** leads to efficient solutions.
