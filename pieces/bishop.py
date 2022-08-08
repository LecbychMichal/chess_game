from pieces.piece import Piece
from window import *

class Bishop(Piece):
    def __init__(self, row, col, team):
        super(Bishop, self).__init__(row, col, team)
        self.material_score = 3000
        if self.team == "w":
            self.image = white_bishop
        if self.team == "b":
            self.image = black_bishop

    def append_moves(self, board):
        self.poss_moves = []
        if self.team == "w":
            for i in range(7 - self.row):
                if self.col - i - 1 >= 0 and self.row + i + 1 <= 7:
                    if board[self.col - i - 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                    elif board[self.col - i - 1][self.row + i + 1].team == "w":
                        break
                    elif board[self.col - i - 1][self.row + i + 1].team == "b":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                        break

            for i in range(self.row):
                if self.col - i - 1 >= 0 and self.row - i - 1 >= 0:
                    if board[self.col - i - 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                    elif board[self.col - i - 1][self.row - i - 1].team == "w":
                        break
                    elif board[self.col - i - 1][self.row - i - 1].team == "b":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                        break

            for i in range(7 - self.row):
                if self.col + i + 1 <= 7 and self.row + i + 1 <= 7:
                    if board[self.col + i + 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                    elif board[self.col + i + 1][self.row + i + 1].team == "w":
                        break
                    elif board[self.col + i + 1][self.row + i + 1].team == "b":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                        break
            for i in range(self.row):
                if self.col + i + 1 <= 7 and self.row - i - 1 >= 0:
                    if board[self.col + i + 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                    elif board[self.col + i + 1][self.row - i - 1].team == "w":
                        break
                    elif board[self.col + i + 1][self.row - i - 1].team == "b":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                        break

        if self.team == "b":
            for i in range(7 - self.row):
                if self.col - i - 1 >= 0 and self.row + i + 1 <= 7:
                    if board[self.col - i - 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                    elif board[self.col - i - 1][self.row + i + 1].team == "w":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                        break
                    elif board[self.col - i - 1][self.row + i + 1].team == "b":
                        break
            for i in range(self.row):
                if self.col - i - 1 >= 0 and self.row - i - 1 >= 0:
                    if board[self.col - i - 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                    elif board[self.col - i - 1][self.row - i - 1].team == "w":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                        break
                    elif board[self.col - i - 1][self.row - i - 1].team == "b":
                        break

            for i in range(7 - self.row):
                if self.col + i + 1 <= 7 and self.row + i + 1 <= 7:
                    if board[self.col + i + 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                    elif board[self.col + i + 1][self.row + i + 1].team == "w":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                        break
                    elif board[self.col + i + 1][self.row + i + 1].team == "b":
                        break
            for i in range(self.row):
                if self.col + i + 1 <= 7 and self.row - i - 1 >= 0:
                    if board[self.col + i + 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                    elif board[self.col + i + 1][self.row - i - 1].team == "w":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                        break
                    elif board[self.col + i + 1][self.row - i - 1].team == "b":
                        break