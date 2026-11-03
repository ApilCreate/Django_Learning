class Fakeadd():
    def __init__(self,num):
        self.num = num
    def __add__(self, value):
        return Fakeadd(self.num - value.num)

a = Fakeadd(100) + Fakeadd(50)

print(type(a))
print(a.num)

