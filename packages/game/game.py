import board;
import player;

class Game:
    def __init__(self, inputstring):
        self.player = Player()
        self.board = Board(inputstring)
