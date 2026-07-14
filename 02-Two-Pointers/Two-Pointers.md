# Two Pointers

## What is the Two Pointer Technique?

The Two Pointer technique is an algorithm where we use two pointers (or indices) to traverse an array or string. Instead of using nested loops, we move the pointers based on certain conditions to solve problems more efficiently.

---

## Why Do We Use Two Pointers?

- Reduces unnecessary comparisons.
- Improves time complexity.
- Uses less extra memory.
- Makes many array and string problems easier to solve.

---

## Types of Two Pointers

### 1. Opposite Direction Pointers

One pointer starts from the beginning, and the other starts from the end.

Example:
- Reverse an Array
- Valid Palindrome
- Squares of a Sorted Array

---

### 2. Same Direction (Fast & Slow Pointers)

Both pointers start from the beginning.

- The fast pointer moves through the array.
- The slow pointer updates only when needed.

Example:
- Remove Element
- Move Zeroes
- Remove Duplicates from Sorted Array

---

## When to Use Two Pointers?

Use this technique when:

- Working with arrays or strings.
- Comparing elements from both ends.
- Removing duplicates.
- Rearranging elements.
- Merging sorted arrays.

---

## Advantages

- Faster than nested loops.
- Easy to implement.
- Reduces time complexity in many problems.

---

## Time Complexity

Most Two Pointer algorithms run in **O(n)** because each element is visited at most once.

---

## Space Complexity

Usually **O(1)** because only a few variables are used.

---

## Summary

The Two Pointer technique is one of the most useful DSA patterns. It helps solve many array and string problems efficiently by using two indices instead of multiple loops.
