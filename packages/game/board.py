from config import *

class Board:
    def __init__(self, inputstring):
        datas = inputstring.split("/")
        flatboard = datas[1].split("-")

        self.x, self.y = datas[0].split("x")
        self.board = [
                [ int(flatboard[y*self.x + x]) if  flatboard[y*self.x + x].isDigit()  else  flatboard[y*self.x + x] 
                    for x in range(self.x)] 
                for y in range(self.y)]
        
        for x in range(self.x):
            self.board[0][x] = INFRANCHISSABLE
            self.board[self.y][x] = INFRANCHISSABLE
        for y in range(self.y):
            self.board[y][0] = INFRANCHISSABLE
            self.board[y][self.x] = INFRANCHISSABLE
        
        self.players = [ p.split(",") for p in datas[2][2::].split("-")] 
