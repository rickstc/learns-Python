# Introduction

# Lists and Membership Operators
Data structures are containers that organize and group data types together in different ways. 
- `list` - A data type for mutable, ordered sequences of elements
    - Defined using `[]`
    - Values can be looked up by index: `months[0]` (first) or `months[-1]` (last) (zero-based indexing)
    - Can contain a mixture of data types

## Slicing
- Lists can be sliced `months[6:9]` - lower bound is inclusive, upper bound is exclusive
- `months[6:]`

## Membership Operations
- Support `in` and `not in`, returning a boolean

## Mutability and Order
- Strings are sequences of characters which cannot be modified
- Lists can contain any data type and can be modified
- Both are ordered

# Why Do We Need Lists?
Lists help us organize and process data

# List Methods
While strings are not mutable:
```
name = "George"
student = name
name = "Jane"
print(name) returns "Jane"
print(student) returns "George"
```

Lists are mutable:
```
grades = [1, 2, 3]
numbers = grades
grades[1] = 3
print(grades) returns [1, 3, 3]
print(numbers) returns [1, 3, 3]
```
- `len()` - how many elements are in a list
- `max()` - greatest element in a list (highest number, last in alphabet, etc)
- `min()` - opposite of max
- `sorted()` - Returns a copy of a list in order from smallest to largest, leaving list unchanged
- `separator_string.join(['list', 'of', 'strings'])` - returns a string consisting of the list elements joined by a separator string
- `append('z')` adds an element to the end of a list
# Tuples
- Data type for immutable ordered sequences of elements often used to store related pieces of information  
`location = (13,4125, 103.8666667)`

# Sets
A **set** is a data type for mutable unordered collections of unique elements.
- They support the **in** operator, as well as the **add** and **pop** methods.
- Note: Because sets are unordered, **pop** will remove a random element from the set.
- Mathmatical operations like union, intersaction and difference are easy to perform and faster than such operators with other containers.  
Define a set: `fruit = {"apple", "banana", "orange", "grapefruit"}`

# Dictionaries and Identity Operators

# When to Use Dictionaries?

# Compound Data Structures

# Conclusion