# TicTacToe class is the game

# imports
from graphics import *

class TicTacToe:
    # static method to draw the lines of the tic tac toe board
    @staticmethod
    def createGameBoard(win):
        Line(Point(200, 20), Point(200, 620)).draw(win)
        Line(Point(400, 20), Point(400, 620)).draw(win)
        Line(Point(0, 220), Point(600, 220)).draw(win)
        Line(Point(0, 420), Point(600, 420)).draw(win)

    def __init__(self, m, window):
        self.win = window
        self.playerSquares = []
        self.computerSquares = []
        self.menace = m
        self.menace.chosenLists = []
        self.menace.chosenMoves = []

    def runGame(self):
        while (not (self.playerWin())) and (not (self.computerWin())) and (not (self.isDrawn())):
            self.checkClickedSpace()
            if self.playerWin():
                self.menace.removeLastMove()
            else:
                self.drawO(self.menace.chooseSquare(self.playerSquares, self.computerSquares, self.isDrawn()))
                if self.playerWin():
                    self.menace.removeLastMove()
        if self.computerWin():
            self.menace.addWinningMoves()
        return self.computerWin(), self.isDrawn()

    def checkClickedSpace(self):
        click = self.win.getMouse()
        if (click.getX() < 200) and (click.getY() < 220):
            self.playerSquares.append(1)
            self.drawX(1)
        elif (click.getX() > 400) and (click.getY() < 220):
            self.playerSquares.append(3)
            self.drawX(3)
        elif (click.getX() > 400) and (click.getY() > 420):
            self.playerSquares.append(9)
            self.drawX(9)
        elif (click.getX() < 200) and (click.getY() > 420):
            self.playerSquares.append(7)
            self.drawX(7)
        elif click.getX() < 200:
            self.playerSquares.append(4)
            self.drawX(4)
        elif click.getY() < 220:
            self.playerSquares.append(2)
            self.drawX(2)
        elif click.getX() > 400:
            self.playerSquares.append(6)
            self.drawX(6)
        elif click.getY() > 420:
            self.playerSquares.append(8)
            self.drawX(8)
        else:
            self.playerSquares.append(5)
            self.drawX(5)

    def drawX(self, square):
        if square == 1:
            Line(Point(10, 30), Point(190, 210)).draw(self.win)
            Line(Point(190, 30), Point(10, 210)).draw(self.win)
        elif square == 2:
            Line(Point(210, 30), Point(390, 210)).draw(self.win)
            Line(Point(390, 30), Point(210, 210)).draw(self.win)
        elif square == 3:
            Line(Point(410, 30), Point(590, 210)).draw(self.win)
            Line(Point(590, 30), Point(410, 210)).draw(self.win)
        elif square == 4:
            Line(Point(10, 230), Point(190, 410)).draw(self.win)
            Line(Point(190, 230), Point(10, 410)).draw(self.win)
        elif square == 5:
            Line(Point(210, 230), Point(390, 410)).draw(self.win)
            Line(Point(390, 230), Point(210, 410)).draw(self.win)
        elif square == 6:
            Line(Point(410, 230), Point(590, 410)).draw(self.win)
            Line(Point(590, 230), Point(410, 410)).draw(self.win)
        elif square == 7:
            Line(Point(10, 430), Point(190, 610)).draw(self.win)
            Line(Point(190, 430), Point(10, 610)).draw(self.win)
        elif square == 8:
            Line(Point(210, 430), Point(390, 610)).draw(self.win)
            Line(Point(390, 430), Point(210, 610)).draw(self.win)
        elif square == 9:
            Line(Point(410, 430), Point(590, 610)).draw(self.win)
            Line(Point(590, 430), Point(410, 610)).draw(self.win)

    def drawO(self, square):
        if square == 1:
            Circle(Point(100, 120), 95).draw(self.win)
            self.computerSquares.append(1)
        elif square == 2:
            Circle(Point(300, 120), 95).draw(self.win)
            self.computerSquares.append(2)
        elif square == 3:
            Circle(Point(500, 120), 95).draw(self.win)
            self.computerSquares.append(3)
        elif square == 4:
            Circle(Point(100, 320), 95).draw(self.win)
            self.computerSquares.append(4)
        elif square == 5:
            Circle(Point(300, 320), 95).draw(self.win)
            self.computerSquares.append(5)
        elif square == 6:
            Circle(Point(500, 320), 95).draw(self.win)
            self.computerSquares.append(6)
        elif square == 7:
            Circle(Point(100, 520), 95).draw(self.win)
            self.computerSquares.append(7)
        elif square == 8:
            Circle(Point(300, 520), 95).draw(self.win)
            self.computerSquares.append(8)
        elif square == 9:
            Circle(Point(500, 520), 95).draw(self.win)
            self.computerSquares.append(9)
        elif not square:
            for i in range(1, 10):
                self.playerSquares.append(i)


    def playerWin(self):
        if ((1 in self.playerSquares) and (2 in self.playerSquares) and (3 in self.playerSquares)) \
            or ((4 in self.playerSquares) and (5 in self.playerSquares) and (6 in self.playerSquares)) \
            or ((7 in self.playerSquares) and (8 in self.playerSquares) and (9 in self.playerSquares)) \
            or ((1 in self.playerSquares) and (4 in self.playerSquares) and (7 in self.playerSquares)) \
            or ((2 in self.playerSquares) and (5 in self.playerSquares) and (8 in self.playerSquares)) \
            or ((3 in self.playerSquares) and (6 in self.playerSquares) and (9 in self.playerSquares)) \
            or ((1 in self.playerSquares) and (5 in self.playerSquares) and (9 in self.playerSquares)) \
            or ((3 in self.playerSquares) and (5 in self.playerSquares) and (7 in self.playerSquares)):
            return True
        else:
            return False

    def computerWin(self):
        if ((1 in self.computerSquares) and (2 in self.computerSquares) and (3 in self.computerSquares)) \
            or ((4 in self.computerSquares) and (5 in self.computerSquares) and (6 in self.computerSquares)) \
            or ((7 in self.computerSquares) and (8 in self.computerSquares) and (9 in self.computerSquares)) \
            or ((1 in self.computerSquares) and (4 in self.computerSquares) and (7 in self.computerSquares)) \
            or ((2 in self.computerSquares) and (5 in self.computerSquares) and (8 in self.computerSquares)) \
            or ((3 in self.computerSquares) and (6 in self.computerSquares) and (9 in self.computerSquares)) \
            or ((1 in self.computerSquares) and (5 in self.computerSquares) and (9 in self.computerSquares)) \
            or ((3 in self.computerSquares) and (5 in self.computerSquares) and (7 in self.computerSquares)):
            return True
        else:
            return False

    def isDrawn(self):
        totalSquares = []
        for i in self.playerSquares:
            totalSquares.append(i)
        for i in self.computerSquares:
            totalSquares.append(i)
        global hasAllSquares
        hasAllSquares = True
        for i in range(1, 10):
            if not (i in totalSquares):
                hasAllSquares = False
        return hasAllSquares and (not self.playerWin())
