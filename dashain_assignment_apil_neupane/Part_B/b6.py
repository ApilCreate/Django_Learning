# B6
# Ask the user for an email address. Using split("@"), print the username part and the domain part separately.
email = input("Enter your email address: ")
seperator = email.split("@")
print("Email Address: ", email)
print("Username: ", seperator[0])
print("Domain: ", seperator[1])