# E10
# Loop through numbers 1 to 50. Skip numbers divisible by 3 using `continue`, and stop the loop completely when you reach a number greater than 40 that is divisible by 7, using `break`. Print the numbers that were not skipped.

for num in range(1, 51):
    if num % 3 == 0:
        continue
    if num > 40 and num % 7 == 0:
        break
    print(num)
