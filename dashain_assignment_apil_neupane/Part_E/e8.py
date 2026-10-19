# E8
# Keep asking the user to enter numbers until they enter `0`. Then print how many numbers they entered and their total.

count = 0
total = 0

while True:
    try:
        num = int(input("Enter a number (0 to stop): "))
    except ValueError:
        print("Invalid input")
        continue

    if num == 0:
        break

    count += 1
    total += num

print(f"Numbers entered: {count}")
print(f"Total: {total}")
