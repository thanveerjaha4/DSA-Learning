# Binary Search Basics

Binary Search is an efficient searching algorithm used to find an element in a **sorted array**.

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves until the target element is found or the search space becomes empty.

This reduces the time complexity from **O(n)** to **O(log n)**.

---

## Why Do We Use Binary Search?

Suppose you have a sorted array:

```text
[2, 5, 8, 12, 16, 23, 38, 45, 56]
```

You want to find **23**.

### Linear Search

```text
2 → 5 → 8 → 12 → 16 → 23
```

You may have to check many elements.

Time Complexity:

```text
O(n)
```

---

### Binary Search

Find the middle element first.

```text
[2, 5, 8, 12, 16, 23, 38, 45, 56]
             ↑
           Mid = 16
```

Since **23 > 16**, ignore the left half.

Now search only:

```text
[23, 38, 45, 56]
```

Again find the middle.

```text
23 38 45 56
   ↑
 Mid = 38
```

Since **23 < 38**, search the left half.

```text
23
```

Target found.

Instead of searching every element, Binary Search keeps reducing the search space by half.

---

## Prerequisite

Binary Search works **only on sorted data**.

❌ Unsorted Array

```text
8 2 5 1 9
```

Binary Search will not work correctly.

✅ Sorted Array

```text
1 2 5 8 9
```

Binary Search works correctly.

---

## How Binary Search Works

Maintain two pointers:

```text
left = 0
right = n - 1
```

Repeat while:

```text
left <= right
```

Find the middle index:

```python
mid = left + (right - left) // 2
```

Compare:

- If `nums[mid] == target` → Found.
- If `nums[mid] < target` → Search the right half.
- If `nums[mid] > target` → Search the left half.

Continue until the target is found or the search space becomes empty.

---

## Why Use

```python
mid = left + (right - left) // 2
```

Instead of

```python
mid = (left + right) // 2
```

In some programming languages, `left + right` may cause **integer overflow** for very large values.

Using:

```python
left + (right - left) // 2
```

avoids this problem.

In Python, integer overflow is not an issue, but this formula is considered the standard interview practice.

---

## Example

Find **7**.

```text
Array:

1 3 5 7 9 11 13

left = 0

right = 6
```

### Step 1

```text
mid = 3

nums[mid] = 7
```

Target found.

---

Find **11**

### Step 1

```text
1 3 5 7 9 11 13
      ↑
     mid = 7
```

Target is greater.

Move:

```text
left = mid + 1
```

Now search:

```text
9 11 13
```

### Step 2

```text
9 11 13
   ↑
  mid = 11
```

Target found.

---

## When to Use Binary Search?

Use Binary Search when:

- The array is sorted.
- Searching for an element.
- Finding the first or last occurrence.
- Finding the insertion position.
- Searching in a monotonic (always increasing or decreasing) function.

---

## Advantages

- Much faster than Linear Search.
- Efficient for large sorted arrays.
- Reduces search space by half in every step.
- Widely used in coding interviews.

---

## Disadvantages

- Works only on sorted data.
- Slightly more difficult to understand than Linear Search.
- Sorting an unsorted array first may take extra time.

---

## Time Complexity

### Best Case

```text
O(1)
```

Target is found at the middle immediately.

---

### Average Case

```text
O(log n)
```

---

### Worst Case

```text
O(log n)
```

The search space is halved at every step.

---

## Space Complexity

### Iterative Binary Search

```text
O(1)
```

---

### Recursive Binary Search

```text
O(log n)
```

Due to the recursion call stack.

---

## Applications

Binary Search is commonly used in:

- Searching in sorted arrays
- Search Insert Position
- First Bad Version
- Guess Number Higher or Lower
- Finding Square Root
- Finding Peak Element
- Searching in Rotated Sorted Array
- Lower Bound and Upper Bound
- Binary Search on Answer

----

## Summary

Binary Search is one of the most important searching algorithms. It works only on **sorted data** and repeatedly divides the search space into two halves until the target is found. This makes it much faster than Linear Search, reducing the time complexity from **O(n)** to **O(log n)**.
