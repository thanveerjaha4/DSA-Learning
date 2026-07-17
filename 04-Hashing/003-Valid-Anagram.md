# Valid Anagram

**Platform:** LeetCode

**Problem Number:** 242

---

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, otherwise return `false`.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

---

## Example

### Example 1

**Input**

```text
s = "anagram"
t = "nagaram"
```

**Output**

```text
true
```

**Explanation**

Both strings contain the same characters with the same frequency.

---

### Example 2

**Input**

```text
s = "rat"
t = "car"
```

**Output**

```text
false
```

**Explanation**

The characters are different, so they are not anagrams.

---

# Approach 1: Sorting

If two strings are anagrams, then after sorting them, both strings will become identical.

---

## Algorithm

1. Check if both strings have the same length.
2. Sort both strings.
3. Compare the sorted strings.
4. If they are equal, return `True`.
5. Otherwise, return `False`.

---

## Python Code (Sorting)

```python
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
```

---

## Time Complexity

**O(n log n)**

Reason:

Sorting both strings takes **O(n log n)** time.

---

## Space Complexity

**O(n)**

Reason:

Extra space is used during sorting.

---

# Approach 2: Optimized (Using Hash Map / Dictionary)

Store the frequency of each character using a dictionary.

If both strings have the same frequency for every character, then they are anagrams.

---

## Algorithm

1. Check if both strings have the same length.
2. Create an empty dictionary.
3. Traverse the first string and count each character.
4. Traverse the second string and decrease the count.
5. If any count becomes negative or a character is missing, return `False`.
6. If all counts become zero, return `True`.

---

## Python Code (Optimized)

```python
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
```

---

## Time Complexity

**O(n)**

Reason:

We traverse both strings only once.

Dictionary operations take **O(1)** average time.

---

## Space Complexity

**O(n)**

Reason:

The dictionary stores the frequency of unique characters.

---

# Alternative Optimized Code (Using Counter)

Python provides a built-in `Counter` class that automatically counts character frequencies.

```python
from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

# Key Takeaway

An anagram means **both strings contain exactly the same characters with the same frequency**.

Instead of sorting the strings, we can count the frequency of each character using a dictionary. This reduces the time complexity from **O(n log n)** to **O(n)**.

---

# What I Learned

- How to use a **Dictionary (Hash Map)** for frequency counting.
- How to compare two strings efficiently.
- The difference between the sorting approach and the hashing approach.
- Why **frequency counting** is one of the most common hashing techniques in DSA.
