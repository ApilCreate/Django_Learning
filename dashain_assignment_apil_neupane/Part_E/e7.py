# E7
# Ask the user for a number and print the sum of its digits, e.g. `1234` gives `10` (hint: use `% 10` and `// 10`).

try:
    num = abs(int(input("Enter a number: ")))
    total = 0

    if num == 0:
        total = 0
    else:
        while num > 0:
            total += num % 10
            num //= 10

    print(f"Sum of digits: {total}")
except ValueError:
    print("Invalid input")
