def square(n):
    return n * n

result = list(map(square, [1,2,3,4]))
print(result)

lazy from functools import reduce
def find_max(x,y):
    if x > y:
        return x
    return y

result = reduce(find_max,[1,2,3,4,5])
print(result)