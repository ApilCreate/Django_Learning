# D1
# Ask the user for a number and print whether it is positive, negative, or zero.

try:
    num = float(input("Enter a number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input")
