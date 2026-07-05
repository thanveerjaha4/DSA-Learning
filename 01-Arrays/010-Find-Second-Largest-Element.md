# Find Second Largest Element

**Platform:** GeeksforGeeks

**Problem:** Second Largest Element in an Array

---

## Problem

Given an array of integers, find the second largest distinct element.

If no second largest element exists, return `-1`.

---

## Example

**Input:**

```text
arr = [12, 35, 1, 10, 34, 1]
```

**Output:**

```text
34
```

**Example 2**

**Input:**

```text
arr = [10, 10, 10]
```

**Output:**

```text
-1
```

**Explanation:**

All elements are the same, so there is no second largest element.

---

## Approach 1: Brute Force

Sort the array in descending order.

Traverse the sorted array until a different element from the largest is found.

That element is the second largest.

---

## Algorithm

1. Sort the array.
2. Store the largest element.
3. Traverse the array from the end.
4. Return the first element different from the largest.
5. If no such element exists, return `-1`.

---

## Python Code (Brute Force)

```python
class Solution:
    def getSecondLargest(self, arr):
        arr.sort()

        largest = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] != largest:
                return arr[i]

        return -1
```

---

## Time Complexity

**O(n log n)**

Reason: Sorting the array.

---

## Space Complexity

**O(1)**

---

## Approach 2: Optimized

Keep track of the largest and second largest elements while traversing the array only once.

- If a larger element is found, update both largest and second largest.
- If an element is between the largest and second largest, update the second largest.

---

## Algorithm

1. Initialize `largest` and `secondLargest` to `-1`.
2. Traverse the array.
3. Update both values whenever necessary.
4. Return `secondLargest`.

---

## Python Code (Optimized)

```python
class Solution:
    def getSecondLargest(self, arr):
        largest = secondLargest = -1

        for num in arr:
            if num > largest:
                secondLargest = largest
                largest = num
            elif largest > num > secondLargest:
                secondLargest = num

        return secondLargest
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Takeaway

There is no need to sort the array.

Keeping track of the largest and second largest values in one traversal gives a more efficient solution.

---

## What I Learned

- How to find the second largest element in one pass.
- Why sorting is not always the best solution.
- How to update multiple variables while traversing an array.
