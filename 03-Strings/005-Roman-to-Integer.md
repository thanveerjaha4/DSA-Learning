# Roman to Integer

**Platform:** LeetCode

**Problem Number:** 13

---

## Problem

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|------:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Given a Roman numeral, convert it to an integer.

---

## Example

### Example 1

**Input**

```text
s = "III"
```

**Output**

```text
3
```

---

### Example 2

**Input**

```text
s = "LVIII"
```

**Output**

```text
58
```

---

### Example 3

**Input**

```text
s = "MCMXCIV"
```

**Output**

```text
1994
```

---

## Approach

Store every Roman numeral and its value in a dictionary.

Traverse the string from left to right.

- If the current value is smaller than the next value, subtract it.
- Otherwise, add it.

---

## Algorithm

1. Create a dictionary for Roman symbols.
2. Traverse the string.
3. Compare the current symbol with the next symbol.
4. If the current value is smaller, subtract it.
5. Otherwise, add it.
6. Return the total.

---

## Python Code (Optimized)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
```

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

Reason: The dictionary contains only seven fixed entries.

---

## Key Takeaway

When a smaller Roman numeral appears before a larger one, it is subtracted instead of added.

Examples:

- IV = 4
- IX = 9
- XL = 40
- XC = 90
- CD = 400
- CM = 900

---

## What I Learned

- How to use a dictionary for quick lookups.
- How to compare adjacent characters.
- How Roman numeral subtraction works.
- How to solve mapping-based string problems efficiently.
