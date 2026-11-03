class Hen:
    def fly(self):
        return "Low Fly"

class Bird:
    def fly(self):
        return "Medium Fly"

class Plane:
    def fly(self):
        return "High Fly"

class Rocket:
    def fly(self):
        return "Very High Fly"

for flyables in [Hen(),Bird(),Plane(),Rocket()]:
    print(flyables.fly())