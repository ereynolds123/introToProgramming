#File: chaoticfunction.py
#A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x=eval(input("How many numbers should I print?"))
    for i in range(x):
        x=3.9 * x * (1-x)
        print(x)
        
main()