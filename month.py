#Month Lookup table
# A program to print the abbreviation of a month

def monthsAbbreviationCalc():
    # Lookup table of abbreviations
    months = ["Jan","Feb", "Mar", "Apr" "May", "Jun",
    "Jul", "Aug", "Sep", "Nov", "Dec"]
    
    #get input on the month number from user
    monthNumber = int(input("Enter a month number (1-12): "))

    #output result of abbreviation
    print("The month abbreviation is ", months[monthNumber-1] +".")

monthsAbbreviationCalc()
    
