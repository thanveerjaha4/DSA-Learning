# Time Complexity

## What is Time Complexity?

Time Complexity tells us how much time an algorithm takes to run as the input size increases.

In simple words, it measures how fast or slow a program is.

---

## Why is it Important?

- Helps compare different solutions.
- Makes programs efficient for large inputs.
- Reduces unnecessary operations.

---

## Example 1: O(1) - Constant Time

```cpp
int arr[] = {10, 20, 30};
cout << arr[1];
```

Accessing an element by its index always takes the same time.

So, the time complexity is **O(1)**.

---

## Example 2: O(n) - Linear Time

```cpp
for(int i = 0; i < n; i++) {
    cout << arr[i];
}
```

The loop runs `n` times.

So, the time complexity is **O(n)**.

---

## Key Points

- Fewer operations mean faster code.
- Avoid unnecessary loops.
- Try to write efficient solutions.

---

## Summary

Time Complexity tells us how long a program takes to execute.

Common time complexities:
- O(1) → Constant Time
- O(n) → Linear Time
- O(n²) → Quadratic Time
