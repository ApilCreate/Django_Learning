# 1
n = int(input("Enter a number: "))
if n == 0 :
    print("Zero")
elif n < 0 :
    print("Negative")
else: print("Positive")

# 2
e = int(input("Enter a number to check even or odd: "))
if e % 2 == 0:
    print("Even")
else: print("Odd")

# 3
age = int(input("Enter your  age: "))
if age < 0 :
    print("Invalid age")
elif age in range(0,13):
    print("You are a child")
elif age in range (13,19):
    print("You are a teenager")
else: print("You are an adult")

# 4
a, b = 8, 3 
if a > b :
    print(f"a: {a} is the greater number")
else: print(f"b: {b} is the greater number")

# 5
pw = input("Enter your password:")
main_pw = 'Password123'
if pw == main_pw :
    print("Welcome for django123")
else: print("Incorrect password try again")

# 6
year = int(input("Enter a year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else: print("It is not a leap year")