import numpy as np
from pieces.piece import Piece
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn
from window import *



class Board:
    def __init__(self):
        self.selected = None
        self.wchecked = False
        self.bchecked = False
        self.checkmate = False
        self.player_white = True
        self.player_black = False
        self.white_call = True
        self.black_call = False
        self.all_white_moves = []
        self.all_black_moves = []
        self.board_score = 0
        self.position_score_piece = 0
        self.position_score_pawn1 = 0
        self.position_score_pawn2 = 0
        self.round = 1

        self.set_pieces = [[Piece(col, row, team = "n") for row in range(8)] for col in range(8)]

        self.set_pieces[0][0] = Rook(0, 0, "b")
        self.set_pieces[0][1] = Knight(0, 1, "b")
        self.set_pieces[0][2] = Bishop(0, 2, "b")
        self.set_pieces[0][3] = Queen(0, 3, "b")
        self.set_pieces[0][4] = King(0, 4, "b")
        self.set_pieces[0][5] = Bishop(0, 5, "b")
        self.set_pieces[0][6] = Knight(0, 6, "b")
        self.set_pieces[0][7] = Rook(0, 7, "b")
        
        self.set_pieces[7][0] = Rook(7, 0, "w")
        self.set_pieces[7][1] = Knight(7, 1, "w")
        self.set_pieces[7][2] = Bishop(7, 2, "w")
        self.set_pieces[7][3] = Queen(7, 3, "w")
        self.set_pieces[7][4] = King(7, 4, "w")
        self.set_pieces[7][5] = Bishop(7, 5, "w")
        self.set_pieces[7][6] = Knight(7, 6, "w")
        self.set_pieces[7][7] = Rook(7, 7, "w")

        for i in range(8):
            pass
            self.set_pieces[6][i] = Pawn(6, i, "w")
            self.set_pieces[1][i] = Pawn(1, i, "b")

        self.set_position_score()

    def draw_selected(self, mouse_col, mouse_row, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (mouse_row * cell_size + cell_size / 2, mouse_col * cell_size + cell_size / 2), 25)

    def draw_poss_moves(self, screen, mouse_col, mouse_row):
        for move in self.set_pieces[mouse_col][mouse_row].poss_moves:
            pygame.draw.circle(screen, (0, 0, 255),
                               (move.row * cell_size + cell_size / 2, move.col * cell_size + cell_size / 2), 30)

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                self.set_pieces[i][j].draw_pieces()

    def draw_board_moves(self, screen, mouse_col, mouse_row):
        if self.set_pieces[mouse_col][mouse_row].team == "w" and self.player_white:
            self.draw_selected(mouse_col, mouse_row, screen)
        if self.set_pieces[mouse_col][mouse_row].team == "b" and self.player_black:
            self.draw_selected(mouse_col, mouse_row, screen)

    def make_move(self, mouse_col, mouse_row, screen):
        self.set_pieces[mouse_col][mouse_row].append_moves(self.set_pieces)
        self.draw_poss_moves(screen, mouse_col, mouse_row)
        if self.selected:
            for move in self.selected.poss_moves: #plati pro druhy klik
                if move.row == mouse_row and move.col == mouse_col or self.selected.row == mouse_row and self.selected.col == mouse_col:
                    self.switch_piece(mouse_col, mouse_row, move)
                    if move.row == mouse_row and move.col == mouse_col:
                        self.set_pieces[self.selected.col][self.selected.row] = Piece(self.selected.col, self.selected.row, "n")
                    self.check_en_passant(mouse_row, mouse_col)
                    self.king_check()
                    self.swap_players()
                    self.selected = None
                    return

        if self.set_pieces[mouse_col][mouse_row].image != empty and not self.selected: #plati pro prvni klik
            if self.player_black and self.set_pieces[mouse_col][mouse_row].team == "b":
                self.selected = self.set_pieces[mouse_col][mouse_row]
            if self.player_white and self.set_pieces[mouse_col][mouse_row].team == "w":
                self.selected = self.set_pieces[mouse_col][mouse_row]

    def switch_piece(self, mouse_col, mouse_row, move):
        if self.selected.__class__.__name__ == "Pawn":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = Pawn(mouse_col, mouse_row, "w")
                if move.en_passant_moved:
                    self.set_pieces[mouse_col + 1][mouse_row] = Piece(mouse_col + 1, mouse_row, "n")
            if self.selected.team == "b":
                self.set_pieces[mouse_col][mouse_row] = Pawn(mouse_col, mouse_row, "b")
                if move.en_passant_moved:
                    self.set_pieces[mouse_col - 1][mouse_row] = Piece(mouse_col - 1, mouse_row, "n")

        if self.selected.__class__.__name__ == "Rook":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = Rook(mouse_col, mouse_row, "w")
            if self.selected.team == "b":
                self.set_pieces[mouse_col][mouse_row] = Rook(mouse_col, mouse_row, "b")

        if self.selected.__class__.__name__ == "Knight":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = Knight(mouse_col, mouse_row, "w")
            if self.selected.team == "b" and self.player_black:
                self.set_pieces[mouse_col][mouse_row] = Knight(mouse_col, mouse_row, "b")

        if self.selected.__class__.__name__ == "Bishop":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = Bishop(mouse_col, mouse_row, "w")
            if self.selected.team == "b":
                self.set_pieces[mouse_col][mouse_row] = Bishop(mouse_col, mouse_row, "b")

        if self.selected.__class__.__name__ == "King":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = King(mouse_col, mouse_row, "w")
            if self.selected.team == "b" and self.player_black:
                self.set_pieces[mouse_col][mouse_row] = King(mouse_col, mouse_row, "b")

        if self.selected.__class__.__name__ == "Queen":
            if self.selected.team == "w":
                self.set_pieces[mouse_col][mouse_row] = Queen(mouse_col, mouse_row, "w")
            if self.selected.team == "b":
                self.set_pieces[mouse_col][mouse_row] = Queen(mouse_col, mouse_row, "b")

    def swap_players(self):
        self.selected = None
        if self.player_white:
            self.player_white = False
            self.player_black = True
            self.black_call = True
            self.evaluate_board()
            print(f"WHITE SCORE: {int(self.board_score/1000)}")
            print(f"ROUND: {self.round}")

        else:
            self.player_black = False
            self.player_white = True
            self.white_call = True
            self.evaluate_board()
            print(f"BLACK SCORE: {int(self.board_score/1000)}")
            print(f"ROUND: {self.round}")

        print("---------------")

    def check_en_passant(self, mouse_row, mouse_col):
        if self.set_pieces[mouse_col][mouse_row].__class__.__name__ == "Pawn" and self.set_pieces[mouse_col][
            mouse_row].team == "w":
            if self.selected.col == 6 and self.set_pieces[mouse_col][mouse_row].col == 4:
                self.set_pieces[mouse_col][mouse_row].en_passant = True

        if self.set_pieces[mouse_col][mouse_row].__class__.__name__ == "Pawn" and self.set_pieces[mouse_col][
            mouse_row].team == "b":
            if self.selected.col == 1 and self.set_pieces[mouse_col][mouse_row].col == 3:
                self.set_pieces[mouse_col][mouse_row].en_passant = True

    def king_check(self):
        self.bchecked = False
        for i in range(8):
            for j in range(8):
                if self.set_pieces[i][j].team == "w":
                    self.set_pieces[i][j].append_moves(self.set_pieces)
                    for move in self.set_pieces[i][j].poss_moves:
                        self.all_white_moves.append(move)
                        if move.__class__.__name__ == "King":
                            self.bchecked = True

        self.wchecked = False
        for i in range(8):
            for j in range(8):
                if self.set_pieces[i][j].team == "b":
                    self.set_pieces[i][j].append_moves(self.set_pieces)
                    for move in self.set_pieces[i][j].poss_moves:
                        self.all_black_moves.append(move)
                        if move.__class__.__name__ == "King":
                            self.wchecked = True

    def king_checked_move(self, mouse_col, mouse_row, screen):
        print("schovej krale")
        self.make_move_while_checked(mouse_col, mouse_row, screen)

    def make_move_while_checked(self, mouse_col, mouse_row, screen):
        self.set_pieces[mouse_col][mouse_row].append_moves(self.set_pieces)
        self.draw_poss_moves(screen, mouse_col, mouse_row)
        if self.selected:
            for move in self.selected.poss_moves:
                if move.row == mouse_row and move.col == mouse_col:
                    self.switch_piece(mouse_col, mouse_row, move)
                    self.check_en_passant(mouse_row, mouse_col)
                    self.king_check()

                    if self.bchecked:
                        self.reverse_move(mouse_col, mouse_row)
                    else:
                        try:
                            self.set_pieces[self.selected.col][self.selected.row] = Piece(self.selected.col, self.selected.row, "n")
                        except Exception as e:
                            print(e)
                        self.swap_players()

                    self.selected = None

        if self.set_pieces[mouse_col][mouse_row].image != empty and not self.selected:
            if self.player_black and self.set_pieces[mouse_col][mouse_row].team == "b":
                self.selected = self.set_pieces[mouse_col][mouse_row]
            if self.player_white and self.set_pieces[mouse_col][mouse_row].team == "w":
                self.selected = self.set_pieces[mouse_col][mouse_row]

    def reverse_move(self, mouse_col, mouse_row):
        self.set_pieces[mouse_col][mouse_row] = Piece(mouse_col, mouse_row, "n")

        if self.selected.__class__.__name__ == "Pawn":
            if self.selected.team == "w":  # duplikace
                self.set_pieces[self.selected.col][self.selected.row] = Pawn(self.selected.col, self.selected.row, "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = Pawn(self.selected.col, self.selected.row, "b")

        if self.selected.__class__.__name__ == "Rook":
            if self.selected.team == "w":
                self.set_pieces[self.selected.col][self.selected.row] = Rook(self.selected.col, self.selected.row, "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = Rook(self.selected.col, self.selected.row, "b")

        if self.selected.__class__.__name__ == "Knight":
            if self.selected.team == "w":
                self.set_pieces[self.selected.col][self.selected.row] = Knight(self.selected.col, self.selected.row,
                                                                               "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = Knight(self.selected.col, self.selected.row,
                                                                               "b")

        if self.selected.__class__.__name__ == "Bishop":
            if self.selected.team == "w":
                self.set_pieces[self.selected.col][self.selected.row] = Bishop(self.selected.col, self.selected.row,
                                                                               "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = Bishop(self.selected.col, self.selected.row,
                                                                               "b")

        if self.selected.__class__.__name__ == "King":
            if self.selected.team == "w":
                self.set_pieces[self.selected.col][self.selected.row] = King(self.selected.col, self.selected.row, "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = King(self.selected.col, self.selected.row, "b")

        if self.selected.__class__.__name__ == "Queen":
            if self.selected.team == "w":
                self.set_pieces[self.selected.col][self.selected.row] = Queen(self.selected.col, self.selected.row, "w")
            if self.selected.team == "b":
                self.set_pieces[self.selected.col][self.selected.row] = Queen(self.selected.col, self.selected.row, "b")


    def make_move_AI(self, mouse_col, mouse_row):
        if self.selected:

            for move in self.selected.poss_moves:
                if move in self.selected.poss_moves:
                    if move.row == mouse_row and move.col == mouse_col or self.selected.row == mouse_row and self.selected.col == mouse_col:
                        self.switch_piece(mouse_col, mouse_row, move)
                        if move.row == mouse_row and move.col == mouse_col:
                            self.set_pieces[self.selected.col][self.selected.row] = Piece(self.selected.col, self.selected.row, "n")
                        self.check_en_passant(mouse_row, mouse_col)
                        self.king_check()
                        return

        self.selected = self.set_pieces[mouse_col][mouse_row]


    def set_position_score(self):
        self.position_score_piece = [[2 for i in range(8)] for j in range(8)]
        for i in range(4):
            for j in range(4):
                self.position_score_piece[i][j] += (i + j) ** 2
                self.position_score_piece[-i - 1][j] += (i + j) ** 2
                self.position_score_piece[-i - 1][-j - 1] += (i + j) ** 2
                self.position_score_piece[i][-j - 1] += (i + j) ** 2

        self.position_score_pawn1 = [[j * 2 for i in range(8)] for j in range(8)]

        self.position_score_pawn2 = [[l * 4 for l in range(8)] for k in range(8)]
        for i in range(8):
            for j in range(4):
                self.position_score_pawn2[i][j + 4] -= j*8 + 4

    def evaluate_board(self):
        self.board_score = 0
        for i in range(8):
            for j in range(8):
                if self.set_pieces[i][j].team == "w":
                    self.board_score -= self.set_pieces[i][j].material_score
                if self.set_pieces[i][j].team == "b":
                    self.board_score += self.set_pieces[i][j].material_score

        return self.board_score
