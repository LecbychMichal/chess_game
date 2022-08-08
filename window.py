import pygame
import os

screen_size = 500
cell_size = screen_size / 8


chessboard = pygame.image.load(os.path.join("images", "board.png"))
empty = pygame.image.load(os.path.join("images", "blank.png"))

black_pawn = pygame.image.load(os.path.join("images", "black_pawn.png"))
black_bishop = pygame.image.load(os.path.join("images", "black_bishop.png"))
black_king = pygame.image.load(os.path.join("images", "black_king.png"))
black_knight = pygame.image.load(os.path.join("images", "black_knight.png"))
black_queen = pygame.image.load(os.path.join("images", "black_queen.png"))
black_rook = pygame.image.load(os.path.join("images", "black_rook.png"))

white_pawn = pygame.image.load(os.path.join("images", "white_pawn.png"))
white_bishop = pygame.image.load(os.path.join("images", "white_bishop.png"))
white_king = pygame.image.load(os.path.join("images", "white_king.png"))
white_knight = pygame.image.load(os.path.join("images", "white_knight.png"))
white_queen = pygame.image.load(os.path.join("images", "white_queen.png"))
white_rook = pygame.image.load(os.path.join("images", "white_rook.png"))

pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Chess")
screen.blit(chessboard, (0, 0))