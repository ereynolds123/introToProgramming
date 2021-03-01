# x, y= y,x

def averageScore():
    print("This programs averages two scores.")
    score1, score2= eval(input("Enter two scores seperated by a comma:" ))
    average =((score1+score2 )/2)
    print("The average of the two scores is", average)
                         
averageScore()