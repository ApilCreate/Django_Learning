# map
names = ['Apil', 'Neupane', 'Ram']

def greet(n):
    return "Hi" + " " + n.title()
print(list(map(greet, names)))

# filter

marks = [10,20,30,40,50]

def passed(m):
    return m >=40
print(list(filter(passed, marks)))

students = [
    ("Ram", 80),
    ("Sita", 95),
    ("Hari", 70)
]

result = sorted(students, key=lambda student: student[1], reverse=True)

print(result)