class Candy:
   def __init__(self, name, isChocolate, sugarPercentile, winPercentage):
     self.name = name
     if isChocolate == '0':
        self.isChocolate = False
     else:
        self.isChocolate = True
     self.sugarPercentile = float(sugarPercentile)
     self.winPercentage = float(winPercentage)

def main():
   candyFile = open ("candy-data.txt", "r")
   maxWin = None
   for line in candyFile:
      line = line.strip()
      name, isChocolate, sugarPercentile, winPct = line.split('\t')
      candyData = Candy(name, isChocolate, sugarPercentile, winPct)
      if not candyData.isChocolate:
         if maxWin == None or candyData.winPercentage > maxWin.winPercentage:
             maxWin =candyData    
print (maxWin.name)
print (maxWin.winPercentage)

main()