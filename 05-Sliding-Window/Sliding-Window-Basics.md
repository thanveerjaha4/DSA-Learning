# Sliding Window Basics

Sliding Window is a technique used to solve array and string problems efficiently.

Instead of checking every possible subarray or substring from scratch, we maintain a **window** that moves through the array or string. As the window slides, we remove the leftmost element and add the next element on the right.

This helps reduce the time complexity from **O(n²)** to **O(n)** in many problems.

---

## Why Do We Use Sliding Window?

Without the Sliding Window technique, we may calculate the same values repeatedly.

Sliding Window avoids this by reusing the previous computation.

This makes the solution much faster and more efficient.

---

## Example

Find the sum of every subarray of size **3**.

### Input

```text
Array = [2, 4, 6, 8, 10]

Window Size = 3
```

### Windows

```text
[2, 4, 6]  → Sum = 12

    [4, 6, 8]  → Sum = 18

        [6, 8, 10] → Sum = 24
```

Instead of calculating each sum from the beginning:

```
Window 1 = 2 + 4 + 6 = 12

Window 2 = 12 - 2 + 8 = 18

Window 3 = 18 - 4 + 10 = 24
```

We remove the outgoing element and add the incoming element.

---

## How Does Sliding Window Work?

1. Create the first window.
2. Process the current window.
3. Remove the leftmost element.
4. Add the next right element.
5. Repeat until the end.

---

## When Should We Use Sliding Window?

Use Sliding Window when:

- The problem involves **arrays** or **strings**.
- The problem asks about **subarrays** or **substrings**.
- The elements must be **contiguous**.
- We need to find:
  - Maximum
  - Minimum
  - Sum
  - Average
  - Longest
  - Shortest

---

## Types of Sliding Window

### 1. Fixed Size Window

The window size remains constant.

Example:

- Maximum Average Subarray I
- Maximum Number of Vowels in a Substring

---

### 2. Variable Size Window

The window size changes based on a condition.

Example:

- Longest Substring Without Repeating Characters
- Permutation in String

---

## Advantages

- Reduces unnecessary calculations.
- Faster than brute force.
- Easy to optimize many array and string problems.
- Frequently asked in coding interviews.

---

## Disadvantages

- Works only for contiguous elements.
- Not suitable for every problem.
- Variable-size windows can be slightly harder to implement.

---

## Time Complexity

Most Sliding Window problems are solved in:

**O(n)**

Reason: Each element enters and leaves the window at most once.

---

## Space Complexity

Usually:

**O(1)**

Some problems may require extra space (**O(k)** or **O(n)**), depending on whether a HashMap or HashSet is used.

---

## Applications

Sliding Window is commonly used in:

- Maximum Sum Subarray
- Maximum Average Subarray
- Longest Substring Without Repeating Characters
- Permutation in String
- Minimum Size Subarray Sum
- Maximum Number of Vowels
- Contains Duplicate II

---

## Summary

Sliding Window is one of the most important DSA techniques for solving array and string problems involving contiguous elements. By moving a window through the data instead of recalculating everything, many problems can be optimized from **O(n²)** to **O(n)**.
