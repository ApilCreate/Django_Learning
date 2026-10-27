def square(n):
    return n * n

result = square(10)

name = square

print(result)
print(name(5))

def apply_opreation(func, num):
    return func(num)

def double(n):
    return n*2

def new_square(n):
    return n * n

print(apply_opreation(double,20))
print(apply_opreation(square,20))

def multiplier(n):
    def create_multiplier(num):
        return n * num

    return create_multiplier  
two_multiplier = multiplier(2)
three_multiplier = multiplier(3)

print(two_multiplier(10))
print(three_multiplier(20))