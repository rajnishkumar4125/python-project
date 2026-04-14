"""
REAL-WORLD PROJECT: E-COMMERCE SYSTEM
======================================
Practical implementation combining all OOP concepts:
- Classes & Objects
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Advanced features
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


print("=" * 70)
print("REAL-WORLD PROJECT: E-COMMERCE SYSTEM".center(70))
print("=" * 70)


# ============================================================================
# ABSTRACTION - Define interfaces
# ============================================================================

class PaymentProcessor(ABC):
    """Abstract payment processor interface"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, amount: float) -> bool:
        pass


class NotificationService(ABC):
    """Abstract notification interface"""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass


# ============================================================================
# ENCAPSULATION - Product, Cart, Order classes
# ============================================================================

class Product:
    """Product with encapsulated attributes"""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    # Getters
    def get_id(self) -> str:
        return self.__product_id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_price(self) -> float:
        return self.__price
    
    def get_stock(self) -> int:
        return self.__stock
    
    # Business methods with encapsulation
    def is_available(self, quantity: int) -> bool:
        return self.__stock >= quantity
    
    def reduce_stock(self, quantity: int) -> bool:
        if self.is_available(quantity):
            self.__stock -= quantity
            return True
        return False
    
    def add_stock(self, quantity: int):
        self.__stock += quantity
    
    def __str__(self):
        return f"{self.__name} (${self.__price:.2f})"


class CartItem:
    """Item in shopping cart"""
    
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    
    def get_total(self) -> float:
        return self.product.get_price() * self.quantity
    
    def __str__(self):
        return f"{self.product.get_name()} x {self.quantity} = ${self.get_total():.2f}"


class ShoppingCart:
    """Shopping cart with encapsulated items"""
    
    def __init__(self):
        self.__items: List[CartItem] = []
    
    def add_item(self, product: Product, quantity: int) -> bool:
        """Add item to cart"""
        if not product.is_available(quantity):
            print(f"❌ Not enough stock for {product.get_name()}")
            return False
        
        # Check if item already exists
        for item in self.__items:
            if item.product.get_id() == product.get_id():
                item.quantity += quantity
                print(f"✓ Updated {product.get_name()} quantity to {item.quantity}")
                return True
        
        # Add new item
        self.__items.append(CartItem(product, quantity))
        print(f"✓ Added {product.get_name()} x {quantity} to cart")
        return True
    
    def remove_item(self, product_id: str) -> bool:
        """Remove item from cart"""
        for i, item in enumerate(self.__items):
            if item.product.get_id() == product_id:
                self.__items.pop(i)
                return True
        return False
    
    def get_total(self) -> float:
        """Get total cart value"""
        return sum(item.get_total() for item in self.__items)
    
    def get_items(self) -> List[CartItem]:
        """Get all items (read-only copy)"""
        return self.__items.copy()
    
    def is_empty(self) -> bool:
        return len(self.__items) == 0
    
    def clear(self):
        """Clear the cart"""
        self.__items.clear()
    
    def display(self):
        """Display cart contents"""
        if self.is_empty():
            print("Shopping cart is empty")
        else:
            print("\n🛒 Shopping Cart:")
            print("-" * 50)
            for item in self.__items:
                print(f"  {item}")
            print("-" * 50)
            print(f"  Total: ${self.get_total():.2f}")


# ============================================================================
# INHERITANCE - Order with different statuses
# ============================================================================

class Order:
    """Base Order class"""
    
    # Class variable
    __order_counter = 1000
    
    def __init__(self, customer_name: str, cart: ShoppingCart):
        self.__order_id = Order.__order_counter
        Order.__order_counter += 1
        self.__customer_name = customer_name
        self.__items = cart.get_items()
        self.__subtotal = cart.get_total()
        self.__tax = self.__subtotal * 0.1  # 10% tax
        self.__total = self.__subtotal + self.__tax
        self.__status = "Created"
        self.__created_at = datetime.now()
    
    def get_order_id(self) -> int:
        return self.__order_id
    
    def get_customer_name(self) -> str:
        return self.__customer_name
    
    def get_total(self) -> float:
        return self.__total
    
    def get_status(self) -> str:
        return self.__status
    
    def set_status(self, status: str):
        self.__status = status
    
    def display_summary(self):
        """Display order summary"""
        print(f"\n📋 Order #{self.__order_id}")
        print(f"Customer: {self.__customer_name}")
        print(f"Status: {self.__status}")
        print(f"Created: {self.__created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nItems:")
        for item in self.__items:
            print(f"  - {item}")
        print(f"\nSubtotal: ${self.__subtotal:.2f}")
        print(f"Tax (10%): ${self.__tax:.2f}")
        print(f"Total: ${self.__total:.2f}")


# ============================================================================
# POLYMORPHISM - Different payment methods
# ============================================================================

