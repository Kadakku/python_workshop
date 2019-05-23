import random

class Square:
    def __init__(self, side):
        if side == 0:
            self.side = random.uniform(2, 10)
        else:
            self.side = side

    def calc_perimeter(self):
        return self.side * 4

    def calc_area(self):
        return self.side ** 2

    def calc_volume(self):
        return self.side ** 3

squares = []

for i in range(0, 10):
    s = Square(5)
    squares.append(s)

text = "Side: {} m, Perimeter: {} m, Area: {} m2, Volume: {} m3"

for s in squares:
    print(text.format(s.side, s.calc_perimeter(), s.calc_area(), s.calc_volume()))
