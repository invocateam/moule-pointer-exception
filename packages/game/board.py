from config import *

class Board:
    def __init__(self, datas):
        flatboard = datas[1].split("-")

        self.x, self.y = [ int(_) for _ in datas[0].split("x") ]
        self.board = [
                [ int(flatboard[y*self.x + x]) if  flatboard[y*self.x + x].isdigit()  else  flatboard[y*self.x + x] 
                    for x in range(self.x)] 
                for y in range(self.y)]
        
        for x in range(self.x):
            self.board[0][x] = INFRANCHISSABLE
            self.board[self.y-1][x] = INFRANCHISSABLE
        for y in range(self.y):
            self.board[y][0] = INFRANCHISSABLE
            self.board[y][self.x-1] = INFRANCHISSABLE 
