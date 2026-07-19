# Maximum Number of Vowels in a Substring of Given Length

**Platform:** LeetCode

**Problem Number:** 1456

---

## Problem

Given a string `s` and an integer `k`, return the **maximum number of vowel letters** in any substring of length `k`.

The vowels are:

```text
a, e, i, o, u
```

---

## Example

### Example 1

**Input**

```text
s = "abciiidef"
k = 3
```

**Output**

```text
3
```

**Explanation**

Substrings of length 3:

```text
abc → 1 vowel

bci → 1 vowel

cii → 2 vowels

iii → 3 vowels

iid → 2 vowels

ide → 2 vowels

def → 1 vowel
```

Maximum vowels = **3**

---

### Example 2

**Input**

```text
s = "aeiou"
k = 2
```

**Output**

```text
2
```

---

### Example 3

**Input**

```text
s = "leetcode"
k = 3
```

**Output**

```text
2
```

---

# Approach 1: Brute Force

Check every substring of size `k`.

Count how many vowels it contains.

Keep track of the maximum count.

---

## Algorithm

1. Traverse every possible substring of size `k`.
2. Count vowels in the current substring.
3. Update the maximum count.
4. Return the maximum.

---

## Python Code (Brute Force)

```python
class Solution:
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0

        for i in range(len(s) - k + 1):
            count = 0

            for j in range(i, i + k):
                if s[j] in vowels:
                    count += 1

            max_count = max(max_count, count)

        return max_count
```

---

## Time Complexity

**O(n × k)**

Reason:

For every window, we count vowels again.

---

## Space Complexity

**O(1)**

---

# Approach 2: Optimized (Sliding Window)

Instead of counting vowels again for every window:

- Count vowels in the first window.
- As the window slides:
  - Remove the left character.
  - Add the right character.
- Update the vowel count.

---

## Algorithm

1. Count vowels in the first window.
2. Store it as `max_count`.
3. Slide the window:
   - If the outgoing character is a vowel, decrease the count.
   - If the incoming character is a vowel, increase the count.
4. Update the maximum count.
5. Return the maximum.

---

## Python Code (Sliding Window)

```python
class Solution:
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, len(s)):

            if s[i - k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count
```

---

## Time Complexity

**O(n)**

Reason:

Every character enters and leaves the window only once.

---

## Space Complexity

**O(1)**

Only a few variables and a set of vowels are used.

---

# Dry Run

### Input

```text
s = "abciiidef"

k = 3
```

### Step 1

First window:

```text
abc
```

Vowels =

```text
a
```

Count = 1

Max = 1

---

### Step 2

Slide

Remove

```text
a
```

Add

```text
i
```

Window:

```text
bci
```

Count = 1

---

### Step 3

Slide

Window:

```text
cii
```

Count = 2

Max = 2

---

### Step 4

Slide

Window:

```text
iii
```

Count = 3

Max = 3

---

Continue until the end.

Final Answer:

```text
3
```

---

# Key Takeaway

This is a **Fixed Size Sliding Window** problem.

Instead of counting vowels from scratch for every substring, maintain the current vowel count by:

- Removing the left character.
- Adding the right character.

This reduces the time complexity from **O(n × k)** to **O(n)**.

---

# What I Learned

- How to maintain a running count in a Sliding Window.
- How to efficiently update the count when the window moves.
- How Fixed Size Sliding Window avoids repeated calculations.
- How to solve substring problems in linear time using a moving window.
