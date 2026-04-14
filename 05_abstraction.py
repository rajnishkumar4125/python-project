"""
OOPS CONCEPT 5: ABSTRACTION
===========================
Abstraction means hiding implementation details and showing only the necessary features.
Using abstract classes and abstract methods to define a contract that subclasses must follow.
"""

from abc import ABC, abstractmethod


# Example 1: Abstract Base Classes
print("=" * 60)
print("EXAMPLE 1: Abstract Base Classes (ABC)")
print("=" * 60)

class Animal(ABC):
    """Abstract base class defining interface for all animals"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """Subclasses must implement this method"""
        pass
    
    @abstractmethod
    def move(self):
        """Subclasses must implement this method"""
        pass
    
    # Concrete method (optional to override)
    def introduce(self):
        """Concrete method that all subclasses inherit"""
        print(f"I am {self.name}")


class Dog(Animal):
    """Concrete implementation of Animal"""
    
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def move(self):
        print(f"{self.name} is running on four legs")


class Bird(Animal):
    """Another concrete implementation of Animal"""
    
    def make_sound(self):
        print(f"{self.name} says: Tweet! Tweet!")
    
    def move(self):
        print(f"{self.name} is flying in the sky")


class Fish(Animal):
    """Third concrete implementation of Animal"""
    
    def make_sound(self):
        print(f"{self.name} makes bubbles")
    
    def move(self):
        print(f"{self.name} is swimming")


# Create objects
dog = Dog("Buddy")
bird = Bird("Tweety")
fish = Fish("Nemo")

# All animals implement the abstract methods
dog.introduce()
dog.make_sound()
dog.move()

print()
bird.introduce()
bird.make_sound()
bird.move()

print()
fish.introduce()
fish.make_sound()
fish.move()

# Trying to instantiate abstract class would raise error:
# animal = Animal("Generic")  # TypeError: Can't instantiate abstract class


# Example 2: Abstract Methods and Properties
print("\n" + "=" * 60)
print("EXAMPLE 2: Abstract Methods and Properties")
print("=" * 60)

class Vehicle(ABC):
    """Abstract vehicle class"""
    
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
    
    @abstractmethod
    def start(self):
        """Start the vehicle"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the vehicle"""
        pass
    
    @property
    @abstractmethod
    def speed(self):
        """Get vehicle speed"""
        pass
    
    def display_info(self):
        """Concrete method"""
        print(f"Brand: {self._brand}, Model: {self._model}")


class Car(Vehicle):
    """Concrete Car class"""
    
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self._speed = 0
        self.fuel_type = fuel_type
    
    def start(self):
        print(f"Car {self._brand} engine started with {self.fuel_type}")
        self._speed = 20
    
    def stop(self):
        print(f"Car {self._brand} stopped")
        self._speed = 0
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value


class Bike(Vehicle):
    """Concrete Bike class"""
    
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self._speed = 0
        self.bike_type = bike_type
    
    def start(self):
        print(f"Bike {self._brand} engine started ({self.bike_type})")
        self._speed = 30
    
    def stop(self):
        print(f"Bike {self._brand} stopped")
        self._speed = 0
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value


car = Car("Toyota", "Camry", "Petrol")
bike = Bike("Honda", "CB500", "Cruiser")

car.display_info()
car.start()
print(f"Speed: {car.speed}")
car.speed = 100
print(f"New Speed: {car.speed}")
car.stop()

print()

bike.display_info()
bike.start()
print(f"Speed: {bike.speed}")
bike.speed = 120
print(f"New Speed: {bike.speed}")
bike.stop()


# Example 3: Abstract Methods with Multiple Implementations
print("\n" + "=" * 60)
print("EXAMPLE 3: Database Operations (Abstract Interface)")
print("=" * 60)

class Database(ABC):
    """Abstract database class"""
    
    @abstractmethod
    def connect(self):
        """Connect to database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from database"""
        pass
    
    @abstractmethod
    def query(self, sql):
        """Execute a query"""
        pass
    
    @abstractmethod
    def insert(self, data):
        """Insert data"""
        pass


