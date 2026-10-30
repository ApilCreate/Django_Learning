# 1:
def total(*nums):
    return sum(nums)

print(total(1,2,3))
print(total())

#2:
def profile(**details):
    for key, value in details.items():
        print(f"{key}:{value}")

profile(name = "ram", age = 22)

#3:
def order(item, *extras, **notes):
    print(item,extras, notes)
order("momo", "achar", spicy = True)

# This means we cannot send keyword arguments
# Positional Only
def power(base,exp,/):
    return base ** exp

print(power(2,3))
# power(base = 2,exp=3)

# This means we have to give keyword arguments
# Keyword only
def connect(host, *, timeout = 10):
    print(host,timeout)

connect("localhost", timeout=5)