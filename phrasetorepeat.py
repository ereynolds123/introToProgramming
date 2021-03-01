# print wubba lubba dub dub 3 times
# write a function for the phrase
# allow user to input a phrase
# allow user to input the amount of times to repeat the phrase
# loop through the phrase at the given amount of times

def phraseToRepeat():
    phrase = input("What phrase would you like to say: ")
    amountToRepeat = int(input("How many times would you like to repeat the phrase: "))
    for index in range(amountToRepeat):
          print(phrase)
          
phraseToRepeat()