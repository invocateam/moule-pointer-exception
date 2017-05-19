import timeit

from config import *


class Board:
    def __init__(self, datas):
        flatboard = datas[1].split("-")

        self.x, self.y = [int(_) for _ in datas[0].split("x")]
        self.board = [
                [[int(flatboard[y*self.x + x]), 999] if flatboard[y*self.x + x].isdigit() else [flatboard[y*self.x + x], 999]
                    for x in range(self.x)] 
                for y in range(self.y)]
        
        for x in range(self.x):
            self.board[0][x][0] = INFRANCHISSABLE
            self.board[self.y-1][x][0] = INFRANCHISSABLE
        for y in range(self.y):
            self.board[y][0][0] = INFRANCHISSABLE
            self.board[y][self.x-1][0] = INFRANCHISSABLE

    def update_board(self, player):
        coord = (player.x, player.y)
        self.board[coord[0]][coord[1]][1] = 0

        print(timeit.timeit())
        self.explore(*coord, 0)
        print("\n".join(["".join(str([str(i[1]).rjust(3) for i in _])) for _ in self.board]))
        print(timeit.timeit())
        pass

    def explore(self, x, y, weight):
        # print("\n".join(["".join(str(_)) for _ in self.board]))
        print()
        if weight >= MAX_WEIGHT:
            return
        tiles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for tile in tiles:
            if self.board[tile[1]][tile[0]][0] != INFRANCHISSABLE and self.board[tile[1]][tile[0]][0] != DUNE and self.board[tile[1]][tile[0]][1] > weight:
                self.board[tile[1]][tile[0]][1] = weight+1
                self.explore(*tile, weight+1)
        pass
