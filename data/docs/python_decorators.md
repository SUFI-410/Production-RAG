# Python Decorators

## What is a Decorator?

A decorator is a callable that takes another function as input, adds additional behavior, and returns the modified function without changing the original source code.

Decorators are commonly used for:

- Logging
- Authentication
- Authorization
- Caching
- Timing execution
- Input validation
- Rate limiting

## Basic Example

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```

Output:

```
Before
Hello
After
```

## Why Use Decorators?

Decorators allow developers to reuse logic without modifying existing functions.

They follow the DRY (Don't Repeat Yourself) principle and are widely used in frameworks such as Django, Flask, FastAPI, and LangChain.

## Decorators with Arguments

```python
def log(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@log
def add(a, b):
    return a + b
```

## Built-in Decorators

Python provides several built-in decorators including:

- @property
- @classmethod
- @staticmethod

## Real-world Usage

Django uses decorators for authentication.

```python
@login_required
def dashboard(request):
    ...
```

FastAPI uses decorators to define API routes.

```python
@app.get("/users")
def get_users():
    ...
```

## Summary

Decorators are one of Python's most powerful features. They allow behavior to be added dynamically while keeping business logic clean and reusable.
