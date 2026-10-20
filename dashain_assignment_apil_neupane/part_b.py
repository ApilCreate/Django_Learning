# B1
name = input("Dear user, enter your full name: ").strip()
print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(len(name))

# B2
greeting = "Happy Dashain to you and your family"
split = greeting.split()
print(split)
print(split[0])
print(split[len(split) - 1])
print(greeting[:5])
print(greeting[-6:])
print(greeting[::-1])

# B3
user = input("Type a random sentence: ").strip()
count = 0
for char in user:
    if char.lower() == "a":
        count += 1
print(count)

# B4
msg = "   Vijaya Dashami ko hardik shubhakamana   "
space = msg.strip()
space = space.replace("hardik", "dherai")
print(space)
list = space.split()
print(list)
print("Total Word Count: ", len(list))

# B5
char = input("Enter the wordr that you want to check: ").lower()
char_reverse = char[::-1]
if char == char_reverse:
    print(f"{char} is a palindrome character")
else:
    print(f"{char} is not a palindrome character")

# B6
email = input("Enter your email address: ")
seperator = email.split("@")
print("Email Address: ", email)
print("Username: ", seperator[0])
print("Domain: ", seperator[1])
