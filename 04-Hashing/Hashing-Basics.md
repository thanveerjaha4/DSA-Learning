# Hashing Basics

Hashing is a technique used to store and retrieve data quickly.

Instead of searching through every element one by one, hashing stores data in a way that allows us to find it much faster.

In Python, hashing is mainly done using **Dictionary (dict)** and **Set (set)**.

---

## Why Do We Use Hashing?

Without hashing, we may need to check every element in a list.

Example:

```text
Array = [5, 8, 2, 9, 4]

Find 9
```

We compare:

```text
5 ❌
8 ❌
2 ❌
9 ✅
```

This takes **O(n)** time.

With hashing, we can find an element in **O(1)** average time.

---

## What is a Hash Function?

A Hash Function converts a key into an index where the value is stored.

You don't have to write the hash function yourself in Python. Dictionaries and sets automatically use hashing internally.

---

## What is a Hash Table?

A Hash Table is a data structure that stores data as **key-value pairs**.

Python's **Dictionary** is implemented using a hash table.

Example:

```python
student = {
    "Name": "Jaha",
    "Age": 20,
    "Branch": "ECE"
}
```

Here,

- Name → Jaha
- Age → 20
- Branch → ECE

The keys help us quickly access the values.

---

## Dictionary in Python

A dictionary stores data in **key-value pairs**.

Example:

```python
student = {
    "Name": "Jaha",
    "Age": 20
}

print(student["Name"])
```

### Output

```text
Jaha
```

---

## Set in Python

A set stores only **unique elements**.

Duplicate values are automatically removed.

Example:

```python
numbers = {1, 2, 2, 3, 4, 4}

print(numbers)
```

### Output

```text
{1, 2, 3, 4}
```

---

## Advantages of Hashing

- Fast searching
- Fast insertion
- Fast deletion
- Stores unique data easily using a set
- Used in many coding interview problems

---

## Disadvantages of Hashing

- Uses extra memory.
- Performance can decrease if many keys map to the same location (called a collision).
- Dictionaries do not support indexing like lists.

---

## Time Complexity

| Operation | Average Time |
|-----------|--------------|
| Search | O(1) |
| Insert | O(1) |
| Delete | O(1) |

---

## Space Complexity

**O(n)**

Reason: Extra space is needed to store the keys and values.

---

## Where is Hashing Used?

- Two Sum
- Contains Duplicate
- Valid Anagram
- First Unique Character
- Frequency Count
- Majority Element
- Intersection of Arrays

---

## Summary

Hashing is one of the most important techniques in DSA. It helps us store and retrieve data quickly using dictionaries and sets. Learning hashing makes many array and string problems much easier and more efficient.
