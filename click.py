from graphics import *

def clickEvent():
    win= GraphWin("Click Me!")
    for i in range(10):
        p=win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())
clickEvent()