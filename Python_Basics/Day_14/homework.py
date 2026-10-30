# 1:
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))

# 2:
# g = countdown(2)
# print(next(g))
# print(next(g))
# print(next(g))

# The first next(g) gives value 2, the second gives value 1 and last raises StopIteration

# 3:
def squares(n):
    for i in range(1, n+1):
        yield i * i

for s in squares(4):
    print(s)
