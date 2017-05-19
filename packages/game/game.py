from packages.game.board import Board
from packages.game.player import Player


class Game:
    def __init__(self, inputstring):
        data = inputstring.split("/")
        self.players = [Player(i, p.split(",")) for i, p in enumerate(data[2][2::].split("-"))]
        self.board = Board(data[:2])
        self.currentDir = []

    def set_direction(self, x, y):
        self.currentDir.clear()
        for _ in "*" * self.board.board[y][x][1]:
            previous = min([(self.board.board[y - 1][x][1], y - 1, x),
                            (self.board.board[y + 1][x][1], y + 1, x),
                            (self.board.board[y][x - 1][1], y, x - 1),
                            (self.board.board[y][x + 1][1], y, x + 1)])
            self.currentDir.append(previous[1:])
            y, x = previous[1:]

    def next(self):
        return self.currentDir.pop()
