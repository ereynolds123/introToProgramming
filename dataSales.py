# Summing Data from a sales chart and printing to another file

#Getting the inputs from user
#have a user input the file name that contains the sales data
inputFileName = input ("Enter the file name with sales data: ")
#have a user input the file name where the file will be output
outputFileName = input ("Enter the file name to write sales to: ")
#open input data sales, mode ="r"
inputFile=open(inputFileName, "r")
# open output data sales, file mode="w"
outputFile= open(outputFileName, "w")

# read the lines of the file
dataSales= inputFile.readlines()

#For each line
for line in dataSales:
    #split the sales data on the line break
    splitDataSales= line.split(" ")
    #Grab the first number of the line
    firstData = splitDataSales[0].replace("$", " ")
    firstData =float(firstData)
    #Grab the second number of the line
    secondData = splitDataSales[1].replace("$", " ")
    secondData = float(secondData)
    #Add the total Sales together
    totalSales = firstData + secondData
    #Create a string for the original numbers and the total
    salesLine = "${0:8.2f} ${1:8.2f} ${2:8.2f}"
    #Create the line to print
    salesLinePrinted = salesLine.format(firstData, secondData, totalSales)
    #print the line to the output program
    print(salesLinePrinted, file= outputFile)

#Close the input and output files
inputFile.close()
outputFile.close()
#Alert the user that everything worked properly
print("Done writing totals to 17-oct-total.txt")