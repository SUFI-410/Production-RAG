# Python Basics

## Introduction to Python Basics

Python basics are the fundamental concepts required to write Python programs.

Python is a high-level, interpreted, general-purpose programming language known for:

- Simple and readable syntax
- Dynamic typing
- Object-oriented programming support
- Large ecosystem
- Extensive libraries
- Cross-platform compatibility

Python is widely used in:

- Web development
- Backend development
- Data science
- Artificial intelligence
- Machine learning
- Automation
- Scripting
- Software development

---

# Python Program Structure

A Python program is a collection of statements and instructions executed by the Python interpreter.

Example:

```python
print("Hello Python")
```

Output:

```
Hello Python
```

Python programs usually use the `.py` file extension.

Example:

```
program.py
```

---

# Variables in Python

A variable is a name that refers to an object stored in memory.

Python variables do not require declaring their data type.

Example:

```python
name = "Python"

age = 30

price = 99.99
```

In this example:

- `name` stores a string value.
- `age` stores an integer value.
- `price` stores a floating-point value.

---

# Dynamic Typing

Python is a dynamically typed language.

This means the type of a variable is determined automatically during execution.

Example:

```python
value = 100

print(value)

value = "Python"

print(value)
```

A variable can store different types of values during program execution.

---

# Variable Naming Rules

Python variable names follow specific rules.

Valid variable names:

```python
username = "Sufyan"

user_age = 30

_private = True
```

Rules:

- Must start with a letter or underscore.
- Cannot start with a number.
- Cannot contain spaces.
- Variable names are case-sensitive.

Example:

```python
name = "Python"

Name = "Java"
```

These are different variables.

---

# Python Data Types

Python provides built-in data types for storing different kinds of values.

Main Python data types include:

- Integer
- Float
- String
- Boolean
- List
- Tuple
- Set
- Dictionary

---

# Integer

Integers are whole numbers without decimal points.

Example:

```python
age = 30

number = -10
```

---

# Float

Float values contain decimal numbers.

Example:

```python
price = 99.99

temperature = 36.5
```

---

# String

A string is a sequence of characters.

Strings are created using:

- Single quotes
- Double quotes

Example:

```python
name = "Python"

message = 'Hello World'
```

String operations:

```python
first = "Hello"

second = "Python"

result = first + second
```

---

# Boolean

Boolean values represent true or false conditions.

Python has two Boolean values:

- `True`
- `False`

Example:

```python
is_active = True

is_logged_in = False
```

Booleans are commonly used in conditions.

---

# Lists

A list is an ordered collection that can store multiple values.

Lists are mutable, meaning their values can be changed.

Example:

```python
languages = [
    "Python",
    "Java",
    "C++"
]
```

Accessing list values:

```python
print(languages[0])
```

Output:

```
Python
```

---

# Tuples

A tuple is an ordered collection that cannot be modified after creation.

Example:

```python
coordinates = (10, 20)
```

Tuples are immutable.

---

# Sets

A set stores unique values.

Example:

```python
numbers = {
    1,
    2,
    3
}
```

Duplicate values are automatically removed.

Example:

```python
values = {1,1,2,3}

print(values)
```

Output:

```
{1,2,3}
```

---

# Dictionaries

A dictionary stores data as key-value pairs.

Example:

```python
student = {

    "name": "Ali",

    "age": 20,

    "language": "Python"
}
```

Accessing values:

```python
print(student["name"])
```

Output:

```
Ali
```

---

# Type Checking

The `type()` function is used to check the data type of a value.

Example:

```python
number = 100

print(type(number))
```

Output:

```
<class 'int'>
```

---

# Type Conversion

Type conversion changes one data type into another.

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

Example:

```python
age = "30"

number = int(age)

print(number)
```

---

# Input in Python

The `input()` function allows users to enter values.

Example:

```python
name = input("Enter your name: ")

print(name)
```

The input function always returns a string.

---

# Output in Python

The `print()` function displays information.

Example:

```python
print("Hello Python")
```

Multiple values:

```python
name = "Ali"

age = 20

print(name, age)
```

---

# Operators in Python

Operators perform operations on values.

Python operators include:

- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators

---

# Arithmetic Operators

Arithmetic operators perform mathematical operations.

Example:

```python
a = 10

b = 5

print(a + b)

print(a - b)

print(a * b)

print(a / b)
```

Operators:

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus
- `**` Power

---

# Comparison Operators

Comparison operators compare values.

Example:

```python
age = 20

print(age >= 18)
```

Output:

```
True
```

Operators:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

---

# Conditional Statements

Python uses conditions to control program flow.

Example:

```python
age = 18


if age >= 18:

    print("Adult")

else:

    print("Minor")
```

---

# Loops in Python

Loops repeat code multiple times.

Python provides:

- `for` loop
- `while` loop

Example:

```python
for number in range(5):

    print(number)
```

---

# Exception Handling

Python handles errors using `try` and `except`.

Example:

```python
try:

    number = int(input())

except:

    print("Invalid input")
```

Exception handling prevents programs from crashing.

---

# Importing Modules

Python allows importing reusable code from modules.

Example:

```python
import math

print(math.sqrt(25))
```

Output:

```
5.0
```

---

# Python Basics Summary

Important Python fundamentals include:

- Variables
- Data types
- Dynamic typing
- Input and output
- Operators
- Conditions
- Loops
- Functions
- Exception handling
- Modules
- Lists
- Tuples
- Sets
- Dictionaries

These concepts form the foundation for advanced Python programming.
