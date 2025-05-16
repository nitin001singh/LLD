class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Violating SRP: ShoppingCart has multiple responsibilities
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

    # 1. Calculates total price in cart
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    # 2. Violates SRP - Handles presentation (Should be separate)
    def print_invoice(self):
        print("Shopping Cart Invoice:")
        for product in self.products:
            print(f"{product.name} - Rs {product.price}")
        print(f"Total: Rs {self.calculate_total()}")

    # 3. Violates SRP - Handles persistence (Should be separate)
    def save_to_database(self):
        print("Saving shopping cart to database...")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Laptop", 50000))
    cart.add_product(Product("Mouse", 2000))

    cart.print_invoice()
    cart.save_to_database()
