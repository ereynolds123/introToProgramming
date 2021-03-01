# A program to find the maximum value

"""a =2
b=7
c=5

if a >=b and a>= c:
    print(a, "is the greatest value")
    
elif b >= c:
    print(b, "is the greatest value")

else:
    print(c, "is the greatest value")
    
    
#A better way to write
maxValue = a
if b> maxValue:
    maxValue =b
if c> maxValue:
    maxValue = c
    
    
#good way
valuesNumber =int(input("The the number of values: "))

maxValue = int(input("Enter the first value: "))

for index in range (valuesNumber -1):
    nextValue=int(input("Enter your next value: "))
    if nextValue >= maxValue:
        maxValue = nextValue
        
print("The maximum value is", maxValue)"""

#best way with indefinite loop

nextValueBest = int(input("Enter the first value. To quit, type -1: "))
maxValueBest =nextValueBest

while nextValueBest != -1:
    nextValueBest=int(input("Enter your next value: "))
    if nextValueBest >= maxValueBest:
        maxValueBest = nextValueBest
        
print("The maximum value is", maxValueBest)