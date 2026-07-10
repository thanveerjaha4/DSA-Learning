# Reverse String

**Platform:** LeetCode

**Problem Number:** 344

---

## Problem

Write a function that reverses a string.

The input string is given as an array of characters `s`.

You must modify the input array **in-place** with **O(1)** extra memory.

---

## Example

### Example 1

**Input**

```text
s = ["h","e","l","l","o"]
```

**Output**

```text
["o","l","l","e","h"]
```

---

### Example 2

**Input**

```text
s = ["H","a","n","n","a","h"]
```

**Output**

```text
["h","a","n","n","a","H"]
```

---

## Approach 1: Using an Extra Array

Create a new reversed array and copy it back.

This approach is simple but uses extra memory.

---

## Algorithm

1. Create a new array in reverse order.
2. Copy the reversed array back to the original array.

---

## Python Code (Brute Force)

```python
class Solution:
    def reverseString(self, s):
        temp = s[::-1]

        for i in range(len(s)):
            s[i] = temp[i]
```

---

## Time Complexity

**O(n)**

Reason: Every character is copied once.

---

## Space Complexity

**O(n)**

Reason: An extra array is created.

---

## Approach 2: Optimized (Two Pointers)

Use two pointers.

- One pointer starts from the beginning.
- Another pointer starts from the end.
- Swap both characters.
- Move both pointers toward the center.

---

## Algorithm

1. Initialize `left = 0` and `right = len(s)-1`.
2. Swap `s[left]` and `s[right]`.
3. Increment `left`.
4. Decrement `right`.
5. Continue until `left < right`.

---

## Python Code (Optimized)

```python
class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

---

## Time Complexity

**O(n)**

Reason: Each character is visited only once.

---

## Space Complexity

**O(1)**

Reason: No extra array is used.

---

## Key Takeaway

The Two Pointer technique allows us to reverse a string efficiently by swapping characters from both ends without using extra memory.

---

## What I Learned

- How to reverse a string in-place.
- How the Two Pointer technique works on strings.
- Why swapping elements is more space-efficient than creating a new array.
- How to solve in-place problems with **O(1)** extra space.
