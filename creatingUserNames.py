#Program to create a file of usernames in batch mode

def createUserNames():
    print("This program creates a file of usernames from a")
    print(" file of names.")
    
    #get the file names
    infileName = input("What file are the names in?")
    outfileName= input ("What file should the usernames go in?")
    
    #open the files
    infile = open(infileName, "r")
    outfile = open (outfileName, "w")
    
    #process each line of input file
    for ling in infile:
        #ge tthe first and last names from the line
        first, last =line.split
        #create username
        userName = (first[0]+last[:7]).lower()
        #write it to the output file
        print(userName, file=outfile)
        
    #close both files
        infile.close()
        outfile.close()
createUserNames()