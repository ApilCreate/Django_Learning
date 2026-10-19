# E2
# Print the sum of all numbers from 1 to 100, and separately the sum of only the even numbers from 1 to 100.

all_sum = 0
even_sum = 0

for num in range(1, 101):
    all_sum += num
    if num % 2 == 0:
        even_sum += num

print(f"Sum of all numbers: {all_sum}")
print(f"Sum of even numbers: {even_sum}")
