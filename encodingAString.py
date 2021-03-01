# Encoding a string

#Declaring global variables
myStr ="welcome to monday"
encodedStr= " "

#For each character in the string, get the ordinal value
for char in myStr:
    message = ord(char)
    #Accumulating the ordinal value
    encodedStr = encodedStr + " "+ str(message)

#print the encoded message
print(encodedStr)

#Decoding a message
myMessage = encodedStr
encodedTokens =myMessage.split(" ")


concatenatedString = " "
for numberString in encodedTokens:
    if numberString != ' ' and numberString != '':
        decodedChr=chr(int(numberString))
        concatenatedString = concatenatedString +decodedChr

print(concatenatedString)

