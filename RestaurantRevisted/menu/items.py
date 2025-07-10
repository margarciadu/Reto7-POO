class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def total_price(self, quantity: int) -> float:
        return self._price * quantity


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size_ml: int):
        super().__init__(name, price)
        self._size_ml = size_ml

    def total_price(self, quantity: int, has_main_course: bool = False) -> float:
        tax = 0.1
        discount = 0.1 if has_main_course else 0
        return super().total_price(quantity) * (1 + tax) * (1 - discount)


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_fried: bool):
        super().__init__(name, price)
        self._is_fried = is_fried


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, origin: str):
        super().__init__(name, price)
        self._origin = origin
