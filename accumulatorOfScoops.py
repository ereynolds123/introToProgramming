# n scoops of ice cream
# Have to order all 5
# Can be all order

totalScoopOrderings = 1
scoop= int(input("How many scoops in a whole number: "))
#Use a for loop for loop from the first number in the list to the final value
#of the scoop + 1 so you get all values. 
# in range, the first 1 stands for where the range begins

#for scoops in range(1, scoop +1):
for scoops in range( scoop, 0, -1):
    totalScoopOrderings = totalScoopOrderings * scoops
    
print(totalScoopOrderings)