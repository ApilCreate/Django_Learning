# E4
# Given `prices = {"kite": 150, "lattai": 400, "dhago": 250, "new clothes": 3500}`, loop through the dictionary, print each item with its price, and print the total cost at the end.

prices = {"kite": 150, "lattai": 400, "dhago": 250, "new clothes": 3500}
total = 0

for item, price in prices.items():
    print(f"{item}: Rs. {price}")
    total += price

print(f"Total cost: Rs. {total}")
