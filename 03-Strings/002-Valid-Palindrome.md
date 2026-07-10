# Valid Palindrome

**Platform:** LeetCode

**Problem Number:** 125

---

## Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Example

### Example 1

**Input**

```text
s = "A man, a plan, a canal: Panama"
```

**Output**

```text
true
```

**Explanation**

After removing spaces, commas, and punctuation and converting to lowercase:

```text
amanaplanacanalpanama
```

It reads the same from both directions.

---

### Example 2

**Input**

```text
s = "race a car"
```

**Output**

```text
false
```

---

## Approach 1: Brute Force

Create a new string containing only lowercase letters and digits.

Reverse the new string and compare it with the original processed string.

---

## Algorithm

1. Traverse the string.
2. Keep only letters and digits.
3. Convert characters to lowercase.
4. Reverse the processed string.
5. Compare both strings.

---

## Python Code (Brute Force)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""

        for ch in s:
            if ch.isalnum():
                temp += ch.lower()

        return temp == temp[::-1]
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

Reason: A new string is created.

---

## Approach 2: Optimized (Two Pointers)

Use two pointers.

- One pointer starts from the beginning.
- Another pointer starts from the end.
- Skip characters that are not letters or digits.
- Compare lowercase characters.
- If any pair doesn't match, return `False`.
- Otherwise, continue until the pointers meet.

---

## Algorithm

1. Initialize `left = 0` and `right = len(s) - 1`.
2. Skip non-alphanumeric characters.
3. Compare lowercase characters.
4. If they are different, return `False`.
5. Move both pointers.
6. If the loop finishes, return `True`.

---

## Python Code (Optimized)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

## Time Complexity

**O(n)**

Reason: Each character is visited at most once.

---

## Space Complexity

**O(1)**

Reason: No extra string or data structure is used.

---

## Key Takeaway

The Two Pointer technique allows us to compare characters from both ends while ignoring spaces and special characters, making the solution efficient in both time and space.

---

## What I Learned

- How to ignore non-alphanumeric characters using `isalnum()`.
- How to compare characters without considering case using `lower()`.
- How to apply the Two Pointer technique to string problems.
- How to optimize a solution from **O(n)** extra space to **O(1)** extra space.
