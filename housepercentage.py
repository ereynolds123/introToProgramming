#import the dependencies
from graphics import*

#Create a window
win = GraphWin("Percentage of payments", 625, 625)

#Each square moves 25 units
pointMove = 25

#Declare inital x and y start values
X1= 0
X2=25
Y1=0
Y2 =25
#Accumulator value
count =1
color="Blue"

for squareX in range(1):
    #If the count is not divisible by 25, create a blue square
    if count % 25 > 0:
        graphicSquare = Rectangle(Point(X1, Y1), Point (X2, Y2))
        graphicSquare.setFill("Blue")
        graphicSquare.draw(win)
        #Add to the x cooridnates
        X1 = X1 + pointMove
        X2 = X2 + pointMove
        #Increment the count
        count =count +1
            
        #When the count is divisible by 25, increase the y increments.
        #Draw a square
    else:
        graphicSquare = Rectangle(Point(X1, Y1), Point (X2, Y2))
        graphicSquare.setFill("Blue")
        graphicSquare.draw(win)
        #Reset the x cooridnates
        X1 = 0
        X2 =25
        #Add to the y cooridnate 
        Y1 = Y1 + 25
        Y2= Y2 +25
        #Increment the count
        count= count + 1
        
for square2 in range(360):
    
    if count % 25 > 0:
        graphicSquare = Rectangle(Point(X1, Y1), Point (X2, Y2))
        graphicSquare.setFill("Yellow")
        graphicSquare.draw(win)
        X1 = X1 + pointMove
        X2 = X2 + pointMove
        count =count +1
    else:
        graphicSquare = Rectangle(Point(X1, Y1), Point (X2, Y2))
        graphicSquare.setFill("Yellow")
        graphicSquare.draw(win)
        X1 = 0
        X2 =25
        Y1 = Y1 + 25
        Y2= Y2 +25
        count= count + 1
        