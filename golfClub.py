# A program to determine the club for golfing

#Print opening statements
print("Welcome to the Golf Club Helper!")
print("Tell me your situation, and I'll recommend a club.")

#Get input from user on if they are on the green and how far from the hole they are
onGreen = input("Did you hit the ball on the green (y/n)? ")
farFromHole = int(input("How far is the ball from the hole (in yards)? "))

# Sanitize inputs
onGreen= onGreen.lower()

#If user is on green, print a recommendation for putter
if onGreen =="y":
    print("I recommend using your Putter")

#Conditional for if on green
if onGreen == "n":
    #If more than 200 yards from hole, print use drive
    if farFromHole >= 200:
        print ("I recommend using the Driver")
    #If between 140 and 200 years from hole, print use 5-iron
    elif farFromHole >=140 and farFromHole < 200:
        print ("I recommend using the 5-iron")
    #If between 100 and 140 yards, print use 9-iron
    elif farFromHole >= 100 and farFromHole < 140:
        print("I recommend using the 9-iron")
    #For any distance less than 100 yards, not on green, print use Pitching Wedge
    else:
        print("I recommend using the Pitching Wedge")
    