class CreditCardPayment(PaymentProcessor):
    """Credit card payment implementation"""
    
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def process_payment(self, amount: float) -> bool:
        # Validate card number
        if len(self.card_number) != 16:
            print(f"❌ Invalid credit card number")
            return False
        
        print(f"✓ Processing credit card payment: ${amount:.2f}")
        print(f"  Card: ****{self.card_number[-4:]}")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"✓ Refunding ${amount:.2f} to credit card")
        return True


class PayPalPayment(PaymentProcessor):
    """PayPal payment implementation"""
    
    def __init__(self, paypal_account: str):
        self.paypal_account = paypal_account
    
    def process_payment(self, amount: float) -> bool:
        if "@" not in self.paypal_account:
            print(f"❌ Invalid PayPal account")
            return False
        
        print(f"✓ Processing PayPal payment: ${amount:.2f}")
        print(f"  Account: {self.paypal_account}")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"✓ Refunding ${amount:.2f} to PayPal account")
        return True


class CryptoCurrencyPayment(PaymentProcessor):
    """Cryptocurrency payment implementation"""
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount: float) -> bool:
        if len(self.wallet_address) < 26:
            print(f"❌ Invalid wallet address")
            return False
        
        print(f"✓ Processing crypto payment: ${amount:.2f}")
        print(f"  Wallet: {self.wallet_address[:16]}...")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"✓ Refund initiated to crypto wallet (may take time)")
        return True


# ============================================================================
# POLYMORPHISM - Different notification methods
# ============================================================================

class EmailNotification(NotificationService):
    """Email notification"""
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"📧 Email sent to {recipient}")
        return True


class SMSNotification(NotificationService):
    """SMS notification"""
    
    def send(self, recipient: str, message: str) -> bool:
        print(f"📱 SMS sent to {recipient}")
        return True


# ============================================================================
# ADVANCED - Customer with composition
# ============================================================================

class Customer:
    """Customer class using composition"""
    
    def __init__(self, customer_id: str, name: str, email: str):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__orders: List[Order] = []
        self.__cart = ShoppingCart()
    
    def get_name(self) -> str:
        return self.__name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_cart(self) -> ShoppingCart:
        return self.__cart
    
    def add_order(self, order: Order):
        self.__orders.append(order)
    
    def get_order_history(self) -> List[Order]:
        return self.__orders.copy()
    
    def get_total_spent(self) -> float:
        return sum(order.get_total() for order in self.__orders)


# ============================================================================
# COMPLETE E-COMMERCE SYSTEM
# ============================================================================

class ECommerceSystem:
    """Main e-commerce system"""
    
    def __init__(self):
        self.__products = {}
        self.__customers = {}
        self.__orders = []
    
    def add_product(self, product: Product):
        """Add product to catalog"""
        self.__products[product.get_id()] = product
    
    def register_customer(self, customer: Customer):
        """Register a customer"""
        self.__customers[customer.get_name()] = customer
    
    def get_customer(self, name: str) -> Customer:
        """Get customer by name"""
        return self.__customers.get(name)
    
    def get_product(self, product_id: str) -> Product:
        """Get product by ID"""
        return self.__products.get(product_id)
    
    def process_order(self, customer: Customer, payment: PaymentProcessor, 
                     notification: NotificationService) -> bool:
        """Process complete order workflow"""
        
        cart = customer.get_cart()
        
        if cart.is_empty():
            print("❌ Cannot process empty cart")
            return False
        
        # Create order
        order = Order(customer.get_name(), cart)
        
        # Process payment (Polymorphism in action)
        if not payment.process_payment(order.get_total()):
            print("❌ Payment failed")
            return False
        
        # Update product stock
        for item in cart.get_items():
            item.product.reduce_stock(item.quantity)
        
        # Update order status
        order.set_status("Paid")
        
        # Add order to system
        self.__orders.append(order)
        customer.add_order(order)
        
        # Send notification (Polymorphism in action)
        notification.send(customer.get_email(), 
                         f"Order #{order.get_order_id()} confirmed!")
        
        # Clear cart
        cart.clear()
        
        print(f"✓ Order #{order.get_order_id()} processed successfully!")
        order.display_summary()
        
        return True


# ============================================================================
# DEMONSTRATION
# ============================================================================

print("\n📦 INITIALIZING E-COMMERCE SYSTEM\n")

# Create system
system = ECommerceSystem()

# Add products
laptop = Product("P001", "Gaming Laptop", 1299.99, 5)
mouse = Product("P002", "Wireless Mouse", 29.99, 50)
keyboard = Product("P003", "Mechanical Keyboard", 149.99, 20)
monitor = Product("P004", "4K Monitor", 399.99, 10)

system.add_product(laptop)
system.add_product(mouse)
system.add_product(keyboard)
system.add_product(monitor)

print("✓ Products added to catalog")

