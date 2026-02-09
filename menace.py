# machine educable naughts and crosses engine

# imports
import random
# used to convert string to list
import ast
import json

class Menace:

    def __init__(self):
        # each list in movesList has 1 list of the x squares 1 list of o squares and 1 list of the squares to choose
        txt_file = open(r'D:\python programs\tic_tac_toe\Results.txt', 'r')
        lines = txt_file.readlines()
        for i in lines:
            i = str(i)
        prevGameMoves = []
        for i in range(len(lines)):
            if (i % 3) == 0:
                prevGameMoves.append([])
            prevGameMoves[-1].append(ast.literal_eval(lines[i]))
        txt_file.close()
        self.movesList = prevGameMoves
        # list of the indices of the lists that it has chosen
        self.chosenLists = []
        # list of the values of the moves that it has chosen
        self.chosenMoves = []

    def chooseSquare(self, ps, cs, isDrawn):
        if not isDrawn:
            playerSquares = []
            computerSquares = []
            for i in ps:
                playerSquares.append(i)
            for i in cs:
                computerSquares.append(i)
            hasMoves = False
            global chosenList
            chosenList = []
            for i in range(len(self.movesList)):
                if (self.movesList[i][0] == playerSquares) and (self.movesList[i][1] == computerSquares):
                    hasMoves = True
                    chosenList = self.movesList[i][2]
                    self.chosenLists.append(i)
            if not hasMoves:
                newMoves = []
                for i in range(1, 10):
                    if (i not in playerSquares) and (i not in computerSquares):
                        newMoves.append(i)
                self.movesList.append([playerSquares, computerSquares, newMoves])
                chosenList = self.movesList[-1][2]
                self.chosenLists.append(len(self.movesList)-1)
            if(len(chosenList) > 0):
                chosenSquare = chosenList[random.randrange(len(chosenList))]
            else:
                return False

            self.chosenMoves.append(chosenSquare)
            return chosenSquare
        return True

    def removeLastMove(self):
        global index
        index = -1
        if len(self.movesList[self.chosenLists[-1]][2]) > 0:
            self.movesList[self.chosenLists[-1]][2].remove(self.chosenMoves[-1])
        elif len(self.movesList[self.chosenLists[0]][2]) > 0:
            while len(self.movesList[self.chosenLists[index]][2]) == 0:
                index -= 1
            ind = -1
            while self.chosenMoves[ind] not in self.movesList[self.chosenLists[index]][2]:
                ind -= 1
            self.movesList[self.chosenLists[index]][2].remove(self.chosenMoves[ind])

    def addWinningMoves(self):
            self.movesList[self.chosenLists[-1]][2].append(self.chosenMoves[-1])
