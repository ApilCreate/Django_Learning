# Task: build a bill calculator​

# Ask for the customer name with input()​

# Ask for the item count, convert with int()​

# Ask for the unit price, convert with float()​

# Print the receipt with an f-string, total to 2 decimals​

# Bonus: add 13% VAT with round(total * 1.13, 2)​

while True:
        name = input("Dear customer, enter your name: ")
        if name.isalpha() and len(name) > 2:
            break
        else:
            print("Enter a valid name")
while True:  
    try:
            item_count = int(input("Enter your total number of items: "))
            unit_price = float(input("Enter the price per unit: "))
            total = item_count * unit_price
            total_with_vat = round(total * 1.13, 2)
            print(f"{name}, your total is {total_with_vat}")
            break
        
    except ValueError:
            print("Enter a valid number..")
