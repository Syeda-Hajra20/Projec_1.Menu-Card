menu = {
    'classic burger': 500,
    'cheese burger': 600,
    'bbq burger': 700,
    'veggie burger': 550,
    'chicken burger': 650,
    'zinger burger': 750,
}

print("Welcome to The Burger King!")
print("We are delighted to serve you. Here is our menu:\n")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs. {price}")

order_total = 0
while True:
    item = input("\nEnter the name of the item you want to order (or 'done' to finish): ").strip().lower()

    if item == 'done':
        break
    
    if item in menu:
        order_total += menu[item]
        print(f"{item.capitalize()} has been added to your order.")
    else:
        print(f"Sorry, {item.capitalize()} is not available yet!")

print(f"\nThe total amount of items is Rs. {order_total}")
print("Thank you for ordering from The Burger King! Have a great day!")

