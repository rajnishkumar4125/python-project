"""
OOPS CONCEPT 4: POLYMORPHISM
============================
Polymorphism means "many forms". Same method name can have different behaviors
in different classes. There are two types:
1. Method Overriding (Compile-time/Static)
2. Method Overloading (Runtime/Dynamic)
"""

# Example 1: Method Overriding
print("=" * 60)
print("EXAMPLE 1: Method Overriding (Runtime Polymorphism)")
print("=" * 60)

class Shape:
    """Base class for shapes"""
    
    def area(self):
        print("Calculating area of shape")
    
    def perimeter(self):
        print("Calculating perimeter of shape")


class Rectangle(Shape):
    """Rectangle class overrides area() and perimeter()"""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Override parent method"""
        result = self.length * self.width
        print(f"Rectangle Area: {result}")
        return result
    
    def perimeter(self):
        """Override parent method"""
        result = 2 * (self.length + self.width)
        print(f"Rectangle Perimeter: {result}")
        return result


class Circle(Shape):
    """Circle class overrides area() and perimeter()"""
    
    def __init__(self, radius):
        self.radius = radius
    
    import math
    
    def area(self):
        """Override parent method"""
        result = 3.14159 * self.radius ** 2
        print(f"Circle Area: {result:.2f}")
        return result
    
    def perimeter(self):
        """Override parent method"""
        result = 2 * 3.14159 * self.radius
        print(f"Circle Circumference: {result:.2f}")
        return result


class Triangle(Shape):
    """Triangle class overrides area()"""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        """Override parent method"""
        result = 0.5 * self.base * self.height
        print(f"Triangle Area: {result}")
        return result
    
    def perimeter(self):
        print("Triangle perimeter calculation depends on all 3 sides")


# Using polymorphism - same method name, different behaviors
shapes = [Rectangle(5, 4), Circle(3), Triangle(10, 8)]

print("Demonstrating Polymorphism:")
for shape in shapes:
    shape.area()
    shape.perimeter()
    print()


# Example 2: Duck Typing (Python's Polymorphism)
print("=" * 60)
print("EXAMPLE 2: Duck Typing Polymorphism")
print("=" * 60)

class Duck:
    """Duck class"""
    
    def quack(self):
        print("Duck quacks: Quack! Quack!")
    
    def fly(self):
        print("Duck is flying")


class Chicken:
    """Chicken class"""
    
    def quack(self):
        print("Chicken makes sound: Bawk! Bawk!")
    
    def fly(self):
        print("Chicken flies a little bit")


def make_it_quack(bird):
    """Function that works with any object that has quack() method"""
    bird.quack()


def make_it_fly(bird):
    """Function that works with any object that has fly() method"""
    bird.fly()


# Any object with quack() method can be passed
duck = Duck()
chicken = Chicken()

make_it_quack(duck)
make_it_quack(chicken)

print()
make_it_fly(duck)
make_it_fly(chicken)


# Example 3: Operator Overloading
print("\n" + "=" * 60)
print("EXAMPLE 3: Operator Overloading")
print("=" * 60)

class Vector:
    """Vector class demonstrating operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """Overload < operator - compare magnitudes"""
        this_magnitude = (self.x ** 2 + self.y ** 2) ** 0.5
        other_magnitude = (other.x ** 2 + other.y ** 2) ** 0.5
        return this_magnitude < other_magnitude


v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Addition
v3 = v1 + v2
print(f"v1 + v2 = {v3}")

# Subtraction
v4 = v1 - v2
print(f"v1 - v2 = {v4}")

# Multiplication
v5 = v1 * 2
print(f"v1 * 2 = {v5}")

# Equality
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(2, 3): {v1 == Vector(2, 3)}")

# Less than
print(f"v1 < v2: {v1 < v2}")


# Example 4: Practical Polymorphism Example - Payment System
print("\n" + "=" * 60)
print("EXAMPLE 4: Practical - Payment Gateway System")
print("=" * 60)

class PaymentGateway:
    """Base payment gateway class"""
    
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        raise NotImplementedError("Subclass must implement pay() method")
    
    def validate(self):
        raise NotImplementedError("Subclass must implement validate() method")


class CreditCard(PaymentGateway):
    """Credit Card Payment"""
    
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def validate(self):
        if len(self.card_number) == 16 and self.amount > 0:
            return True
        return False
    
    def pay(self):
        if self.validate():
            print(f"✓ Payment of ${self.amount} processed via Credit Card")
            print(f"  Card Number: ****{self.card_number[-4:]}")
            return True
        else:
            print("❌ Credit Card payment failed")
            return False


class PayPal(PaymentGateway):
    """PayPal Payment"""
    
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def validate(self):
        if "@" in self.email and self.amount > 0:
            return True
        return False
    
    def pay(self):
        if self.validate():
            print(f"✓ Payment of ${self.amount} processed via PayPal")
            print(f"  Email: {self.email}")
            return True
        else:
            print("❌ PayPal payment failed")
            return False


class Bitcoin(PaymentGateway):
    """Bitcoin Payment"""
    
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address
    
    def validate(self):
        if len(self.wallet_address) >= 26 and self.amount > 0:
            return True
        return False
    
    def pay(self):
        if self.validate():
            print(f"✓ Payment of ${self.amount} processed via Bitcoin")
            print(f"  Wallet: {self.wallet_address[:10]}...")
            return True
        else:
            print("❌ Bitcoin payment failed")
            return False


# Process different payment methods polymorphically
def process_payment(payment_gateway):
    """Function that works with any payment gateway"""
    payment_gateway.pay()


print("Processing payments with different gateways:\n")

# All payment methods work through the same interface
payments = [
    CreditCard(100, "1234567890123456"),
    PayPal(50, "user@example.com"),
    Bitcoin(25, "1A1z7agoat2YTIQW8YGWAX7GsW7sMR8VhH"),
    CreditCard(200, "1234"),  # Invalid
]

for payment in payments:
    process_payment(payment)
    print()


# Example 5: Method Overloading (Python's way)
print("=" * 60)
print("EXAMPLE 5: Method Overloading with Default Arguments")
print("=" * 60)

class Calculator:
    """Calculator with overloaded methods"""
    
    def add(self, a, b, c=0, d=0):
        """Add 2-4 numbers"""
        return a + b + c + d
    
    def multiply(self, *args):
        """Multiply any number of arguments"""
        result = 1
        for num in args:
            result *= num
        return result


calc = Calculator()

print(f"add(5, 3) = {calc.add(5, 3)}")
print(f"add(5, 3, 2) = {calc.add(5, 3, 2)}")
print(f"add(5, 3, 2, 1) = {calc.add(5, 3, 2, 1)}")

print(f"\nmultiply(2, 3) = {calc.multiply(2, 3)}")
print(f"multiply(2, 3, 4) = {calc.multiply(2, 3, 4)}")
print(f"multiply(2, 3, 4, 5) = {calc.multiply(2, 3, 4, 5)}")
