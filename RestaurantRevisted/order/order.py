import random
from menu.items import Beverage, MainCourse

class Order:
    def __init__(self):
        self.order_number = random.randint(1000, 9999)
        self.items = []

    def add(self, item, quantity: int):
        self.items.append((item, quantity))

    def has_main_course(self):
        return any(isinstance(item, MainCourse) for item, _ in self.items)

    def total(self) -> float:
        has_main = self.has_main_course()
        return sum(item.total_price(quant, has_main) if isinstance(item, Beverage)
                   else item.total_price(quant) for item, quant in self.items)

    def apply_discount(self) -> float:
        subtotal = self.total()
        if subtotal > 80000:
            return subtotal * 0.85
        elif subtotal > 50000:
            return subtotal * 0.90
        elif subtotal > 30000:
            return subtotal * 0.95
        return subtotal

    def summary(self):
        print(f"\nPedido #{self.order_number}")
        print("Resumen del pedido:")
        has_main = self.has_main_course()
        for item, quant in self.items:
            price = item.total_price(quant, has_main) if isinstance(item, Beverage) else item.total_price(quant)
            print(f" - {item.get_name()} x{quant} = ${price:,.2f}")
        print(f"\nSubtotal: ${self.total():,.2f}")
        print(f"Total con descuento: ${self.apply_discount():,.2f}")
