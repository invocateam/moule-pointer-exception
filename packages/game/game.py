from packages.game.board import Board
from packages.game.player import Player

class Game:
    def __init__(self, inputstring):
        data = inputstring.split("/")
        self.players = [ Player(i, p.split(",")) for i, p in enumerate(data[2][2::].split("-"))] 
        self.board = Board(data[:2])
