# D6
# Bus fare for going home for Dashain: children under 5 travel free, ages 5-12 pay Rs. 500, ages 13-59 pay Rs. 1000, and 60 and above pay Rs. 600. Ask for the passenger's age and print the fare.

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
