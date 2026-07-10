# Longest Common Prefix

**Platform:** LeetCode

**Problem Number:** 14

---

## Problem

Write a function to find the longest common prefix string among an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Example

### Example 1

**Input**

```text
strs = ["flower","flow","flight"]
```

**Output**

```text
"fl"
```

---

### Example 2

**Input**

```text
strs = ["dog","racecar","car"]
```

**Output**

```text
""
```

**Explanation**

There is no common prefix among the given strings.

---

## Approach 1: Brute Force (Character by Character)

Take the first string as the reference.

Compare each character of the first string with the corresponding character of every other string.

If a mismatch occurs, return the prefix found so far.

---

## Algorithm

1. Take the first string as the prefix.
2. Traverse each character of the prefix.
3. Compare it with the corresponding character in all other strings.
4. If a mismatch occurs, return the prefix up to that point.
5. If all characters match, return the complete prefix.

---

## Python Code (Brute Force)

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first = strs[0]

        for i in range(len(first)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != first[i]:
                    return first[:i]

        return first
```

---

## Time Complexity

**O(n × m)**

- `n` = Number of strings
- `m` = Length of the shortest string

---

## Space Complexity

**O(1)**

---

## Approach 2: Optimized (Prefix Reduction)

Assume the first string is the common prefix.

Compare it with every other string.

If the current string doesn't start with the prefix, remove the last character from the prefix.

Repeat until the prefix matches or becomes empty.

---

## Algorithm

1. Set the first string as the prefix.
2. Traverse the remaining strings.
3. While the current string doesn't start with the prefix:
   - Remove the last character from the prefix.
4. Return the final prefix.

---

## Python Code (Optimized)

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
```

---

## Time Complexity

**O(n × m)**

- `n` = Number of strings
- `m` = Length of the shortest string

---

## Space Complexity

**O(1)**

---

## Key Takeaway

Instead of comparing every possible prefix separately, we continuously reduce the current prefix until it matches all strings. This makes the solution simple, clean, and efficient.

---

## What I Learned

- How to compare multiple strings.
- How to find a common prefix among strings.
- How to use the `startswith()` method effectively.
- How prefix reduction helps solve string comparison problems efficiently.
