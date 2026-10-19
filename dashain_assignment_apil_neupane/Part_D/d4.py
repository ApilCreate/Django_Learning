# D4
# Ask the user for a year and print whether it is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400.

try:
    year = int(input("Enter a year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
except ValueError:
    print("Invalid input")
