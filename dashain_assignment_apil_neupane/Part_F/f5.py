# F5
# Write a function `find_max(numbers)` that takes a list and returns the largest number, using a loop instead of `max()`.

def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(find_max([4, 9, 2, 7]))
print(find_max([-3, -8, -1]))
