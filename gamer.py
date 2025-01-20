from game import Game

class Gamer:
    id = None

    def __init__(self, id):
        self.id = id
        g = Game
        self.game = g.roll_dice()