from graphics import *
win= GraphWin("Shapes")
 # Draw a red circle centered at point (100,100) with a
 #radius 30
 
center= Point(100, 100)
circ= Circle (center, 30)
circ.setFill("red")
circ.draw(win)

#Put a textual label in the center of the circle
label= Text(center, "Red Circle")
label.draw(win)

#Drwaw a square
rect= Rectangle(Point (30, 30), Point (70,70))
rect.draw(win)

#Draw a line segment
line = Line(Point(20,30), Point (180, 165))
line.draw(win)

#Draw an oval
oval = Oval(Point(20, 150), Point (180, 199))
oval.draw(win)

circ= Circle (Point (100, 100), 30)
win=GraphWin()
circ.draw(win)


#Create two circles
leftCircle =Circle(Point(80,50), 5)
leftCircle.setFill("Yellow")
leftCircle.setOutline("Red")
leftCircle.draw(win)
rightCircle=leftCircle.clone()
rightCircle.move(20,0)
rightCircle.draw(win)
