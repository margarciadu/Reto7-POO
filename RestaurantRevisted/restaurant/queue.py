from queue import Queue
from payment.methods import Card, Cash

class RestaurantQueue:
    def __init__(self):
        self.order_queue = Queue()
        self.completed_orders = []

    def create_order(self):
        from order.order import Order
        order = Order()
        self.order_queue.put(order)
        return order

    def next_order(self):
        if not self.order_queue.empty():
            order = self.order_queue.get()
            self.completed_orders.append(order)
            return order
        print("No hay pedidos pendientes.")
        return None

    def show_pending_orders(self):
        print(f"Pedidos pendientes en cola: {self.order_queue.qsize()}")

    def process_orders_with_payment(self):
        while not self.order_queue.empty():
            order = self.next_order()
            order.summary()
            amount = order.apply_discount()

            print("\nSelección de método de pago:")
            method = input("Elige (1: Tarjeta, 2: Efectivo): ")
            if method == "1":
                number = input("Número de tarjeta: ")
                cvv = input("CVV: ")
                payment = Card(number, cvv)
            elif method == "2":
                delivered = float(input(f"Ingrese monto entregado (Total: ${amount:,.2f}): "))
                payment = Cash(delivered)
            else:
                print("Método inválido. Se omite este pago.")
                continue

            payment.pagar(amount)
