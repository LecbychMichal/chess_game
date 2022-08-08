from pieces.piece import Piece
from window import *

class Pawn(Piece):
    def __init__(self, row, col, team):
        super(Pawn, self).__init__(row, col, team)
        self.material_score = 1000

        if self.team == "w":
            self.image = white_pawn
        if self.team == "b":
            self.image = black_pawn

    def append_moves(self, board):
        self.poss_moves = []
        if self.team == "w":
            if self.col - 1 >= 0:
                if board[self.col - 1][self.row].team == "n" and board[self.col - 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row]))
            if self.col == 6:
                if board[self.col - 2][self.row].team == "n" and board[self.col - 2][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 2][self.row]))

            if self.col - 1 >= 0 and self.row - 1 >= 0:
                if board[self.col - 1][self.row - 1].team == "b" and board[self.col - 1][
                    self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row - 1]))

            if self.col - 1 >= 0 and self.row + 1 <= 7:
                if board[self.col - 1][self.row + 1].team == "b" and board[self.col - 1][
                    self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row + 1]))

            if self.row + 1 <= 7:
                if board[self.col][self.row + 1].en_passant and board[self.col][self.row].col == 3 and board[self.col][
                    self.row + 1].team == "b" and board[self.col][self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row + 1]))
                    board[self.col - 1][self.row + 1].en_passant_moved = True

            if self.row - 1 >= 0:
                if board[self.col][self.row - 1].en_passant and board[self.col][self.row].col == 3 and board[self.col][
                    self.row - 1].team == "b" and board[self.col][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col - 1][self.row - 1]))
                    board[self.col - 1][self.row - 1].en_passant_moved = True

        if self.team == "b":
            if self.col + 1 <= 7:
                if board[self.col + 1][self.row].team == "n" and board[self.col + 1][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row]))
            if self.col == 1:
                if board[self.col + 2][self.row].team == "n" and board[self.col + 2][self.row] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 2][self.row]))

            if self.col + 1 >= 0 and self.row - 1 >= 0 and self.col + 1 <= 7 and self.row - 1 <= 7:
                if board[self.col + 1][self.row - 1].team == "w" and board[self.col + 1][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row - 1]))

            if self.col + 1 >= 0 and self.row + 1 <= 7 and self.col + 1 <= 7:
                if board[self.col + 1][self.row + 1].team == "w" and board[self.col + 1][
                    self.row + 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row + 1]))

            if self.row - 1 >= 0:
                if board[self.col][self.row - 1].en_passant and board[self.col][self.row].col == 4 and board[self.col][
                    self.row - 1].team == "w" and board[self.col][self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row - 1]))
                    board[self.col + 1][self.row - 1].en_passant_moved = True

            if self.row + 1 <= 7:
                if board[self.col][self.row + 1].en_passant and board[self.col][self.row].col == 4 and board[self.col][
                    self.row + 1].team == "w" and board[self.col][self.row + 1].team == "w" and board[self.col][
                    self.row - 1] not in self.poss_moves:
                    self.poss_moves.append((board[self.col + 1][self.row + 1]))
                    board[self.col + 1][self.row + 1].en_passant_moved = True
