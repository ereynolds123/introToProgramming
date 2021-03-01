#Create a color gradient

#Import graphics library
from graphics import *

#Create the window
win=GraphWin("Color Gradient", 400, 250)

#Declare window variables
windowWidth = 400

#Accumulator Variables
gradientsAccumulator=0
numberOfGradients =1

#Set up the gradient width 
gradientWidth = windowWidth/12


#Color Variables
red=0
green =0
blue=0

#Loop to draw the rectangles
for gradient in range(12):
    #Accumulate the amount of gradients
    gradientsAccumulator= gradientsAccumulator +  1
    #Set the amount of gradients to the accumulated gradients value 
    numberOfGradients= gradientsAccumulator
    
    #Change the color for every rectangle a small increment
    green = green +8
 
   
    #Draw a Rectangle
    gradientRectangle = Rectangle(Point(gradientWidth-33.33, 0), Point(gradientWidth, 250))
    #Eliminate the width of the the rectangle
    gradientRectangle.setWidth(0)
    #Fill in the color of the rectangle
    gradientRectangle.setFill(color_rgb(red,green,blue))
    gradientRectangle.draw(win)
    
    #Accumulate the gradient width
    gradientWidth =gradientWidth +33.33