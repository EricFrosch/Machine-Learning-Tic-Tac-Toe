# runtictactoe runs the program

# imports
from tictactoe import *
from menace import *
from cvctictactoe import *

gameNum = 0
winNum = 0
draws = 0
lossNum = 0


# creates the tictactoe computer
menace1 = Menace()
menace2 = Menace()

while gameNum < 1500000:
    gameNum += 1
    game = CVCTicTacToe(menace1, menace2)
    result = game.runGame()
    if result[1]:
        draws += 1
    elif result[0]:
        winNum += 1
    else:
        lossNum += 1
    if (gameNum % 10) == 0:
        print("G:", gameNum, "W:", winNum, "D: ", draws, "L: ", lossNum)
    if (gameNum % 10000) == 0:
        menace1.movesList = []
txt_file = open(r'D:\python programs\tic_tac_toe\Results.txt', 'w')
for i in menace2.movesList:
    for j in i:
        txt_file.write(str(j)+"\n")
txt_file.close()




