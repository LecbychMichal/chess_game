from window import *

def get_pos():
    x, y = pygame.mouse.get_pos()
    mouse_row = x // cell_size
    mouse_col = y // cell_size
    return int(mouse_col), int(mouse_row)

class VS_Player:
    def __init__(self):
        pass

    def play(self, board):
        run = True
        while True:
            while run:
                board.draw_pieces()

                if board.player_white:
                    if board.white_call:
                        print("PLAYER TURN: WHITE")
                        board.white_call = False
                        if board.wchecked:
                            print("wchecked")

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                        if event.type == pygame.MOUSEBUTTONUP:
                            screen.blit(chessboard, (0, 0))
                            mouse_col, mouse_row = get_pos()
                            board.draw_board_moves(screen, mouse_col, mouse_row)
                            if board.wchecked:
                                board.king_checked_move(mouse_col, mouse_row, screen)

                            else:
                                board.make_move(mouse_col, mouse_row, screen)

                    if board.checkmate:
                        print("End of game")

                if board.player_black:

                    if board.black_call:
                        print("PLAYER TURN: BLACK")
                        board.black_call = False
                        if board.bchecked:
                            print("bchecked")

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                        if event.type == pygame.MOUSEBUTTONUP:
                            screen.blit(chessboard, (0, 0))
                            mouse_col, mouse_row = get_pos()
                            board.draw_board_moves(screen, mouse_col, mouse_row)
                            if board.bchecked:
                                print("bchecked")
                                board.king_checked_move(mouse_col, mouse_row, screen)
                            else:
                                board.make_move(mouse_col, mouse_row, screen)
                    if board.checkmate:
                        print("End of game")

            pygame.quit()

class VS_AI:
    def __init__(self, depth=2, maximizing=False):
        self.highest_score = 0

    def algorithm(self, board):

        new_move = None
        new_row = None
        new_col = None
        old_move = None
        old_row = None
        old_col = None
        new_score = 0

        if board.bchecked:
            while board.bchecked:
                for row in range(8):
                    for col in range(8):
                        if board.set_pieces[col][row].team == "b":
                            board.set_pieces[col][row].append_moves(board.set_pieces)
                            if board.set_pieces[col][row].__class__.__name__ == "King":
                                if not board.set_pieces[col][row].poss_moves :
                                    try:
                                        print("CHECKMATE - End of game")
                                        pygame.quit()
                                        return
                                    except Exception as e:
                                        print("Hra byla ukončena", e)
                                        return


                            if board.set_pieces[col][row].poss_moves:
                                for move in board.set_pieces[col][row].poss_moves:
                                    board.make_move_AI(col, row)
                                    board.make_move_AI(move.col, move.row)
                                    board.king_check()

                                    if board.bchecked:
                                        board.reverse_move(move.col, move.row)

                                    else:
                                        self.make_move(board, row, col, move.row, move.col)
                                        return

        else:
            for row in range(8):
                for col in range(8):
                    if board.set_pieces[col][row].team == "b":
                        board.set_pieces[col][row].append_moves(board.set_pieces)
                        if board.set_pieces[col][row].poss_moves:
                            if board.round < 40:
                                board.set_pieces[0][4].poss_moves = []
                                for move in board.set_pieces[col][row].poss_moves:
                                    new_score = self.evaluate_moves(board, col, row, move.row, move.col)

                                    if new_score > self.highest_score:
                                        self.highest_score = new_score
                                        new_move = move
                                        new_row = row
                                        new_col = col
                                    else:
                                        old_move = move
                                        old_row = row
                                        old_col = col

            try:
                self.make_move(board, new_row, new_col, new_move.row, new_move.col)
            except:
                # print(old_row, old_col, old_move.row, old_move.col)
                self.make_move(board, old_row, old_col, old_move.row, old_move.col)

    def evaluate_moves(self, board, col, row, move_row, move_col):
        new_score = 0
        board.make_move_AI(col, row) #s cim budu hrat
        if board.set_pieces[move_col][move_row].team == "n":
            board.make_move_AI(move_col, move_row)  # kam budu hrat
            new_score = self.score_of_board(board)
            board.reverse_move(move_col, move_row)
        elif board.set_pieces[move_col][move_row].team == "w":
            piece_taken = board.set_pieces[move_col][move_row]
            board.make_move_AI(move_col, move_row)
            new_score = self.score_of_board(board)
            board.reverse_move(move_col, move_row)
            board.set_pieces[move_col][move_row] = piece_taken
        return new_score

    def make_move(self, board, row, col, move_row, move_col):
        board.make_move_AI(col, row)  # s cim budu h rat
        board.make_move_AI(move_col, move_row)  # kam budu hrat

    def score_of_board(self, board):
        self.curr_score = 0
        for i in range(8):
            for j in range(8):
                if board.set_pieces[j][i].team == "b":
                    self.curr_score += self.eval(board, i, j)
        return self.curr_score + board.evaluate_board()

    def eval(self, board, row, col):
        if board.set_pieces[col][row].__class__.__name__ == "Pawn":
            pos_score = board.position_score_pawn1[col][row] + board.position_score_pawn2[col][row] + board.position_score_piece[col][row]
        elif board.set_pieces[col][row].__class__.__name__ != "Pawn" or board.set_pieces[col][row].team == "n":
            pos_score = board.position_score_piece[col][row]
        return pos_score

    def play(self, board):
        run = True
        while True:
            while run:
                board.draw_pieces()

                if board.player_white:
                    if board.white_call:
                        print("PLAYER TURN: WHITE")
                        board.white_call = False
                        if board.wchecked:
                            print("wchecked")

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                        if event.type == pygame.MOUSEBUTTONUP:
                            screen.blit(chessboard, (0, 0))
                            mouse_col, mouse_row = get_pos()
                            board.draw_board_moves(screen, mouse_col, mouse_row)
                            if board.wchecked:
                                board.king_checked_move(mouse_col, mouse_row, screen)

                            else:
                                board.make_move(mouse_col, mouse_row, screen)

                    if board.checkmate:
                        print("End of game")

                if board.player_black:
                    if board.black_call:
                        print("PLAYER TURN: BLACK")
                        board.black_call = False
                        if board.bchecked:
                            print("bchecked")

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    self.algorithm(board)
                    board.swap_players()
                    board.round += 1



            pygame.quit()
