# A program to calculate change
#This version represents the total cash in cents

def countCash():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters= int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    
    total = quarters *25 + dimes * 10 + nickles * 5 + pennies
    
    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))
    
countCash()