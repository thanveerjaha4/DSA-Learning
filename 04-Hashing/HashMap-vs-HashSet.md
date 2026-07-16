# HashMap vs HashSet

Both **HashMap** and **HashSet** are hashing data structures that provide fast searching, insertion, and deletion. They are widely used in DSA to solve problems efficiently.

---

## What is a HashMap?

A HashMap stores data in the form of **key-value pairs**.

Each key is unique and is used to access its corresponding value.

In Python, a **Dictionary (`dict`)** is a HashMap.

### Example

```python
student = {
    "Name": "Jaha",
    "Age": 20,
    "Branch": "ECE"
}

print(student["Name"])
```

### Output

```text
Jaha
```

---

## What is a HashSet?

A HashSet stores **only unique elements**.

It does not store key-value pairs.

Duplicate values are automatically removed.

In Python, a **Set (`set`)** is a HashSet.

### Example

```python
numbers = {1, 2, 2, 3, 4, 4}

print(numbers)
```

### Output

```text
{1, 2, 3, 4}
```

---

## Difference Between HashMap and HashSet

| HashMap | HashSet |
|---------|---------|
| Stores key-value pairs | Stores only unique values |
| Implemented using `dict` | Implemented using `set` |
| Values are accessed using keys | No keys are used |
| Duplicate keys are not allowed | Duplicate values are not allowed |
| Used when we need to store information about an element | Used when we only need to check whether an element exists |

---

## When to Use HashMap?

Use a HashMap when you need to:

- Count frequencies
- Store values with keys
- Find pairs (Two Sum)
- Store student details
- Store character counts

### Example

```python
marks = {
    "Math": 95,
    "Science": 90
}
```

---

## When to Use HashSet?

Use a HashSet when you need to:

- Remove duplicates
- Check whether an element exists
- Find unique elements

### Example

```python
nums = [1, 2, 2, 3, 4, 4]

unique = set(nums)

print(unique)
```

### Output

```text
{1, 2, 3, 4}
```

---

## Time Complexity

| Operation | HashMap | HashSet |
|-----------|---------|---------|
| Search | O(1) | O(1) |
| Insert | O(1) | O(1) |
| Delete | O(1) | O(1) |

---

## Real-Life Example

### HashMap

A student database:

```text
Roll No → Name

101 → Jaha
102 → Harsha
103 → Arjun
```

Here, each **Roll Number (Key)** is associated with a **Student Name (Value)**.

---

### HashSet

A list of students attending a workshop:

```text
Jaha
Harsha
Jaha
Arjun

```

Using a HashSet:

```text
Jaha
Harsha
Arjun

```

Duplicates are automatically removed.

---

## Summary

- Use a **HashMap** when you want to store **key-value pairs**.
- Use a **HashSet** when you only need **unique elements**.
- Both provide fast operations with an average time complexity of **O(1)**.
- HashMaps and HashSets are among the most commonly used data structures in coding interviews.
