# G4
# Student result system
# • Ask for the names and marks in 3 subjects for at least 3 students, and store them in a list of dictionaries.
# • Write functions to calculate the total, the percentage, and the grade (reuse your grading logic from D3).
# • Print a result table for all students and the name of the topper.

students = []

# Input details of 3 students
for i in range(3):
    name = input(f"\nEnter name of student {i + 1}: ")

    marks = []
    for j in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks in subject {j + 1} (out of 100): "))

                if mark not in range(0,101):
                    print("Invalid marks")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Invalid marks")

    students.append({"name": name, "marks": marks})


def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


print("\nStudent Result Table: ")
print(f"{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade':<10}")
print("-" * 50)

topper = students[0]

for student in students:
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(student["marks"])
    grade = calculate_grade(percentage)

    print(f"{student['name']:<15}{total:<10.1f}{percentage:<15.2f}{grade:<10}")

    if total > calculate_total(topper["marks"]):
        topper = student

print("-" * 50)
print("Topper:", topper["name"])