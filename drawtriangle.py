from graphics import *

def createTri():
    win=GraphWin("Draw A Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message=Text(Point(5, 0.50), "Click on three points.")
    message.draw(win)
    
    #Create the points
    p1= win.getMouse()
    p1.draw(win)
    p2= win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    
    #Create the polygon
    triangle= Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
createTri()
