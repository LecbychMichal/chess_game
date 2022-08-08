from enemy import VS_Player
from enemy import VS_AI
from chessboard import Board
from window import *

board = Board()
enemynumber = 1

if __name__ == "__main__":
    if enemynumber == 0:
        enemy = VS_Player()
        enemy.play(board)
    if enemynumber == 1:
        enemy = VS_AI()
        enemy.play(board)
