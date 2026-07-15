# Length of Last Word

**Platform:** LeetCode

**Problem Number:** 58

---

## Problem

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a sequence of non-space characters.

---

## Example

### Example 1

**Input**

```text
s = "Hello World"
```

**Output**

```text
5
```

---

### Example 2

**Input**

```text
s = "   fly me   to   the moon  "
```

**Output**

```text
4
```

---

### Example 3

**Input**

```text
s = "luffy is still joyboy"
```

**Output**

```text
6
```

---

## Approach 1: Using Built-in Functions

Remove extra spaces using `strip()`, split the string into words using `split()`, and return the length of the last word.

---

## Algorithm

1. Remove leading and trailing spaces.
2. Split the string into words.
3. Return the length of the last word.

---

## Python Code (Simple)

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

Reason: A list of words is created.

---

## Approach 2: Optimized

Traverse the string from the end.

- Ignore trailing spaces.
- Count characters until a space is found.

---

## Algorithm

1. Start from the last character.
2. Skip trailing spaces.
3. Count characters until a space appears.
4. Return the count.

---

## Python Code (Optimized)

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        length = 0

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

## Key Takeaway

Traversing the string from the end avoids creating extra arrays and gives an optimized solution.

---

## What I Learned

- How to traverse strings from right to left.
- How to ignore extra spaces.
- How to optimize a solution by avoiding extra memory.
