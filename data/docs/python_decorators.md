# Python Decorators

## Introduction to Decorators

A decorator is a special type of function in Python that allows you to modify or extend the behavior of another function without changing its original source code.

Decorators wrap another function and add additional functionality before or after the original function runs.

Decorators are widely used in:

- Web frameworks
- Authentication systems
- Logging systems
- Performance monitoring
- Caching systems
- Validation systems
- API development

---

# Why Use Decorators?

Without decorators, developers often repeat the same code in multiple functions.

Example:

```python
def login():

    print("Checking authentication")

    print("User login")


def profile():

    print("Checking authentication")

    print("Opening profile")
```

The authentication code is repeated.

A decorator allows this common behavior to be reused.

---

# Functions are First-Class Objects

In Python, functions are first-class objects.

This means functions can be:

- Stored in variables
- Passed as arguments
- Returned from other functions
- Stored inside data structures

Example:

```python
def hello():

    return "Hello Python"


message = hello

print(message())
```

Output:

```
Hello Python
```

The variable `message` now references the `hello` function.

---

# Passing Functions as Arguments

Python allows one function to receive another function as an argument.

Example:

```python
def say_hello():

    print("Hello")


def execute_function(function):

    function()


execute_function(say_hello)
```

Output:

```
Hello
```

This concept is the foundation of decorators.

---

# Creating a Simple Decorator

A decorator is usually created using nested functions.

Example:

```python
def my_decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")


    return wrapper
```

The decorator receives a function and returns a new function.

---

# Using a Decorator

Decorators are applied using the `@` symbol.

Example:

```python
def decorator(function):

    def wrapper():

        print("Before execution")

        function()

        print("After execution")


    return wrapper



@decorator
def hello():

    print("Hello Python")


hello()
```

Output:

```
Before execution
Hello Python
After execution
```

---

# How Decorators Work Internally

This:

```python
@decorator
def hello():

    print("Hello")
```

is equivalent to:

```python
def hello():

    print("Hello")


hello = decorator(hello)
```

The original function is replaced by the wrapped function.

---

# Decorators with Arguments

A decorator must handle functions that receive parameters.

Example:

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result


    return wrapper
```

`*args` and `**kwargs` allow the decorator to work with any function.

---

# Example: Logging Decorator

A logging decorator records when a function runs.

Example:

```python
def logger(function):

    def wrapper(*args, **kwargs):

        print(
            "Running:",
            function.__name__
        )

        result = function(*args, **kwargs)

        return result


    return wrapper



@logger
def add(a, b):

    return a + b


print(add(5, 3))
```

Output:

```
Running: add
8
```

---

# Example: Timing Decorator

A timing decorator measures function execution time.

Example:

```python
import time


def timer(function):

    def wrapper():

        start = time.time()

        function()

        end = time.time()

        print(
            "Execution time:",
            end - start
        )


    return wrapper
```

This is useful for:

- Performance testing
- Optimization
- Monitoring slow functions

---

# Authentication Decorator

Decorators are commonly used to protect functions.

Example:

```python
def require_login(function):

    def wrapper(user):

        if user == "admin":

            return function(user)

        else:

            return "Access denied"


    return wrapper



@require_login
def dashboard(user):

    return "Welcome dashboard"
```

Frameworks such as Django use decorators for authentication and permissions.

---

# Built-in Python Decorators

Python provides built-in decorators.

Common examples:

## @staticmethod

Creates a static method inside a class.

Example:

```python
class Math:

    @staticmethod
    def add(a,b):

        return a+b
```

---

## @classmethod

Creates a class method.

Example:

```python
class Person:

    count = 0


    @classmethod
    def show_count(cls):

        return cls.count
```

---

## @property

Allows a method to be accessed like an attribute.

Example:

```python
class Person:

    def __init__(self,name):

        self._name = name


    @property
    def name(self):

        return self._name
```

---

# Multiple Decorators

Python allows multiple decorators on one function.

Example:

```python
@decorator_one
@decorator_two
def function():

    pass
```

Execution order:

```python
function = decorator_one(
             decorator_two(function)
          )
```

The closest decorator runs first.

---

# Decorator with Arguments

Sometimes decorators need their own configuration.

Example:

```python
def repeat(times):

    def decorator(function):

        def wrapper():

            for i in range(times):

                function()


        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def hello():

    print("Hello")
```

Output:

```
Hello
Hello
Hello
```

---

# Real-World Uses of Decorators

Decorators are used in many applications.

## Web Development

Examples:

- Authentication
- Authorization
- Route handling
- Request processing

Framework examples:

- Django decorators
- Flask decorators
- FastAPI dependencies

---

## Software Engineering

Common uses:

- Logging
- Error handling
- Caching
- Validation
- Rate limiting
- Monitoring

---

# Advantages of Decorators

Decorators provide:

- Code reuse
- Cleaner functions
- Separation of concerns
- Less duplicate code
- Easier maintenance
- Better application structure

---

# Limitations of Decorators

Decorators can make code harder to understand if:

- Too many decorators are used
- Decorators are poorly documented
- Complex logic is hidden inside wrappers

Good decorators should have clear names and simple behavior.

---

# Summary

Python decorators are functions that modify other functions without changing their original code.

Important decorator concepts:

- Functions are first-class objects
- Functions can be passed as arguments
- Wrapper functions
- `@decorator` syntax
- `*args` and `**kwargs`
- Built-in decorators
- Decorators with arguments
- Multiple decorators
- Real-world usage in frameworks
