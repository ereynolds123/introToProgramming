class Candy:
    def __init__(self, name, isChocolate, sugarPct, winPct):
        self.name = name
        
        if isChocolate =="0":
            self.isChocolate = False
        else:
            self.isChocolate =True
        
        self.sugarPct =float(sugarPct)
        self.winPct = float(winPct)
        
    def getName(self):
        return self.name
    
    def getIsChocolate(self):
        return self.isChocolate
    
    def getWinPct(self):
        return self.winPct
        
def parseCandyDataFromLine(line):
    name, isChocolate, sugarPct, WinPct= line.split("\t")
    return Candy(name, isChocolate, sugarPct, winPct)

def main():
  file = "candy-data.txt"
  openFile = open(file, "r")
  
  noChocCandyWithMaxWinPct = None
  
  for line in openFile:
      line =line.strip()
      
      candyData = parseCandyDataFromLine(line)
      
      if not candyData.getIsChocolate():
          if noChocCandyWithMaxWinPct==None or candyData.getWinpCt():
              candyData = noChocCandyWithMaxWinPct
              
print( noChocCandyWithMaxWinPct.getName())
main()