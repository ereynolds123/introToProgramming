# Calculating a restaurants service score

# User inputs amount of scores
amountScores = int(input("How many days of scores? "))

#Declare total Score at the beginning
totalScore= 0

#Accumulator for loop
for day in range(1, amountScores +1 , 1):
    #convert the number day into a string so you can concatanate later on
    day = str(day)
    # user inputs the amount of score per day
    score = int(input("Enter score for day " + day + ": "))
    # total score accumulates every time through the loop
    totalScore = totalScore + score

#Print the total score message
print("The total score of the " + day + " days is " + str(totalScore))