#Draw a face using graphical library

#import graphics library
from graphics import *

#draw the window
win= GraphWin("A lovely face", 250, 250)



#draw the circle
eyeOne= Circle(Point(75, 50), 25)
eyeOne.setFill("white")
eyeOne.setOutline("magenta")
eyeOne.draw(win)

#clone the circle
eyeTwo= eyeOne.clone()
eyeTwo.move(100, 0)
eyeTwo.draw(win)

#draw the pupils
pupilOne= Point(75, 50).draw(win)
pupilTwo= Point(175, 50).draw(win)
#eyeTwo= Circle(Point(175, 50), 25).draw(win)

#draw the rectangele nose
nose = Rectangle(Point(100, 100), Point(150, 150)).draw(win)

#draw the lines for the mouth

mouthLineOne= Line(Point(50, 180), Point(125, 200)).draw(win)
mouthLineTwo= Line(Point(125, 200), Point(200, 180)).draw(win)                 

#Create text
message =Text(Point(125, 220), "Hello World").draw(win)