# merge two dictionarirs and what challenges we can face - homework

dic1 = {"name": "Apil", "age": 21}
dic2 = {"address": "Chitwan", "email": "apilneupane123@gmail.com"}
merge = dic1 | dic2
print(merge)

# OR

dic1.update(dic2)

#both merges two dictionaries but main difference is | creates a new dictionary while .update() just updates the exsiting dictionary

# Functions:

# 1 
def greet(name):
    print("Hello", name)

greet("Apil")

# 2
def square(n):
    return (n * n)

print(square(4))

# 3
def is_even(n):
    return n % 2 == 0

print(is_even(4))

# 4
def area(l ,w):
    return l * w

print(area(20,10))

# 5
def biggest(a,b,c):
    if b > a and b > c:
        largest = b
    elif c > a and c > b:
        largest = c
    else: largest = a

    return largest

print(biggest(4,5,3))

# 6
count = 0
def add():
    global count
    count += 1

add()
print(count)
    