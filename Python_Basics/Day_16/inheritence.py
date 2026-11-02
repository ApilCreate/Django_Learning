
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    @property
    def info(self):
        return f"The vehicle is {self.brand} with {self.wheels} wheels."

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 4)

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)
        self.has_carrier = True

    @property
    def info(self):
        return f"The bike is {self.brand} with {self.wheels} wheels and carrier {self.has_carrier}."

class ElectricCar(Car):
    def __init__(self,brand,battery):
        super().__init__(brand)
        self.battery = battery

    @property
    def info(self):
        return f"{self.brand} with {self.wheels} wheels and battery of {self.battery} kwh"

c = Car("Toyota")
b = Bike("Yamaha")
e = ElectricCar("BYD",1000)
print(c.info)
print(b.info)
print(e.info)

