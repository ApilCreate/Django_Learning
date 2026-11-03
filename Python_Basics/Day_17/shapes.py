class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w,self.h = w,h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return round(3.14 * self.r ** 2,1)

class New_Rectangle(Rectangle):
    def __init__(self,w,h):
        super().__init__(w,h)

    def area(self):
        return self.w * self.h

for a in [Rectangle(4,5), Circle(50), New_Rectangle(6,8)]:
    print(a.area())