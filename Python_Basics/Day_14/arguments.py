# Mix of positional and key word arguments
def pet(name, animal):
    print(f"{name}:{animal}")
pet("Tommy", animal="dog")

# 1: 
def greet(name, city):
    print(f"Hi {name} from {city}")

greet(name="Asha", city="Pokhara")

# 2:
def area(l,w):
    return l * w

print(area(w=2, l=5))
print(area(l=5, w=2))
print(area(5, w=2))

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("milk"))

def new_add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(new_add_item("apple"))
print(new_add_item("milk"))