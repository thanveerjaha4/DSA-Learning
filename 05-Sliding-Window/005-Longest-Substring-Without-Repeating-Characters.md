# Longest Substring Without Repeating Characters

**Platform:** LeetCode

**Problem Number:** 3

---

## Problem

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a continuous sequence of characters.

---

## Example

### Example 1

**Input**

```text
s = "abcabcbb"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is:

```text
"abc"
```

Length = **3**

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

The longest substring is:

```text
"b"
```

Length = **1**

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

The longest substring is:

```text
"wke"
```

Length = **3**

---

# Approach 1: Brute Force

Check every possible substring.

For each substring:

- Check whether all characters are unique.
- If yes, update the maximum length.

---

## Algorithm

1. Generate every substring.
2. Use a set to check uniqueness.
3. If a duplicate is found, stop checking that substring.
4. Update the maximum length.
5. Return the answer.

---

## Python Code (Brute Force)

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):

                if s[j] in seen:
                    break

                seen.add(s[j])
                ans = max(ans, j - i + 1)

        return ans
```

---

## Time Complexity

**O(n²)**

Reason:

We may examine many overlapping substrings.

---

## Space Complexity

**O(n)**

Used by the set.

---

# Approach 2: Optimized (Sliding Window + Hash Set)

Maintain a window with **unique characters only**.

If a duplicate character is found:

- Remove characters from the left side of the window until the duplicate is removed.

Keep updating the maximum window size.

---

## Algorithm

1. Create an empty set.
2. Initialize `left = 0`.
3. Traverse the string using `right`.
4. If the current character is already in the set:
   - Remove characters from the left until it is no longer present.
5. Add the current character.
6. Update the maximum window length.
7. Return the answer.

---

## Python Code (Sliding Window)

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()

        left = 0
        ans = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            ans = max(ans, right - left + 1)

        return ans
```

---

## Time Complexity

**O(n)**

Reason:

Each character enters and leaves the window at most once.

---

## Space Complexity

**O(n)**

Reason:

The set stores the unique characters in the current window.

---

# Dry Run

### Input

```text
s = "abcabcbb"
```

---

### Step 1

Window:

```text
a
```

Length = **1**

---

### Step 2

Window:

```text
ab
```

Length = **2**

---

### Step 3

Window:

```text
abc
```

Length = **3**

---

### Step 4

Next character:

```text
a
```

Duplicate found.

Remove characters from the left:

```text
Remove 'a'
```

Window becomes:

```text
bca
```

Length = **3**

---

### Step 5

Continue sliding until the end.

Maximum length remains:

```text
3
```

---

# Key Takeaway

This is a **Variable Size Sliding Window** problem.

Instead of restarting whenever a duplicate is found, we **shrink the window** by moving the left pointer until the window contains only unique characters again.

This ensures every character is processed at most twice, giving an efficient **O(n)** solution.

---

# What I Learned

- How to use a **Variable Size Sliding Window**.
- How to maintain a window of unique characters using a **Hash Set**.
- How to expand and shrink the window efficiently.
- Why each character is added and removed at most once.
- How to optimize a substring problem from **O(n²)** to **O(n)**.
