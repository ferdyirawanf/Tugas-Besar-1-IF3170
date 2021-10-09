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

class BotLocalSearch:
    
    def __init__(self, board: Board, n_player: int):
        self.board = board
        self.n_player = n_player

    def objectiveFunction(self, neighbour, n_player):
        neighbourRow = neighbour[0]
        neighbourCol = neighbour[1]
        board = neighbour[2]

        value = 0
        if n_player == 0:
            shape = GameConstant.PLAYER1_SHAPE
            color = GameConstant.PLAYER1_COLOR
        else :
            shape = GameConstant.PLAYER2_SHAPE
            color = GameConstant.PLAYER2_COLOR
        
        shape_value = ""
        
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
            
        return value, shape_value

    def makeNeighbour(self, board: Board, n_player):
        neighbours = []
        if n_player == 0:
            player_color = ColorConstant.RED
            player_shape = ShapeConstant.CIRCLE
        elif n_player == 1:
            player_color = ColorConstant.BLUE
            player_shape = ShapeConstant.CROSS
        for i in range(board.col):
            if (board[0, i].shape == ShapeConstant.BLANK):
                copy_board = copy.deepcopy(board)
                row = copy_board.row - 1
                while (copy_board[row, i].shape != ShapeConstant.BLANK and row >= 0):
                    row = row - 1
                copy_board[row, i].color = player_color
                copy_board[row, i].shape = player_shape
                neighbours.append((row,i,copy_board))
        print(neighbours)
        return neighbours
        
    def bestNeighbour(self, neighbours, n_player):
        bestValue = self.objectiveFunction(neighbours[0], n_player)
        bestNeighbour = neighbours[0]
        for neighbour in neighbours:
            neighbourValue = self.objectiveFunction(neighbour, n_player)
            if neighbourValue >= bestValue:
                bestValue = neighbourValue
                bestNeighbour = neighbour
        return bestValue, bestNeighbour

    def randomSuccessor(self, board: Board, color):
        randomCol, randomShape = (random.randint(0, board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE]))
        copy_board = copy.deepcopy(board)
        row = copy_board.row - 1
        while (copy_board[row, randomCol].shape != ShapeConstant.BLANK and row >= 0):
            row = row - 1
        board[row,randomCol].color = color
        board[row,randomCol].shape = randomShape
        return (row, randomCol, board)

        
    def HillClimbing(self, board: Board, state: State, n_player: int, thinking_time: float) :
        start = time()

        if n_player == 0:
            shape = GameConstant.PLAYER1_SHAPE
            color = GameConstant.PLAYER1_COLOR
        else :
            shape = GameConstant.PLAYER2_SHAPE
            color = GameConstant.PLAYER2_COLOR


        currentState = self.randomSuccessor(board, color)
        currentStateValue = self.objectiveFunction(currentState, n_player)
        neighbours = self.makeNeighbour(currentState, n_player)
        bestValue, bestNeighbour = self.bestNeighbour(neighbours, n_player)

        while bestValue < currentStateValue:
            currentState = bestNeighbour
            currentStateValue = bestValue
            neighbours = self.makeNeighbour(currentState, n_player)
            bestValue, bestNeighbour = self.bestNeighbour(neighbours, n_player)
            now = time()
            thinking_time = thinking_time - (now - start)
            if thinking_time <= 0 :
                break

        return currentState[2]

#BotLocalSearch.makeNeighbour(BotLocalSearch(Board(6,7),1), Board(6,7), 0)