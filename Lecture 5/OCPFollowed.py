from abc import ABC, abstractmethod


# Product class representing any item in eCommerce
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 1. ShoppingCart: Only responsible for cart-related business logic
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products(self):
        return self.products

    def calculate_total(self):
        return sum(product.price for product in self.products)


# 2. ShoppingCartPrinter: Only responsible for printing invoices
class ShoppingCartPrinter:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for product in self.cart.get_products():
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.cart.calculate_total()}")


# 3. Persistence interface (using Abstract Base Class)
class Persistence(ABC):
    @abstractmethod
    def save(self, cart: ShoppingCart):
        pass


class SQLPersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to SQL DB...")


class MongoPersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to MongoDB...")


class FilePersistence(Persistence):
    def save(self, cart: ShoppingCart):
        print("Saving shopping cart to a file...")


# Main execution
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    printer = ShoppingCartPrinter(cart)
    printer.print_invoice()

    db = SQLPersistence()
    mongo = MongoPersistence()
    file = FilePersistence()

    db.save(cart)       # Save to SQL
    mongo.save(cart)    # Save to MongoDB
    file.save(cart)     # Save to file
