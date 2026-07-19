# Permutation in String

**Platform:** LeetCode

**Problem Number:** 567

---

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, otherwise return `false`.

A **permutation** is simply a rearrangement of all the characters of a string.

---

## Example

### Example 1

**Input**

```text
s1 = "ab"
s2 = "eidbaooo"
```

**Output**

```text
true
```

**Explanation**

The substring `"ba"` exists in `s2`.

`"ba"` is a permutation of `"ab"`.

---

### Example 2

**Input**

```text
s1 = "ab"
s2 = "eidboaoo"
```

**Output**

```text
false
```

**Explanation**

No substring of length 2 is a permutation of `"ab"`.

---

# Approach 1: Brute Force

Generate every substring of length equal to `len(s1)`.

Sort the substring and compare it with the sorted `s1`.

If they are equal, return `True`.

Otherwise continue.

---

## Algorithm

1. Sort `s1`.
2. Traverse every substring of length `len(s1)` in `s2`.
3. Sort the substring.
4. Compare both.
5. If equal, return `True`.
6. Otherwise return `False`.

---

## Python Code (Brute Force)

```python
class Solution:
    def checkInclusion(self, s1, s2):
        n = len(s1)

        target = sorted(s1)

        for i in range(len(s2) - n + 1):
            if sorted(s2[i:i+n]) == target:
                return True

        return False
```

---

## Time Complexity

**O((m - n + 1) × n log n)**

Reason:

Every window is sorted.

---

## Space Complexity

**O(n)**

---

# Approach 2: Optimized (Sliding Window + Frequency Count)

Instead of sorting every substring:

Store the frequency of characters.

Maintain another frequency count for the current window.

Whenever both frequency maps become equal, a permutation exists.

---

## Algorithm

1. If `len(s1) > len(s2)`, return `False`.
2. Count frequencies of `s1`.
3. Count frequencies of the first window in `s2`.
4. Compare both frequency maps.
5. Slide the window:
   - Remove the left character.
   - Add the right character.
6. Compare the frequency maps after every slide.
7. If equal, return `True`.
8. Otherwise return `False`.

---

## Python Code (Sliding Window)

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if s1_count == window:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            window[s2[right]] += 1

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if window == s1_count:
                return True

        return False
```

---

## Time Complexity

**O(n)**

Reason:

Each character enters and leaves the window once.

---

## Space Complexity

**O(1)**

Reason:

Only lowercase English letters are used, so the frequency maps have a bounded size.

---

# Dry Run

### Input

```text
s1 = "ab"

s2 = "eidbaooo"
```

Window Size =

```text
2
```

---

### First Window

```text
ei
```

Frequency

```text
e : 1

i : 1
```

Not equal.

---

### Slide

Window

```text
id
```

Not equal.

---

### Slide

Window

```text
db
```

Not equal.

---

### Slide

Window

```text
ba
```

Frequency

```text
a : 1

b : 1
```

Matches `s1`.

Return

```text
True
```

---

# Key Takeaway

This problem combines **Sliding Window** with **HashMap (Frequency Counting)**.

Instead of sorting every substring, maintain the frequency of the current window. As the window slides, update only the characters that leave and enter the window.

This reduces the complexity significantly and is a common interview pattern.

---

# What I Learned

- How to combine **Sliding Window** with **HashMap (Counter)**.
- How frequency counting helps compare two strings efficiently.
- Why updating only the changed characters is faster than sorting every window.
- How to solve permutation and anagram-related problems using Sliding Window.
