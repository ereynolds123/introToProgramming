from graphics import *

def createGraph():
    #Introduction
    print("This program plots the growth of a 10 year investment")
    #Get principal and interest rate
    principal = float(input("Enter the initial principle: "))
    #apr = float(input("Enter the annualized interest rate: "))
    
    #Create a graphic window with labels
    win= GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), "0.0K").draw(win)
    Text(Point(20, 180), "2.5K").draw(win)
    Text(Point(20, 130), "5.0K").draw(win)
    Text(Point(20, 80), "7.5K").draw(win)
    Text(Point (20, 30), "10.0k").draw(win)
    
    #Draw rectangle for initial principle
    height= principal * 0.02
    bar= Rectangle (Point (40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win) 

createGraph()