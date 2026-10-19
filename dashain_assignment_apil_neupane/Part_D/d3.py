# D3
# Ask the user for marks out of 100 and print the grade using this table. If the marks are below 0 or above 100, print "Invalid marks".

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
