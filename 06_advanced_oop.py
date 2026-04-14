"""
OOPS FEATURES: ADVANCED CONCEPTS
=================================
Additional important OOP concepts:
1. Static Methods and Class Methods
2. Decorators
3. Operator Overloading
4. Composition vs Inheritance
5. SOLID Principles
"""

# Example 1: Static Methods and Class Methods
print("=" * 60)
print("EXAMPLE 1: Static Methods vs Class Methods")
print("=" * 60)

class MathOperations:
    """Demonstrates static and class methods"""
    
    pi = 3.14159
    instance_count = 0
    
    def __init__(self, value):
        self.value = value
        MathOperations.instance_count += 1
    
    # Static method - doesn't use self or cls
    @staticmethod
    def add(a, b):
        """Static method: doesn't need instance"""
        return a + b
    
    @staticmethod
    def is_even(number):
        """Check if number is even"""
        return number % 2 == 0
    
    # Class method - uses cls parameter
    @classmethod
    def circle_area(cls, radius):
        """Class method: can access class variables"""
        return cls.pi * radius ** 2
    
    @classmethod
    def get_instance_count(cls):
        """Get total instances created"""
        return cls.instance_count
    
    # Instance method
    def square(self):
        """Instance method: uses self"""
        return self.value ** 2


print("Static Methods:")
print(f"2 + 3 = {MathOperations.add(2, 3)}")
print(f"Is 4 even? {MathOperations.is_even(4)}")
print(f"Is 7 even? {MathOperations.is_even(7)}")

print("\nClass Methods:")
print(f"Area of circle with radius 5: {MathOperations.circle_area(5):.2f}")

obj1 = MathOperations(10)
obj2 = MathOperations(20)
obj3 = MathOperations(30)

print(f"Total instances created: {MathOperations.get_instance_count()}")
print(f"Square of 10: {obj1.square()}")


# Example 2: Decorators
print("\n" + "=" * 60)
print("EXAMPLE 2: Python Decorators")
print("=" * 60)

def my_decorator(func):
    """Simple decorator"""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper


@my_decorator
def greet(name):
    """Greeting function"""
    print(f"Hello, {name}!")
    return f"Greeted {name}"


print("Using decorator:")
result = greet("Alice")
print(f"Result: {result}")


