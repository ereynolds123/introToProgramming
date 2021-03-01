#numberOfWords =int(input("How many words will you enter: "))

countOfEs = 0
totalWords= 1
sentinel="quit"

#for index in range(numberOfWords):
    #inputWord =input("Enter word {0}: ".format(index +1))
    #countOfEs =countOfEs + inputWord.count("e")
    #totalLengthOfInput = totalLengthOfInput +len(inputWord)


#another way
inputWord =input("Enter word {0}: ".format(totalWords))

while inputWord !=sentinel:
    countOfEs =countOfEs + inputWord.count("e")
    totalWords = totalWords+1
    inputWord =input("Enter word {0}: ".format(totalWords))

print(countOfEs, totalWords)