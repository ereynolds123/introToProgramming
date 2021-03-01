#have a user input the file name that contains the user's name
inputFileName = input ("Enter the file name with people's names: ")
#have a user input the file name where the file will be output
outputFileName = input ("Enter the file name to write user names to: ")
#open input user name mode ="r"
inFile=open(inputFileName, "r")
# open input user name file mode="w"
outFile= open(outputFileName, "w")
# read the lines of the file
namesSeq= inFile.readlines()
#for each name in sequence (for .... in ( sequence))
for name in namesSeq:
    # split name on space
    splitName= name.strip().split(" ")
    #assign the first item of split to first name
    firstName = splitName[0]
    # assign second item of te split to last name
    lastName= splitName[1]
    #take the first letter of the first name and 7 of last name to lower case
    userName = firstName[0]+ lastName[:7]
    userName = userName.lower()
    #debugging print userName
    print(userName)
    # write out new usernames
    print(userName, file=outFile)
    
#close input file
inFile.close()
#close output file
outFile.close()
# print that process is complete
print("All finished.")

