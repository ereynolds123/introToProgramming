#import graphic library
from graphics import*
#declare variables
textHeight= 50
graphHeight =50
horizontalMargin=20
graphWidth= 3*128 #128 is the max donuts can be made in a day
totalSales=0

#calculate the width and height
totalWidth=graphWidth+ 2* horizontalMargin
totalHeight= graphHeight + 2 * textHeight


#draw the window
win=GraphWin("Donuts Sold", totalWidth,
             totalHeight)

#Draw the axis
topAxisPoint = Point(horizontalMargin, textHeight)
totalAxisHeight = totalHeight-textHeight
bottomAxisPoint= Point(horizontalMargin, totalAxisHeight)
axis= Line(topAxisPoint, bottomAxisPoint)
axis.draw(win)

#Create the points for the labels
labelPoint= Point(totalWidth/2, textHeight/2)
entryPoint=Point(totalWidth/4, textHeight/2)
                  
#Create the Sales Entry Box
salesEntry=Entry(labelPoint, 5)
salesEntry.draw(win)
salesEntryLabel= Text(entryPoint, "Enter Sales: ")
salesEntryLabel.draw(win)


#For each day of sales
for dayOfSales in range(3):
    #Get the input
    win.getMouse()
    nextSales = int(salesEntry.getText())
    salesEntry.setText("")
    
    #Draw rectangle
    topLeftRectPoint=topAxisPoint.clone()
    topLeftRectPoint.move(totalSales, 5)
    bottomRightRectPoint= bottomAxisPoint.clone()
    bottomRightRectPoint.move(totalSales+nextSales, -5)
    salesRect=Rectangle(topLeftRectPoint, bottomRightRectPoint)
    salesRect.draw(win)
    
    #Add text to box
    salesTextPoint= topAxisPoint.clone()
    salesTextPoint.move(totalSales+nextSales/2, totalAxisHeight/2 -30)
    salesAmountText= Text(salesTextPoint, str(nextSales))
    salesAmountText.draw(win)
    
    #Accumulate the total sales
    totalSales= totalSales + nextSales

#Total Sales Text Box
totalSalesText= Text(Point(totalWidth/5, totalHeight-30), "Total: " + str(totalSales))
totalSalesText.draw(win)

#Create the average text box and calculate average
averageSales=totalSales/3
averageSalesText= Text(Point(totalWidth/2 +75, totalHeight -30), "Average: " + str(averageSales))
averageSalesText.draw(win)


