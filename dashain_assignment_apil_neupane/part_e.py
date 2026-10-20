# E1
try:
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input")

# E2
all_sum = 0
even_sum = 0
for num in range(1, 101):
    all_sum += num
    if num % 2 == 0:
        even_sum += num
print(f"Sum of all numbers: {all_sum}")
print(f"Sum of even numbers: {even_sum}")

# E3
word = input("Enter a word: ")
for index in range(len(word)):
    print(f"{index} -> {word[index]}")

# E4
prices = {"kite": 150, "lattai": 400, "dhago": 250, "new clothes": 3500}
total = 0
for item, price in prices.items():
    print(f"{item}: Rs. {price}")
    total += price
print(f"Total cost: Rs. {total}")

# E5
for row in range(1, 6):
    for star in range(row):
        print("*", end=" ")
    print()

# E6
num = 10
while num >= 1:
    print(num)
    num -= 1
print("Happy Dashain!")

# E7
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

# E8
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

# E9
secret = 7
attempts = 0
while True:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Invalid input")
        continue
    attempts += 1
    if guess == secret:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

# E10
for num in range(1, 51):
    if num % 3 == 0:
        continue
    if num > 40 and num % 7 == 0:
        break
    print(num)
