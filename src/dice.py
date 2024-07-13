import random
from choice import Choice

class Dice:
    def __init__(self, number_of_sides=6):
        self.sides = []
        for i in range(number_of_sides):
            self.sides.append(random.choice(list(Choice)))

    def roll(self):
        return random.choice(self.sides)