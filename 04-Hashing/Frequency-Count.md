# Frequency Count

Frequency Count is a technique used to count how many times each element appears in an array or string.

Instead of checking the same element again and again, we store its count in a HashMap (Dictionary). This makes many problems faster and easier to solve.

---

## Why Do We Use Frequency Count?

Frequency Count helps us to:

- Count the occurrence of elements.
- Find duplicate elements.
- Find unique elements.
- Compare two strings.
- Solve many hashing problems efficiently.

---

## Example 1: Array

### Input

```text
arr = [1, 2, 2, 3, 1, 2]
```

### Frequency

```text
1 → 2 times
2 → 3 times
3 → 1 time
```

---

## Example 2: String

### Input

```text
s = "banana"
```

### Frequency

```text
b → 1
a → 3
n → 2
```

---

## Frequency Count Using Dictionary

```python
arr = [1, 2, 2, 3, 1, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
```

### Output

```text
{1: 2, 2: 3, 3: 1}
```

---

## Frequency Count Using Counter

Python provides a built-in class called `Counter` in the `collections` module.

```python
from collections import Counter

s = "banana"

freq = Counter(s)

print(freq)
```

### Output

```text
Counter({'a': 3, 'n': 2, 'b': 1})
```

---

## Real-Life Example

Suppose a teacher wants to know how many students selected each favorite fruit.

```text
Apple
Banana
Apple
Orange
Banana
Apple
```

Using Frequency Count:

```text
Apple  → 3
Banana → 2
Orange → 1
```

---

## Applications

Frequency Count is used in many DSA problems, such as:

- Contains Duplicate
- Valid Anagram
- First Unique Character in a String
- Majority Element
- Top K Frequent Elements
- Find Duplicate Numbers
- Character Counting

---

## Time Complexity

**O(n)**

Reason: We visit each element only once.

---

## Space Complexity

**O(n)**

Reason: We store the frequency of each unique element.

---

## Summary

Frequency Count is one of the most useful techniques in hashing. By storing the count of each element in a Dictionary or Counter, we can solve many array and string problems efficiently. It is a common pattern used in coding interviews.
