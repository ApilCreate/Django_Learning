# F1
def greet(name):
    return f"Happy Dashain, {name}!"

print(greet("Aarav"))
print(greet("Sita"))

# F2
def area_of_rectangle(length, width):
    return length * width

print(area_of_rectangle(5, 4))
print(area_of_rectangle(10, 3))

# F3
def is_even(n):
    return n % 2 == 0

print(is_even(8))
print(is_even(5))

# F4
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))

# F5
def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max([4, 9, 2, 7]))
print(find_max([-3, -8, -1]))

# F6
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Dashain"))
print(count_vowels("Kathmandu"))

# F7
def calculate_dakshina(age):
    if age < 10:
        return 1001
    elif age <= 17:
        return 501
    else:
        return 101

print(calculate_dakshina(7))
print(calculate_dakshina(15))
print(calculate_dakshina(25))

# F8
def simple_interest(principal, rate, time=1):
    return principal * rate * time / 100

print(simple_interest(10000, 5, 2))
print(simple_interest(10000, 5))
