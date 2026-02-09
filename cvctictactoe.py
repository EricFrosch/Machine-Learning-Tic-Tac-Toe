# CVC is computer vs computer tictactoe

# imports
from graphics import *

class CVCTicTacToe:

    def __init__(self, m1, m2):
        self.computer1Squares = []
        self.computer2Squares = []
        self.menace1 = m1
        self.menace1.chosenLists = []
        self.menace1.chosenMoves = []
        self.menace2 = m2
        self.menace2.chosenLists = []
        self.menace2.chosenMoves = []

    def runGame(self):
        while (not (self.computer1Win())) and (not (self.computer2Win())) and (not (self.isDrawn())):
            self.drawX(self.menace1.chooseSquare(self.computer2Squares, self.computer1Squares, self.isDrawn()))
            if self.computer1Win():
                self.menace2.removeLastMove()
            else:
                self.drawO(self.menace2.chooseSquare(self.computer1Squares, self.computer2Squares, self.isDrawn()))
                if self.computer1Win():
                    self.menace2.removeLastMove()
        if self.computer2Win():
            #self.menace2.addWinningMoves()
            self.menace1.removeLastMove()
        if self.computer1Win():
            self.menace1.addWinningMoves()
        return self.computer2Win(), self.isDrawn()

    def drawX(self, square):
        if square == 1:
            self.computer1Squares.append(1)
        elif square == 2:
            self.computer1Squares.append(2)
        elif square == 3:
            self.computer1Squares.append(3)
        elif square == 4:
            self.computer1Squares.append(4)
        elif square == 5:
            self.computer1Squares.append(5)
        elif square == 6:
            self.computer1Squares.append(6)
        elif square == 7:
            self.computer1Squares.append(7)
        elif square == 8:
            self.computer1Squares.append(8)
        elif square == 9:
            self.computer1Squares.append(9)

    def drawO(self, square):
        if square == 1:
            self.computer2Squares.append(1)
        elif square == 2:
            self.computer2Squares.append(2)
        elif square == 3:
            self.computer2Squares.append(3)
        elif square == 4:
            self.computer2Squares.append(4)
        elif square == 5:
            self.computer2Squares.append(5)
        elif square == 6:
            self.computer2Squares.append(6)
        elif square == 7:
            self.computer2Squares.append(7)
        elif square == 8:
            self.computer2Squares.append(8)
        elif square == 9:
            self.computer2Squares.append(9)
        elif not square:
            for i in range(1, 10):
                self.computer1Squares.append(i)


    def computer1Win(self):
        if ((1 in self.computer1Squares) and (2 in self.computer1Squares) and (3 in self.computer1Squares)) \
            or ((4 in self.computer1Squares) and (5 in self.computer1Squares) and (6 in self.computer1Squares)) \
            or ((7 in self.computer1Squares) and (8 in self.computer1Squares) and (9 in self.computer1Squares)) \
            or ((1 in self.computer1Squares) and (4 in self.computer1Squares) and (7 in self.computer1Squares)) \
            or ((2 in self.computer1Squares) and (5 in self.computer1Squares) and (8 in self.computer1Squares)) \
            or ((3 in self.computer1Squares) and (6 in self.computer1Squares) and (9 in self.computer1Squares)) \
            or ((1 in self.computer1Squares) and (5 in self.computer1Squares) and (9 in self.computer1Squares)) \
            or ((3 in self.computer1Squares) and (5 in self.computer1Squares) and (7 in self.computer1Squares)):
            return True
        else:
            return False

    def computer2Win(self):
        if ((1 in self.computer2Squares) and (2 in self.computer2Squares) and (3 in self.computer2Squares)) \
            or ((4 in self.computer2Squares) and (5 in self.computer2Squares) and (6 in self.computer2Squares)) \
            or ((7 in self.computer2Squares) and (8 in self.computer2Squares) and (9 in self.computer2Squares)) \
            or ((1 in self.computer2Squares) and (4 in self.computer2Squares) and (7 in self.computer2Squares)) \
            or ((2 in self.computer2Squares) and (5 in self.computer2Squares) and (8 in self.computer2Squares)) \
            or ((3 in self.computer2Squares) and (6 in self.computer2Squares) and (9 in self.computer2Squares)) \
            or ((1 in self.computer2Squares) and (5 in self.computer2Squares) and (9 in self.computer2Squares)) \
            or ((3 in self.computer2Squares) and (5 in self.computer2Squares) and (7 in self.computer2Squares)):
            return True
        else:
            return False

    def isDrawn(self):
        totalSquares = []
        for i in self.computer1Squares:
            totalSquares.append(i)
        for i in self.computer2Squares:
            totalSquares.append(i)
        global hasAllSquares
        hasAllSquares = True
        for i in range(1, 10):
            if not (i in totalSquares):
                hasAllSquares = False
        return hasAllSquares and (not self.computer1Win())
