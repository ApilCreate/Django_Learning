class Payment:
    def pay(self):
        return 0

class Esewa(Payment):
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        return self.amount
    def __str__(self):
         return "Esewa"
class Khalti(Payment):
    def __init__(self,amount):
            self.amount = amount
    def pay(self):
            return self.amount
    def __str__(self):
         return "Khalti"
class Cash(Payment):
    def __init__(self,amount):
            self.amount = amount
    def pay(self):
            return self.amount
    def __str__(self):
         return "Cash"
for p in [Esewa(5000),Khalti(6000),Cash(7000)]:
    print(f"{p}: {p.pay()}")