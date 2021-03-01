#A program to search invoices

#Input id or customer last name
searchParams = input("Search by invoice id (id) or customer last name (lname)? ")

#Input search term
searchTerm = input("Enter your search term: ")


#Require input until user puts in either id or lname
while searchParams !="id" and searchParams != "lname":
        print("ERROR.You must either enter 'id' for invoice id or 'lname' for customer last name search.")
        searchParams = input("Search by invoice id (id) or customer last name (lname)? ")

#Declare file name
searchFileName = "sales_data.csv"

#Open the file
searchFile = open(searchFileName, "r")

#Declare accumulator variables
nextLine =searchFile.readline()
totalRecord =0


# Try either of these
#While the next line is not empty, split the words on the comma
while nextLine != "":
    words =nextLine.split("\n")
    nextLine =searchFile.readline()
    if searchTerm in nextLine:
        print(nextLine)
        totalRecord = totalRecord +1
    
print(totalRecord, "records found.")
#totalRecords = totalFileSequence.split("\n") This is not working. 