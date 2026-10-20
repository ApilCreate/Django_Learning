# A1
my_str = "Hello, Python!"
my_int = 25
my_float = 3.14
my_bool = True
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
my_set = {1, 2, 3}
my_dict = {"name": "Apil", "age": 21}

print(my_str, type(my_str))
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_bool, type(my_bool))
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_dict, type(my_dict))

# A2
ask = input("Enter your age: ")
age = int(ask) + 1
print(f"You shall turn {age} next dashain..")

# A3
ask = float(input("Enter the price for a single kite: "))
quantity = int(input("How many kites do they want?: "))
total_cost = ask * quantity
print(f"The total cost as a float is: {total_cost}")
print(f"The rounded total cost is: {int(round(total_cost))}")

# A4
print("5" + "5")
print(5 + 5)
print("5" * 3)
print(int("7") + float("2.5"))
print(bool(0), bool(""), bool("0"), bool([]))

# A5
list = [1, 2, 2, 3, 3, 3]
set = set(list)
print(set)
tuple = tuple(set)
print(tuple)
