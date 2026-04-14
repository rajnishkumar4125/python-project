"""
OOPS CONCEPT 2: INHERITANCE
============================
Inheritance allows a class to inherit properties and methods from another class.
Parent class (Base class) / Child class (Derived class)
"""

# Example 1: Simple Inheritance
print("=" * 60)
print("EXAMPLE 1: Simple Inheritance - Animal Hierarchy")
print("=" * 60)

class Animal:
    """Parent/Base class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Dog(Animal):
    """Child class inherits from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def show_info(self):  # Override parent method
        super().show_info()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    """Another child class"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow! Meow!")
    
    def show_info(self):
        super().show_info()
        print(f"Color: {self.color}")


# Create objects
dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "Orange")

print("Dog Info:")
dog.show_info()
dog.eat()
dog.sleep()
dog.bark()

print("\nCat Info:")
cat.show_info()
cat.eat()
cat.sleep()
cat.meow()


# Example 2: Multi-level Inheritance
print("\n" + "=" * 60)
print("EXAMPLE 2: Multi-level Inheritance")
print("=" * 60)

class Vehicle:
    """Base class"""
    
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle is starting")
    
    def stop(self):
        print(f"{self.brand} vehicle is stopping")


class FourWheeler(Vehicle):
    """Intermediate class"""
    
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors
    
    def open_trunk(self):
        print("Trunk opened")


class Car(FourWheeler):
    """Final class"""
    
    def __init__(self, brand, num_doors, fuel_type):
        super().__init__(brand, num_doors)
        self.fuel_type = fuel_type
    
    def show_info(self):
        print(f"Brand: {self.brand}, Doors: {self.num_doors}, Fuel: {self.fuel_type}")


car = Car("Toyota", 4, "Petrol")
car.show_info()
car.start()
car.open_trunk()
car.stop()


# Example 3: Multiple Inheritance
print("\n" + "=" * 60)
print("EXAMPLE 3: Multiple Inheritance")
print("=" * 60)

class Flyer:
    """Mixin class for flying ability"""
    
    def fly(self):
        print(f"{self.name} is flying")


class Swimmer:
    """Mixin class for swimming ability"""
    
    def swim(self):
        print(f"{self.name} is swimming")


class Bird(Flyer):
    """Bird class with flying ability"""
    
    def __init__(self, name):
        self.name = name
    
    def chirp(self):
        print(f"{self.name} is chirping")


class Duck(Bird, Swimmer):
    """Duck can both fly and swim"""
    
    def quack(self):
        print(f"{self.name} is quacking")


duck = Duck("Donald")
duck.chirp()
duck.fly()
duck.swim()
duck.quack()

# Method Resolution Order (MRO)
print("\nMethod Resolution Order (MRO) for Duck class:")
print(Duck.__mro__)


# Example 4: Practical Example - Employee Hierarchy
print("\n" + "=" * 60)
print("EXAMPLE 4: Practical - Employee Management System")
print("=" * 60)

class Employee:
    """Base class for all employees"""
    
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}")
    
    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    """Manager class inherits from Employee"""
    
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size
    
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
    
    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} people")


class Developer(Employee):
    """Developer class inherits from Employee"""
    
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
    
    def show_details(self):
        super().show_details()
        print(f"Programming Language: {self.programming_language}")
    
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")


class ProjectManager(Manager, Developer):
    """Project Manager who can both manage and code"""
    
    def __init__(self, name, emp_id, salary, team_size, programming_language):
        # Initialize only the first parent's __init__
        Manager.__init__(self, name, emp_id, salary, team_size)
        self.programming_language = programming_language
    
    def show_details(self):
        Manager.show_details(self)
        print(f"Programming Language: {self.programming_language}")


# Create employees
manager = Manager("Alice Johnson", "M001", 5000, 5)
developer = Developer("Bob Smith", "D001", 4000, "Python")
project_mgr = ProjectManager("Carol White", "PM001", 6000, 3, "JavaScript")

print("Manager Details:")
manager.show_details()
manager.manage_team()

print("\nDeveloper Details:")
developer.show_details()
developer.code()

print("\nProject Manager Details:")
project_mgr.show_details()
project_mgr.manage_team()
project_mgr.code()
