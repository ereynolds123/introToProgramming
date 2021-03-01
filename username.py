#username.py
#Simple string processing program

def createUserName():
    print("This program generates computer usernames. \n")
    
    #get users first and last name
    firstName = input("Please enter your first name: ")
    lastName= input("Please enter your last name: ")
    
    #Create the username of first letter of first name and7 chars of last name
    userName = firstName[0]+ lastName[:7]
    
    #output userName
    print("Your user name is: " +userName)
    
createUserName()