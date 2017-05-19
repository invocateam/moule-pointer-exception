import timeit

from config import *


class Board:
    def __init__(self, datas):
        flatboard = datas[1].split("-")

        self.x, self.y = [int(_) for _ in datas[0].split("x")]
        self.board = [
            [[int(flatboard[y * self.x + x]), 999] if flatboard[y * self.x + x].isdigit() else [
                flatboard[y * self.x + x], 999]
             for x in range(self.x)]
            for y in range(self.y)]

        for x in range(self.x):
            self.board[0][x][0] = INFRANCHISSABLE
            self.board[self.y - 1][x][0] = INFRANCHISSABLE
        for y in range(self.y):
            self.board[y][0][0] = INFRANCHISSABLE
            self.board[y][self.x - 1][0] = INFRANCHISSABLE

    def update_weight(self, player):
        coord = (player.x, player.y)
        self.board[coord[1]][coord[0]][1] = 0

        return self.explore(*coord, 0, [])

    def explore(self, x, y, weight, loot_list):
        # print("\n".join(["".join(str(_)) for _ in self.board]))
        if weight >= MAX_WEIGHT:
            return
        tiles = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for tile in tiles:
            if self.board[tile[1]][tile[0]][0] != INFRANCHISSABLE and self.board[tile[1]][tile[0]][0] != DUNE and \
                            self.board[tile[1]][tile[0]][1] > weight:
                if self.board[tile[1]][tile[0]][0] in [BIERE, FRITE] or type(self.board[tile[1]][tile[0]][0]) == int:
                    loot_list.append((tile[0], tile[1]))
                self.board[tile[1]][tile[0]][1] = weight + 1
                self.explore(*tile, weight + 1, loot_list)
        return loot_list
