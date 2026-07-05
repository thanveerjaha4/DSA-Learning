# Find Maximum and Minimum Element

**Platform:** GeeksforGeeks

**Problem:** Find Minimum and Maximum Element in an Array

---

## Problem

Given an array of integers, find the minimum and maximum elements present in the array.

---

## Example

**Input:**

```text
arr = [4, 2, 8, 1, 9, 5]
```

**Output:**

```text
Minimum = 1
Maximum = 9
```

**Explanation:**

- The smallest element in the array is `1`.
- The largest element in the array is `9`.

---

## Approach 1: Brute Force

Compare every element with all the other elements to determine whether it is the smallest or largest.

This approach works but performs many unnecessary comparisons, making it inefficient.

---

## Algorithm

1. For each element, compare it with every other element.
2. Check if it is the smallest and largest.
3. Print the minimum and maximum values.

---

## Python Code (Brute Force)

```python
class Solution:
    def getMinMax(self, arr):
        n = len(arr)

        for i in range(n):
            isMin = True
            isMax = True

            for j in range(n):
                if arr[j] < arr[i]:
                    isMin = False
                if arr[j] > arr[i]:
                    isMax = False

            if isMin:
                minimum = arr[i]
            if isMax:
                maximum = arr[i]

        return minimum, maximum
```

---

## Time Complexity

**O(n²)**

**Reason:** Every element is compared with every other element.

---

## Space Complexity

**O(1)**

---

## Approach 2: Optimized

Initialize both minimum and maximum with the first element.

Traverse the array only once.

- If the current element is smaller than the minimum, update the minimum.
- If the current element is larger than the maximum, update the maximum.

This finds both values in a single traversal.

---

## Algorithm

1. Initialize `minimum` and `maximum` with the first element.
2. Traverse the remaining elements.
3. Update `minimum` if a smaller element is found.
4. Update `maximum` if a larger element is found.
5. Return both values.

---

## Python Code (Optimized)

```python
class Solution:
    def getMinMax(self, arr):
        minimum = maximum = arr[0]

        for num in arr[1:]:
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num

        return minimum, maximum
```

---

## Time Complexity

**O(n)**

**Reason:** The array is traversed only once.

---

## Space Complexity

**O(1)**

**Reason:** Only two variables are used.

---

## Key Takeaway

- One traversal is enough to find both the minimum and maximum.
- Initializing both values with the first element avoids unnecessary comparisons.
- This is one of the most common array traversal techniques.

---

## What I Learned

- How to traverse an array once.
- How to keep track of the smallest and largest values.
- How to optimize a solution from **O(n²)** to **O(n)**.
