# C5
# Create a dictionary student = {"name": "Aarav", "age": 17, "city": "Pokhara"}. Change the city to "Kathmandu", add a key "course" with the value "Python", delete the "age" key, and print all keys, all values, and all key–value pairs.

student = {"name": "Aarav", "age": 17, "city": "Pokhara"}
student["city"] = "Kathmandu"
student["course"] = "Python"
del student["age"]

print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Key-value pairs: {student.items()}")
