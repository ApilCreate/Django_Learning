# C7
# Using list(range(...)), create and print: numbers 1 to 10, even numbers from 2 to 20, numbers 10 down to 1, and multiples of 5 from 5 to 50.

nums = list(range(1, 11))
evens = list(range(2, 21, 2))
down = list(range(10, 0, -1))
fives = list(range(5, 51, 5))

print(f"Numbers 1 to 10: {nums}")
print(f"Even numbers from 2 to 20: {evens}")
print(f"Numbers 10 down to 1: {down}")
print(f"Multiples of 5 from 5 to 50: {fives}")
