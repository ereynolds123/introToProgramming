# A program to calculate the amount of filler in a bowling ball

import math

# User imputs number of bowling balls
bowlingBallNumber= int(input("How many bowling balls will be manufactured? "))

# User inputs the diameter of the ball
diameterBowlingBall = float(input("What is the diameter of each ball in inches? "))

#User inputs the core volume in inches
coreVolume = float(input("What is the core volume in inches cubed? "))

# Calculate the radius of the ball
radiusBowlingBall = diameterBowlingBall /2
#Calculating the total volume of the ball
volume = (4/3) * math.pi * ((radiusBowlingBall)**3)
#Calculating the filler required 
filler = volume - coreVolume
#Calculate total filler
totalFiller = filler * bowlingBallNumber

#Print the amount of total filler to make all bowling balls
print("You will need", totalFiller, "inches cubed of filler")