# 1:
def power(base, exp=2):
    return base**exp
print(power(3))
print(power(2,10))

# 2:
def add(item,box=None):
    if box is None:
        box = []
    box.append(item)
    return box

print(add(1))
print(add(2))

def total(*numbers):
    print(type(numbers), numbers)
    return sum(numbers)
print(total(5,10))
print(total(1,2,2,3,5,4,5,35,56,7))

def profile(name, **details):
    print(name, details)

profile("Asha", age=21, city="Pokhara")
