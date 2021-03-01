from graphics import *

#Create a window
win= GraphWin("Tic-Tac-Toe")

#Coordnates go from (0,0) in lower left to (3, 3) right
win.setCoords(0.0, 0.0, 3.0, 3.0)

#Draw Vertical Lines
Line(Point(1,0), Point(1,3)).draw(win)
Line(Point(2,0), Point(2,3)).draw(win)

#Draw Horizontal Lines
Line(Point(0, 1), Point(3,1)).draw(win)
Line(Point(0, 2), Point(3,2)).draw(win)