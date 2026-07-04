# Space Complexity

## What is Space Complexity?

Space Complexity tells us how much memory an algorithm uses while solving a problem.

In simple words, it measures the extra memory required by a program.

---

## Why is it Important?

- Helps write memory-efficient programs.
- Uses less memory for large inputs.
- Makes programs run more efficiently.

---

## Example 1: O(1) - Constant Space

```cpp
int a = 10;
int b = 20;
int sum = a + b;
```

Only a few variables are used, so the space complexity is **O(1)**.

---

## Example 2: O(n) - Linear Space

```cpp
int arr[n];
```

As the value of `n` increases, the memory used also increases.

So, the space complexity is **O(n)**.

---

## Key Points

- Less memory usage is generally better.
- Extra arrays or data structures increase space complexity.
- Sometimes we use extra memory to make the program faster.

---

## Summary

Space Complexity tells us how much memory a program needs.

Common space complexities:
- O(1) → Constant Space
- O(n) → Linear Space
- O(n²) → Quadratic Space
