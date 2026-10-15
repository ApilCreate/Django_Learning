# A3
# Ask the user for the price of one kite (it may have decimals, e.g. 45.50) and how many kites they want. Print the total cost as a float and also rounded to a whole number with int().

ask = float(input("Enter the price for a single kite: "))
quantity = int(input("How many kites do they want?: "))

total_cost = ask * quantity

print(f"The total cost as a float is: {total_cost}")
print(f"The rounded total cost is: {int(round(total_cost))}")
