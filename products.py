"""
    Author: Ahmad
    This is the Product class"""

class Product:
    """ Product class"""
    def __init__(self, name, price, quantity):

        if not name or not isinstance(name, str):
            raise ValueError("Product Name must be a non-empty string")

        if not isinstance(price, (int, float)) and price <= 0:
            raise ValueError("Product Price must be a non-negative integer")

        if not isinstance(quantity, int) and quantity <= 0:
            raise ValueError("Product Quantity must be a non-negative integer")

        self.name = name
        self.price = price
        self.quantity = quantity
        self._active = True

    def get_quantity(self) -> int:
        """ Returns the quantity of the product """
        return self.quantity

    def set_quantity(self, quantity):
        """ Sets the quantity of the product """
        self.quantity = quantity
        if self.quantity == 0:
            self._active = False

    def is_active(self) -> bool:
        """ Returns whether the product is active """
        return self._active

    def activate(self):
        """ Activate the product """
        self._active = True

    def deactivate(self):
        """ Deactivate the product """
        self._active = False

    def show(self):
        """ Show the product """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """ Buy the product """
        if quantity > self.quantity:
            print(f"Not enough stock. Available: {self.quantity}")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
