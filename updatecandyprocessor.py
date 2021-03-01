
#Candy class 
class Candy:
    def __init__( self, name, isChocolate, sugarPercentile, winPct ):
        self.name = name
        
        #If the isChocolate value is 0, it is not a chocolate candy
        if isChocolate == "0":
            self.isChocolate = False
        else:
            self.isChocolate = True
        
        #The sugar percentage
        self.sugarPercentile = float( sugarPercentile )
        self.winPct = float( winPct )
     
     #Get the name
    def getName( self ):
        return self.name
    
    #Get the isChocolate
    def getIsChocolate( self ):
        return self.isChocolate
    
    #Get the sugar percentage
    def getSugarPercentile( self ):
        return self.sugarPercentile
    
    #Get the win percentage
    def getWinPct( self ):
        return self.winPct
    
    #return a string with the objects characteristics
    def __repr__(self):
        return("{}: Win Percentage {}".format(self.name, self.winPct))

#Parse the candy data to return data for object
def parseCandyDataFromLine( line ):
    name, isChocolate, sugarPercentile, winPct = line.split('\t')
    return Candy( name, isChocolate, sugarPercentile, winPct )

#Gets the win Pct for various candies        
def useWinPct(candy):
    return candy.getWinPct()
    


def main():
    #Open the candy file to read
    candyDataFile = open("candy-data.txt", "r")
    
    candyList = []
    
     #For every line, strip the blank space and parse data
    for line in candyDataFile:
        line = line.strip()
        
        candyData = parseCandyDataFromLine( line )
        #Add the candy to the list
        candyList.append(candyData)
   
    candyList.sort(key=useWinPct)
    
    print(candyList[0:6])
    
    candyList.reverse()
    
    print(candyList[0:6])
    
    candyDataFile.close()
main()