#A program to create random shapes

#Import graphics and random to support functions
from graphics import *
import random

#Get inputs for the file name and how many shapes to make
file = input("Enter the drawing file name to create : ")
numberOfShapes = int(input("Enter the number of shapes to make : "))

#Open file to write to
writeFile = open(file, "w")


#Declare accumulator variable for shapes created
countOfShapes = 1

#While the amount of shapes created is less than the input for shapes required
while countOfShapes <= numberOfShapes:
    #The shape will be a random shape created using random function 
    shapeRandom = random.random()
    #If the random value is lower than 0.5 a circle will be created
    if shapeRandom < 0.5:
        #Set up variables to create the circle
        xPointCircle = random.randrange(0, 501)
        yPointCircle = random.randrange(0,501)
        maxRadius = min(min(xPointCircle, yPointCircle), min(501-xPointCircle, 501-yPointCircle))
        radius = random.randrange(0, maxRadius)
        red = random.randrange(192, 256)
        green = random.randrange(192, 256)
        blue = random.randrange(192, 256)
    
        
        # Print out what is drawn
        print("Circle; {}, {}; {}; {}, {}, {}".format(xPointCircle, yPointCircle, radius, red, green, blue), file=writeFile)
    
    #If the random value is greater than 0.5 a rectangle will be drawn
    else:
        #Set up variables to create the rectangle
        x1PointRect = random.randrange(0, 501)
        y1PointRect = random.randrange(0,501)
        x2PointRect = random.randrange(0,501)
        y2PointRect = random.randrange(0, 501)
        red = random.randrange(192, 256)
        green = random.randrange(192, 256)
        blue = random.randrange(192, 256)
        
        
        #Print what is drawn
        print("Rectangle; {}, {}; {}, {}; {}, {}, {}".format(x1PointRect, y1PointRect, x2PointRect, y2PointRect, red, green, blue), file=writeFile)
    
    #Increment the count of the shapes created accumulator
    countOfShapes =countOfShapes + 1
    
writeFile.close()
    