class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def connect(self):
        print("✓ Connected to MySQL database")
    
    def disconnect(self):
        print("✓ Disconnected from MySQL database")
    
    def query(self, sql):
        print(f"MySQL executing: {sql}")
        return ["Row 1", "Row 2", "Row 3"]
    
    def insert(self, data):
        print(f"✓ Data inserted in MySQL: {data}")


class MongoDBDatabase(Database):
    """MongoDB implementation"""
    
    def connect(self):
        print("✓ Connected to MongoDB")
    
    def disconnect(self):
        print("✓ Disconnected from MongoDB")
    
    def query(self, sql):
        print(f"MongoDB executing query: {sql}")
        return [{"_id": 1, "name": "John"}, {"_id": 2, "name": "Jane"}]
    
    def insert(self, data):
        print(f"✓ Document inserted in MongoDB: {data}")


class PostgreSQLDatabase(Database):
    """PostgreSQL implementation"""
    
    def connect(self):
        print("✓ Connected to PostgreSQL")
    
    def disconnect(self):
        print("✓ Disconnected from PostgreSQL")
    
    def query(self, sql):
        print(f"PostgreSQL executing: {sql}")
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    
    def insert(self, data):
        print(f"✓ Record inserted in PostgreSQL: {data}")


# Using different databases without changing client code
def process_database(db: Database):
    """Function works with any database implementation"""
    db.connect()
    db.query("SELECT * FROM users")
    db.insert({"name": "John", "age": 30})
    db.disconnect()


print("Using MySQL:")
process_database(MySQLDatabase())

print("\nUsing MongoDB:")
process_database(MongoDBDatabase())

print("\nUsing PostgreSQL:")
process_database(PostgreSQLDatabase())


# Example 4: Complex Abstraction - Payment Processing System
print("\n" + "=" * 60)
print("EXAMPLE 4: Payment Processing System (Advanced Abstraction)")
print("=" * 60)

class PaymentProcessor(ABC):
    """Abstract payment processor"""
    
    def __init__(self, amount):
        self.amount = amount
        self.transaction_id = None
    
    @abstractmethod
    def validate(self):
        """Validate payment details"""
        pass
    
    @abstractmethod
    def charge(self):
        """Charge the payment"""
        pass
    
    @abstractmethod
    def refund(self):
        """Refund the payment"""
        pass
    
    @abstractmethod
    def get_status(self):
        """Get payment status"""
        pass
    
    def process(self):
        """Template method - defines payment process"""
        if self.validate():
            if self.charge():
                print(f"✓ Payment processed successfully. Amount: ${self.amount}")
                return True
        print("❌ Payment processing failed")
        return False


class StripePayment(PaymentProcessor):
    """Stripe payment implementation"""
    
    def __init__(self, amount, card_token):
        super().__init__(amount)
        self.card_token = card_token
    
    def validate(self):
        print("Validating with Stripe...")
        return len(self.card_token) > 10
    
    def charge(self):
        print(f"Charging ${self.amount} to Stripe card")
        self.transaction_id = "St_" + "12345"
        return True
    
    def refund(self):
        print(f"Refunding ${self.amount} via Stripe")
        return True
    
    def get_status(self):
        return "Stripe transaction completed"


class SquarePayment(PaymentProcessor):
    """Square payment implementation"""
    
    def __init__(self, amount, location_id):
        super().__init__(amount)
        self.location_id = location_id
    
    def validate(self):
        print("Validating with Square...")
        return len(self.location_id) > 5
    
    def charge(self):
        print(f"Charging ${self.amount} via Square")
        self.transaction_id = "Sq_" + "54321"
        return True
    
    def refund(self):
        print(f"Refunding ${self.amount} via Square")
        return True
    
    def get_status(self):
        return "Square transaction completed"


# Process different payment systems
stripe_payment = StripePayment(100, "tok_1234567890")
stripe_payment.process()
print(f"Status: {stripe_payment.get_status()}")

print()

square_payment = SquarePayment(50, "location_abc123")
square_payment.process()
print(f"Status: {square_payment.get_status()}")
