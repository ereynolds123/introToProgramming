#Create a house graphic using python

#Note I tried to refactor so that the windowHeight -30 was a variable, but it broke the program, so I left it as is.
#If you figure out how to refactor, let me know 

#import graphics library
from graphics import *

#Create the window
win= GraphWin("My Beautiful House - Emily Reynolds", 250, 250)

#Variable for window
windowWidth= 250
windowHeight = 250
midPoint =windowWidth/2
textHeightPoint= 10
windowBeginPointX= 0

#Create text label
textLabel = Text(Point(midPoint, textHeightPoint), "Click the screen to turn to night!")
textLabel.draw(win)

#Create the Sun
sun = Circle(Point(midPoint, 50), 20)
sun.setFill("yellow")
sun.draw(win)

#Create the ground
ground = Rectangle(Point(windowBeginPointX, windowHeight -30), Point(windowWidth, windowHeight - 30))
ground.setFill("lime") #This setFil is not working
ground.draw(win)

#Create the house
house = Rectangle(Point(midPoint -40, windowHeight-30), Point(midPoint +40, windowHeight -100))
house.setFill("chocolate")
house.draw(win)

#Create the roof
roof =Polygon(Point(midPoint-40, windowHeight -100), Point(midPoint, windowHeight -140), Point(midPoint+40, windowHeight-100))
roof.setFill("orange")
roof.draw(win)

#Create tree
treeRect= Rectangle(Point(200, windowHeight -30), Point(210, windowHeight-70))
treeRect.setFill("saddlebrown")
treeRect.draw(win)
treeCircle=Polygon(Point(195, windowHeight -70), Point(205, windowHeight-80), Point(215, windowHeight-70))
treeCircle.setFill("green")
treeCircle.draw(win)

#Fill in the background for day
win.setBackground("cyan")

#Wait for click to turn background black
win.getMouse()
sun.setFill("black")
win.setBackground("black")