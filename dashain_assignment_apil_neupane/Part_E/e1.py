# E1
# Ask the user for a number and print its multiplication table from 1 to 10 in the format `5 x 1 = 5`.

try:
    num = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input")
