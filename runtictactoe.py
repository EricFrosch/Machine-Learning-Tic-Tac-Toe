# runtictactoe runs the program

# imports
from tictactoe import *
from menace import *


# create the window
win = GraphWin("Tic Tac Toe", 600, 610)
win.setBackground("gray")

# creates a tracker for the number of games
gameNum = 0
gameTracker = Text(Point(60,10), "Game Number: " + str(gameNum))
gameTracker.draw(win)

# creates trackers for wins loses, and draws for the computer
winNum = 0
winTracker = Text(Point(250,10), "Computer Wins: " + str(winNum))
winTracker.draw(win)

lossNum = 0
lossTracker = Text(Point(400,10), "Computer Losses: " + str(lossNum))
lossTracker.draw(win)

draws = 0
drawTracker = Text(Point(550, 10), "Draws: " + str(draws))
drawTracker.draw(win)

# draws game board
TicTacToe.createGameBoard(win)

# creates the tictactoe computer
menace = Menace()

while win.isOpen():
    gameNum += 1
    game = TicTacToe(menace, win)
    result = game.runGame()
    if result[1]:
        draws += 1
    elif result[0]:
        winNum += 1
    else:
        lossNum += 1

    clear = Rectangle(Point(0, 20), Point(win.getWidth(), win.getHeight()))
    clear.setFill("gray")
    clear.setOutline("gray")
    clear.draw(win)

    gameTracker.undraw()
    gameTracker = Text(Point(60, 10), "Game Number: " + str(gameNum))
    gameTracker.draw(win)
    winTracker.undraw()
    winTracker = Text(Point(250, 10), "Computer Wins: " + str(winNum))
    winTracker.draw(win)
    lossTracker.undraw()
    lossTracker = Text(Point(400, 10), "Computer Losses: " + str(lossNum))
    lossTracker.draw(win)
    drawTracker.undraw()
    drawTracker = Text(Point(550, 10), "Draws: " + str(draws))
    drawTracker.draw(win)

    TicTacToe.createGameBoard(win)
txt_file = open(r'D:\python programs\tic_tac_toe\Results.txt', 'w')
for i in menace.movesList:
    for j in i:
        txt_file.write(str(j)+"\n")
txt_file.close()
