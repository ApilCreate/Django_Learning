# D2
# Ask the user for a number and print whether it is even or odd.

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input")
