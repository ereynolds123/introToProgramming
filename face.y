#Draw a face using graphical library

#import graphics library
from graphics import *

#draw the window
win= GraphWin("A lovely face", 250, 250)

#draw the pupils
pupilOne= Point(75, 50).draw(win)
pupilTwo= Point(175, 50).draw(win)

#draw the circle
eyeOne= Circle(Point(75, 50), 25).draw(win)
eyeTwo= Circle(Point(175, 50), 25).draw(win)
