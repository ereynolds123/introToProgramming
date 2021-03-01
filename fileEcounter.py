#Define the file name
wordsFileNames = ["words_1.csv", "words_2.csv", "words_3.csv"]

#Total accumulator value
totalNumberOfEs = 0

for fileName in wordsFileNames:
    #Open the file
    wordsFile= open(fileName, "r")

    #Declare accumulator variables
    nextLine =wordsFile.readline()

    #While the next line is not empty, split the words on the comma
    while nextLine != "":
        words =nextLine.split(",")
    
        #For ever word, count the amount of e's, add the amount of e's to the total
        for word in words:
            numberOfEs= word.count("e")
            totalNumberOfEs = totalNumberOfEs + numberOfEs
    
        #Change the accumulator so that you advance lines
        nextLine = wordsFile.readline()

    #Close the file
    wordsFile.close()

#Print your final message
print("All the words have a total of", totalNumberOfEs, "e's!")
