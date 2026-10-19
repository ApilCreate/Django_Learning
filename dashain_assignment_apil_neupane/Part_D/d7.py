# D7
# Ask the user for a username and password. If the username is "admin" and the password is "dashain2083", print "Login successful"; if only the username is right, print "Wrong password"; otherwise print "User not found".

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "dashain2083":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("User not found")
