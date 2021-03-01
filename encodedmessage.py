#Encoding a message

def encodeMessage():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message")
    
    #input from user for message
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")
    #Loop through the message and print the Unicode values
    for ch in message:
        print(ord(ch), end=" ")
        
    print() #blank line
    
encodeMessage()

#Decoding a Message

def decodeMessage():
    #Print messages to user
    print("This program decodes a message and converts")
    print("to Unicode numbers")
    
    #get user input of message to decode
    messageToDecode =input("Please enter the message you wish to decode : ")
    
    #declare message
    message =""
    #Loop through each substring and build Unicode message
    for numStr in messageToDecode.split():
        #Convert digits to a number
        codeNum = int(numStr)
        #concatenate character to message
        message = message + chr(codeNum)
        
        print("\nThe decoded message is: ", message)
        
decodeMessage()