from restaurant.queue import RestaurantQueue
from menu.items import *
from combos import ItemCombo

# Menu
coca_cola = Beverage("CocaCola", 5000, 350)
lemonade = Beverage("Limonada", 4000, 300)
beer = Beverage("Cerveza", 7000, 330)
water = Beverage("Agua", 2000, 500)

arepa_rellena = Appetizer("Arepa Rellena", 6000, True)
empanada = Appetizer("Empanada", 2500, True)
patacon = Appetizer("Patacón", 3000, True)
nachos = Appetizer("Nachos", 5500, False)

spaguetti = MainCourse("Spaguetti", 18000, "Italiana")
beef = MainCourse("Carne Asada", 25000, "Colombiana")
pork_loin = MainCourse("Lomo de Cerdo", 23000, "Internacional")
hamburger = MainCourse("Hamburguesa", 20000, "Americana")
bandeja_paisa = MainCourse("Bandeja Paisa", 30000, "Colombiana")

combo_paisa = ItemCombo("Combo Paisa", [
    (bandeja_paisa, 1),
    (coca_cola, 1),
    (empanada, 2)
])

combo_mexicano = ItemCombo("Combo Mexicano", [
    (nachos, 1),
    (beer, 1),
    (hamburger, 1)
])

if __name__ == "__main__":
    restaurant = RestaurantQueue()

    # Order 1
    order1 = restaurant.create_order()
    order1.add(nachos, 1)
    order1.add(spaguetti, 1)
    for item, quant in combo_paisa.items:
        order1.add(item, quant)

    # Order 2
    order2 = restaurant.create_order()
    order2.add(lemonade, 1)
    order2.add(beer, 2)
    order2.add(arepa_rellena, 2)
    for item, quant in combo_mexicano.items:
        order2.add(item, quant)

    # Order 3
    order3 = restaurant.create_order()
    order3.add(coca_cola, 2)
    order3.add(water, 2)
    order3.add(empanada, 4)
    order3.add(patacon, 1)
    order3.add(pork_loin, 1)
    order3.add(beef, 2)
    order3.add(spaguetti, 1)

    # Process orders
    restaurant.show_pending_orders()
    restaurant.process_orders_with_payment()
    restaurant.show_pending_orders()
