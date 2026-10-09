def greet(name):
    print(f"Hello!, {name}")

greet('Apil')

def square(n):
    return n * n

print(square(4))


def is_even(n):
    if n % 2 == 0:
        return True
    else: return False

print(is_even(7))

def area(l,w):
    return l * w

print(area(4,10))

def biggest(a,b,c):
    return max(a,b,c)

print(biggest(4,7,388))

count = 0

def add():
    global count
    count += 1
    return count

add()
print(count)