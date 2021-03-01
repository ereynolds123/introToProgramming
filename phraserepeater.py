# Allow user to input a phrase and repeat the phrase

# User input phrase to repeat
phraseToRepeat= (input("Input your phrase: "))
# User inputs how many times they would like to repeat
timesToRepeat = (int(input("How many times should it be repeated: ")))

#loop through phrase to repeat the amount of times to repeat
for index in range(timesToRepeat):
    print((str(index +1))+ " "+ phraseToRepeat)
    
                 