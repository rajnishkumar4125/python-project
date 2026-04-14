"""
OOPS CONCEPT 1: CLASSES AND OBJECTS
====================================
A class is a blueprint for creating objects.
An object is an instance of a class.
"""

# Example 1: Basic Class and Object
print("=" * 60)
print("EXAMPLE 1: Basic Class Definition")
print("=" * 60)

class Car:
    """A simple class to represent a car"""
    
    # Class variables (shared by all objects)
    total_cars = 0
    
    # Constructor - called when object is created
    def __init__(self, brand, model, year):
        """Initialize car attributes"""
        self.brand = brand      # Instance variable
        self.model = model
        self.year = year
        self.speed = 0          # Initial speed
        Car.total_cars += 1     # Increment class variable
    
    # Instance methods (functions inside class)
    def accelerate(self, increase):
        """Increase the speed of the car"""
        self.speed += increase
        print(f"{self.brand} {self.model} is now at {self.speed} km/h")
    
    def brake(self, decrease):
        """Decrease the speed of the car"""
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} {self.model} is now at {self.speed} km/h")
    
    def __str__(self):
        """Return string representation of the object"""
        return f"{self.year} {self.brand} {self.model}"
    
    @classmethod
    def get_total_cars(cls):
        """Class method - can access class variables"""
        return cls.total_cars
    
    @staticmethod
    def car_info():
        """Static method - doesn't need self or cls"""
        return "This is class method for Car"


# Creating objects (instances of the class)
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("BMW", "X5", 2024)

print(f"Car 1: {car1}")
print(f"Car 2: {car2}")
print(f"Car 3: {car3}")

# Calling instance methods
print("\nCalling methods:")
car1.accelerate(50)
car1.accelerate(30)
car1.brake(20)

# Accessing instance variables
print(f"\nCar 1 Brand: {car1.brand}")
print(f"Car 1 Speed: {car1.speed}")

# Accessing class variables and class methods
print(f"\nTotal cars created: {Car.get_total_cars()}")
print(f"Static method: {Car.car_info()}")


# Example 2: Practical Real-world Example
print("\n" + "=" * 60)
print("EXAMPLE 2: Bank Account System")
print("=" * 60)

class BankAccount:
    """Represents a bank account"""
    
    interest_rate = 0.05  # Class variable
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        print(f"Account created for {account_holder} with balance: ${self.balance}")
    
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"✓ Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > self.balance:
            print(f"❌ Insufficient balance. Available: ${self.balance}")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"✓ Withdrawn ${amount}. New balance: ${self.balance}")
    
    def apply_interest(self):
        """Apply interest to balance"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest: +${interest:.2f}")
        print(f"✓ Interest applied: ${interest:.2f}")
    
    def show_balance(self):
        """Display current balance"""
        print(f"Balance for {self.account_holder}: ${self.balance:.2f}")
    
    def show_transactions(self):
        """Display all transactions"""
        print(f"\nTransaction History for {self.account_holder}:")
        for transaction in self.transactions:
            print(f"  - {transaction}")


# Using BankAccount class
account1 = BankAccount("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.apply_interest()
account1.show_balance()
account1.show_transactions()

print("\n")
account2 = BankAccount("Jane Smith", 2000)
account2.deposit(1000)
account2.withdraw(500)
account2.apply_interest()
account2.show_balance()
account2.show_transactions()


# Example 3: Understanding the difference between class and instance
print("\n" + "=" * 60)
print("EXAMPLE 3: Class vs Instance Variables")
print("=" * 60)

class Student:
    school_name = "ABC School"  # Class variable - shared by all objects
    
    def __init__(self, name, roll_no):
        self.name = name              # Instance variable - unique to each object
        self.roll_no = roll_no
    
    def display(self):
        print(f"School: {self.school_name}, Name: {self.name}, Roll: {self.roll_no}")


student1 = Student("Alice", 1)
student2 = Student("Bob", 2)
student3 = Student("Charlie", 3)

print("Displaying all students:")
student1.display()
student2.display()
student3.display()

print(f"\nAccessing class variable:")
print(f"student1.school_name: {student1.school_name}")
print(f"Student.school_name: {Student.school_name}")

# If you modify class variable, it affects all objects
Student.school_name = "XYZ School"
print(f"\nAfter changing school name:")
print(f"student1.school_name: {student1.school_name}")
print(f"student3.school_name: {student3.school_name}")
