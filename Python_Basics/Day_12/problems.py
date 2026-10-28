# Problem 1: Write apply_twice(func, x) that calls func two times.
def apply_twice(func, x):
    return func(func(x))
print(apply_twice(lambda n: n + 3, 10))

# Problem 2: Write make_greeting(word) that returns a function.
def make_greeting(word):
    def greet(name):
        return f"{word}, {name}!"
    return greet

print(make_greeting("Namaste")("Ram"))

# Problem 3: Write a decorator that uppercases what a function returns.
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_result
def say_message():
    return "hello from python"

print(say_message())

# Problem 4: Use map() to turn ["10", "20", "30"] into integers, then add them.
numbers = list(map(int, ["10", "20", "30"]))
print(sum(numbers))

# Problem 5: Use filter() to keep only words longer than 4 letters.
words = ["cat", "tiger", "house", "sun", "apple"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)

# Problem 6: Sort (name, age) tuples by age, oldest first.
people = [("Ram", 25), ("Sita", 30), ("Mohan", 20)]
sorted_people = sorted(people, key=lambda person: person[1], reverse=True)
print(sorted_people)

# Problem 7: Use reduce() to find the largest number without max().
from functools import reduce
numbers = [12, 45, 7, 89, 34]
largest = reduce(
    lambda current_largest, number:
    current_largest if current_largest > number else number, numbers)
print(largest)