#Program to find the maximum value

def main():
    n= int(input("How many numbers are there?"))
    
    #Set max to the first value
    maxval = float(input("Enter a number >> "))
    
    #Compare the n-1 successive value
    for i in range (n-1):
        x= float(input("Enter a number >> "))
        if x > maxval:
            maxval =x
            
    print("The largest value is", maxval)

main()