from graphics import *

win = GraphWin( "My amazing graph", 250, 250, )

win.getMouse()
win.setBackground("blue") #setBackground calling an mutator method on the window object
win.getMouse() #getMouse calling an action method on the window object
win.close()