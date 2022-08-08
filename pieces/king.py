from pieces.piece import Piece
from window import *

class King(Piece):
    def __init__(self, row, col, team):
        super(King, self).__init__(row, col, team)
        self.material_score = 90000
        if self.team == "w":
            self.image = white_king
        if self.team == "b":
            self.image = black_king

    def append_moves(self, board):
        if self.team == "w":
            if self.row + 1 <= 7 and self.row + 1:
                if board[self.col][self.row + 1].team != "w" and board[self.col][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col][self.row + 1]))
            if self.col + 1 <= 7 and self.col + 1:
                if board[self.col + 1][self.row].team != "w" and board[self.col + 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row]))
            if self.col + 1 <= 7 and self.row + 1 <= 7 and self.col + 1 and self.row + 1:
                if board[self.col + 1][self.row + 1].team != "w" and board[self.col + 1][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row + 1]))
            if self.col + 1 <= 7 and self.row - 1 >= 0 and self.col + 1 and self.row - 1:
                if board[self.col + 1][self.row - 1].team != "w" and board[self.col + 1][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row - 1]))
            if self.row - 1 >= 0 and self.row - 1:
                if board[self.col][self.row - 1].team != "w" and board[self.col][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col][self.row - 1]))
            if self.col - 1 >= 0 and self.row + 1 <= 7 and self.col - 1 and self.row + 1:
                if board[self.col - 1][self.row + 1].team != "w" and board[self.col - 1][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row + 1]))
            if self.col - 1 >= 0 and self.row - 1 >= 0 and self.col - 1 and self.row - 1:
                if board[self.col - 1][self.row - 1].team != "w" and board[self.col - 1][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row - 1]))
            if self.col - 1 >= 0 and self.col - 1:
                if board[self.col - 1][self.row].team != "w" and board[self.col - 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row]))

        if self.team == "b":
            if self.row + 1 <= 7 and self.row + 1:
                if board[self.col][self.row + 1].team != "b" and board[self.col][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col][self.row + 1]))
            if self.col + 1 <= 7 and self.col + 1:
                if board[self.col + 1][self.row].team != "b" and board[self.col + 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row]))
            if self.col + 1 <= 7 and self.row + 1 <= 7 and self.col + 1 and self.row + 1:
                if board[self.col + 1][self.row + 1].team != "b" and board[self.col + 1][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row + 1]))
            if self.col + 1 <= 7 and self.row - 1 >= 0 and self.col + 1 and self.row - 1:
                if board[self.col + 1][self.row - 1].team != "b" and board[self.col + 1][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row - 1]))
            if self.row - 1 >= 0 and self.row - 1:
                if board[self.col][self.row - 1].team != "b" and board[self.col][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col][self.row - 1]))
            if self.col - 1 >= 0 and self.row + 1 <= 7 and self.col - 1 and self.row + 1:
                if board[self.col - 1][self.row + 1].team != "b" and board[self.col - 1][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row + 1]))
            if self.col - 1 >= 0 and self.row - 1 >= 0 and self.col - 1 and self.row - 1:
                if board[self.col - 1][self.row - 1].team != "b" and board[self.col - 1][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row - 1]))
            if self.col - 1 >= 0 and self.col - 1:
                if board[self.col - 1][self.row].team != "b" and board[self.col - 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row]))
