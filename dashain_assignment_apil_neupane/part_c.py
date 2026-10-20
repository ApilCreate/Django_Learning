# C1
foods = ["sel roti", "masu", "chiura", "achar"]
foods.append("dahi")
foods.insert(1, "bara")
foods.remove("achar")
print("Final list:", foods)
print("Length:", len(foods))

# C2
marks = [78, 45, 92, 66, 88, 59]
print("Highest Marks: ", max(marks))
print("Lowest Marks: ", min(marks))
print("Total Marks: ", sum(marks))
print("Average Marks: ", round(sum(marks) / len(marks), 2))
print("Ascending Order: ", sorted(marks))
print("Descending Order: ", sorted(marks, reverse=True))

# C3
dashain_days = ("Ghatasthapana", "Fulpati", "Maha Ashtami", "Maha Navami", "Vijaya Dashami")
print(f"First Day: {dashain_days[0]}\n Last Day: {dashain_days[len(dashain_days) - 1]}")
print(f"Number of Days: {len(dashain_days)}")
if "Fulpati" in dashain_days:
    print(True)
else:
    print(False)

# C4
ram_family = {"Hari", "Sita", "Gopal", "Maya"}
sita_family = {"Maya", "Bikash", "Hari", "Anju"}
print(f"Relatives in both families: {ram_family & sita_family}")
print(f"All relatives: {ram_family | sita_family}")
print(f"Only in ram_family: {ram_family - sita_family}")

# C5
student = {"name": "Aarav", "age": 17, "city": "Pokhara"}
student["city"] = "Kathmandu"
student["course"] = "Python"
del student["age"]
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Key-value pairs: {student.items()}")

# C6
prices = {
    "apple": 250,
    "banana": 120,
    "mango": 300,
    "orange": 180,
    "grapes": 350,
}
fruit = input("Enter a fruit name: ").lower()
price = prices.get(fruit)
if price is not None:
    print(f"Price: {price} per kg")
else:
    print("Not available")

# C7
nums = list(range(1, 11))
evens = list(range(2, 21, 2))
down = list(range(10, 0, -1))
fives = list(range(5, 51, 5))
print(f"Numbers 1 to 10: {nums}")
print(f"Even numbers from 2 to 20: {evens}")
print(f"Numbers 10 down to 1: {down}")
print(f"Multiples of 5 from 5 to 50: {fives}")
