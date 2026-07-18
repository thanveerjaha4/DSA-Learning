# Fixed Size Window vs Variable Size Window

Sliding Window problems are mainly divided into two types:

1. Fixed Size Window
2. Variable Size Window

Understanding the difference helps you identify the correct approach for solving a problem.

---

# 1. Fixed Size Window

In a Fixed Size Window, the window length is already given and never changes.

We simply move the window one position at a time until we reach the end.

---

## Example

Find the maximum sum of every subarray of size **3**.

### Input

```text
Array = [2, 4, 6, 8, 10]

Window Size = 3
```

### Windows

```text
[2 4 6] 8 10

2 [4 6 8] 10

2 4 [6 8 10]
```

The window size is always **3**.

---

## How It Works

1. Calculate the first window.
2. Remove the leftmost element.
3. Add the next element.
4. Repeat until the end.

---

## When to Use Fixed Size Window?

Use this approach when:

- Window size **K** is given.
- We need to process every subarray or substring of the same length.

---

## Common Problems

- Maximum Average Subarray I (LC 643)
- Maximum Number of Vowels in a Substring (LC 1456)
- Maximum Sum Subarray of Size K

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

# 2. Variable Size Window

In a Variable Size Window, the window size is **not fixed**.

The window expands or shrinks depending on a condition.

---

## Example

Find the longest substring without repeating characters.

### Input

```text
s = "abcabcbb"
```

### Window Movement

```text
[a]

[a b]

[a b c]

Duplicate found (a)

Move left pointer

[b c a]

Continue...
```

The window size changes based on whether a duplicate character exists.

---

## How It Works

1. Expand the window by moving the right pointer.
2. Check whether the current window satisfies the condition.
3. If not, move the left pointer until the condition becomes valid.
4. Continue until the end.

---

## When to Use Variable Size Window?

Use this approach when:

- The window size is **not given**.
- We need the:
  - Longest substring
  - Shortest subarray
  - Maximum length
  - Minimum length
- A condition determines whether to expand or shrink the window.

---

## Common Problems

- Longest Substring Without Repeating Characters (LC 3)
- Permutation in String (LC 567)
- Minimum Size Subarray Sum (LC 209)
- Longest Repeating Character Replacement (LC 424)

---

## Time Complexity

**O(n)**

Reason: Every element enters and leaves the window at most once.

---

## Space Complexity

Usually:

**O(1)** or **O(k)**

Depends on whether a HashMap or HashSet is used.

---

# Difference Between Fixed and Variable Window

| Fixed Size Window | Variable Size Window |
|-------------------|----------------------|
| Window size is fixed | Window size changes |
| Window length is given | Window length is decided during execution |
| Easier to implement | Slightly more difficult |
| Mostly one loop | Uses left and right pointers |
| Used when K is given | Used when a condition is given |

---

# How to Identify the Correct Window?

### Use Fixed Size Window if:

- The problem gives **K**.
- Every window has the same length.
- Find maximum, minimum, sum, or average of size **K**.

---

### Use Variable Size Window if:

- No window size is given.
- Need the longest or shortest subarray/substring.
- A condition controls the window size.

---

# Summary

- **Fixed Size Window** is used when the window length is known in advance.
- **Variable Size Window** is used when the window grows or shrinks based on a condition.
- Both techniques help reduce the time complexity of many array and string problems from **O(n²)** to **O(n)**.
