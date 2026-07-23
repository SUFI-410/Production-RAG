# Python Functions

## Introduction to Functions

A function is a reusable block of code that performs a specific task.

Functions are one of the fundamental concepts in Python programming. They allow developers to divide large programs into smaller, organized, and reusable pieces.

Using functions improves:

- Code reusability
- Program organization
- Readability
- Testing
- Debugging
- Maintainability

A function is executed only when it is called.

---

# Defining a Function

Python functions are created using the `def` keyword.

## Syntax

```python
def function_name(parameters):
    function_body
```

Example:

```python
def say_hello():
    print("Hello Python")


say_hello()
```

Output:

```
Hello Python
```

Explanation:

- `def` creates a function.
- `say_hello` is the function name.
- Parentheses contain parameters.
- The indented code is the function body.

---

# Calling a Function

Creating a function does not execute it.

The function must be called.

Example:

```python
def welcome():
    print("Welcome to Python")


welcome()
```

Output:

```
Welcome to Python
```

A function can be called multiple times.

Example:

```python
def message():
    print("Learning Python")


message()
message()
message()
```

---

# Function Parameters and Arguments

Functions can receive input values through parameters.

A parameter is a variable defined inside the function declaration.

An argument is the actual value passed when calling the function.

Example:

```python
def greet(name):
    print("Hello", name)


greet("Sufyan")
```

Output:

```
Hello Sufyan
```

Here:

- `name` is a parameter.
- `"Sufyan"` is an argument.

---

# Multiple Parameters

A function can accept multiple parameters.

Example:

```python
def add(number1, number2):

    result = number1 + number2

    print(result)


add(10, 20)
```

Output:

```
30
```

---

# Returning Values from Functions

Functions can return results using the `return` statement.

Example:

```python
def multiply(a, b):

    return a * b


result = multiply(5, 4)

print(result)
```

Output:

```
20
```

The `return` statement:

- Sends a value back to the caller.
- Ends function execution.
- Allows results to be stored in variables.

---

# Difference Between print() and return

`print()` displays output.

`return` sends data back.

Example:

```python
def add(a, b):

    print(a + b)


add(2, 3)
```

The result is displayed but cannot be reused.

Using return:

```python
def add(a, b):

    return a + b


value = add(2, 3)

print(value * 10)
```

Output:

```
50
```

---

# Default Parameters

Python allows default values for parameters.

Example:

```python
def greet(name="Guest"):

    print("Hello", name)


greet()

greet("Ali")
```

Output:

```
Hello Guest
Hello Ali
```

Default parameters are used when no argument is provided.

---

# Keyword Arguments

Python allows arguments to be passed using parameter names.

Example:

```python
def student(name, age):

    print(name)
    print(age)


student(
    age=20,
    name="Ahmed"
)
```

Keyword arguments improve readability.

---

# Positional Arguments

Arguments can be passed according to their position.

Example:

```python
def person(name, age):

    print(name, age)


person("Ali", 25)
```

The first value goes to `name`.

The second value goes to `age`.

---

# Variable Length Arguments

Python functions can accept a variable number of arguments.

There are two special types:

- `*args`
- `**kwargs`

---

# *args in Python

`*args` allows a function to accept unlimited positional arguments.

The arguments are collected into a tuple.

Example:

```python
def calculate_total(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_total(1, 2, 3))

print(calculate_total(10, 20, 30, 40))
```

Output:

```
6
100
```

Explanation:

- `*numbers` collects all extra positional arguments.
- The data type is tuple.
- The function can receive any number of values.

---

# **kwargs in Python

`**kwargs` allows a function to accept unlimited keyword arguments.

The arguments are stored as a dictionary.

Example:

```python
def display_profile(**information):

    for key, value in information.items():

        print(key, value)


display_profile(
    name="Sufyan",
    skill="Python",
    level="Advanced"
)
```

Output:

```
name Sufyan
skill Python
level Advanced
```

Explanation:

- `**information` collects keyword arguments.
- The data type is dictionary.
- Each value has a key.

---

# Difference Between *args and **kwargs

| Feature | *args | **kwargs |
|---|---|---|
| Full meaning | Variable positional arguments | Variable keyword arguments |
| Data type | Tuple | Dictionary |
| Symbol | Single star | Double star |
| Input example | 1,2,3 | name="Python" |
| Used for | Unknown number of values | Unknown number of named values |

---

# Combining *args and **kwargs

Both can be used together.

Example:

```python
def information(*args, **kwargs):

    print(args)

    print(kwargs)


information(
    10,
    20,
    name="Python",
    version=3
)
```

Output:

```
(10,20)

{
'name':'Python',
'version':3
}
```

---

# Lambda Functions

Lambda functions are small anonymous functions.

They do not have a name.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x


print(square(5))
```

Output:

```
25
```

Lambda functions are commonly used with:

- map()
- filter()
- sorted()

---

# Nested Functions

A function can be created inside another function.

Example:

```python
def outer():

    def inner():

        print("Inside inner function")


    inner()


outer()
```

Nested functions are used in:

- Closures
- Decorators
- Encapsulation

---

# Higher Order Functions

A higher-order function accepts another function as an argument or returns a function.

Example:

```python
def apply_function(operation, value):

    return operation(value)


result = apply_function(
    lambda x: x * 2,
    5
)

print(result)
```

Output:

```
10
```

---

# Recursive Functions

A recursive function calls itself.

Example:

```python
def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
```

Output:

```
120
```

Recursive functions need:

1. Base condition
2. Recursive call

---

# Function Scope

Python variables have different scopes.

## Local Scope

A variable created inside a function.

Example:

```python
def test():

    value = 100

    print(value)
```

`value` only exists inside the function.

---

## Global Scope

A variable created outside functions.

Example:

```python
language = "Python"


def show():

    print(language)


show()
```

---

# Docstrings

Functions can contain documentation using docstrings.

Example:

```python
def add(a,b):
    """
    Adds two numbers.
    """

    return a+b
```

Docstrings explain what a function does.

---

# Best Practices for Python Functions

Good functions should:

- Have meaningful names
- Perform one clear task
- Avoid unnecessary complexity
- Use proper parameters
- Return useful results
- Include documentation when needed

---

# Summary

Python functions provide:

- Code reuse
- Better program structure
- Parameters and arguments
- Return values
- Default values
- Keyword arguments
- Variable arguments using `*args`
- Keyword variable arguments using `**kwargs`
- Lambda functions
- Nested functions
- Higher-order functions
- Recursive programming
- Scope management
