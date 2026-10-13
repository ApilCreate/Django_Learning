# find the sum of natural numbers using recursive function

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(100))

#using recursive function create a fibonacci series
# 0 1 1 2 3 5 8 13 21


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

n = 5
list = []
for i in range(n):
    list.append(fibonacci(i))

print(list)
