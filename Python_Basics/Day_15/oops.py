class Car():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def drive(self):
        return f'{self.brand} is moving'

car1 = Car("Audi", "Red")
print(car1.brand)
print(car1.color)
print(car1.drive())


class Student():
    def __init__(self,name,grade,section,rollnum):
        self.name = name
        self.grade = grade
        self.section = section
        self.rollnum = rollnum

    def introduce(self):
        return f'Hi, I am {self.name}'

s1 = Student("Aarav", 10, 'A', 13)
s2 = Student("Apil", 10, 'A', 1)
s3 = Student("Damno", 10, 'B', 50)

print(s1.name, s1.grade, s1.section, s1.rollnum)
print(s2.name, s2.grade, s2.section, s2.rollnum)
print(s3.name, s3.grade, s3.section, s3.rollnum)

class Club():
    club = 'Tech Club'

    def __init__(self,name,grade,marks):
        self.name = name
        self.grade = grade
        self.marks = marks
    def add_mark(self,mark):
        self.marks.append(mark)
    def average(self):
        return sum(self.marks) / len(self.marks)

student1 = Club("Apil","Ten",[60,70,80])
student2 = Club("Ram","Ten",[40,70,90])
print(student1.name,student1.grade,student1.marks,student1.club)
print(student2.name,student2.grade,student2.marks,student2.club)