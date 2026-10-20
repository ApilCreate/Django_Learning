# D1
try:
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input")

# D2
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input")

# D3
try:
    marks = float(input("Enter marks out of 100: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 90:
        print("A+")
    elif marks >= 80:
        print("A")
    elif marks >= 70:
        print("B+")
    elif marks >= 60:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")
except ValueError:
    print("Invalid marks")

# D4
try:
    year = int(input("Enter a year: "))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
except ValueError:
    print("Invalid input")

# D5
try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))
    if first >= second and first >= third:
        largest = first
    elif second >= first and second >= third:
        largest = second
    else:
        largest = third
    print(f"Largest: {largest}")
except ValueError:
    print("Invalid input")

# D6
try:
    age = int(input("Enter the passenger's age: "))
    if age < 0:
        print("Invalid age")
    elif age < 5:
        print("Fare: Rs. 0")
    elif age <= 12:
        print("Fare: Rs. 500")
    elif age <= 59:
        print("Fare: Rs. 1000")
    else:
        print("Fare: Rs. 600")
except ValueError:
    print("Invalid age")

# D7
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "dashain2083":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("User not found")
