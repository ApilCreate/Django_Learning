name = input("Enter your name: ")
score = int(input("Enter your score"))

if score < 0 or score > 100:
    print("Enter a valid score within range 0 to 100")
elif score in range(90,101):
    print("You got an A+")
elif score in range(75,90):
    print("You got a B")
elif score in range(60,75):
    print("You got a C")
elif score < 60:
    print("You got a F")
