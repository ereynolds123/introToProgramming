dateStr = input("Enter a date(mm/dd/yyy):")
monthStr, dayStr, yearStr = dateStr.split("/")

# Lookup table of abbreviations
months = ["Jan","Feb", "Mar", "Apr" ,"May", "Jun",
"Jul", "Aug", "Sep", "Nov", "Dec"]

monthStr = months[int(monthStr)-1]

print("The converted date is ", monthStr, dayStr +",", yearStr)