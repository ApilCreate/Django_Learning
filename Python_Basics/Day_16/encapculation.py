class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = list(marks)

    def add_marks(self, added_marks):
        if 1 <= added_marks <= 100:
            self.__marks.append(added_marks)
        else:
            print("Invalid marks!!")

    @property
    def average(self):
        return sum(self.__marks) / len(self.__marks)


std1 = Student("Apil", [80, 40, 30])
std1.add_marks(50)

print(std1.average)          # 50.0
print(std1._Student__marks)  # [80, 40, 30, 50]