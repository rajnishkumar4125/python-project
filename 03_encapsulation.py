"""
OOPS CONCEPT 3: ENCAPSULATION
=============================
Encapsulation means bundling data and methods together, and hiding internal details.
Using private variables and methods to protect data integrity.
"""

# Example 1: Basic Encapsulation with Public and Private Variables
print("=" * 60)
print("EXAMPLE 1: Public and Private Variables")
print("=" * 60)

class BankAccount:
    """Demonstrates encapsulation in a bank account"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public variable
        self._account_number = "1234567890"   # Protected (_) by convention
        self.__balance = initial_balance      # Private (__) variable
        self.__pin = "1234"                   # Private PIN
        self.__transactions = []
    
    # Public method to access private data safely
    def deposit(self, amount):
        """Safe deposit method with validation"""
        if amount <= 0:
            print("❌ Deposit amount must be positive")
            return False
        
        self.__balance += amount
        self.__transactions.append(f"Deposit: +${amount}")
        print(f"✓ Deposited ${amount}. New balance: ${self.get_balance()}")
        return True
    
    def withdraw(self, amount, pin):
        """Safe withdrawal with PIN verification"""
        if not self.__verify_pin(pin):
            print("❌ Invalid PIN!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient balance. Available: ${self.__balance}")
            return False
        
        if amount <= 0:
            print("❌ Withdrawal amount must be positive")
            return False
        
        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: -${amount}")
        print(f"✓ Withdrawn ${amount}. New balance: ${self.__balance}")
        return True
    
    # Private method - cannot be called from outside
    def __verify_pin(self, pin):
        """Private method to verify PIN"""
        return pin == self.__pin
    
    # Getter method for private variable
    def get_balance(self):
        """Get current balance"""
        return self.__balance
    
    # Getter method for transactions
    def get_transactions(self):
        """Get transaction history"""
        return self.__transactions.copy()
    
    def show_statement(self):
        """Show account statement"""
        print(f"\nAccount Statement for {self.account_holder}")
        print(f"Current Balance: ${self.__balance}")
        print("Transactions:")
        for transaction in self.__transactions:
            print(f"  - {transaction}")


# Using BankAccount with encapsulation
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200, "1234")  # Correct PIN
account.withdraw(100, "0000")  # Wrong PIN
print(f"Current Balance: ${account.get_balance()}")

# Try to access private variable (will cause error if uncommented)
# print(account.__balance)  # This will raise AttributeError
print(f"Account Holder: {account.account_holder}")  # This works (public)

account.show_statement()


# Example 2: Using Properties (Getters and Setters)
print("\n" + "=" * 60)
print("EXAMPLE 2: Properties with @property and @setter")
print("=" * 60)

class Student:
    """Student class with property decorators"""
    
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected
        self.__gpa = 0.0  # Private
    
    # Property getter
    @property
    def age(self):
        """Get age"""
        return self._age
    
    # Property setter with validation
    @property
    def gpa(self):
        """Get GPA"""
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        """Set GPA with validation"""
        if 0 <= value <= 4.0:
            self.__gpa = value
            print(f"✓ GPA set to {value}")
        else:
            print(f"❌ GPA must be between 0 and 4.0")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.__gpa}")


student = Student("Alice", 20)
print(f"Student age: {student.age}")

student.gpa = 3.8
student.display()

student.gpa = 5.0  # Invalid GPA
student.gpa = 3.5  # Valid GPA
student.display()


# Example 3: Complete Encapsulation Example - Car Class
print("\n" + "=" * 60)
print("EXAMPLE 3: Car Class with Full Encapsulation")
print("=" * 60)

class Car:
    """Car class demonstrating full encapsulation"""
    
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0
        self.__engine_on = False
        self.__fuel_level = 100  # 0-100%
    
    # Getters
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_speed(self):
        return self.__speed
    
    def get_fuel_level(self):
        return self.__fuel_level
    
    # Public methods
    def start_engine(self):
        """Start the car engine"""
        if self.__fuel_level > 0:
            self.__engine_on = True
            print(f"✓ {self.__brand} {self.__model} engine started")
        else:
            print("❌ No fuel! Cannot start engine")
    
    def stop_engine(self):
        """Stop the car engine"""
        if self.__engine_on:
            self.__speed = 0
            self.__engine_on = False
            print(f"✓ {self.__brand} {self.__model} engine stopped")
        else:
            print("❌ Engine is already off")
    
    def accelerate(self, amount=10):
        """Increase speed"""
        if not self.__engine_on:
            print("❌ Start the engine first!")
            return
        
        if self.__fuel_level <= 0:
            print("❌ Out of fuel!")
            self.stop_engine()
            return
        
        self.__speed += amount
        self.__fuel_level -= (amount * 0.5)  # Consume fuel
        
        if self.__fuel_level < 0:
            self.__fuel_level = 0
        
        print(f"✓ Accelerating... Speed: {self.__speed} km/h, Fuel: {self.__fuel_level:.1f}%")
    
    def brake(self, amount=10):
        """Decrease speed"""
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0
        print(f"✓ Braking... Speed: {self.__speed} km/h")
    
    def refuel(self):
        """Fill up fuel tank"""
        self.__fuel_level = 100
        print("✓ Tank refueled to 100%")
    
    def show_status(self):
        """Display car status"""
        status = "ON" if self.__engine_on else "OFF"
        print(f"\n{self.__year} {self.__brand} {self.__model}")
        print(f"Engine: {status}")
        print(f"Speed: {self.__speed} km/h")
        print(f"Fuel: {self.__fuel_level:.1f}%")


# Using Car with encapsulation
car = Car("BMW", "X5", 2023)
car.show_status()

car.accelerate()  # Try without starting
car.start_engine()
car.show_status()

car.accelerate(20)
car.accelerate(30)
car.show_status()

car.brake(25)
car.show_status()

car.accelerate(50)
car.accelerate(50)
car.show_status()

car.refuel()
car.show_status()

car.stop_engine()
car.show_status()


# Example 4: Data Validation through Encapsulation
print("\n" + "=" * 60)
print("EXAMPLE 4: Email Validation with Encapsulation")
print("=" * 60)

class User:
    """User class with email validation"""
    
    def __init__(self, username, email):
        self.username = username
        self.set_email(email)  # Use setter for validation
    
    def set_email(self, email):
        """Set email with validation"""
        if self.__is_valid_email(email):
            self.__email = email
            print(f"✓ Email set: {email}")
        else:
            print(f"❌ Invalid email format: {email}")
    
    def get_email(self):
        """Get email"""
        return self.__email
    
    @staticmethod
    def __is_valid_email(email):
        """Validate email format"""
        return "@" in email and "." in email


user = User("john_doe", "john@example.com")
user.set_email("invalid_email")
user.set_email("jane@example.co.uk")

print(f"Username: {user.username}")
print(f"Email: {user.get_email()}")
