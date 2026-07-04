# Big-O Notation

## What is Big-O Notation?

Big-O Notation is used to describe the performance of an algorithm.

It shows how the running time or memory usage grows as the input size increases.

---

## Why is it Important?

- Helps compare different algorithms.
- Chooses the most efficient solution.
- Predicts how a program performs with large inputs.

---

## Common Big-O Notations

- O(1) → Constant Time
- O(log n) → Logarithmic Time
- O(n) → Linear Time
- O(n log n) → Efficient Sorting
- O(n²) → Quadratic Time

---

## Example

```cpp
for(int i = 0; i < n; i++) {
    cout << arr[i];
}
```

The loop runs `n` times.

So, the time complexity is **O(n)**.

---

## Key Points

- Smaller Big-O is usually better.
- It helps write faster and efficient programs.
- It is mainly used to compare algorithms.

---

## Summary

Big-O Notation helps us understand how an algorithm performs as the input size grows.

It is an important concept for writing efficient programs.
