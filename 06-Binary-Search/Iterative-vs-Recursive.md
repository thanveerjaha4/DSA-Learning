# Iterative vs Recursive Binary Search

Binary Search can be implemented in two ways:

1. Iterative Binary Search
2. Recursive Binary Search

Both approaches follow the same logic but differ in how they repeatedly search the array.

---

# 1. Iterative Binary Search

In the iterative approach, we use a **while loop** to repeatedly divide the search space until the target is found or the search space becomes empty.

---

## How It Works

1. Set two pointers:
   - `left = 0`
   - `right = n - 1`
2. Find the middle element.
3. Compare it with the target.
4. If found, return the index.
5. Otherwise, move either the left or right pointer.
6. Repeat until `left > right`.

---

## Code

```python
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

---

## Advantages

- Faster than recursion because there are no function calls.
- Uses constant memory.
- Preferred in coding interviews.

---

## Disadvantages

- The loop may seem less intuitive for beginners.

---

## Time Complexity

```text
O(log n)
```

---

## Space Complexity

```text
O(1)
```

---

# 2. Recursive Binary Search

In the recursive approach, the function calls itself on either the left half or the right half of the array.

The search continues until the target is found or there are no elements left.

---

## How It Works

1. Find the middle element.
2. Compare it with the target.
3. If found, return the index.
4. Otherwise:
   - Search the left half recursively.
   - Or search the right half recursively.
5. Stop when `left > right`.

---

## Code

```python
def binarySearch(nums, left, right, target):

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, right, target)

    else:
        return binarySearch(nums, left, mid - 1, target)
```

Function Call:

```python
binarySearch(nums, 0, len(nums) - 1, target)
```

---

## Advantages

- Short and easy to understand.
- Closely matches the divide-and-conquer idea.

---

## Disadvantages

- Uses extra memory because of recursive function calls.
- May cause stack overflow for very deep recursion.

---

## Time Complexity

```text
O(log n)
```

---

## Space Complexity

```text
O(log n)
```

Reason:

Recursive function calls are stored on the call stack.

---

# Difference Between Iterative and Recursive Binary Search

| Iterative | Recursive |
|-----------|-----------|
| Uses a `while` loop | Uses function calls |
| Faster | Slightly slower due to function call overhead |
| Space Complexity: **O(1)** | Space Complexity: **O(log n)** |
| No recursion stack | Uses recursion stack |
| Preferred in interviews | Easier to understand conceptually |

---

# Which One Should You Use?

### Use Iterative Binary Search when:

- Solving coding interview questions.
- Writing efficient code.
- Memory usage is important.

---

### Use Recursive Binary Search when:

- Learning recursion.
- Solving divide-and-conquer problems.
- The recursive solution is easier to understand.

---

# Summary

Both iterative and recursive Binary Search divide the search space into halves and have a time complexity of **O(log n)**.

- **Iterative Binary Search** uses a loop, is more memory-efficient, and is generally preferred in interviews.
- **Recursive Binary Search** uses function calls, making the code shorter and closer to the divide-and-conquer concept, but it requires extra stack space.
