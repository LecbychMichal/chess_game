from window import *
from pieces.bishop import Bishop
from pieces.rook import Rook

class Queen(Bishop, Rook):
    def __init__(self, row, col, team):
        super(Queen, self).__init__(row, col, team)
        self.material_score = 9000
        if self.team == "w":
            self.image = white_queen
        if self.team == "b":
            self.image = black_queen

    def append_moves(self, board):

        self.poss_moves = []
        if self.team == "w":
            for i in range(7 - self.col):
                if self.col + i + 1 <= 7 and board[self.col + i + 1][self.row] not in self.poss_moves:
                    if board[self.col + i + 1][self.row].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row]))
                    if board[self.col + i + 1][self.row].team == "w":
                        break
                    if board[self.col + i + 1][self.row].team == "b":
                        self.poss_moves.append((board[self.col + i + 1][self.row]))
                        break
            for i in range(self.col):
                if self.col - i - 1 >= 0 and board[self.col - i - 1][self.row] not in self.poss_moves:
                    if board[self.col - i - 1][self.row].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row]))
                    if board[self.col - i - 1][self.row].team == "w":
                        break
                    if board[self.col - i - 1][self.row].team == "b":
                        self.poss_moves.append((board[self.col - i - 1][self.row]))
                        break
            for i in range(7 - self.row):
                if self.row + i + 1 <= 7 and board[self.col][self.row + i + 1] not in self.poss_moves:
                    if board[self.col][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col][self.row + i + 1]))
                    if board[self.col][self.row + i + 1].team == "w":
                        break
                    if board[self.col][self.row + i + 1].team == "b":
                        self.poss_moves.append((board[self.col][self.row + i + 1]))
                        break
            for i in range(self.row):
                if self.row - i - 1 >= 0 and board[self.col][self.row - i - 1] not in self.poss_moves:
                    if board[self.col][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col][self.row - i - 1]))
                    if board[self.col][self.row - i - 1].team == "w":
                        break
                    if board[self.col][self.row - i - 1].team == "b":
                        self.poss_moves.append((board[self.col][self.row - i - 1]))
                        break

            for i in range(7 - self.row):
                if self.col - i - 1 >= 0 and self.row + i + 1 <= 7 and board[self.col - i - 1][
                    self.row + i + 1] not in self.poss_moves:
                    if board[self.col - i - 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                    if board[self.col - i - 1][self.row + i + 1].team == "w":
                        break
                    if board[self.col - i - 1][self.row + i + 1].team == "b":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                        break
            for i in range(self.row):
                if self.col - i - 1 >= 0 and self.row - i - 1 >= 0 and board[self.col - i - 1][
                    self.row - i - 1] not in self.poss_moves:
                    if board[self.col - i - 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                    if board[self.col - i - 1][self.row - i - 1].team == "w":
                        break
                    if board[self.col - i - 1][self.row - i - 1].team == "b":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                        break

            for i in range(7 - self.row):
                if self.col + i + 1 <= 7 and self.row + i + 1 <= 7 and board[self.col + i + 1][
                    self.row + i + 1] not in self.poss_moves:
                    if board[self.col + i + 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                    if board[self.col + i + 1][self.row + i + 1].team == "w":
                        break
                    if board[self.col + i + 1][self.row + i + 1].team == "b":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                        break
            for i in range(self.row):
                if self.col + i + 1 <= 7 and self.row - i - 1 >= 0 and board[self.col + i + 1][
                    self.row - i - 1] not in self.poss_moves:
                    if board[self.col + i + 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                    if board[self.col + i + 1][self.row - i - 1].team == "w":
                        break
                    if board[self.col + i + 1][self.row - i - 1].team == "b":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                        break

        if self.team == "b":
            for i in range(7 - self.col):
                if self.col + i + 1 <= 7 and board[self.col + i + 1][self.row] not in self.poss_moves:
                    if board[self.col + i + 1][self.row].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row]))
                    if board[self.col + i + 1][self.row].team == "b":
                        break
                    if board[self.col + i + 1][self.row].team == "w":
                        self.poss_moves.append((board[self.col + i + 1][self.row]))
                        break
            for i in range(self.col):
                if self.col - i - 1 >= 0 and board[self.col - i - 1][self.row] not in self.poss_moves:
                    if board[self.col - i - 1][self.row].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row]))
                    if board[self.col - i - 1][self.row].team == "b":
                        break
                    if board[self.col - i - 1][self.row].team == "w":
                        self.poss_moves.append((board[self.col - i - 1][self.row]))
                        break
            for i in range(7 - self.row):
                if self.row + i + 1 <= 7 and board[self.col][self.row + i + 1] not in self.poss_moves:
                    if board[self.col][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col][self.row + i + 1]))
                    if board[self.col][self.row + i + 1].team == "b":
                        break
                    if board[self.col][self.row + i + 1].team == "w":
                        self.poss_moves.append((board[self.col][self.row + i + 1]))
                        break
            for i in range(self.row):
                if self.row - i - 1 >= 0 and board[self.col][self.row - i - 1] not in self.poss_moves:
                    if board[self.col][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col][self.row - i - 1]))
                    if board[self.col][self.row - i - 1].team == "b":
                        break
                    if board[self.col][self.row - i - 1].team == "w":
                        self.poss_moves.append((board[self.col][self.row - i - 1]))
                        break

            for i in range(7 - self.row):
                if self.col - i - 1 >= 0 and self.row + i + 1 <= 7 and board[self.col - i - 1][
                    self.row + i + 1] not in self.poss_moves:
                    if board[self.col - i - 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                    if board[self.col - i - 1][self.row + i + 1].team == "w":
                        self.poss_moves.append((board[self.col - i - 1][self.row + i + 1]))
                        break
                    if board[self.col - i - 1][self.row + i + 1].team == "b":
                        break
            for i in range(self.row):
                if self.col - i - 1 >= 0 and self.row - i - 1 >= 0 and board[self.col - i - 1][
                    self.row - i - 1] not in self.poss_moves:
                    if board[self.col - i - 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                    if board[self.col - i - 1][self.row - i - 1].team == "w":
                        self.poss_moves.append((board[self.col - i - 1][self.row - i - 1]))
                        break
                    if board[self.col - i - 1][self.row - i - 1].team == "b":
                        break

            for i in range(7 - self.row):
                if self.col + i + 1 <= 7 and self.row + i + 1 <= 7 and board[self.col + i + 1][
                    self.row + i + 1] not in self.poss_moves:
                    if board[self.col + i + 1][self.row + i + 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                    if board[self.col + i + 1][self.row + i + 1].team == "w":
                        self.poss_moves.append((board[self.col + i + 1][self.row + i + 1]))
                        break
                    if board[self.col + i + 1][self.row + i + 1].team == "b":
                        break
            for i in range(self.row):
                if self.col + i + 1 <= 7 and self.row - i - 1 >= 0 and board[self.col + i + 1][
                    self.row - i - 1] not in self.poss_moves:
                    if board[self.col + i + 1][self.row - i - 1].team == "n":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                    if board[self.col + i + 1][self.row - i - 1].team == "w":
                        self.poss_moves.append((board[self.col + i + 1][self.row - i - 1]))
                        break
                    if board[self.col + i + 1][self.row - i - 1].team == "b":
                        break