# Decorator with arguments
def repeat_decorator(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_decorator(3)
def say_hello():
    print("Hello!")


print("\nUsing parameterized decorator:")
say_hello()


# Example 3: Composition vs Inheritance
print("\n" + "=" * 60)
print("EXAMPLE 3: Composition vs Inheritance")
print("=" * 60)

print("--- Inheritance Approach ---")

class Employee:
    """Base employee class"""
    def __init__(self, name):
        self.name = name
    
    def work(self):
        print(f"{self.name} is working")


class Manager(Employee):
    """Manager inherits from Employee"""
    def manage_team(self):
        print(f"{self.name} is managing the team")


class Developer(Employee):
    """Developer inherits from Employee"""
    def code(self):
        print(f"{self.name} is coding")


manager = Manager("John")
manager.work()
manager.manage_team()

developer = Developer("Alice")
developer.work()
developer.code()

print("\n--- Composition Approach ---")

class Task:
    """Task to be done"""
    def __init__(self, description):
        self.description = description
    
    def perform(self):
        print(f"Performing task: {self.description}")


class Person:
    """Person class using composition"""
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def assign_task(self, task):
        """Add task using composition"""
        self.tasks.append(task)
    
    def do_tasks(self):
        for task in self.tasks:
            task.perform()


person = Person("Bob")
person.assign_task(Task("Write report"))
person.assign_task(Task("Send email"))
person.assign_task(Task("Attend meeting"))

person.do_tasks()


# Example 4: Method Chaining
print("\n" + "=" * 60)
print("EXAMPLE 4: Method Chaining (Fluent Interface)")
print("=" * 60)

class QueryBuilder:
    """Build SQL queries using method chaining"""
    
    def __init__(self, table):
        self.table = table
        self.select_columns = "*"
        self.where_clause = ""
        self.order_by_clause = ""
        self.limit_value = None
    
    def select(self, columns):
        """Select columns"""
        self.select_columns = columns
        return self
    
    def where(self, condition):
        """Add where clause"""
        self.where_clause = condition
        return self
    
    def order_by(self, column, direction="ASC"):
        """Add order by clause"""
        self.order_by_clause = f"{column} {direction}"
        return self
    
    def limit(self, value):
        """Add limit clause"""
        self.limit_value = value
        return self
    
    def build(self):
        """Build and return the query"""
        query = f"SELECT {self.select_columns} FROM {self.table}"
        
        if self.where_clause:
            query += f" WHERE {self.where_clause}"
        
        if self.order_by_clause:
            query += f" ORDER BY {self.order_by_clause}"
        
        if self.limit_value:
            query += f" LIMIT {self.limit_value}"
        
        return query


# Using method chaining
query = (QueryBuilder("users")
         .select("id, name, email")
         .where("age > 18")
         .order_by("created_at", "DESC")
         .limit(10)
         .build())

print(f"Built Query:\n{query}")


# Another example with fluent interface
class StringBuilder:
    """Build strings fluently"""
    
    def __init__(self):
        self.content = ""
    
    def append(self, text):
        self.content += text
        return self
    
    def append_line(self, text):
        self.content += text + "\n"
        return self
    
    def uppercase(self):
        self.content = self.content.upper()
        return self
    
    def bold(self):
        self.content = f"**{self.content}**"
        return self
    
    def get(self):
        return self.content


text = (StringBuilder()
        .append("hello ")
        .append("world")
        .append_line("!")
        .uppercase()
        .get())

print(f"\nBuilt String:\n{text}")


# Example 5: Singleton Pattern
print("\n" + "=" * 60)
print("EXAMPLE 5: Singleton Pattern")
print("=" * 60)

class DatabaseConnection:
    """Singleton - only one instance can exist"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new DatabaseConnection instance")
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            print("Database connected")
            self.connected = True
    
    def disconnect(self):
        if self.connected:
            print("Database disconnected")
            self.connected = False


# Try to create multiple instances
db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

print(f"db1 is db2: {db1 is db2}")  # True - same instance
print(f"db2 is db3: {db2 is db3}")  # True - same instance

db1.connect()
db2.disconnect()


# Example 6: SOLID Principles - Single Responsibility
print("\n" + "=" * 60)
print("EXAMPLE 6: SOLID Principles")
print("=" * 60)

print("--- Single Responsibility Principle ---")

class User:
    """User only handles user data"""
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserValidator:
    """Separate class for validation"""
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def validate_name(name):
        return len(name) > 0


class UserRepository:
    """Separate class for data persistence"""
    def __init__(self):
        self.users = []
    
    def save(self, user):
        if UserValidator.validate_email(user.email):
            self.users.append(user)
            print(f"✓ User {user.name} saved")
            return True
        else:
            print(f"❌ Invalid email for {user.name}")
            return False
    
    def get_all(self):
        return self.users


repo = UserRepository()
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "invalid-email")
user3 = User("Charlie", "charlie@example.com")

repo.save(user1)
repo.save(user2)
repo.save(user3)

print(f"\nSaved users: {len(repo.get_all())}")


print("\n--- Open/Closed Principle ---")

class NotificationService:
    """Open for extension, closed for modification"""
    
    def __init__(self):
        self.notifiers = []
    
    def add_notifier(self, notifier):
        self.notifiers.append(notifier)
    
    def notify(self, message):
        for notifier in self.notifiers:
            notifier.send(message)


class EmailNotifier:
    """Can add new notifiers without changing NotificationService"""
    def send(self, message):
        print(f"📧 Email sent: {message}")


class SMSNotifier:
    """Another notifier"""
    def send(self, message):
        print(f"📱 SMS sent: {message}")


class SlackNotifier:
    """Yet another notifier"""
    def send(self, message):
        print(f"💬 Slack message sent: {message}")


service = NotificationService()
service.add_notifier(EmailNotifier())
service.add_notifier(SMSNotifier())
service.add_notifier(SlackNotifier())

service.notify("Important update!")
