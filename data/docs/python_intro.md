# Python Introduction

## What is Python?

Python is a high-level, interpreted, general-purpose programming language designed to be simple, readable, and powerful.

Python was created by Guido van Rossum and first released in 1991.

Python focuses on:

- Simple syntax
- Code readability
- Developer productivity
- Rapid application development

Python programs are easy to write and understand compared to many other programming languages.

---

# Why Learn Python?

Python is one of the most popular programming languages because it can be used in many different fields.

Python is commonly used for:

- Web development
- Backend development
- Data science
- Machine learning
- Artificial intelligence
- Automation
- Scripting
- Software development
- Testing
- Scientific computing

---

# Python Characteristics

Python has several important characteristics.

## High-Level Language

Python hides complex computer operations and allows developers to focus on solving problems.

Example:

```python
print("Hello Python")
```

The programmer does not need to manage memory manually.

---

## Interpreted Language

Python code is executed by the Python interpreter.

Unlike compiled languages, Python programs are usually executed line by line.

Example:

```python
print("First line")
print("Second line")
```

---

## Easy and Readable Syntax

Python syntax is designed to be close to natural language.

Example:

```python
if age >= 18:
    print("Adult")
```

Python uses indentation instead of curly brackets to define code blocks.

---

# Python Features

Python provides many powerful features:

## Simple Syntax

Python code is shorter and easier to read.

Example:

```python
message = "Hello Python"

print(message)
```

---

## Dynamic Typing

Python variables do not require a data type declaration.

The type is automatically determined at runtime.

Example:

```python
value = 10

value = "Python"
```

The same variable can store different types of values.

---

## Object-Oriented Programming Support

Python supports object-oriented programming concepts including:

- Classes
- Objects
- Inheritance
- Encapsulation
- Polymorphism

Example:

```python
class Person:

    def __init__(self, name):

        self.name = name
```

---

## Large Standard Library

Python includes many built-in modules for common tasks.

Examples:

- `math` for mathematical operations
- `datetime` for dates and times
- `os` for operating system interaction
- `json` for JSON data handling

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

## Third-Party Packages

Python has a huge ecosystem of external libraries.

Popular Python packages include:

- NumPy for numerical computing
- Pandas for data analysis
- Django for web development
- Flask for web applications
- TensorFlow for machine learning
- PyTorch for deep learning

---

# Installing Python

Python can be installed from the official Python website.

After installation, Python can be checked using:

```bash
python --version
```

Example output:

```
Python 3.x.x
```

---

# Running Python Code

Python programs are stored in files with the `.py` extension.

Example:

```
hello.py
```

File content:

```python
print("Hello World")
```

Run:

```bash
python hello.py
```

Output:

```
Hello World
```

---

# Python Comments

Comments are notes written inside code.

Python ignores comments during execution.

Single-line comment:

```python
# This is a comment

print("Hello")
```

Comments improve code readability.

---

# Variables in Python

Variables are names that reference objects stored in memory.

Python variables do not need explicit declaration.

Example:

```python
name = "Sufyan"

age = 30

price = 99.99
```

Here:

- `name` stores a string value.
- `age` stores an integer value.
- `price` stores a floating-point value.

---

# Variable Naming Rules

Python variable names:

- Must start with a letter or underscore.
- Cannot start with a number.
- Cannot contain spaces.
- Are case-sensitive.

Valid:

```python
user_name = "Ali"

age1 = 20

_price = 100
```

Invalid:

```python
1name = "Ali"

user name = "Ali"
```

---

# Python Data Types

Python provides several built-in data types.

## Numeric Types

### Integer

Whole numbers.

Example:

```python
age = 30
```

### Float

Decimal numbers.

Example:

```python
price = 99.99
```

---

## String

A sequence of characters.

Example:

```python
name = "Python"
```

---

## Boolean

Represents True or False values.

Example:

```python
is_active = True
```

---

## List

A collection that can store multiple values.

Example:

```python
languages = [
    "Python",
    "Java",
    "C++"
]
```

---

## Tuple

An ordered collection that cannot be changed.

Example:

```python
coordinates = (10,20)
```

---

## Dictionary

Stores data as key-value pairs.

Example:

```python
student = {

    "name": "Ali",

    "age": 20
}
```

---

## Set

Stores unique values.

Example:

```python
numbers = {1,2,3}
```

---

# Type Checking

The `type()` function checks the data type of a value.

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

Python allows converting one data type into another.

Example:

```python
age = "30"

number = int(age)

print(number)
```

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

---

# Python Indentation

Python uses indentation to define blocks of code.

Example:

```python
if True:

    print("Python uses indentation")
```

Incorrect indentation causes an error.

---

# Python Execution Model

Python source code is processed by the interpreter.

The general flow:

```
Python Code
     |
     v
Python Interpreter
     |
     v
Execution
```

---

# Python Applications

Python is used in many industries.

## Web Development

Frameworks:

- Django
- Flask
- FastAPI

---

## Artificial Intelligence

Python libraries:

- TensorFlow
- PyTorch
- Scikit-learn

---

## Data Science

Libraries:

- NumPy
- Pandas
- Matplotlib

---

## Automation

Python can automate:

- File operations
- Web tasks
- Reports
- Data processing

---

# Summary

Python is a powerful programming language used for many applications.

Important Python concepts include:

- Simple syntax
- Variables
- Data types
- Dynamic typing
- Functions
- Object-oriented programming
- Libraries and packages
- Automation
- Web development
- Artificial intelligence
- Data science
