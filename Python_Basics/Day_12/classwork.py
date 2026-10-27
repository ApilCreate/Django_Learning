# # Higher Order Function

# #Build a model calc with hof

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

def add(a ,b):
    return a + b

def sub(a ,b):
    return a - b

def mul(a ,b):
    return a * b 

def div(a,b):
    return a % b

def result(func, num, aarkonum):
    return func(num, aarkonum)

print(result(add, num1, num2))

# Dynamic hof
name = input("Dear user, enter your name: ")
def user(username):
    def greet_user(namm):
        return f" {namm}, {username} "
    return greet_user

hi_greet = user(name)
hello_greet = user(name)

print(hi_greet("Hi"))
print(hello_greet("Hello"))
