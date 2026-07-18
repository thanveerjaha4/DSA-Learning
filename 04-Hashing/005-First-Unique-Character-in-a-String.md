# First Unique Character in a String

**Platform:** LeetCode

**Problem Number:** 387

---

## Problem

Given a string `s`, find the first non-repeating character in it and return its index.

If no unique character exists, return **-1**.

---

## Example

### Example 1

**Input**

```text
s = "leetcode"
```

**Output**

```text
0
```

**Explanation**

The first unique character is **'l'**, whose index is **0**.

---

### Example 2

**Input**

```text
s = "loveleetcode"
```

**Output**

```text
2
```

**Explanation**

The first unique character is **'v'**, whose index is **2**.

---

### Example 3

**Input**

```text
s = "aabb"
```

**Output**

```text
-1
```

**Explanation**

Every character appears more than once.

---

# Approach 1: Brute Force

For every character, count how many times it appears in the string.

If its frequency is **1**, return its index.

---

## Algorithm

1. Traverse the string.
2. Count the frequency of the current character.
3. If the frequency is 1, return its index.
4. If no unique character is found, return -1.

---

## Python Code (Brute Force)

```python
class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i

        return -1
```

---

## Time Complexity

**O(n²)**

**Reason:**

For every character, `count()` traverses the entire string.

---

## Space Complexity

**O(1)**

No extra space is used.

---

# Approach 2: Optimized (Using Hash Map)

Store the frequency of every character in a dictionary.

Then traverse the string again.

The first character whose frequency is **1** is the answer.

---

## Algorithm

1. Create an empty dictionary.
2. Count the frequency of every character.
3. Traverse the string again.
4. Return the index of the first character whose frequency is 1.
5. If none exists, return -1.

---

## Python Code (Optimized)

```python
class Solution:
    def firstUniqChar(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
```

---

## Time Complexity

**O(n)**

**Reason:**

- First traversal → Count frequencies.
- Second traversal → Find the first unique character.

Overall complexity is **O(n)**.

---

## Space Complexity

**O(n)**

**Reason:**

The dictionary stores the frequency of each unique character.

---

# Alternative Optimized Code (Using Counter)

Python provides the `Counter` class to count character frequencies easily.

```python
from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        freq = Counter(s)

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

# Key Takeaway

Frequency counting is one of the most useful hashing techniques.

Instead of counting each character repeatedly, store the frequency of every character once using a dictionary. Then find the first character whose frequency is **1**.

This reduces the time complexity from **O(n²)** to **O(n)**.

---

# What I Learned

- How to use a **Hash Map (Dictionary)** for frequency counting.
- How to solve string problems efficiently using hashing.
- Why traversing the string twice is still **O(n)**.
- How to use Python's **Counter** class for concise solutions.
