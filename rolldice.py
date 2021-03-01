#A program to simulate rolling dice
import random

#Print program message
print("This program rolls two 6-sided dice until thei sum is a given target value.")

#Get input for target roll amount
targetRoll = int(input("Enter the target sum to roll for : "))

#Accumulator variables
countOfRolls =0
sumOfRolls =0

#While the sum isn't the target roll, roll the dice, add to the accumulator and print message
while sumOfRolls != targetRoll:
    firstRoll = random.randrange(1,7)
    secondRoll = random.randrange(1,7)
    sumOfRolls = firstRoll + secondRoll
    countOfRolls = countOfRolls +1
    print("Roll: {} and {}, sum is {}".format(firstRoll, secondRoll, sumOfRolls))

print("Got it in {} rolls!".format(countOfRolls))