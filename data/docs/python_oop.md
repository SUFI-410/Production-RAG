
content = """# Python OOP

## Introduction to Python OOP

Python OOP (Object-Oriented Programming) is a programming paradigm that organizes code around objects and classes.

Python supports OOP through:

- Classes and objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

Python OOP is widely used in:

- Large-scale software development
- Game development
- GUI applications
- Web frameworks
- API design
- Data modeling
- Reusable code libraries
- Enterprise applications

---

# Classes in Python

A class is a blueprint for creating objects. It defines attributes and methods that the created objects will have.

Example:

```python
class Person:
    pass

p = Person()
print(p)
```

Output:

```
<__main__.Person object at 0x...>
```

Classes are defined using the `class` keyword followed by the class name.

Example:

```python
class Dog:
    pass
```

---

# Objects in Python

An object is an instance of a class. It contains real data and can perform actions defined by the class.

Example:

```python
class Car:
    pass

toyota = Car()
honda = Car()
```

In this example:

- `toyota` is an object of the `Car` class.
- `honda` is another object of the `Car` class.
- Both are independent instances.

---

# The __init__ Method

The `__init__` method is a constructor that initializes object attributes when an object is created.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Ali", 20)
print(s.name)
print(s.age)
```

A class can have multiple attributes initialized in `__init__`.

---

# Instance Attributes

Instance attributes are variables that belong to a specific object.

Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Sara", 5000)
print(emp.name)
print(emp.salary)
```

Rules:

- Instance attributes are accessed using `self`.
- Each object has its own copy of instance attributes.
- Instance attributes can be modified after object creation.

Example:

```python
emp.salary = 6000
print(emp.salary)
```

---

# Class Attributes

Class attributes are variables shared among all instances of a class.

Example:

```python
class Company:
    employees = 100

    def __init__(self, name):
        self.name = name

c1 = Company("TechCorp")
c2 = Company("SoftInc")

print(c1.employees)
print(c2.employees)
```

These are the same for all objects.

---

# Instance Methods

Instance methods are functions defined inside a class that operate on instance attributes.

Example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(10, 5)
print(r.area())
```

Output:

```
50
```

---

# The self Parameter

The `self` parameter refers to the current instance of the class.

Example:

```python
class Book:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(self.title)

b = Book("Python Guide")
b.show()
```

Rules:

- `self` must be the first parameter of instance methods.
- `self` allows access to instance attributes and methods.
- `self` is passed automatically when calling methods on objects.

---

# Class Methods

Class methods operate on class attributes rather than instance attributes.

Example:

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
print(Counter.count)
```

Output:

```
1
```

---

# Static Methods

Static methods do not access instance or class attributes. They behave like regular functions inside a class.

Example:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))
```

Output:

```
8
```

---

# Inheritance

Inheritance allows a class to acquire attributes and methods from another class.

Example:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

Output:

```
Animal speaks
```

---

# Method Overriding

Method overriding allows a child class to provide a specific implementation of a method inherited from the parent class.

Example:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

c = Cat()
c.speak()
```

Output:

```
Cat meows
```

---

# The super() Function

The `super()` function allows access to methods and attributes of the parent class.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

emp = Employee("Ali", 5000)
print(emp.name)
print(emp.salary)
```

---

# Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one parent class.

Example:

```python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
```

Output:

```
Flying
Swimming
```

---

# Encapsulation

Encapsulation restricts direct access to some of an object's attributes and methods.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
```

Output:

```
1500
```

---

# Private Attributes

Private attributes are prefixed with double underscores and cannot be accessed directly from outside the class.

Example:

```python
class User:
    def __init__(self, password):
        self.__password = password

u = User("secret123")
```

Accessing `u.__password` directly will raise an error.

---

# Protected Attributes

Protected attributes are prefixed with a single underscore. They indicate that the attribute should not be accessed directly, though it is still possible.

Example:

```python
class Vehicle:
    def __init__(self):
        self._speed = 0

v = Vehicle()
print(v._speed)
```

---

# Property Decorators

Property decorators allow controlled access to attributes using getter, setter, and deleter methods.

Example:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value

c = Circle(5)
print(c.radius)
c.radius = 10
print(c.radius)
```

---

# Polymorphism

Polymorphism allows different classes to be treated as instances of the same class through a common interface.

Example:

```python
class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")

for animal in [Bird(), Fish()]:
    animal.move()
```

Output:

```
Flying
Swimming
```

---

# Duck Typing

Duck typing is a form of polymorphism where an object's suitability is determined by the presence of certain methods and properties.

Example:

```python
class Dog:
    def make_sound(self):
        print("Bark")

class Cat:
    def make_sound(self):
        print("Meow")

def play_sound(animal):
    animal.make_sound()

play_sound(Dog())
play_sound(Cat())
```

Output:

```
Bark
Meow
```

---

# Abstraction

Abstraction hides complex implementation details and shows only the essential features.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())
```

Output:

```
16
```

---

# Abstract Classes

Abstract classes cannot be instantiated and are meant to be subclassed. They define methods that must be implemented by child classes.

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()
```

Output:

```
Car started
```

---

# Magic Methods

Magic methods are special methods with double underscores that enable custom behavior for built-in operations.

Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
```

Output:

```
Point(4, 6)
```

---

# Common Magic Methods

Common magic methods include:

- `__init__` Constructor
- `__str__` String representation
- `__repr__` Official string representation
- `__len__` Length
- `__eq__` Equality comparison
- `__lt__` Less than comparison
- `__add__` Addition
- `__getitem__` Index access

---

# Operator Overloading

Operator overloading allows custom classes to define behavior for Python operators.

Example:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)
```

Output:

```
Vector(6, 8)
```

---

# Composition

Composition is a design technique where a class contains objects of other classes as attributes.

Example:

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

c = Car()
c.start()
```

Output:

```
Engine started
```

---

# Aggregation

Aggregation is a weaker form of composition where the contained object can exist independently of the container.

Example:

```python
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, department):
        self.department = department

d = Department("Computer Science")
u = University(d)
```

---

# Class Variables vs Instance Variables

Class variables are shared across all instances, while instance variables are unique to each object.

Example:

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Ali")
s2 = Student("Sara")

print(s1.school)
print(s2.school)
print(s1.name)
print(s2.name)
```

Output:

```
ABC School
ABC School
Ali
Sara
```

---

# The __str__ and __repr__ Methods

`__str__` provides an informal string representation for end users.

`__repr__` provides an official string representation for developers.

Example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

p = Product("Laptop", 999)
print(str(p))
print(repr(p))
```

Output:

```
Laptop: $999
Product('Laptop', 999)
```

---

# Method Resolution Order (MRO)

MRO defines the order in which Python looks for methods in a hierarchy of classes.

Example:

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__mro__)
```

Output:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

---

# Python OOP Summary

Important Python OOP concepts include:

- Classes and objects
- __init__ constructor
- Instance and class attributes
- Instance, class, and static methods
- Inheritance and method overriding
- super() function
- Multiple inheritance
- Encapsulation and access modifiers
- Property decorators
- Polymorphism and duck typing
- Abstraction and abstract classes
- Magic methods and operator overloading
- Composition and aggregation
- Class vs instance variables
- __str__ and __repr__ methods
- Method Resolution Order

These concepts form the foundation for advanced object-oriented programming in Python.
"""

with open('/mnt/agents/output/python_oop.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved successfully!")