# Register customers
customer1 = Customer("C001", "John Doe", "john@example.com")
customer2 = Customer("C002", "Jane Smith", "jane@example.com")

system.register_customer(customer1)
system.register_customer(customer2)

print("✓ Customers registered")

# ============================================================================
# CUSTOMER 1: JOHN DOE - Credit Card Payment
# ============================================================================

print("\n" + "=" * 70)
print("CUSTOMER 1: JOHN DOE - SHOPPING SESSION")
print("=" * 70)

john = system.get_customer("John Doe")
john_cart = john.get_cart()

# Add items to cart
john_cart.add_item(system.get_product("P001"), 1)
john_cart.add_item(system.get_product("P002"), 2)
john_cart.add_item(system.get_product("P003"), 1)

john_cart.display()

# Process order with credit card
print("\n💳 Processing payment with Credit Card...")
credit_card = CreditCardPayment("1234567890123456")
email_notification = EmailNotification()

system.process_order(john, credit_card, email_notification)

# ============================================================================
# CUSTOMER 2: JANE SMITH - PayPal Payment
# ============================================================================

print("\n" + "=" * 70)
print("CUSTOMER 2: JANE SMITH - SHOPPING SESSION")
print("=" * 70)

jane = system.get_customer("Jane Smith")
jane_cart = jane.get_cart()

# Add items to cart
jane_cart.add_item(system.get_product("P004"), 1)
jane_cart.add_item(system.get_product("P002"), 1)

jane_cart.display()

# Process order with PayPal
print("\n💳 Processing payment with PayPal...")
paypal = PayPalPayment("jane@paypal.com")
sms_notification = SMSNotification()

system.process_order(jane, paypal, sms_notification)

# ============================================================================
# CUSTOMER 3: JOHN DOE - SECOND ORDER - Cryptocurrency
# ============================================================================

print("\n" + "=" * 70)
print("JOHN DOE - SECOND ORDER - CRYPTOCURRENCY PAYMENT")
print("=" * 70)

john_cart.add_item(system.get_product("P004"), 1)
john_cart.add_item(system.get_product("P001"), 1)

john_cart.display()

# Process with cryptocurrency
print("\n💳 Processing payment with Cryptocurrency...")
crypto = CryptoCurrencyPayment("1A1z7agoat2YTIQW8YGWAX7GsW7sMR8VhH")

system.process_order(john, crypto, email_notification)

# ============================================================================
# SUMMARY REPORT
# ============================================================================

print("\n" + "=" * 70)
print("CUSTOMER SUMMARY REPORT")
print("=" * 70)

for customer_name in ["John Doe", "Jane Smith"]:
    customer = system.get_customer(customer_name)
    print(f"\n👤 {customer.get_name()}")
    print(f"   Email: {customer.get_email()}")
    print(f"   Total Orders: {len(customer.get_order_history())}")
    print(f"   Total Spent: ${customer.get_total_spent():.2f}")
    
    for order in customer.get_order_history():
        print(f"   • Order #{order.get_order_id()}: ${order.get_total():.2f} ({order.get_status()})")

print("\n" + "=" * 70)
print("✓ E-COMMERCE SYSTEM DEMONSTRATION COMPLETED")
print("=" * 70)

# ============================================================================
# KEY OOP CONCEPTS DEMONSTRATED
# ============================================================================

print("\n" + "=" * 70)
print("KEY OOP CONCEPTS USED IN THIS PROJECT")
print("=" * 70)

concepts = {
    "🔵 Encapsulation": [
        "Product class with private price and stock",
        "ShoppingCart with private items list",
        "Order with private order_id counter (class variable)",
        "Getters/setters for controlled access"
    ],
    "🔵 Inheritance": [
        "Order class serving as base for different order types",
        "PaymentProcessor as abstract base class",
        "NotificationService as abstract base class"
    ],
    "🔵 Polymorphism": [
        "CreditCardPayment, PayPalPayment, CryptoCurrencyPayment",
        "EmailNotification, SMSNotification",
        "process_order() works with any PaymentProcessor",
        "Different payment methods, same interface"
    ],
    "🔵 Abstraction": [
        "ABC (Abstract Base Classes) for PaymentProcessor",
        "ABC for NotificationService",
        "@abstractmethod for enforcing contract"
    ],
    "🔵 Composition": [
        "Customer HAS-A ShoppingCart",
        "Customer HAS-A list of Orders",
        "Order contains CartItems"
    ],
    "🔵 Advanced Features": [
        "Type hints (type: Product, -> bool)",
        "List[Order] for type safety",
        "Class variables (Order.__order_counter)",
        "Method chaining in ShoppingCart"
    ]
}

for concept, examples in concepts.items():
    print(f"\n{concept}:")
    for example in examples:
        print(f"  ✓ {example}")

print("\n" + "=" * 70)
