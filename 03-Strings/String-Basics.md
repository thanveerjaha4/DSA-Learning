# String Basics

## What is a String?

A string is a sequence of characters.

Examples:

```text
"hello"
"Python"
"12345"
```

A string can contain:

- Letters
- Numbers
- Special characters
- Spaces

---

## Why Do We Use Strings?

Strings are used to store and manipulate text.

Examples:

- Names
- Email addresses
- Passwords
- Messages
- URLs

---

## Creating a String

```python
name = "Jaha"
city = 'Warangal'
```

Strings can be created using single quotes (' ') or double quotes (" ").

---

## String Indexing

Each character has an index.

Example:

```text
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
```

Negative indexing starts from the end.

```text
String:   P  y  t  h  o  n
Index:   -6 -5 -4 -3 -2 -1
```

---

## String Traversal

Traversal means visiting each character one by one.

Example:

```python
text = "Python"

for ch in text:
    print(ch)
```

Output:

```text
P
y
t
h
o
n
```

---

## String Length

Use `len()` to find the number of characters.

```python
text = "Python"
print(len(text))
```

Output:

```text
6
```

---

## String Slicing

Slicing is used to get a part of a string.

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

---

## Common String Operations

```python
text = "Python"

text.upper()
text.lower()
text.strip()
text.replace("P","J")
text.split()
```

---

## Are Strings Mutable?

No.

Strings are **immutable**.

This means we cannot change a character directly.

❌ Incorrect

```python
text = "Python"

text[0] = "J"
```

✔ Correct

```python
text = "Python"

text = "J" + text[1:]
```

---

## Time Complexity

Access a character → O(1)

Traverse a string → O(n)

Create a new string → O(n)

Length of string → O(1)

---

## Summary

- A string is a sequence of characters.
- Strings are immutable in Python.
- Indexing starts from 0.
- Negative indexing starts from the end.
- Traversal means visiting every character.
- Slicing extracts part of a string.
- Python provides many built-in string functions.
