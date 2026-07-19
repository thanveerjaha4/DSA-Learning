# Maximum Average Subarray I

**Platform:** LeetCode

**Problem Number:** 643

---

## Problem

You are given an integer array `nums` consisting of `n` elements and an integer `k`.

Find the contiguous subarray of length `k` that has the maximum average and return that average.

Any answer with a calculation error less than `10⁻⁵` will be accepted.

---

## Example

### Example 1

**Input**

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

**Output**

```text
12.75
```

**Explanation**

Subarrays of size 4:

```text
[1,12,-5,-6]  Sum = 2   Average = 0.5

[12,-5,-6,50] Sum = 51  Average = 12.75

[-5,-6,50,3]  Sum = 42  Average = 10.5
```

The maximum average is **12.75**.

---

### Example 2

**Input**

```text
nums = [5]
k = 1
```

**Output**

```text
5.0
```

---

# Approach 1: Brute Force

Calculate the sum of every subarray of size `k`.

For each subarray:

- Find its sum.
- Calculate its average.
- Update the maximum average.

---

## Algorithm

1. Initialize `max_avg` to a very small value.
2. Traverse every possible subarray of size `k`.
3. Calculate the sum using a loop.
4. Compute the average.
5. Update the maximum average.
6. Return the maximum average.

---

## Python Code (Brute Force)

```python
class Solution:
    def findMaxAverage(self, nums, k):
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):
            total = 0

            for j in range(i, i + k):
                total += nums[j]

            avg = total / k
            max_avg = max(max_avg, avg)

        return max_avg
```

---

## Time Complexity

**O(n × k)**

Reason:

For every subarray, we calculate the sum again.

---

## Space Complexity

**O(1)**

---

# Approach 2: Optimized (Sliding Window)

Instead of recalculating the sum every time:

- Compute the first window sum.
- Remove the leftmost element.
- Add the next right element.

This updates the window sum in constant time.

---

## Algorithm

1. Calculate the sum of the first `k` elements.
2. Store it as the current maximum sum.
3. Slide the window:
   - Subtract the outgoing element.
   - Add the incoming element.
4. Update the maximum sum.
5. Return `max_sum / k`.

---

## Python Code (Sliding Window)

```python
class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
```

---

## Time Complexity

**O(n)**

Reason:

- First window sum takes **O(k)**.
- Sliding the window takes **O(n - k)**.

Overall complexity is **O(n)**.

---

## Space Complexity

**O(1)**

No extra space is used.

---

# Dry Run

### Input

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

### Step 1

First window:

```text
[1,12,-5,-6]

Sum = 2
Max Sum = 2
```

---

### Step 2

Slide the window

Remove **1**

Add **50**

```text
[12,-5,-6,50]

New Sum = 2 - 1 + 50 = 51

Max Sum = 51
```

---

### Step 3

Slide again

Remove **12**

Add **3**

```text
[-5,-6,50,3]

New Sum = 51 - 12 + 3 = 42

Max Sum = 51
```

---

### Final Answer

```text
Maximum Average = 51 / 4 = 12.75
```

---

# Key Takeaway

The Sliding Window technique avoids recalculating the sum for every subarray.

Instead of computing the sum from scratch, update the current window by removing one element and adding the next.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

# What I Learned

- How a Fixed Size Sliding Window works.
- How to efficiently update the window sum.
- Why Sliding Window is faster than the brute force approach.
- How to optimize subarray problems involving a fixed window size.
