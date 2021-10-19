import math
import random
from time import time
from src.model import Player
from src.model.player import Player

from src.constant import ColorConstant, GameConstant, ShapeConstant
from src.model.board import Board
from src.model.state import State
from src.model.piece import Piece
from src.utility import is_win, is_full, place
import copy

from typing import Tuple

class BotMinimaxAB:
    
    def __init__(self):
        pass
    
    def node(self, board: Board, n_player):
        node = []
        
        if n_player == 0:
            player_color = GameConstant.PLAYER1_COLOR
            player_shape = GameConstant.PLAYER1_SHAPE
        else:
            player_color = GameConstant.PLAYER2_COLOR
            player_shape = GameConstant.PLAYER2_SHAPE

        for i in range(board.col):
            if (board[0, i].shape == ShapeConstant.BLANK):
                copy_board = copy.deepcopy(board)
                row = copy_board.row - 1
                while (copy_board[row, i].shape != ShapeConstant.BLANK and row >= 0):
                    row = row - 1
                copy_board[row, i].color = player_color
                copy_board[row, i].shape = player_shape
                node.append((i,copy_board))
        return node
                
    def heuristicAB(self, board: Board, n_player: int) :
        value = 0

        if n_player == 1:
            shape = GameConstant.PLAYER1_SHAPE
            color = GameConstant.PLAYER1_COLOR
            shape_opp = GameConstant.PLAYER2_SHAPE
        else :
            shape = GameConstant.PLAYER2_SHAPE
            color = GameConstant.PLAYER2_COLOR
            shape_opp = GameConstant.PLAYER1_SHAPE
        
        shape_value = shape
        
        for row in range(board.row-1, 0, -1):
            for col in range(0, board.col):
                #Cek horizontal
                try:
                    #Maximazing 2 streak
                    if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK) :
                        value = value + 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape == shape  and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+1].shape == shape and board[row, col].shape != ShapeConstant.BLANK) :
                        value = value + 10**1
                        shape_value = shape
                    
                    #Minimazing 2 streak
                    if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK) :
                        value = value - 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+1].shape != shape and board[row, col].shape != ShapeConstant.BLANK) :
                        value = value - 10**1
                        shape_value = shape
                    
                    #Maximazing 3 streak
                    if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+2].color == color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**2
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row, col+1].shape == shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+2].shape == shape and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**2
                        shape_value = shape_opp
                        
                    #Minimazing 3 streak
                    if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+2].color != color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**2
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row, col+1].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+2].shape != shape and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**2
                        shape_value = shape
                    
                    #Maximazing 4 streak
                    if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+2].color == color and board[row, col+3].color == color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**3
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row, col+1].shape == shape and board[row, col+2].shape == shape and board[row, col+3].shape == shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**3
                        shape_value = shape_opp
                        
                    #Minimazing 4 streak
                    if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+2].color != color and board[row, col+3].color != color and board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK and board[row, col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**3
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row, col+1].shape != shape and board[row, col+2].shape != shape and board[row, col+3].shape != shape and board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK and board[row, col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**3
                        shape_value = shape
                        
                except IndexError:
                    pass
                
                #Cek Vertikal
                try :
                    #Maximazing 2 streak
                    if (board[row, col].color == color and board[row-1, col].color == color and board[row-1, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**1
                        shape_value = shape
                        
                    #Minimazing 2 streak
                    if (board[row, col].color != color and board[row-1, col].color != color and board[row-1, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**1
                        shape_value = shape
                    
                    #Maximazing 3 streak
                    if (board[row, col].color == color and board[row-1, col].color == color and board[row-2, col].color == color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**2
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-2, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**2
                        shape_value = shape_opp
                        
                    #Minimazing 3 streak
                    if (board[row, col].color != color and board[row-1, col].color != color and board[row-2, col].color != color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**2
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-2, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**2
                        shape_value = shape
                    
                    #Maximazing 4 streak
                    if (board[row, col].color == color and board[row-1, col].color == color and board[row-2, col].color == color and board[row-3,col].color == color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row-3, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**3
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row-1, col].shape == shape and board[row-2, col].shape == shape and board[row-3, col].shape == shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row-3, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**3
                        shape_value = shape_opp
                        
                    #Minimazing 4 streak
                    if (board[row, col].color != color and board[row-1, col].color != color and board[row-2, col].color != color and board[row-3,col].color != color and board[row-1, col].color != ColorConstant.BLACK and board[row-2, col].color != ColorConstant.BLACK and board[row-3, col].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**3
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row-1, col].shape != shape and board[row-2, col].shape != shape and board[row-3, col].shape != shape and board[row-1, col].shape != ShapeConstant.BLANK and board[row-2, col].shape != ShapeConstant.BLANK and board[row-3, col].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**3
                        shape_value = shape
                        
                except IndexError :
                    pass
                
                #Cek diagonal positive
                try :
                    #Maximazing 2 streak
                    if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-1,col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**1
                        shape_value = shape
                        
                    #Minimazing 2 streak
                    if (board[row, col].color != color and board[row-1, col+1].color != color  and board[row-1,col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**1
                        shape_value = shape
                    
                    #Maximazing 3 streak
                    if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-2, col+2].color == color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**2
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-2, col+2].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**2
                        shape_value = shape_opp
                        
                    #Minimazing 3 streak
                    if (board[row, col].color != color and board[row-1, col+1].color != color and board[row-2, col+2].color != color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**2
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-2, col+2].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**2
                        shape_value = shape

                    #Maximazing 4 streak
                    if (board[row, col].color == color and board[row-1, col+1].color == color and board[row-2, col+2].color == color and board[row-3, col+3].color == color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row-3,col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**3
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row-1, col+1].shape == shape and board[row-2, col+2].shape == shape and board[row-3, col+3].shape == shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row-3,col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**3
                        shape_value = shape_opp
                        
                    #Minimazing 4 streak
                    if (board[row, col].color != color and board[row-1, col+1].color != color and board[row-2, col+2].color != color and board[row-3, col+3].color != color and board[row-1,col+1].color != ColorConstant.BLACK and board[row-2, col+2].color != ColorConstant.BLACK and board[row-3,col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**3
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row-1, col+1].shape != shape and board[row-2, col+2].shape != shape and board[row-3, col+3].shape != shape and board[row-1, col+1].shape != ShapeConstant.BLANK and board[row-2, col+2].shape != ShapeConstant.BLANK and board[row-3,col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**3
                        shape_value = shape
                
                except IndexError :
                    pass
            
                #Cek Diagonal Negative
                try :
                    #Maximazing 2 streak
                    if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+1,col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**1
                        shape_value = shape
                        
                    #Minimazing 2 streak
                    if (board[row, col].color != color and board[row+1, col+1].color != color  and board[row+1,col+1].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**1
                        shape_value = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
                    if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**1
                        shape_value = shape

                    #Maximazing 3 streak
                    if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+2, col+2].color == color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**2
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+2, col+2].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**2
                        shape_value = shape_opp
                        
                    #Minimazing 3 streak
                    if (board[row, col].color != color and board[row+1, col+1].color != color and board[row+2, col+2].color != color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**2
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+2, col+2].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**2
                        shape_value = shape
                    
                    #Maximazing 4 streak
                    if (board[row, col].color == color and board[row+1, col+1].color == color and board[row+2, col+2].color == color and board[row+3, col+3].color == color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row+3,col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**3
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row+1, col+1].shape == shape and board[row+2, col+2].shape == shape and board[row+3, col+3].shape == shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row+3,col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**3
                        shape_value = shape_opp
                        
                    #Minimazing 4 streak
                    if (board[row, col].color != color and board[row+1, col+1].color != color and board[row+2, col+2].color != color and board[row+3, col+3].color != color and board[row+1,col+1].color != ColorConstant.BLACK and board[row+2, col+2].color != ColorConstant.BLACK and board[row+3,col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**3
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row+1, col+1].shape != shape and board[row+2, col+2].shape != shape and board[row+3, col+3].shape != shape and board[row+1, col+1].shape != ShapeConstant.BLANK and board[row+2, col+2].shape != ShapeConstant.BLANK and board[row+3,col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value - 10**3
                        shape_value = shape
                        
                except IndexError :
                    pass
        
        return value, shape_value
    
    def find(self, state, n_player, thinking_time) :
        value, col, shape = self.MinimaxAB(state, state.board, n_player, 5, -math.inf, math.inf, thinking_time)
        print(value, col, shape)
        return col, shape 
        
    def MinimaxAB(self, state, board: Board, n_player: int, depth: int, alpha: int, beta: int, thinking_time) :
        start = time()

        col_move = random.randint(0, board.col-1)
        nodes = self.node(board, n_player)

        if n_player == 0:
            shape = GameConstant.PLAYER1_SHAPE
        else :
            shape = GameConstant.PLAYER2_SHAPE

        is_terminal_state = False
        if is_win(board) != None or is_full(board) :
            is_terminal_state = True

        #Basis
        if is_terminal_state:
            if (n_player==0) :
                value, shape = self.heuristicAB(board, n_player)
                listShape = []
                player = (state.round - 1) % 2
                for k, v in state.players[player].quota.items():
                    listShape += list([[k,v]])

                for i in range (len(listShape[0])):
                    if listShape[i][0] == GameConstant.PLAYER1_SHAPE and listShape[i][1] == 0:
                        shape = GameConstant.PLAYER2_SHAPE
                    elif listShape[i][0] == GameConstant.PLAYER2_SHAPE and listShape[i][1] == 0:
                        shape = GameConstant.PLAYER1_SHAPE
                return -math.inf, col_move, shape
            else :
                value, shape = self.heuristicAB(board, n_player)
                listShape = []
                player = (state.round - 1) % 2
                for k, v in state.players[player].quota.items():
                    listShape += list([[k,v]])

                for i in range (len(listShape[0])):
                    if listShape[i][0] == GameConstant.PLAYER1_SHAPE and listShape[i][1] == 0:
                        shape = GameConstant.PLAYER2_SHAPE
                    elif listShape[i][0] == GameConstant.PLAYER2_SHAPE and listShape[i][1] == 0:
                        shape = GameConstant.PLAYER1_SHAPE
                return math.inf, col_move, shape
        elif depth == 0:
            value, shape = self.heuristicAB(board, n_player)
            listShape = []
            player = (state.round - 1) % 2
            for k, v in state.players[player].quota.items():
                listShape += list([[k,v]])

            for i in range (len(listShape[0])):
                if listShape[i][0] == GameConstant.PLAYER1_SHAPE and listShape[i][1] == 0:
                    shape = GameConstant.PLAYER2_SHAPE
                elif listShape[i][0] == GameConstant.PLAYER2_SHAPE and listShape[i][1] == 0:
                    shape = GameConstant.PLAYER1_SHAPE
            return value, col_move, shape

        #Rekurens
        if (n_player==0):
            value = -math.inf
            for node in nodes:
                col, new_board = node

                now = time()
                if thinking_time <= (now - start) :
                    print("MASUK PAK eko 1")
                    print(now - start)
                    break

                tempMove = self.MinimaxAB(state, new_board, n_player+1, depth-1, alpha, beta, thinking_time)

                if tempMove[0] > value :
                    value = tempMove[0]
                    col_move = col
                    shape = tempMove[2]

                alpha = max(alpha, value)
                
                if alpha >= beta :
                    break
            
            return value, col_move, shape
        else :
            value = math.inf
            for node in nodes:
                col, new_board = node

                now = time()
                if thinking_time <= (now - start) :
                    print("MASUK PAK eko 2")
                    print(now - start)
                    break

                tempMove = self.MinimaxAB(state, new_board, n_player-1, depth-1, alpha, beta, thinking_time)

                if tempMove[0] < value:
                    value = tempMove[0]
                    col_move = col
                    shape = tempMove[2]

                beta = min(beta, value)
                if alpha >= beta :
                    break
            
            return value, col_move, shape
               
#BotMinimaxAB.find(BotMinimaxAB(), Board(6,7), 0, 5, -math.inf, math.inf)
#BotMinimaxAB.node(BotMinimaxAB(Board(6,7),0), Board(6,7), 0);
#BotMinimaxAB.MinimaxAB(BotMinimaxAB(Board(6,7),0), Board(6,7), State(Board(6,7), [0,1], 1), 0, 5, -math.inf, math.inf, True, 10.0)
#BotMinimaxAB.heuristicAB(BotMinimaxAB(Board(6,7),0), Board(6,7), 0)