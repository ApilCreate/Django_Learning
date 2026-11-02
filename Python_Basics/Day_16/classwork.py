class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if self.__price <= 0:
            raise ValueError
        self.__price = value

    @property
    def price_with_vat(self):
        return round(self.__price * 1.13,2)

p = Product("Laptop", 80000)
p.price = 90000
print(p.price)
print(p.price_with_vat)