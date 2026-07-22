# First Bad Version

**Platform:** LeetCode

**Problem Number:** 278

---

## Problem

You are a product manager and you are currently working on a new product.

Unfortunately, the latest version of your product fails the quality check.

Since each version is developed based on the previous version, all versions after a bad version are also bad.

Suppose we have versions:

```text
1 2 3 4 5
```

If version `4` is the first bad version:

```text
1 → Good
2 → Good
3 → Good
4 → Bad
5 → Bad
```

We need to find the **first bad version**.

We can use the `isBadVersion(version)` API to check whether a version is bad.

---

## Example

### Example 1

**Input**

```text
n = 5
firstBad = 4
```

**Output**

```text
4
```

**Explanation**

The versions are:

```text
1 → Good
2 → Good
3 → Good
4 → Bad
5 → Bad
```

The first bad version is `4`.

---

### Example 2

**Input**

```text
n = 1
firstBad = 1
```

**Output**

```text
1
```

**Explanation**

The only version is bad, so the first bad version is `1`.

---

# Approach 1: Brute Force (Linear Search)

We can check every version starting from version `1`.

For each version, call `isBadVersion()`.

The first version for which `isBadVersion()` returns `True` is the first bad version.

---

## Algorithm

1. Start from version `1`.
2. Check each version one by one.
3. Call `isBadVersion(i)`.
4. If the result is `True`, return `i`.
5. Continue until the first bad version is found.

---

## Python Code (Brute Force)

```python
class Solution:
    def firstBadVersion(self, n):

        for i in range(1, n + 1):

            if isBadVersion(i):
                return i
```

---

## Time Complexity

**O(n)**

Reason:

In the worst case, we may need to check all `n` versions.

---

## Space Complexity

**O(1)**

No extra data structure is used.

---

# Approach 2: Optimized (Binary Search)

The versions follow a specific pattern:

```text
Good Good Good Bad Bad Bad
```

Once a version becomes bad, every version after it is also bad.

This means the array has a **monotonic pattern**, so we can use Binary Search.

We maintain two pointers:

```text
left = 1
right = n
```

Find the middle version:

```text
mid = left + (right - left) // 2
```

There are two cases:

- If `isBadVersion(mid)` is `True`, `mid` could be the first bad version, so search the left half.
- If `isBadVersion(mid)` is `False`, the first bad version must be after `mid`, so search the right half.

---

## Algorithm

1. Set `left = 1`.
2. Set `right = n`.
3. Find the middle version.
4. Check `isBadVersion(mid)`.
5. If `mid` is bad, move `right` to `mid`.
6. If `mid` is good, move `left` to `mid + 1`.
7. Continue until `left == right`.
8. Return `left`.

---

## Python Code (Optimized)

```python
class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid

            else:
                left = mid + 1

        return left
```

---

## Time Complexity

**O(log n)**

Reason:

Binary Search eliminates approximately half of the versions after every API call.

---

## Space Complexity

**O(1)**

Only `left`, `right`, and `mid` variables are used.

---

# Dry Run

### Input

```text
n = 5
firstBad = 4
```

The versions are:

```text
1 → Good
2 → Good
3 → Good
4 → Bad
5 → Bad
```

---

### Step 1

```text
left = 1
right = 5
```

Calculate:

```text
mid = 1 + (5 - 1) // 2
mid = 3
```

Check:

```text
isBadVersion(3)
```

Version `3` is good.

So:

```text
isBadVersion(3) = False
```

Therefore, the first bad version must be after version `3`.

Update:

```text
left = mid + 1
left = 4
```

---

### Step 2

Now:

```text
left = 4
right = 5
```

Calculate:

```text
mid = 4 + (5 - 4) // 2
mid = 4
```

Check:

```text
isBadVersion(4)
```

Version `4` is bad.

So:

```text
isBadVersion(4) = True
```

Version `4` could be the first bad version.

Therefore, keep `mid` as a possible answer.

Update:

```text
right = mid
right = 4
```

---

### Step 3

Now:

```text
left = 4
right = 4
```

The condition:

```text
left < right
```

is false.

The loop ends.

Return:

```text
left = 4
```

Therefore, the first bad version is:

```text
4
```

---

# Key Takeaway

This problem teaches the **First Bad Version** or **First True Binary Search** pattern.

The versions follow this pattern:

```text
False False False True True True
```

Where:

```text
False → Good Version
True  → Bad Version
```

We need to find the **first `True`**.

If `mid` is bad:

```text
right = mid
```

We keep `mid` because it could be the first bad version.

If `mid` is good:

```text
left = mid + 1
```

The first bad version must be after `mid`.

Therefore:

```text
Linear Search  → O(n)

Binary Search  → O(log n)
```

---

# What I Learned

- How to identify a **monotonic pattern** in a problem.
- How to apply Binary Search without using an array.
- How to find the **first bad version** efficiently.
- How to find the **first `True`** in a sequence of `False` and `True` values.
- Why we use `right = mid` when the middle version is bad.
- Why we use `left = mid + 1` when the middle version is good.
- How Binary Search reduces the time complexity from **O(n)** to **O(log n)**.
- How the **First True Binary Search** pattern can be applied to many other DSA problems.
