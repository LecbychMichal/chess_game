from window import *
from abc import ABC, abstractmethod


class Square(ABC):

    @abstractmethod
    def draw_pieces(self):
        pass

    @abstractmethod
    def append_moves(self, board):
        pass

class Piece(Square):
    def __init__(self, col, row, team):
        self.row = row
        self.col = col
        self.posY = col * cell_size
        self.posX = row * cell_size
        self.image = empty
        self.team = team
        self.board = None
        self.poss_moves = []
        self.en_passant = False
        self.en_passant_moved = False
        self.material_score = 0

    def draw_pieces(self):
        try:
            screen.blit(self.image, (self.posX + 8, self.posY + 7))
        except Exception as e:
            print("Hra byla ukončena")


    def append_moves(self, board):
        pass