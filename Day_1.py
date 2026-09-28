while True:
    name = input("Enter your name: ")

    if len(name) <= 2 or not name.isalpha():
        print("Enter a valid name damno...")
    else:
        print(f"Welcome {name}")
        break