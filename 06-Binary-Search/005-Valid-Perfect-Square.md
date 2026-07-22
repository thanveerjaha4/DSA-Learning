# Valid Perfect Square

**Platform:** LeetCode

**Problem Number:** 367

---

## Problem

Given a positive integer `num`, return `true` if `num` is a perfect square, otherwise return `false`.

A **perfect square** is a number that can be written as the product of an integer with itself.

In other words:

```text
x * x = num
```

where `x` is an integer.

You **cannot use any built-in square root function**.

---

## Example

### Example 1

**Input**

```text
num = 16
```

**Output**

```text
true
```

**Explanation**

`16` is a perfect square because:

```text
4 * 4 = 16
```

Therefore, return `true`.

---

### Example 2

**Input**

```text
num = 14
```

**Output**

```text
false
```

**Explanation**

There is no integer `x` such that:

```text
x * x = 14
```

Therefore, `14` is not a perfect square.

---

### Example 3

**Input**

```text
num = 1
```

**Output**

```text
true
```

**Explanation**

`1` is a perfect square because:

```text
1 * 1 = 1
```

---

# Approach 1: Brute Force (Linear Search)

We can start from `1` and check every integer.

For each number `i`, calculate:

```text
i * i
```

If:

```text
i * i == num
```

then `num` is a perfect square.

If:

```text
i * i > num
```

then there is no need to continue because all larger values will have an even larger square.

---

## Algorithm

1. Start with `i = 1`.
2. Calculate `i * i`.
3. If `i * i == num`, return `True`.
4. If `i * i > num`, return `False`.
5. Otherwise, increase `i` by `1`.
6. Repeat until the answer is found.

---

## Python Code (Brute Force)

```python
class Solution:
    def isPerfectSquare(self, num):

        i = 1

        while i * i <= num:

            if i * i == num:
                return True

            i += 1

        return False
```

---

## Time Complexity

**O(√n)**

Reason:

We check numbers from `1` up to approximately `√n`.

---

## Space Complexity

**O(1)**

Only one variable `i` is used.

---

# Approach 2: Optimized (Binary Search)

We can use **Binary Search** to find whether there is an integer whose square is equal to `num`.

The possible value of the square root lies between:

```text
1 and num
```

We maintain two pointers:

```text
left = 1
right = num
```

Find the middle value:

```text
mid = left + (right - left) // 2
```

Calculate:

```text
square = mid * mid
```

There are three cases:

- If `square == num`, return `True`.
- If `square < num`, search the right half.
- If `square > num`, search the left half.

---

## Algorithm

1. Set `left = 1`.
2. Set `right = num`.
3. Find `mid`.
4. Calculate `mid * mid`.
5. If `mid * mid == num`, return `True`.
6. If `mid * mid < num`, move `left` to `mid + 1`.
7. If `mid * mid > num`, move `right` to `mid - 1`.
8. If the loop finishes, return `False`.

---

## Python Code (Optimized)

```python
class Solution:
    def isPerfectSquare(self, num):

        left = 1
        right = num

        while left <= right:

            mid = left + (right - left) // 2

            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1

            else:
                right = mid - 1

        return False
```

---

## Time Complexity

**O(log n)**

Reason:

Binary Search eliminates half of the possible values after every iteration.

---

## Space Complexity

**O(1)**

Only `left`, `right`, `mid`, and `square` variables are used.

---

# Dry Run

### Input

```text
num = 16
```

We need to find whether there is an integer `x` such that:

```text
x * x = 16
```

---

### Step 1

```text
left = 1
right = 16
```

Calculate:

```text
mid = 1 + (16 - 1) // 2
mid = 8
```

Calculate the square:

```text
8 * 8 = 64
```

Since:

```text
64 > 16
```

The middle value is too large.

Search the left half.

Update:

```text
right = mid - 1
right = 7
```

---

### Step 2

```text
left = 1
right = 7
```

Calculate:

```text
mid = 1 + (7 - 1) // 2
mid = 4
```

Calculate the square:

```text
4 * 4 = 16
```

Since:

```text
16 == 16
```

We found the perfect square.

Return:

```text
True
```

---

# Key Takeaway

This problem shows that **Binary Search can be applied to a numeric search space**, not just to an array.

We are searching for an integer `mid` such that:

```text
mid * mid == num
```

If:

```text
mid * mid < num
```

the answer must be on the right side.

If:

```text
mid * mid > num
```

the answer must be on the left side.

If:

```text
mid * mid == num
```

the number is a perfect square.

Therefore:

```text
Brute Force → O(√n)

Binary Search → O(log n)
```

Binary Search provides a faster solution.

---

# What I Learned

- How to check whether a number is a perfect square without using a square root function.
- How to apply Binary Search to a numeric range.
- How to compare `mid * mid` with the target number.
- How to decide whether to search the left or right half.
- How Binary Search reduces the time complexity from **O(√n)** to **O(log n)**.
- How Binary Search can be used on a search space instead of a sorted array.
- How to identify problems where a numeric range can be searched using Binary Search.
