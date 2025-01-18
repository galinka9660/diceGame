import random

class Game:

    def roll_dice(self):
        number = random.randint(1,6)
        print(f"Gespielter Zahl ist {number}")
        return number