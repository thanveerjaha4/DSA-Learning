# String Traversal

## What is String Traversal?

String traversal means visiting each character of a string one by one.

Traversal is used to:

- Search for a character
- Count characters
- Reverse a string
- Check for palindromes
- Compare strings

---

## Why Do We Need String Traversal?

Many string problems require checking every character.

Examples:

- Reverse a String
- Count Vowels
- Check Palindrome
- Find Duplicate Characters
- Convert Uppercase to Lowercase

---

## Method 1: Using a for Loop

The easiest way to traverse a string is using a `for` loop.

```python
text = "Python"

for ch in text:
    print(ch)
```

**Output**

```text
P
y
t
h
o
n
```

---

## Method 2: Using Index

Access each character using its index.

```python
text = "Python"

for i in range(len(text)):
    print(text[i])
```

**Output**

```text
P
y
t
h
o
n
```

---

## Method 3: Using while Loop

A `while` loop can also be used for traversal.

```python
text = "Python"

i = 0

while i < len(text):
    print(text[i])
    i += 1
```

**Output**

```text
P
y
t
h
o
n
```

---

## Method 4: Using enumerate()

`enumerate()` returns both the index and the character.

```python
text = "Python"

for index, ch in enumerate(text):
    print(index, ch)
```

**Output**

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

---

## Forward Traversal

Visit characters from left to right.

```python
text = "Python"

for ch in text:
    print(ch)
```

---

## Reverse Traversal

Visit characters from right to left.

```python
text = "Python"

for i in range(len(text) - 1, -1, -1):
    print(text[i])
```

**Output**

```text
n
o
h
t
y
P
```

---

## Time Complexity

**O(n)**

Reason: Every character is visited exactly once.

---

## Space Complexity

**O(1)**

Reason: No extra space is used (excluding the input string).

---

## Real-Life Example

Suppose you want to count vowels in a word.

```python
text = "Education"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)
```

**Output**

```text
5
```

---

## Applications of String Traversal

- Reverse a String
- Check Palindrome
- Count Characters
- Count Vowels
- Find a Character
- Compare Two Strings
- Convert Case
- Remove Spaces

---

## Summary

- String traversal means visiting every character one by one.
- It can be done using a `for` loop, `while` loop, indexing, or `enumerate()`.
- Traversal is used in most string-related problems.
- Understanding traversal is the first step toward solving string algorithms efficiently.
