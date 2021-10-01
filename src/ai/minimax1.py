import math
import random
from time import time

from src.constant import ColorConstant, GameConstant, ShapeConstant
from src.model.board import Board
from src.model.state import State
from src.model.piece import Piece
from src.utility import is_win, is_full, place
import copy

from typing import Tuple

class BotMinimaxAB:
    
    def __init__(self, board: Board, n_player: int):
        self.board = board
        self.n_player = n_player
        
    def heuristicAB(self, board: Board, n_player: int) :
        value = 0
        if n_player == 0:
            shape = GameConstant.PLAYER1_SHAPE
            color = GameConstant.PLAYER1_COLOR
        else :
            shape = GameConstant.PLAYER2_SHAPE
            color = GameConstant.PLAYER2_COLOR
        
        shape_value = ""
        
        row1 = 5
        row2 = 4
        row3 = 3
        row4 = 5
        row6 = 4
        row5 = 5
        # row1 = random.randint(0, board.row-1)
        board[row1,0].color = ColorConstant.RED
        board[row1,0].shape = ShapeConstant.CIRCLE
        board[row2,0].color = ColorConstant.RED
        board[row2,0].shape = ShapeConstant.CIRCLE
        board[row3,0].color = ColorConstant.RED
        board[row3,0].shape = ShapeConstant.CIRCLE
        board[row4,1].color = ColorConstant.BLUE
        board[row4,1].shape = ShapeConstant.CIRCLE
        board[row6,1].color = ColorConstant.RED
        board[row6,1].shape = ShapeConstant.CIRCLE
        board[row5,2].color = ColorConstant.RED
        board[row5,2].shape = ShapeConstant.CIRCLE
        # board[row1, col1].color = ColorConstant.BLUE
        # board[row1,col1].shape = ShapeConstant.CIRCLE
        
        print(shape, color)
        print(board)
        
        #Cek Horizontal 2 streak
        col = 0
        while (col != board.col - 2) :
            row = 5
            while (row > 0) :
                #Maximazing
                if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+1].color != ColorConstant.BLACK) :
                    value = value + 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape  and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+1].shape == shape) :
                    value = value + 10**1
                
                #Minimazing
                if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+1].color != ColorConstant.BLACK) :
                    value = value - 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+1].shape != shape) :
                    value = value - 10**1
                    
                row = row - 1
            col = col + 1
        
        #Cek Horizontal 3 streak
        col = 0
        while (col != board.col - 3) :
            row = 5
            while (row > 0):
                #Maximazing
                if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+2].color == color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK):
                    value = value + 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row, col+1].shape == shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+2].shape == shape): 
                    value = value + 10**2
                    
                #Minimazing
                if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+2].color != color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK):
                    value = value - 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row, col+1].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+2].shape != shape): 
                    value = value - 10**2

                row = row - 1
            col = col + 1
        
        #Cek Horizontal 4 streak
        col = 0
        while (col != board.col - 4) :
            row = 5
            while (row > 0):
                #Maximazing
                if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+2].color == color and board[row, col+3].color == color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col+3].color != ColorConstant.BLACK):
                    value = value + 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row, col+1].shape == shape and board[row, col+2].shape == shape and board[row, col+3].shape == shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+3].shape != ShapeConstant.BLANK): 
                    value = value + 10**3
                    
                #Minimazing
                if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+2].color != color and board[row, col+3].color != color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col+3].color != ColorConstant.BLACK):
                    value = value - 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row, col+1].shape != shape and board[row, col+2].shape != shape and board[row, col+3].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+3].shape != ShapeConstant.BLANK): 
                    value = value - 10**3

                row = row - 1
            col = col + 1
        
        #Cek vertikal 2 streak
        col = 0
        while (col != board.col - 1):
            row = 5
            while (row >= 1):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col].color == color and board[row-1, col].color != ColorConstant.BLACK):
                    value = value + 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK): 
                    value = value + 10**1
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col].color != color and board[row-1, col].color != ColorConstant.BLACK):
                    value = value - 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK): 
                    value = value - 10**1
        
                row = row - 1
            col = col + 1
            
        #Cek vertikal 3 streak
        col = 0
        while (col != board.col - 1):
            row = 5
            while (row > 2):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col].color == color and board[row-2, col].color == color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK):
                    value = value + 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-2, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK): 
                    value = value + 10**2
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col].color != color and board[row-2, col].color != color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK):
                    value = value - 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-2, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK): 
                    value = value - 10**2

                row = row - 1
            col = col + 1
        
        #Cek vertikal 4 streak
        col = 0
        while (col != board.col - 1) :
            row = 5
            while (row > 3):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col].color == color and board[row-2, col].color == color and board[row-3,col].color == color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row-3, col].color != ColorConstant.BLACK):
                    value = value + 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-2, col].shape == shape and board[row-3, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row-3, col].shape != ShapeConstant.BLANK): 
                    value = value + 10**3
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col].color != color and board[row-2, col].color != color and board[row-3,col].color != color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row-3, col].color != ColorConstant.BLACK):
                    value = value - 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-2, col].shape != shape and board[row-3, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row-3, col].shape != ShapeConstant.BLANK): 
                    value = value - 10**3

                row = row - 1
            col = col + 1
        
        #POSITIVE
        #Cek diagonal 2 streak
        col = 0
        while (col != board.col - 2):
            row = 5
            while (row > 1):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-1,col+1].color != ColorConstant.BLACK):
                    value = value + 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK): 
                    value = value + 10**1
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col+1].color != color  and board[row-1,col+1].color != ColorConstant.BLACK):
                    value = value - 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK): 
                    value = value - 10**1
        
                row = row - 1
            col = col + 1
        
        #Cek diagonal 3 streak
        col = 0
        while (col != board.col - 3):
            row = 5
            while (row > 2):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-2, col+2].color == color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK):
                    value = value + 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-2, col+2].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK): 
                    value = value + 10**2
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col+1].color != color and board[row-2, col+2].color != color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK):
                    value = value - 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-2, col+2].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK): 
                    value = value - 10**2

                row = row - 1
            col = col + 1
        
        #Cek diagonal 4 streak
        col = 0
        while (col != board.col - 4) :
            row = 5
            while (row > 3):
                #Maximazing
                if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-2, col+2].color == color and board[row-3, col+3].color == color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row-3,col+3].color != ColorConstant.BLACK):
                    value = value + 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-2, col+2].shape == shape and board[row-3, col+3].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row-3,col+3].shape != ShapeConstant.BLANK): 
                    value = value + 10**3
                    
                #Minimazing
                if (board[row, col].color != color and board[row-1, col+1].color != color and board[row-2, col+2].color != color and board[row-3, col+3].color != color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row-3,col+3].color != ColorConstant.BLACK):
                    value = value - 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-2, col+2].shape != shape and board[row-3, col+3].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row-3,col+3].shape != ShapeConstant.BLANK): 
                    value = value - 10**3

                row = row - 1
            col = col + 1
        
        #NEGATIVE
        #Cek diagonal 2 streak
        col = 0
        while (col != board.col - 2):
            row = 4
            while (row >= 0):
                #Maximazing
                if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+1,col+1].color != ColorConstant.BLACK):
                    value = value + 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK): 
                    value = value + 10**1
                    
                #Minimazing
                if (board[row, col].color != color and board[row+1, col+1].color != color  and board[row+1,col+1].color != ColorConstant.BLACK):
                    value = value - 10**1
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK): 
                    value = value - 10**1
        
                row = row - 1
            col = col + 1
        
        #Cek diagonal 3 streak
        col = 0
        while (col != board.col - 3):
            row = 3
            while (row >= 0):
                #Maximazing
                if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+2, col+2].color == color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK):
                    value = value + 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+2, col+2].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK): 
                    value = value + 10**2
                    
                #Minimazing
                if (board[row, col].color != color and board[row+1, col+1].color != color and board[row+2, col+2].color != color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK):
                    value = value - 10**2
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+2, col+2].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK): 
                    value = value - 10**2

                row = row - 1
            col = col + 1
        
        #Cek diagonal 4 streak
        col = 0
        while (col != board.col - 4) :
            row = 2
            while (row >= 0):
                #Maximazing
                if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+2, col+2].color == color and board[row+3, col+3].color == color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row+3,col+3].color != ColorConstant.BLACK):
                    value = value + 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+2, col+2].shape == shape and board[row+3, col+3].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row+3,col+3].shape != ShapeConstant.BLANK): 
                    value = value + 10**3
                    
                #Minimazing
                if (board[row, col].color != color and board[row+1, col+1].color != color and board[row+2, col+2].color != color and board[row+3, col+3].color != color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row+3,col+3].color != ColorConstant.BLACK):
                    value = value - 10**3
                    shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+2, col+2].shape != shape and board[row+3, col+3].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row+3,col+3].shape != ShapeConstant.BLANK): 
                    value = value - 10**3

                row = row - 1
            col = col + 1
            
        print(value)
        return value, col
        
    def MinimaxAB(self, board: Board, state: State, n_player: int, depth: int, alpha: int, beta: int, maximazing: bool, thinking_time: float) :
        start = time()
        
        is_terminal_state = False
        
        if is_win(board) != None or is_full(board) :
            is_terminal_state = True
        
        is_time_out = False
        if thinking_time <= 0 :
            is_time_out = True
        
        #Basis
        if is_terminal_state or is_time_out or depth == 0:
            if is_terminal_state:
                if maximazing :
                    return math.inf, -1, ""
                else :
                    return -math.inf, -1, ""
            elif is_time_out :
                col = random.choice(0, state.board.col)
                shape = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                return BotMinimaxAB.heuristicAB(self, state, board, n_player)[0], col, shape
            else :
                return BotMinimaxAB.heuristicAB(self, state, board, n_player)[0], -1, ""
        
        #Rekurens
        if maximazing:
            value = -math.inf
            shape = ""
            col = random.randint(0, state.board.col)
            check_col = 0
            check = False
            while (check_col < board.col - 1 and check == False) :
                row = 0
                if (board[row+5, col].shape == ShapeConstant.BLANK):
                    copyBoard = copy.copy(board)
                    while (board[row, col].shape != ShapeConstant.BLANK and row < board.row):
                        row = row + 1
                    
                    copyBoard.set_piece(row, col, board[row, col])
                    now = time()
                    thinking_time = thinking_time - (now - start)
                    tempMove = BotMinimaxAB.MinimaxAB(self, copyBoard, state, n_player, depth-1, alpha, beta, False, thinking_time)
                    
                    if tempMove[0] > value :
                        value = tempMove[0]
                        col = check_col
                        shape = tempMove[1]
                    alpha = max(alpha, value)
                    
                    if alpha >= beta :
                        check = True
                else :
                    pass
                
                check_col = check_col + 1
            return value, col, shape
        else :
            value = math.inf
            shape = ""
            col = random.randint(0, state.board.col)
            check_col = 0
            check = False
            while (check_col < board.col - 1 and check == False):
                row = 0
                if board[row+5 , col].shape == ShapeConstant.BLANK :
                    copyBoard = copy.copy(board)
                    while(board[row, col].shape != ShapeConstant.BLANK and row < board.row):
                        row = row + 1
                    
                    copyBoard.set_piece(row, col, board[row, col])
                    tempMove = BotMinimaxAB.MinimaxAB(self, copyBoard, state, n_player, depth-1, alpha, beta, True, thinking_time)
                    
                    if tempMove[0] < value:
                        value = tempMove[0]
                        col = check_col
                        shape = tempMove[1]
                    
                    beta = min(beta, value)
                    if alpha >= beta :
                        check = True
                else:
                    pass
                check_col = check_col + 1
            
            print(value, col, shape)
            return value, col, shape
        
    def find(self, board: Board, state: State, n_player: int, depth: int, alpha: int, beta: int, maximazing: bool, thinking_time: float) :
        value, col, shape = self.MinimaxAB(board, state, n_player, depth, alpha, beta, maximazing, thinking_time)
        print(col, shape)
        return col, shape 

#BotMinimaxAB.find(BotMinimaxAB(Board(6,7),1), Board(6,7), State(Board(6,7), [0,1], 1), 1, 5, math.inf, -math.inf, True, 100)

BotMinimaxAB.heuristicAB(BotMinimaxAB(Board(6,7),0), Board(6,7), 0)