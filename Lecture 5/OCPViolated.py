class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 1. ShoppingCart: Only responsible for cart-related business logic
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

    def calculate_total(self):
        return sum(product.price for product in self.products)


# 2. ShoppingCartPrinter: Only responsible for printing invoices
class ShoppingCartPrinter:
    def __init__(self, cart):
        self.cart = cart

    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for product in self.cart.get_products():
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.cart.calculate_total()}")


# 3. ShoppingCartStorage: Violates OCP by having multiple saving methods inside
class ShoppingCartStorage:
    def __init__(self, cart):
        self.cart = cart

    def save_to_sql_database(self):
        print("Saving shopping cart to SQL DB...")

    def save_to_mongo_database(self):
        print("Saving shopping cart to Mongo DB...")

    def save_to_file(self):
        print("Saving shopping cart to File...")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    printer = ShoppingCartPrinter(cart)
    printer.print_invoice()

    storage = ShoppingCartStorage(cart)
    storage.save_to_sql_database()
