import math, random

class Circle:
    def __init__(self, radius):
        if radius == 0:
            self.radius = random.uniform(1.1, 9.5)
        else:
            self.radius = radius

    def calc_circumference(self):
        return math.pi * 2 * self.radius

    def calc_diameter(self):
        return self.radius * 2

    def calc_area(self):
        return math.pi * (self.radius ** 2)

    def calc_volume(self):
        return math.pi * (4/3) * (self.radius ** 3)


circles = []

for i in range(0, 10):
    c = Circle(0)
    circles.append(c)

text = "Radius: {}, Circumference: {}, Diameter: {}, Area: {}, Volume: {}"

for c in circles:
    print(text.format(c.radius, c.calc_circumference(), c.calc_diameter(), c.calc_area(), c.calc_volume()))

