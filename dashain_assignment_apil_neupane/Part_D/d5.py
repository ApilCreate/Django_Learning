# D5
# Ask for three numbers and print the largest one using only if/elif/else (do not use max()).

try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))

    if first >= second and first >= third:
        largest = first
    elif second >= first and second >= third:
        largest = second
    else:
        largest = third

    print(f"Largest: {largest}")
except ValueError:
    print("Invalid input")
