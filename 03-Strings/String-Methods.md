# String Methods

## What are String Methods?

String methods are built-in functions provided by Python to perform different operations on strings.

They make working with strings easier and faster.

---

## upper()

Converts all characters to uppercase.

```python
text = "python"
print(text.upper())
```

**Output**

```text
PYTHON
```

---

## lower()

Converts all characters to lowercase.

```python
text = "PYTHON"
print(text.lower())
```

**Output**

```text
python
```

---

## title()

Converts the first letter of each word to uppercase.

```python
text = "hello world"
print(text.title())
```

**Output**

```text
Hello World
```

---

## capitalize()

Converts only the first letter of the string to uppercase.

```python
text = "python programming"
print(text.capitalize())
```

**Output**

```text
Python programming
```

---

## strip()

Removes spaces from both the beginning and the end of a string.

```python
text = "   Python   "
print(text.strip())
```

**Output**

```text
Python
```

---

## lstrip()

Removes spaces from the left side.

```python
text = "   Python"
print(text.lstrip())
```

**Output**

```text
Python
```

---

## rstrip()

Removes spaces from the right side.

```python
text = "Python   "
print(text.rstrip())
```

**Output**

```text
Python
```

---

## replace()

Replaces one part of a string with another.

```python
text = "Hello World"
print(text.replace("World", "Python"))
```

**Output**

```text
Hello Python
```

---

## split()

Splits a string into a list.

```python
text = "Python Java C++"
print(text.split())
```

**Output**

```text
['Python', 'Java', 'C++']
```

---

## join()

Joins the elements of a list into a single string.

```python
words = ["Python", "Java", "C++"]
print(" ".join(words))
```

**Output**

```text
Python Java C++
```

---

## find()

Returns the index of the first occurrence of a substring.

```python
text = "Python"
print(text.find("t"))
```

**Output**

```text
2
```

If the substring is not found, it returns `-1`.

---

## count()

Counts how many times a character or substring appears.

```python
text = "banana"
print(text.count("a"))
```

**Output**

```text
3
```

---

## startswith()

Checks whether a string starts with a given value.

```python
text = "Python"
print(text.startswith("Py"))
```

**Output**

```text
True
```

---

## endswith()

Checks whether a string ends with a given value.

```python
text = "Python"
print(text.endswith("on"))
```

**Output**

```text
True
```

---

## isalpha()

Returns `True` if all characters are letters.

```python
text = "Python"
print(text.isalpha())
```

**Output**

```text
True
```

---

## isdigit()

Returns `True` if all characters are digits.

```python
text = "12345"
print(text.isdigit())
```

**Output**

```text
True
```

---

## isalnum()

Returns `True` if all characters are letters or numbers.

```python
text = "Python123"
print(text.isalnum())
```

**Output**

```text
True
```

---

## len()

Returns the length of the string.

```python
text = "Python"
print(len(text))
```

**Output**

```text
6
```

---

## Summary

| Method | Purpose |
|---------|---------|
| upper() | Convert to uppercase |
| lower() | Convert to lowercase |
| title() | Capitalize each word |
| capitalize() | Capitalize first letter |
| strip() | Remove spaces from both ends |
| lstrip() | Remove left spaces |
| rstrip() | Remove right spaces |
| replace() | Replace text |
| split() | Convert string to list |
| join() | Convert list to string |
| find() | Find index of a substring |
| count() | Count occurrences |
| startswith() | Check starting characters |
| endswith() | Check ending characters |
| isalpha() | Check only letters |
| isdigit() | Check only digits |
| isalnum() | Check letters and numbers |
| len() | Get string length |

---

## Key Takeaway

- Python provides many built-in methods to work with strings.
- These methods make string manipulation simple and efficient.
- Learning these methods will help solve many string-related coding problems more easily.
