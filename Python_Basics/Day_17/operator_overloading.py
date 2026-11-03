class Money:
    def __init__(self,amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, other):
            return Money(self.amount * other.amount)

total = Money(500) + Money(250)
new_total = Money(500) - Money(250)
naya_total = Money(500) * Money(250)
print(total.amount)
print(new_total.amount)
print(naya_total.amount)
