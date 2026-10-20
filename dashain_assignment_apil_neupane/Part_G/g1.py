# G1
# Dashain Shopping Bill
# • Store a menu of at least 6 items and prices in a dictionary.
# • Show the menu, then keep asking the user which item and how many, until they type done.
# • Print an itemised bill and the total. If the total is above Rs. 5000, give a 10% Dashain discount and print the final amount.
menu = {
    "Perfume": 1100,
    "Chocolates": 750,
    "Snacks": 250,
    "Clothes": 2500,
    "Shoes": 1700,
    "Sweets": 600
}

bill = {}
count = 0
print("Dashain Shopping Menu:")
for item, price in menu.items():
    count += 1
    print(f"{count}.{item}: Rs.{price}")

while True:
    item = input("\nEnter item name or 'done' to finish: ").title()
    if item == "Done":
        break
    if item not in menu:
        print("Invalid item name! Please choose an item from the menu.")
        continue
    try:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            bill[item] = bill.get(item, 0) + quantity
        else:
            print("Quantity must be greater than 0!")
    except ValueError:
        print("Invalid quantity! Please enter a number.")

print("\nShopping Bill:")
total = 0
item_count = 0
for item, quantity in bill.items():
    item_count += 1
    price = menu[item] * quantity
    print(f"{item_count}.{item} x {quantity} = Rs.{price}")
    total += price

print("Total: Rs.", total)

if total > 5000:
    discount = total * 0.10
    print(f"\nDashain Discount (including 10%): Rs.{discount}")
    total = total - discount

print(f"Final Amount: Rs.{total}")