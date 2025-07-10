class PaymentMethod:
    def pagar(self, amount):
        raise NotImplementedError("Subclases deben implementar pagar()")


class Card(PaymentMethod):
    def __init__(self, number, cvv):
        self.number = number
        self.cvv = cvv

    def pagar(self, amount):
        print(f"Pagando ${amount:,.2f} con tarjeta terminada en {self.number[-4:]}")


class Cash(PaymentMethod):
    def __init__(self, delivered_amount):
        self.delivered_amount = delivered_amount

    def pagar(self, amount):
        if self.delivered_amount >= amount:
            print(f"Pago en efectivo aceptado. Cambio: ${self.delivered_amount - amount:,.2f}")
        else:
            print(f"Fondos insuficientes. Faltan ${amount - self.delivered_amount:,.2f}")
