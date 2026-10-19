# C6
# Create a dictionary of 5 fruits and their prices per kg. Ask the user for a fruit name and print its price. If the fruit is not in the dictionary, print "Not available" (hint: use in or .get()).

prices = {
    "apple": 250,
    "banana": 120,
    "mango": 300,
    "orange": 180,
    "grapes": 350,
}

fruit = input("Enter a fruit name: ").lower()
price = prices.get(fruit)

if price is not None:
    print(f"Price: {price} per kg")
else:
    print("Not available")
