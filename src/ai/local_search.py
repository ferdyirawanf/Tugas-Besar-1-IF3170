import random
from time import time

from src.constant import *
from src.model.board import Board
from src.model.state import State
from src.model.piece import Piece
from src.utility import is_win, is_full, place
import copy

class LocalSearchGroup16:
    
    def __init__(self):
        pass

    def randomSuccessor(self, board: Board, color):
        randomCol = random.randint(0, board.col-1)
        randomShape = random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])
        
        copy_board = copy.deepcopy(board)
        row = board.row - 1
        while (copy_board[row, randomCol].shape != ShapeConstant.BLANK and row >= 0):
            row = row - 1

        
        copy_board[row,randomCol].color = color
        copy_board[row,randomCol].shape = randomShape

        return (row, randomCol, copy_board)

    def generateNeighbours(self, board: Board, n_player: int):
        (player_color, player_shape) = \
        (ColorConstant.RED, ShapeConstant.CIRCLE) if n_player == 0 else (ColorConstant.BLUE, ShapeConstant.CROSS)

        neighbours = []
        for i in range(board.col):
            if (board[0, i].shape == ShapeConstant.BLANK):
                copy_board = copy.deepcopy(board)

                row = copy_board.row - 1
                while (copy_board[row, i].shape != ShapeConstant.BLANK and row >= 0):
                    row = row - 1

                copy_board[row, i].color = player_color
                copy_board[row, i].shape = player_shape

                neighbours.append((row,i,copy_board))
        # print(neighbours)
        return neighbours   # [(row, col, copy_board), ...]

    def bestNeighbour(self, neighbours, n_player):
        # Set bestValue -> first neighbour
        bestNeighborValue, bestShape = self.objectiveFunction(neighbours[0], n_player)
        bestNeighbour = neighbours[0]
        
        for neighbour in neighbours:
            neighbourValue, shape = self.objectiveFunction(neighbour, n_player)
            if neighbourValue >= bestNeighborValue:
                bestNeighborValue = neighbourValue
                bestNeighbour = neighbour
                bestShape = shape
        return bestNeighborValue, bestShape, bestNeighbour

    def objectiveFunction(self, neighbour, n_player: int):
        
        if n_player == 1:
            shape = GameConstant.PLAYER1_SHAPE
            color = GameConstant.PLAYER1_COLOR
            shape_opp = GameConstant.PLAYER2_SHAPE
        else :
            shape = GameConstant.PLAYER2_SHAPE
            color = GameConstant.PLAYER2_COLOR
            shape_opp = GameConstant.PLAYER1_SHAPE

        board = neighbour[2]
        value = 0
        shape_value = ""
        
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
                    
                    #Maximazing 4 streak with hole in the middle
                    if (board[row, col].color == color and board[row, col+1].color == color and board[row, col+2].color == color and board[row, col+3].color == color and ((board[row, col+1].color == ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK) or (board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color == ColorConstant.BLACK)) and board[row, col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value + 10**3
                        shape_value = shape
                    if (board[row, col].shape == shape and board[row, col+1].shape == shape and board[row, col+2].shape == shape and board[row, col+3].shape == shape and ((board[row, col+1].shape == ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK) or (board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape == ShapeConstant.BLANK)) and board[row, col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
                        value = value + 10**3
                        shape_value = shape_opp
                        
                    #Minimazing 4 streak
                    if (board[row, col].color != color and board[row, col+1].color != color and board[row, col+2].color != color and board[row, col+3].color != color and ((board[row, col+1].color == ColorConstant.BLACK and board[row, col+2].color != ColorConstant.BLACK) or (board[row, col+1].color != ColorConstant.BLACK and board[row, col+2].color == ColorConstant.BLACK)) and board[row, col+3].color != ColorConstant.BLACK and board[row, col].color != ColorConstant.BLACK):
                        value = value - 10**3
                        shape_value = shape
                    if (board[row, col].shape != shape and board[row, col+1].shape != shape and board[row, col+2].shape != shape and board[row, col+3].shape != shape and ((board[row, col+1].shape == ShapeConstant.BLANK and board[row, col+2].shape != ShapeConstant.BLANK) or (board[row, col+1].shape != ShapeConstant.BLANK and board[row, col+2].shape == ShapeConstant.BLANK)) and board[row, col+3].shape != ShapeConstant.BLANK and board[row, col].shape != ShapeConstant.BLANK): 
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

    def find(self, state, n_player, thinking_time):
        start = time()
        value, col, shape = self.HillClimbing(state.board, n_player, thinking_time, start)
        listShape = []
        for k, v in state.players[n_player].quota.items():
            listShape += list([[k,v]])

        for i in range (len(listShape[0])):
            if listShape[i][0] == GameConstant.PLAYER1_SHAPE and listShape[i][1] == 0:
                shape = GameConstant.PLAYER2_SHAPE
            elif listShape[i][0] == GameConstant.PLAYER2_SHAPE and listShape[i][1] == 0:
                shape = GameConstant.PLAYER1_SHAPE
        return col, shape 
        
    def HillClimbing(self, board: Board, n_player: int, thinking_time: float, start_time) :
        color = GameConstant.PLAYER1_COLOR if n_player == 0 else GameConstant.PLAYER2_COLOR

        currentState = self.randomSuccessor(board, color)
        currentStateValue, currentShape = self.objectiveFunction(currentState, n_player)

        neighbours = self.generateNeighbours(currentState[2], n_player)
        bestNeighborValue, bestShape, bestNeighbour = self.bestNeighbour(neighbours, n_player)

        if bestNeighborValue > currentStateValue:
            currentState = bestNeighbour
            currentStateValue = bestNeighborValue
            currentShape = bestShape

        # while bestNeighborValue > currentStateValue:
        #     currentState = bestNeighbour
        #     currentStateValue = bestNeighborValue
        #     currentShape = bestShape

        #     now = time()
        #     thinking_time -= (now - start_time)
        #     if thinking_time <= 0 :
        #         break
        #     start_time = time()

        #     neighbours = self.generateNeighbours(currentState, n_player)
        #     bestNeighborValue, bestShape, bestNeighbour = self.bestNeighbour(neighbours, n_player)

        return currentStateValue, currentState[1], currentShape
        # return bestNeighborValue, bestNeighbour[1], bestShape