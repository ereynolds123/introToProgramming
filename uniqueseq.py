# A program to tell if a unique sequence has been added

#Declaring accumulator variables
seq = []
numberOfNumbers =1

print("This program tests if the sequence of positive numbers ou input are unique.")
print("Enter -1 to quit.")

#Input first number
inputNumber = int(input("Enter your first number: "))

#loop to test if the input is a positive integer, or the quit integer
while inputNumber != -1:
    #If the input is -1, break out of the loop
    if inputNumber == -1:
        #Add a blank value to the seq
        seq.append("")
        break
    #If the input number is negative, user will re-enter the input and the number count stays the same
    elif inputNumber <= 0:
        inputNumber = int(input("Enter number {0}: ".format(numberOfNumbers) ))
    #If the input number is positve, user will re-enter 
    else:
        seq.append(inputNumber)
        numberOfNumbers = numberOfNumbers + 1
        inputNumber = int(input("Enter number {0} :".format(numberOfNumbers)))

#Compare length for unique sequences.
#This code derives from a common solution from https://www.tutorialspoint.com/check-if-list-contains-all-unique-elements-in-python 
if(len(set(seq)))==len(seq):
   print("The sequence {0} is unique!".format(seq))
else:
    print("The sequence {0} is not unique!".format(seq))