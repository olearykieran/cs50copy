menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
lowercase_keys = [key.lower() for key in menu.keys()]

try:
    while True:
        item = input("Item: ")
        lower_item = item.lower()
        if lower_item in lowercase_keys:
            total += menu[next(key for key in menu if key.lower() == lower_item)]
        print("Total: ${:.2f}" .format(total))
except EOFError:
    print()









