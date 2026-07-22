# Guess Number Higher or Lower

**Platform:** LeetCode

**Problem Number:** 374

---

## Problem

We are playing the **Guess Game**.

The number `pick` is randomly chosen from the range `1` to `n`.

We need to guess the picked number.

We can use the `guess(num)` API.

The API returns:

- `-1` if our guess is higher than the picked number.
- `1` if our guess is lower than the picked number.
- `0` if our guess is equal to the picked number.

Return the picked number.

---

## Example

### Example 1

**Input**

```text
n = 10
pick = 6
```

**Output**

```text
6
```

**Explanation**

The picked number is `6`.

---

### Example 2

**Input**

```text
n = 1
pick = 1
```

**Output**

```text
1
```

**Explanation**

The only possible number is `1`, so the picked number is `1`.

---

### Example 3

**Input**

```text
n = 2
pick = 1
```

**Output**

```text
1
```

**Explanation**

The picked number is `1`.

---

# Approach 1: Brute Force (Linear Search)

We can check every number starting from `1`.

For each number, call the `guess()` API.

If `guess(i) == 0`, we have found the picked number.

---

## Algorithm

1. Start from `1`.
2. Check each number one by one.
3. Call `guess(i)`.
4. If the result is `0`, return `i`.
5. Continue until the picked number is found.

---

## Python Code (Brute Force)

```python
class Solution:
    def guessNumber(self, n):

        for i in range(1, n + 1):

            if guess(i) == 0:
                return i
```

---

## Time Complexity

**O(n)**

Reason:

In the worst case, we may have to check every number from `1` to `n`.

---

## Space Complexity

**O(1)**

No extra data structure is used.

---

# Approach 2: Optimized (Binary Search)

The picked number lies somewhere between `1` and `n`.

Instead of checking every number, we can use **Binary Search**.

We maintain two boundaries:

```text
left = 1
right = n
```

Find the middle number:

```text
mid = left + (right - left) // 2
```

Then use the result of `guess(mid)`.

There are three cases:

- If `guess(mid) == 0`, we found the picked number.
- If `guess(mid) == -1`, our guess is too high, so search the left half.
- If `guess(mid) == 1`, our guess is too low, so search the right half.

---

## Algorithm

1. Set `left = 1`.
2. Set `right = n`.
3. Calculate `mid`.
4. Call `guess(mid)`.
5. If the result is `0`, return `mid`.
6. If the result is `-1`, move `right` to `mid - 1`.
7. If the result is `1`, move `left` to `mid + 1`.
8. Repeat until the picked number is found.

---

## Python Code (Optimized)

```python
class Solution:
    def guessNumber(self, n):

        left = 1
        right = n

        while left <= right:

            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1
```

---

## Time Complexity

**O(log n)**

Reason:

Binary Search eliminates half of the possible numbers after every guess.

---

## Space Complexity

**O(1)**

Only `left`, `right`, `mid`, and `result` variables are used.

---

# Dry Run

### Input

```text
n = 10
pick = 6
```

---

### Step 1

```text
left = 1
right = 10
```

Calculate:

```text
mid = 1 + (10 - 1) // 2
mid = 5
```

Our guess is:

```text
5
```

Since the picked number is `6`:

```text
guess(5) = 1
```

This means our guess is **lower** than the picked number.

So, search the right half.

Update:

```text
left = mid + 1
left = 6
```

---

### Step 2

```text
left = 6
right = 10
```

Calculate:

```text
mid = 6 + (10 - 6) // 2
mid = 8
```

Our guess is:

```text
8
```

Since the picked number is `6`:

```text
guess(8) = -1
```

This means our guess is **higher** than the picked number.

So, search the left half.

Update:

```text
right = mid - 1
right = 7
```

---

### Step 3

```text
left = 6
right = 7
```

Calculate:

```text
mid = 6 + (7 - 6) // 2
mid = 6
```

Our guess is:

```text
6
```

Since:

```text
guess(6) = 0
```

The picked number is found.

Return:

```text
6
```

---

# Key Takeaway

This problem demonstrates how **Binary Search can be applied to a search range**, even when we do not have an actual array.

The `guess()` API tells us which half of the search space to eliminate.

```text
guess(mid) == 0
→ Target found

guess(mid) == -1
→ Guess is too high
→ Search the left half

guess(mid) == 1
→ Guess is too low
→ Search the right half
```

Instead of checking all `n` numbers, Binary Search reduces the search space by half after every guess.

Therefore:

```text
Linear Search  → O(n)

Binary Search  → O(log n)
```

---

# What I Learned

- How to apply Binary Search to a numeric search range.
- How to use the `guess()` API.
- How to interpret the three possible API results.
- How to eliminate half of the search space after every guess.
- How Binary Search reduces the time complexity from **O(n)** to **O(log n)**.
- How to identify when a problem can be solved using Binary Search.
