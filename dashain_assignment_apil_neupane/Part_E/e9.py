# E9
# Number guessing game: set `secret = 7`. Keep asking the user to guess. Print "Too high" or "Too low" after each wrong guess, and when they get it right, print how many attempts they took.

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
