from app.models.order import *



order1 = Order("Anna", "18/01/2020", "Lavender Bundle", "Small", 1, "Ready To Ship")
order2 = Order("Kristina", "17/01/2020", "Pink Daisy Bunch", "Medium", 1, "Shipped")
order3 = Order("Charlotte", "19/01/2020","Pampas", "Large", 5, "Processing Order")
order4 = Order("Eilidh", "16/01/2020", "Eucalyptus", "Medium", 3, "Shipped")
orders = [order1, order2, order3, order4]