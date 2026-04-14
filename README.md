# Complete Guide to OOP in Python

## Table of Contents
1. [Introduction](#introduction)
2. [Classes and Objects](#classes-and-objects)
3. [Inheritance](#inheritance)
4. [Encapsulation](#encapsulation)
5. [Polymorphism](#polymorphism)
6. [Abstraction](#abstraction)
7. [Advanced Concepts](#advanced-concepts)
8. [SOLID Principles](#solid-principles)

---

## Introduction

**Object-Oriented Programming (OOP)** is a programming paradigm that uses "objects" and "classes" to structure code in a way that is modular, reusable, and scalable.

### Why OOP?
- **Modularity**: Code is organized into logical units
- **Reusability**: Write once, use many times
- **Maintainability**: Easier to update and debug
- **Scalability**: Handle complex projects effectively
- **Security**: Encapsulation protects sensitive data

---

## Classes and Objects

### What is a Class?
A **class** is a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods).

### What is an Object?
An **object** is an instance of a class. It's a concrete realization of the class blueprint.

### Key Concepts:
- **Constructor (`__init__`)**: Initializes object attributes
- **Instance Variables**: Variables unique to each object
- **Class Variables**: Variables shared by all objects of the class
- **Instance Methods**: Functions that operate on instances
- **Class Methods**: Functions that operate on the class itself
- **Static Methods**: Functions that don't need access to instance or class data

### Example:
```python
class Car:
    total_cars = 0  # Class variable
    
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model
        Car.total_cars += 1
    
    def describe(self):
        return f"{self.brand} {self.model}"
    
    @classmethod
    def get_total(cls):
        return cls.total_cars
    
    @staticmethod
    def is_luxury(brand):
        return brand in ["BMW", "Mercedes", "Audi"]

car1 = Car("Toyota", "Camry")  # Create object
```

**Key Takeaway**: Classes define structure, objects are the actual data.

---

## Inheritance

### What is Inheritance?
Inheritance allows a **child class** to inherit properties and methods from a **parent class**. This promotes code reuse and establishes relationships.

### Types of Inheritance:
1. **Single Inheritance**: Child inherits from one parent
2. **Multi-level Inheritance**: Grandparent → Parent → Child
3. **Multiple Inheritance**: Child inherits from multiple parents
4. **Hierarchical**: Multiple children from one parent

### Key Concepts:
- **Parent/Base Class**: Class being inherited from
- **Child/Derived Class**: Class that inherits
- **super()**: Reference to parent class methods
- **Method Overriding**: Child implements parent's method differently

### Example:
```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()   # Inherited from Animal
dog.bark()  # Dog's own method
```

**Key Takeaway**: Inheritance creates IS-A relationships and promotes code reuse.

---

## Encapsulation

### What is Encapsulation?
Encapsulation bundles data (attributes) and methods together, and hides internal details from the outside world.

### Access Modifiers in Python:
- **Public** (no prefix): Accessible from anywhere
- **Protected** (`_name`): Convention - should not access from outside
- **Private** (`__name`): Name mangling - difficult to access from outside

### Key Concepts:
- **Data Hiding**: Keep internal implementation hidden
- **Controlled Access**: Use getters and setters
- **Validation**: Enforce business rules
- **Properties**: Use `@property` decorator for controlled access

### Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✓ Works
# print(account.__balance)    # ✗ Error
```

**Key Takeaway**: Encapsulation protects data integrity and provides controlled interface.

---

## Polymorphism

### What is Polymorphism?
Polymorphism means "many forms". Same method name can have different behaviors in different classes.

### Types:
1. **Method Overriding**: Child class redefines parent's method
2. **Method Overloading**: Multiple methods with same name (Python uses default args)
3. **Duck Typing**: "If it quacks like a duck..." - object type matters less than behavior
4. **Operator Overloading**: Custom behavior for operators like `+`, `-`, `==`

### Example:
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Same method, different behavior
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Different calculations
```

**Key Takeaway**: Polymorphism allows writing flexible, reusable code.

---

## Abstraction

### What is Abstraction?
Abstraction means hiding implementation details and showing only essential features. It simplifies complexity.

### Key Concepts:
- **Abstract Classes**: Cannot be instantiated directly
- **Abstract Methods**: Must be implemented by subclasses
- **Interface**: Contract that subclasses must follow
- **@abstractmethod**: Decorator to define abstract methods

### Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# animal = Animal()  # ✗ Error: can't instantiate abstract class
dog = Dog()
dog.make_sound()  # ✓ Works
```

**Key Takeaway**: Abstraction defines contracts and enforces implementation consistency.

---

## Advanced Concepts

### 1. Composition vs Inheritance
- **Inheritance**: IS-A relationship (Dog IS-A Animal)
- **Composition**: HAS-A relationship (Car HAS-A Engine)

```python
# Composition (preferred when logical)
class Car:
    def __init__(self):
        self.engine = Engine()  # HAS-A
```

### 2. Method Chaining (Fluent Interface)
```python
result = (QueryBuilder("users")
          .select("name, email")
          .where("age > 18")
          .limit(10)
          .build())
```

### 3. Singleton Pattern
Ensures only one instance of a class exists.

```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 4. Decorators
Functions that modify behavior of other functions/classes.

```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        # Pre-processing
        result = func(*args, **kwargs)
        # Post-processing
        return result
    return wrapper
```

### 5. Static and Class Methods
```python
class Math:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2
```

---

## SOLID Principles

### S - Single Responsibility Principle (SRP)
A class should have only one reason to change.

```python
# ✓ Good
class User:
    pass

class UserValidator:
    pass

# ✗ Bad
class User:
    def __init__(self, name):
        self.name = name
    def validate(self):
        pass
    def save(self):
        pass
```

### O - Open/Closed Principle (OCP)
Classes should be open for extension, closed for modification.

```python
class NotificationService:
    def __init__(self):
        self.notifiers = []
    
    def add_notifier(self, notifier):
        self.notifiers.append(notifier)
```

### L - Liskov Substitution Principle (LSP)
Subclasses should be substitutable for their parent classes.

### I - Interface Segregation Principle (ISP)
Clients should depend on specific interfaces, not general ones.

### D - Dependency Inversion Principle (DIP)
Depend on abstractions, not concrete implementations.

---

## Running the Examples

### File Structure:
```
python/
├── 01_classes_and_objects.py      # Basic class concepts
├── 02_inheritance.py               # Inheritance examples
├── 03_encapsulation.py             # Encapsulation techniques
├── 04_polymorphism.py              # Polymorphism examples
├── 05_abstraction.py               # Abstract classes
├── 06_advanced_oop.py              # Advanced features
├── main_runner.py                  # Run all examples
└── README.md                       # This file
```

### How to Run:

**Run individual files**:
```bash
python 01_classes_and_objects.py
python 02_inheritance.py
# ... etc
```

**Run all at once**:
```bash
python main_runner.py
```

---

## Quick Reference

| Concept | Purpose | When to Use |
|---------|---------|------------|
| **Class** | Blueprint for objects | Always (fundamental) |
| **Inheritance** | Code reuse, IS-A relation | When classes share behavior |
| **Encapsulation** | Data protection | Always (best practice) |
| **Polymorphism** | Flexible code | When same operation, different objects |
| **Abstraction** | Simplify complexity | When defining contracts |
| **Composition** | Flexible relationships | When HAS-A relationship |
| **Singleton** | One instance only | For shared resources (DB, config) |
| **Decorator** | Modify behavior | For cross-cutting concerns |

---

## Common Mistakes

❌ **Avoid:**
1. Not using encapsulation - exposing internal state
2. Deep inheritance hierarchies - prefer composition
3. Violating SOLID principles - tight coupling
4. Not using abstract classes for contracts
5. 

 over-engineering simple problems

✓ **Do:**
1. Keep classes focused (SRP)
2. Use meaningful names
3. Follow Python conventions
4. Document your code
5. Test your classes thoroughly

---

## Practice Exercises

1. Create a library system with Books, Members, and Borrowing
2. Build a restaurant POS system with different payment methods
3. Design an e-commerce system with products, carts, and orders
4. Create a game with different character classes and abilities
5. Build a logging system with different output targets (file, console, email)

---

## Resources

- Official Python Documentation: https://docs.python.org/3/
- PEP 8 - Style Guide: https://www.python.org/dev/peps/pep-0008/
- Abstract Base Classes: https://docs.python.org/3/library/abc.html

---

## Summary

OOP is about organizing code into logical, reusable, and maintainable units. Master the core concepts:
- **Classes and Objects**: Structure and instances
- **Inheritance**: Code reuse and relationships
- **Encapsulation**: Data protection
- **Polymorphism**: Flexibility
- **Abstraction**: Simplification

These concepts work together to create professional, scalable Python code!
