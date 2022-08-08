from pieces.piece import Piece
from window import *

class Knight(Piece):
    def __init__(self, row, col, team):
        super(Knight, self).__init__(row, col, team)
        self.material_score = 3000
        if self.team == "w":
            self.image = white_knight
        if self.team == "b":
            self.image = black_knight

    def append_moves(self, board):
        self.poss_moves = []
        if self.team == "w":
            if self.col + 2 <= 7 and self.row + 1 <= 7 and board[self.col + 2][self.row + 1] not in self.poss_moves:
                if board[self.col + 2][self.row + 1].team != "w":
                    self.poss_moves.append((board[self.col + 2][self.row + 1]))
            if self.col + 1 <= 7 and self.row + 2 <= 7 and board[self.col + 1][self.row + 2] not in self.poss_moves:
                if board[self.col + 1][self.row + 2].team != "w":
                    self.poss_moves.append((board[self.col + 1][self.row + 2]))
            if self.col + 2 <= 7 and self.row - 1 >= 0 and board[self.col + 2][self.row - 1] not in self.poss_moves:
                if board[self.col + 2][self.row - 1].team != "w":
                    self.poss_moves.append((board[self.col + 2][self.row - 1]))
            if self.col + 1 <= 7 and self.row - 2 >= 0 and board[self.col + 1][self.row - 2] not in self.poss_moves:
                if board[self.col + 1][self.row - 2].team != "w":
                    self.poss_moves.append((board[self.col + 1][self.row - 2]))
            if self.col - 2 >= 0 and self.row - 1 >= 0 and board[self.col - 2][self.row - 1] not in self.poss_moves:
                if board[self.col - 2][self.row - 1].team != "w":
                    self.poss_moves.append((board[self.col - 2][self.row - 1]))
            if self.col - 2 >= 0 and self.row + 1 <= 7 and board[self.col - 2][self.row + 1] not in self.poss_moves:
                if board[self.col - 2][self.row + 1].team != "w":
                    self.poss_moves.append((board[self.col - 2][self.row + 1]))
            if self.col - 1 >= 0 and self.row + 2 <= 7 and board[self.col - 1][self.row + 2] not in self.poss_moves:
                if board[self.col - 1][self.row + 2].team != "w":
                    self.poss_moves.append((board[self.col - 1][self.row + 2]))
            if self.col - 1 >= 0 and self.row - 2 >= 0 and board[self.col - 1][self.row - 2] not in self.poss_moves:
                if board[self.col - 1][self.row - 2].team != "w":
                    self.poss_moves.append((board[self.col - 1][self.row - 2]))

        if self.team == "b":
            if self.col + 2 <= 7 and self.row + 1 <= 7 and board[self.col + 2][self.row + 1] not in self.poss_moves:
                if board[self.col + 2][self.row + 1].team != "b":
                    self.poss_moves.append((board[self.col + 2][self.row + 1]))
            if self.col + 1 <= 7 and self.row + 2 <= 7 and board[self.col + 1][self.row + 2] not in self.poss_moves:
                if board[self.col + 1][self.row + 2].team != "b":
                    self.poss_moves.append((board[self.col + 1][self.row + 2]))
            if self.col + 2 <= 7 and self.row - 1 >= 0 and board[self.col + 2][self.row - 1] not in self.poss_moves:
                if board[self.col + 2][self.row - 1].team != "b":
                    self.poss_moves.append((board[self.col + 2][self.row - 1]))
            if self.col + 1 <= 7 and self.row - 2 >= 0 and board[self.col + 1][self.row - 2] not in self.poss_moves:
                if board[self.col + 1][self.row - 2].team != "b":
                    self.poss_moves.append((board[self.col + 1][self.row - 2]))
            if self.col - 2 >= 0 and self.row - 1 >= 0 and board[self.col - 2][self.row - 1] not in self.poss_moves:
                if board[self.col - 2][self.row - 1].team != "b":
                    self.poss_moves.append((board[self.col - 2][self.row - 1]))
            if self.col - 2 >= 0 and self.row + 1 <= 7 and board[self.col - 2][self.row + 1] not in self.poss_moves:
                if board[self.col - 2][self.row + 1].team != "b":
                    self.poss_moves.append((board[self.col - 2][self.row + 1]))
            if self.col - 1 >= 0 and self.row + 2 <= 7 and board[self.col - 1][self.row + 2] not in self.poss_moves:
                if board[self.col - 1][self.row + 2].team != "b":
                    self.poss_moves.append((board[self.col - 1][self.row + 2]))
            if self.col - 1 >= 0 and self.row - 2 >= 0 and board[self.col - 1][self.row - 2] not in self.poss_moves:
                if board[self.col - 1][self.row - 2].team != "b":
                    self.poss_moves.append((board[self.col - 1][self.row - 2]))

