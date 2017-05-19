from pprint import pprint

from packages.game.board import Board
from packages.game.player import Player
from config import *


class Game:
    def __init__(self, inputstring):
        data = inputstring.split("/")
        self.players = [Player(i, p.split(",")) for i, p in enumerate(data[2][2::].split("-"))]
        self.board = Board(data[:2])
        self.currentDir = []

    def set_direction(self, x, y):
        self.currentDir.clear()
        self.currentDir.append((y,x))
        for _ in "*" * (self.board.board[y][x][1] - 1):
            previous = min([(self.board.board[y - 1][x][1], y - 1, x),
                            (self.board.board[y + 1][x][1], y + 1, x),
                            (self.board.board[y][x - 1][1], y, x - 1),
                            (self.board.board[y][x + 1][1], y, x + 1)])
            self.currentDir.append(previous[1:])
            y, x = previous[1:]

    def next(self, player):
        print(self.currentDir)
        print(self.players[player].x, self.players[player].y)
        destination = self.currentDir.pop()
        print(destination)
        if destination[1] > self.players[player].x and destination[0] == self.players[player].y:
            return RIGHT
        if destination[1] < self.players[player].x and destination[0] == self.players[player].y:
            return LEFT
        if destination[0] > self.players[player].y and destination[1] == self.players[player].x:
            return DOWN
        if destination[0] < self.players[player].y and destination[1] == self.players[player].x:
            return UP
        return IDLE

    def update(self, inputstring):
        data = inputstring.split("/")
        # pprint(inputstring)
        self.players = [Player(i, p.split(",")) for i, p in enumerate(data[2][2::].split("-"))]
        print("updated", self.players[0].x, self.players[0].y)
        self.board = Board(data[:2])
